import random
answers = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes - definitely.', 'You may rely on it.',
           'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
           'Reply hazy, try again.',
           'Ask again later.', 'Better not to tell you now.', 'Cannot predict now.', 'Concentrate and ask again.',
           'Don\'t Count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful']
isactive = 1


def genanswer():
    return random.choice(answers)


while isactive:
    log_file = open('logs.txt', 'a')
    print('To exit the program type \'Exit\' or \'Bye\'')
    question = input('Ask a question: ')
    log_file.write('\nQuestion: ' + question)
    if question.lower() == 'exit' or question.lower() == 'bye':
        log_file.close()
        isactive = 0
    else:
        answer = genanswer()
        log_file.write('\nAnswer: ' + answer)
        print(answer)
