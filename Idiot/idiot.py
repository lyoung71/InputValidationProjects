import pyinputplus as pyip


def english_idiot():
    while True:
        prompt = 'Want to know how to keep an idiot busy for hours?\n'
        response = pyip.inputYesNo(prompt)
        if response == "no":
            break
    print('Thank you. Have a nice day.')


def idiota_español():
    while True:
        prompt = 'Quieres saber cómo mantener a un idiota ocupado por horas?\n'
        response = pyip.inputYesNo(prompt, yesVal="sí", noVal="no")
        if response == "no":
            break
    print("Gracias. Que tenga un buen dia.")


def idiota_português():
    while True:
        prompt = "Quer saber como manter um idiota ocupado por horas?\n"
        response = pyip.inputYesNo(prompt, yesVal="sim", noVal="não")
        if response == "não":
            break
    print("Obrigado. Que tenha um bom dia.")


print(idiota_português())
