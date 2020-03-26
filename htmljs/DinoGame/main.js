var myGamePiece;
var myY;
var canvas = document.getElementById('gameArea');
var grounded = false;
var obstacleSpeed = -4;
var myObstacles = [];
var gameOver = false;

function startGame() {
    myGamePiece = new component(75, 75, "dino.png", 20, 120, "image");
    restartButton = new component(75, 75, "restart.png", 425, 100, "image");
    myGamePiece.gravity = 0.1;
    myGameArea.start();
}

var myGameArea = {
    canvas : document.createElement("canvas"),
    start : function() {
        this.id = "gameArea";
        this.canvas.width = 1000;
        this.canvas.height = 270;
        this.context = this.canvas.getContext("2d");
        document.body.insertBefore(this.canvas, document.body.childNodes[0]);
        this.frameNo = 0;
        this.interval = setInterval(updateGameArea, 20); //updates game 50 times per second.
        },
    clear : function() {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
    },
    stop : function() {
        clearInterval(this.interval);
    }
}

function component(width, height, color, x, y, type) {
    this.type = type;
    if (type == "image") {
        this.image = new Image();
        this.image.src = color;
    }
    this.width = width;
    this.height = height;
    this.speedX = 0;
    this.speedY = 0;
    this.x = x;
    this.y = y;
    this.gravity = 1.5;
    this.gravitySpeed = 5; //higher number = faster falling
    this.update = function() {
        ctx = myGameArea.context;
        if (type == "image") {
            ctx.drawImage(this.image,
                this.x,
                this.y,
                this.width, this.height);
        }
    }
    this.newPos = function() {
        this.speedY += this.gravity * this.gravitySpeed; //add gravity to the speedY and times it by gravity speed for faster falling.
        this.x += this.speedX;
        this.y += this.speedY;
        this.speedY *= .9;
        this.hitBottom();
    }
    this.hitBottom = function() {
        var rockbottom = myGameArea.canvas.height - (this.height + 50);
        if (this.y > rockbottom) {
            this.y = rockbottom;
            grounded = true;

          }
        }
    this.moveForward = function() {
      this.x += obstacleSpeed;
    }
    this.hitObj = function (otherobj) {
      var left = this.x;
      var right = this.x + (this.width);
      var top = this.y;
      var bottom = this.y + (this.height);
      var otherLeft = otherobj.x;
      var otherRight = otherobj.x + (otherobj.width);
      var otherTop = otherobj.y;
      var otherBottom = otherobj.y + (otherobj.height);
      var crash = true;
      if ((bottom < otherTop) ||
      (top > otherBottom) ||
      (right < otherLeft) ||
      (left > otherRight)) {
        crash = false;
      }
      return crash;
    }
}

function everyinterval(n) {
  if ((myGameArea.frameNo / n) % 1 == 0) {return true;}
  return false;
}


function doKeyDown(e){
  if (e.keyCode == 32 && grounded == true) {
    grounded = false;
    myGamePiece.speedY -= 25;
    console.log(myGamePiece.speedY);
  }
}

function updateGameArea() {
  var x, y;
  for (i = 0; i < myObstacles.length; i += 1) {
    if (myGamePiece.hitObj(myObstacles[i])) {
      restartButton.update();
      gameOver = true;
      myGameArea.stop();
      return;
    }
  }
  myGameArea.clear();
  myGameArea.frameNo += 1;
  if (myGameArea.frameNo == 1 || everyinterval(150)) {
    x = myGameArea.canvas.width;
    y = myGameArea.canvas.height - 200
    myObstacles.push(new component(30, 60, "cactus.png", 1000, 163, "image"));
  }
  for (i = 0; i < myObstacles.length; i += 1) {
    myObstacles[i].x += obstacleSpeed;
    myObstacles[i].update();
  }
  myGamePiece.newPos();
  myGamePiece.update();
}

function clearmove() {
    myGamePiece.speedX = 0;
    myGamePiece.speedY = 0;
}
window.addEventListener("keydown", doKeyDown, false);
