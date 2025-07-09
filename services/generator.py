import random

adjectives = ["Fast", "Dark", "Silent", "Crazy", "Mighty", "Shiny"]
nouns = ["Tiger", "Ninja", "Wizard", "Knight", "Ghost", "Wolf"]

def generate_nickname():
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randint(10, 999)
    return f"{adj}{noun}{number}"
