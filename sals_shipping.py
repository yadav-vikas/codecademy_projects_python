
def ground_shipping_cost(weight):
  if weight <= 2:
    price_per_pound= 1.50
  elif weight > 2 and weight <=6:
    price_per_pound=3.00
  elif weight > 6 and weight <=10:
    price_per_pound=4.00
  else:
    price_per_pound=4.75
  return 20 + (price_per_pound * weight) 

print(ground_shipping_cost(8.4))

premium_ground_shipping = 125.00

def drone_shipping_cost(weight):
  if weight <= 2:
    price_per_pound= 4.50
  elif weight > 2 and weight <=6:
    price_per_pound=9.00
  elif weight > 6 and weight <=10:
    price_per_pound=12.00
  else:
    price_per_pound=14.25
  return 0 + (price_per_pound * weight) 

print(drone_shipping_cost(1.5))

def cheapest_price(weight):
  ground=ground_shipping_cost(weight)
  drone=drone_shipping_cost(weight)
  premium=premium_ground_shipping
  if ground < drone and ground < premium :
    method="Ground"
    cost=ground
  elif premium < ground and premium < drone :
    method="Premium Ground"
    cost=premium
  else:
    method="Drone"
    cost=drone
  return cost,method
  

print(cheapest_price(4.8))
print(cheapest_price(41.5))
