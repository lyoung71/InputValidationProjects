import pyinputplus as pyip


def sandwich_maker():
    prices = {
        'white': 2.00, 'wheat': 3.00, 'sourdough': 3.50,
        'chicken': 3.50, 'turkey': 4.50, 'ham': 3.00, 'tofu': 2.00,
        'cheddar': 1.50, 'Swiss': 2.00, 'mozzarella': 1.50,
        'mmlt': 1.00
    }

    cost = 0

    bread = pyip.inputMenu(
        ['white', 'wheat', 'sourdough'],
        prompt="Which type of bread would you like?\n"
    )
    cost += prices[bread]

    protein = pyip.inputMenu(
        ['chicken', 'turkey', 'ham', 'tofu'],
        prompt="Which type of protein would you like?\n"
    )
    cost += prices[protein]

    cheese = pyip.inputYesNo(prompt="Would you like cheese?\n")

    if cheese == "yes":
        cheese_type = pyip.inputMenu(
            ['cheddar', 'Swiss', 'mozzarella'],
            prompt="Which type of cheese would you like?\n"
        )
        cost += prices[cheese_type]

    mmlt = pyip.inputYesNo(
        prompt="Would you like mayo, mustard, lettuce, or tomato?\n"
    )
    if mmlt == "yes":
        cost += prices['mmlt']

    num_of_sandwiches = pyip.inputInt(
        prompt="How many sandwiches?\n",
        min=1
    )

    total_cost = float(cost * num_of_sandwiches)

    return f"Your total cost will be ${total_cost:.2f}"


print(sandwich_maker())
