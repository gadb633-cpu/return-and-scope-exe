# # Question 1
# score = 10

# def update_score():
#     score = 5
#     score = score + 3
#     print(score)

# update_score()
# print(score)
# # 8,10

# # Question 2
# name = "Agent"
# level = 2

# def show_info():
#     name = "Spy"
#     level = 4
#     power = level * 10
#     print(name)
#     print(power)

# show_info()
# print(name)
# print(level)
# # "spy",40,"agent",2

# # Question 3
# coins = 20

# def mission_reward(coins):
#     coins = coins + 10
#     coins = coins * 2
#     print(coins)

# mission_reward(5)
# print(coins)
# # 30,20

# # Question 4
# health = 100

# def take_damage(damage):
#     health = 100
#     health = health - damage
#     damage = damage + 5
#     print(health)
#     print(damage)

# take_damage(30)
# print(health)
# # 70,35,100

# # Question 5
# items = ["map", "key"]

# def add_item():
#     items.append("torch")
#     items.append("coin")
#     print(items)

# add_item()
# print(items)
# # map,key,torch,coin,map,key,torch,coin

# # Question 6
# items = ["map", "key"]

# def replace_items():
#     items = ["potion"]
#     items.append("shield")
#     print(items)

# replace_items()
# print(items)
# # potion,shield,map,key

# # Question 7
# points = 3

# def add_points():
#     global points
#     points = points + 7
#     points = points * 2
#     print(points)

# add_points()
# print(points)
# # 20,20

# # Question 8
# status = "waiting"

# def outer():
#     status = "ready"

#     def inner():
#         status = "running"
#         print(status)

#     inner()
#     print(status)

# outer()
# print(status)
# # running , ready,weiting

# # Question 9
# coins = 10

# def outer():
#     coins = 5

#     def inner():
#         nonlocal coins
#         coins = coins + 3
#         coins = coins * 2
#         print(coins)

#     inner()
#     print(coins)

# outer()
# print(coins)
# # 16,16,10

# # Question 10
# score = 1
# bag = ["key"]

# def outer():
#     score = 10
#     bag.append("map")

#     def inner():
#         nonlocal score
#         score = score + 5
#         bag.append("coin")
#         print(score)
#         print(bag)

#     score = score * 2
#     inner()
#     print(score)
#     print(bag)

# outer()
# print(score)
# print(bag)
# # 25,key,map,coin,25,key,map,coin,1,key,map,coin

# 1. Mission Distance Converter
def receives_distance_meters_to_centimeters(meters):
    meters_to_centimeters = meters*100
    return meters_to_centimeters


def return_message_of_centimeters(centimeters_value):
    message =  f"Robot moved {centimeters_value} centimeters"
    return message

def meters_and_centimeters_distance(meters):

    centimeters = receives_distance_meters_to_centimeters(5)
    print(centimeters)
    message_of_centimeters = return_message_of_centimeters(centimeters)
    print(message_of_centimeters)
meters_and_centimeters_distance(5)

# 2. Simple Price Calculator
def adding_delivery_to_price(product_price):
    return product_price + 10

def multiplying_it_by_2(new_price):
    return new_price*2

def final_price(product_price):
    product_price_and_delivery = adding_delivery_to_price(product_price)
    multiplying = multiplying_it_by_2(product_price_and_delivery)
    print(multiplying)
final_price(680) 

# 3. Name Formatter
def conect_first_and_last_names(first_name,last_name):
    return first_name + " " + last_name

def change_full_name_to_uppercase(full_name_with_uppercase):
    return full_name_with_uppercase.upper()

def prepares_a_user_name(first_name,last_name):
    full_name=conect_first_and_last_names(first_name,last_name)
    uppercase = change_full_name_to_uppercase(full_name)
    print(uppercase)
prepares_a_user_name("gad","biton")

# 4. Temperature Report
def costing_Celsius_to_Fahrenheit(temperature_in_Celsius):
    return temperature_in_Celsius*9/5+32

def message_with_result(temperature_in_Fahrenheit):
    return f"the temperature in Fahrenheit is {temperature_in_Fahrenheit} costing from celsius"

def temperature_report(temperature_in_Celsius):
    costing = costing_Celsius_to_Fahrenheit(temperature_in_Celsius)
    sentens = message_with_result(costing)
    print(sentens)
temperature_report(68)    

# 5. Game Health Calculator
def health_after_damage(health,damaged):
    return health - damaged

def health_after_healing(health_after_damage_,add_healing):
    return health_after_damage_ + add_healing

def calculates_player_health(player_health,demaged,add_healing):
    health_after_damage_ = health_after_damage(player_health,demaged)
    return health_after_healing(health_after_damage_,add_healing)

print(calculates_player_health(100,30,20))

# 6. Shopping Bag Total
def calculate_prices_of_3_products(Pen_price, Notebook_price, Pencil_price):
    return Pen_price + Notebook_price + Pencil_price

def total_after_discount(total_price):
    return total_price * 0.80

def final_price(Pen_price, Notebook_price, Pencil_price):
    total_price = calculate_prices_of_3_products(Pen_price, Notebook_price, Pencil_price)
    final_price = total_after_discount(total_price)
    return f"final price is: {final_price}"

print(final_price(100,100,200))

# 7. Password Cleaner
def lowers_profits(password):
    return password.strip()

def return_length_password(cleaned_password):
    return len(cleaned_password)

def check_length(length_password):
    if length_password <= 8:
        return True
    else:
        return False
    
def return_result(password):
    clean_password = lowers_profits(password)
    length_password = return_length_password(clean_password)
    massage = check_length(length_password)
    return massage
print(return_result("check test"))

# 8. Student Grade Bonus
def adding_5_bonus_points(grade):
    return grade + 5

def grade_multiplied(new_grade):
    return new_grade * 1.1

def result_grade(final_grade):
    if final_grade < 100:
        return final_grade
    else:
        return 100
def massage(grade):
    new_grade = adding_5_bonus_points(grade)
    final_grade = grade_multiplied(new_grade)
    massage = result_grade(final_grade)
    return massage

print(massage(80))







