import pyinputplus as pyip
import random
import time


number_of_questions = 10
correct_answers = 0

for question_number in range(1, number_of_questions + 1):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    answer = num1 * num2
    prompt = f'#{question_number}: {num1} * {num2} = '

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
        correct_answers += 1

    time.sleep(1)
    print(f'Score: {correct_answers}/{number_of_questions}')
