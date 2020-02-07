import random


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "Who created Mario?\n(a) Nintendo\n(b) Bethesda\n(c) Kroger\n",
    "What color is chocolate?\n(a) Yellow\n(b) Brown\n(c) Red\n",
    "What color is the sky?\n(a) Green\n(b) Purple\n(c) Blue\n",
    "What language is this program written in?\n(a) Java\n(b) Python\n(c) C#\n",
    "What module will randomly pick objects?\n(a) random\n(b) math\n(c) wxPython\n",
    "What animation studio developed Howl's Moving Castle?\n(a) Pixar\n(b) Studio Ghibli\n(c) Disney\n",
    "What company invented the Playstation?\n(a) Sony\n(b) Samsung\n(c) Vizio\n",
    "What class is this project for?\n(a) Business\n(b) Fundamentals of Programming\n(c) Chemistry\n",
    "Who is the current Amazon CEO?\n(a) Bill Gates\n(b) Steve Wozniak\n(c) Jeff Bezos\n",
    "What game are we all hoping doesn't flop?\n(a) Cyberpunk 2077\n(b) Mount and Blade Bannerlord\n(c) Microsoft Flight Simulator\n",
    "What insect are the pollinators of the planet?\n(a) Bees\n(b) Mosquitoes\n(c) Dogs\n",
    "What song from the Gorillaz is the most popular?\n(a) DARE\n(b) Clint Eastwood\n(c) Feel Good Inc.\n",
    "What is 2 + 2?\n(a) 3\n(b) 4\n(c) 123,100\n",
    "What animal always lands on their feet?\n(a) Dogs\n(b) Cats\n(c) Sharks\n",
    "What two colors make Purple?\n(a) Blue/Red\n(b) Yellow/Red\n(c) Black/Blue\n",
    "Who was the first president of the United States?\n(a) Trump\n(b) Eminem\n(c) George Washington\n",
    "What game is a hat trading simulator?\n(a) Half Life\n(b) Call of Duty\n(c) Team Fortress 2\n",
    "What is the best candy bar?\n(a) Hershey's Bar\n(b) Payday\n(c) Zero bar\n",
    "Which hero shoots webs?\n(a) Spiderman\n(b) Superman\n(c) Thanos\n",
    "Brunch is a combination of...?\n(a) Dinner/Breakfast\n(b) Breakfast/Lunch\n(c) Breakfast/Breakfast\n"
]

question_pool = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "c"),
    Question(question_prompts[9], "a"),
    Question(question_prompts[10], "a"),
    Question(question_prompts[11], "c"),
    Question(question_prompts[12], "b"),
    Question(question_prompts[13], "b"),
    Question(question_prompts[14], "a"),
    Question(question_prompts[15], "c"),
    Question(question_prompts[16], "c"),
    Question(question_prompts[17], "c"),
    Question(question_prompts[18], "a"),
    Question(question_prompts[19], "b")
]


def shuffle():
    random.shuffle(question_pool)


def run_quiz():
    score = 0
    shuffle()
    chosen_questions = question_pool[slice(10)]
    for question in chosen_questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            score += 1
    print("You got", score, "out of", len(chosen_questions))


run_quiz()
