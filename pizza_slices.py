toppings = ['pepperoni','pineeapple','cheese','sausage','olives',
'anchovies','mushrooms']
print(toppings)
prices = [2,6,1,3,2,7,2]
num_pizzas = len(toppings)
print(num_pizzas)
print("We sell %d diffrent kids of pizza!"%(num_pizzas))
pizzas = list(zip(prices,toppings))
print(pizzas)
pizzas.sort()
cheapest_pizza = sorted(pizzas)
priciest_pizza= pizzas[-1]
print(priciest_pizza)
three_cheapest = pizzas[:3]
print(three_cheapest)
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
