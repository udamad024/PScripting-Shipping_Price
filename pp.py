def ground_shipping(weight):
  if weight > 0 and weight < 2:
    return weight * 1.50 + 20
  elif weight > 2 and weight <= 6:
    return weight * 3 + 20
  elif weight > 6 and weight <= 10:
    return weight * 4 + 20
  elif weight > 10:
    return weight * 4.75 + 20

premium_ground_shipping = 125

def drone_shipping(weight):
  if weight > 0 and weight < 2:
    return weight * 4.50
  elif weight > 2 and weight <= 6:
    return weight * 9
  elif weight > 6 and weight <= 10:
    return weight * 12
  elif weight > 10:
    return weight * 14.25

print(drone_shipping(1.5))


