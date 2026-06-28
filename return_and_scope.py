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