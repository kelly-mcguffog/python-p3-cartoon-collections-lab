def roll_call_dwarves(dwarves):
    for index, item in enumerate(dwarves):
        print(f"{index+1}. {item}")

def summon_captain_planet(planeteer_calls):
    return [f"{call.title()}!" for call in planeteer_calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False


def find_the_cheese(items):
    cheeses = ["cheddar", "gouda", "camembert"]
    for cheese in cheeses:
        if cheese in items:
            return cheese
        else:
            return None

