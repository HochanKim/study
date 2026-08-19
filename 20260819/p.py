drink = {
  "콜라": [1500, 3],
  "사이다": [1300, 2],
  "물": [800, 5],
}

print(drink.get("콜라"))
print(drink.get("콜라")[0])
print(drink.get("콜라")[1])
print(drink.get("게토레이"))