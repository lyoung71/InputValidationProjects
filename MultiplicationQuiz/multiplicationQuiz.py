import pyinputplus as pyip
import random, time


numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    answer = num1 * num2
    prompt = f'#{questionNumber}: {num1} * {num2} = '

    try:
        pyip.inputStr(
            prompt, allowRegexes=[fr'^{answer}$'],
            blockRegexes=[('.*', 'Incorrect!')],
            timeout=8, limit=3
            )
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAnswers += 1

    time.sleep(1)
    print(f'Score: {correctAnswers}/{numberOfQuestions}')
