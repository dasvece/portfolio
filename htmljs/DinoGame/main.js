var myGamePiece;
var myY;
var grounded = false;
var obstacleSpeed;
var myObstacles = [];
var gameOver = false;
var gameStarted = false;
var score = 0;
var frequency = 100; //every 100 frames.
var maxFrequency = 50;
var highScore = 0;
var maxScore = 99999;
var container = document.getElementById("container");
var dead = false;


function startGame() {
    myGamePiece = new component(75, 75, "dino.png", 20, 120, "image");
    restartButton = new component(75, 75, "restart.png", 425, 100, "image");
    jumpSound = new sound("jump.mp3");
    deathSound = new sound("death.mp3");
    myGamePiece.gravity = 0.1;
    myObstacles = [];
    score = 0;
    obstacleSpeed = -7;
    gameOver = false;
    dead = false;
    frequency = 100;
    myGameArea.start();
}

var myGameArea = {
    canvas : document.createElement("canvas"),
    start : function() {
        this.canvas.width = 1000;
        this.canvas.height = 270;
        this.context = this.canvas.getContext("2d");
        document.body.insertBefore(this.canvas, document.body.childNodes[0]);
        this.frameNo = 0;
        this.interval = setInterval(updateGameArea, 20); //updates game 50 times per second.
        var ctx = this.canvas.getContext("2d");
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
        this.speedY *= 0.9;
        this.hitBottom();
    }
    this.hitBottom = function() {
        var rockbottom = myGameArea.canvas.height - (this.height + 45);
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
  if(e.keyCode == 32 && !gameStarted|| e.keyCode == 87 && !gameStarted|| e.keyCode == 38 && !gameStarted){
      jumpSound.play();
      myGamePiece.speedY -= 25;
      gameStarted = true;
  }
  if (e.keyCode == 32 && grounded|| e.keyCode == 87 && grounded|| e.keyCode == 38 && grounded) { //includes spacebar, w, up arrow
    jumpSound.play();
    grounded = false;
    myGamePiece.speedY -= 25;
    console.log(myGamePiece.speedY);
  }
}

function restart() {
  myGameArea.canvas.removeEventListener("click", restart);
  myGameArea.stop();
  myGameArea.clear();
  startGame();
}

function death() {
  deathSound.play();
}

function updateGameArea() {
  var x, y;
  if(!gameOver) {
    for (i = 0; i < myObstacles.length; i += 1) {
      if (myGamePiece.hitObj(myObstacles[i])) {
        restartButton.update();
        ctx.font = "50px Arial";
        ctx.fillText("Game Over", 325, 75);
        ctx.fillStyle = "#535353";
        gameOver = true;
        if(gameOver) {
          death();
          myGameArea.canvas.addEventListener("click", restart);
          return dead
        }
        //myGameArea.stop();
        return;
      }
    }
  }
  if (!gameOver && gameStarted){
    container.appendChild(myGameArea.canvas);
    score += 1;
    myGameArea.clear();
    myGameArea.frameNo += 1;
    if(myGameArea.frameNo == 1 || everyinterval(400)) {frequency -= 5; console.log("obstacle frequency " + frequency);
    if(frequency <= maxFrequency){frequency = maxFrequency;}}
    if (myGameArea.frameNo == 1 || everyinterval(frequency)) {
      x = myGameArea.canvas.width;
      y = myGameArea.canvas.height - 200
      rNumber = Math.floor(Math.random() * 3) + 1;
      obstaclePosition = 950;
      for (i = 0; i < rNumber; i++){
        console.log("random number " + rNumber);
        obstaclePosition += 50; //pixels cacti appear apart from each other.
        myObstacles.push(new component(30, 60, "cactus.png", obstaclePosition, 163, "image"));
      }
    }
    if (myGameArea.frameNo == 1 || everyinterval(100)) { //Increase obstacleSpeed every 100 frames
      obstacleSpeed *= 1.1;
      if (obstacleSpeed < -25) {
        obstacleSpeed = -25; // caps the obstacleSpeed to -25
      }
      console.log(obstacleSpeed);
    }
    for (i = 0; i < myObstacles.length; i += 1) {
      myObstacles[i].x += obstacleSpeed;
      myObstacles[i].update();
    }
    myGamePiece.newPos();
    myGamePiece.update();
    ctx.font = "30px Arial";
    ctx.fillText(score, 900, 30); //scoreboard
    if(score > maxScore){score = maxScore;}
    ctx.font = "30px Arial";
    ctx.strokeText("HI " + highScore, 750, 30);
    if(score > highScore){highScore = score;}
    ctx.fillRect(0, 210, 1000, 2)
    ctx.fillStyle = "#535353"
  } else if (!gameOver){
    container.appendChild(myGameArea.canvas);
    myGamePiece.update();
    ctx.font = "50px Arial";
    ctx.fillText("Jump to Start", 325, 75);
    ctx.font = "20px Arial";
    ctx.fillText("Jump: W | Space | UP", 375, 110);
    ctx.fillRect(0, 210, 1000, 2)
    ctx.fillStyle = "#535353"
  }
}

function sound(src) {
  this.sound = document.createElement("audio");
  this.sound.src = src;
  this.sound.setAttribute("preload", "auto");
  this.sound.setAttribute("controls", "none");
  this.sound.style.display = "none";
  this.sound.volume = 0.4;
  this.sound.loop = false;
  document.body.appendChild(this.sound);
  this.play = function (){
    this.sound.play();
  }
  this.stop = function(){
    this.sound.pause();
  }
}

function clearmove() {
    myGamePiece.speedX = 0;
    myGamePiece.speedY = 0;
}
window.addEventListener("keydown", doKeyDown, false);
