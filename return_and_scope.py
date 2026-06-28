# Question 1
score = 10

def update_score():
    score = 5
    score = score + 3
    print(score)

update_score()
print(score)
# 8,10

# Question 2
name = "Agent"
level = 2

def show_info():
    name = "Spy"
    level = 4
    power = level * 10
    print(name)
    print(power)

show_info()
print(name)
print(level)
# "spy",40,"agent",2

# Question 3
coins = 20

def mission_reward(coins):
    coins = coins + 10
    coins = coins * 2
    print(coins)

mission_reward(5)
print(coins)
# 30,20

# Question 4
health = 100

def take_damage(damage):
    health = 100
    health = health - damage
    damage = damage + 5
    print(health)
    print(damage)

take_damage(30)
print(health)
# 70,35,100

# Question 5
items = ["map", "key"]

def add_item():
    items.append("torch")
    items.append("coin")
    print(items)

add_item()
print(items)
# map,key,torch,coin,map,key,torch,coin

# Question 6
items = ["map", "key"]

def replace_items():
    items = ["potion"]
    items.append("shield")
    print(items)

replace_items()
print(items)
# potion,shield,map,key

# Question 7
points = 3

def add_points():
    global points
    points = points + 7
    points = points * 2
    print(points)

add_points()
print(points)
# 20,20

# Question 8
status = "waiting"

def outer():
    status = "ready"

    def inner():
        status = "running"
        print(status)

    inner()
    print(status)

outer()
print(status)
# running , ready,weiting

# Question 9
coins = 10

def outer():
    coins = 5

    def inner():
        nonlocal coins
        coins = coins + 3
        coins = coins * 2
        print(coins)

    inner()
    print(coins)

outer()
print(coins)
# 16,16,10