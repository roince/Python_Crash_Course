import random

"""
# Start with empty dictionary add
alien = {}

alien['color']= 'red'
alien['points'] = 5
print(f"Alien-color : {alien['color'].title()}; Award-Point : {alien['points']}")

# add key pair into dictionary
alien['x_pos'] = 10
alien['y_pos'] = 20
print(alien)

# remove one item from dic
del alien['points']
print(alien)

# multi-line dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
# loop through a dictionary
for key, value in favorite_languages.items():
    print(f"\nKey : {key}")
    print(f"Value : {value}")


alien_0 = c
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
"""
# init a list of aliens
aliens = []

# make 30 aliens and add it into the list
alien_colors = ['green', 'yellow', 'blue', 'red']
alien_points = [5, 10, 15]
alien_speeds = ['fast', 'medium', 'slow']

for alien_number in range(30):
    new_alien = {'color': alien_colors[random.randint(0, 3)], 'points':
        alien_points[random.randint(0, 2)], 'speed': alien_speeds[
        random.randint(0, 2)]}
    aliens.append(new_alien)
print(f"In total, there are {len(aliens)} aliens!")
print(aliens)
