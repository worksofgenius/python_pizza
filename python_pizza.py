# Types of pizzas sold
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Cost of pizzas
prices = [2, 6, 1, 3, 2, 7, 2]

# Count number of occurances of 2 dollar slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Length of toppings list
num_pizzas = len(toppings)

print("We sell", num_pizzas, "different kinds of pizza!")

# New pizza data
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)

# Sort by ascending price
pizza_and_prices.sort()
print(pizza_and_prices)

# Cheapest pizza
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

# Priciest pizza
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

# Anchovies sold out
pizza_and_prices.pop(-1)
print(pizza_and_prices)

# Add new topping
pizza_and_prices.insert(-2,[2.5, "peppers"])
print(pizza_and_prices)

# Sell 3 cheapest pizzas
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
