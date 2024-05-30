data = [
    {
        'name': 'Aryan Jhagirdar',
        'follower_count': 29,
        'description': 'is A fellow capybara',
        'country': 'South America'
    },
    {
        'name': 'Shirish Sharma',
        'follower_count': 49,
        'description': 'is Very Handsome',
        'country': 'India'
    },
    {
        'name': 'Neev Pawar',
        'follower_count': 136,
        'description': 'is Cow',
        'country': 'where cow live ig'
    },
    {
        'name': 'Mayank Kakade',
        'follower_count': 98,
        'description': 'is Shaktiman',
        'country': 'India'
    },
    {
        'name': 'Vedant Lehane',
        'follower_count': 42,
        'description': 'Anime boi',
        'country': 'India'
    },
    {
        'name': 'Ananya Kamat',
        'follower_count': 192,
        'description': 'plays badminton and hate shivtare',
        'country': 'India'
    },
    {
        'name': 'Sairaj Ingawale',
        'follower_count': 315,
        'description': 'gay af',
        'country': 'India'
    },
    {
        'name': 'Gigachad Sarthak',
        'follower_count': 104,
        'description': 'Anime boi',
        'country': 'India'
    },
    {
        'name': 'Shravani Patil',
        'follower_count': 168,
        'description': 'is Short',
        'country': 'India'
    },
    {
        'name': 'Mayuresh',
        'follower_count': 749,
        'description': 'Cricket',
        'country': 'India'
    },
    {
        'name': 'Shaurya Pagar',
        'follower_count': 89,
        'description': 'CR7',
        'country': 'India'
    },
    
]
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
import random
print(logo)
def rand_chocie(l):
    return random.choice(l)
def rand_pick(a,b):
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.\n")
    print(vs + "\n")
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")
correct = 0
choice_1 = rand_chocie(data)
data.remove(choice_1)
while True:
    if correct != 0:
        print(f"You're right! Current score: {correct}.")
    choice_2 = rand_chocie(data)
    rand_pick(choice_1, choice_2)
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess == "a" and choice_1['follower_count'] > choice_2['follower_count']:
        print("Correct")
        correct += 1
        data.append(choice_1)
        choice_1 = choice_2
    elif guess == "a" and choice_1['follower_count'] < choice_2['follower_count']:
        print("You lose")
        break
    elif guess == "b" and choice_1['follower_count'] < choice_2['follower_count']:
        print("Correct")
        correct += 1
        data.append(choice_1)
        choice_1 = choice_2
    elif guess == "b" and choice_1['follower_count'] < choice_2['follower_count']:
        print("You lose")
        break
print(f"Sorry, that's wrong. Final score: {correct}")