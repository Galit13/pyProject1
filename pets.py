import enum


class Pet(enum.Enum):
    Dog = 1
    Cat = 2
    Parrot = 3


DOG_SIMPLE_FOOD = 10
DOG_BETTER_FOOD = 20
DOG_BEST_FOOD = 30
CAT_SIMPLE_FOOD = 5
CAT_BETTER_FOOD = 10
CAT_BEST_FOOD = 15
PARROT_SIMPLE_FOOD = 2
PARROT_BETTER_FOOD = 6
PARROT_BEST_FOOD = 10

MONTHS = 12
DOG_CAPASITY = MONTHS / 1
CAT_CAPASITY = MONTHS / 2
PARROT_CAPASITY = MONTHS / 3

dog_simple_food_budget = DOG_CAPASITY * DOG_SIMPLE_FOOD
dog_better_food_budget = DOG_CAPASITY * DOG_BETTER_FOOD
dog_best_food_budget = DOG_CAPASITY * DOG_BEST_FOOD

cat_simple_food_budget = CAT_CAPASITY * CAT_SIMPLE_FOOD
cat_better_food_budget = CAT_CAPASITY * CAT_BETTER_FOOD
cat_best_food_budget = CAT_CAPASITY * CAT_BEST_FOOD

parrot_simple_food_budget = PARROT_CAPASITY * PARROT_SIMPLE_FOOD
parrot_better_food_budget = PARROT_CAPASITY * PARROT_BETTER_FOOD
parrot_best_food_budget = PARROT_CAPASITY * PARROT_BEST_FOOD

pet_type = Pet[input("Enter pet type ")].value
budget = int(input("Enter your budget "))

if budget >= parrot_simple_food_budget:
    if pet_type == Pet.Dog.value:
        if budget >= dog_best_food_budget:
            print("you can buy our best food for dogs")
        elif budget >= dog_better_food_budget:
            print("you can buy our better food for dogs")
        elif budget >= dog_simple_food_budget:
            print("you can buy our simple food for dogs")
        else:
            print("you can't buy any food for dogs")
    elif pet_type == Pet.Cat.value:
        if budget >= cat_best_food_budget:
            print("you can buy our best food for cats")
        elif budget >= cat_better_food_budget:
            print("you can buy our better food for cats")
        elif budget >= cat_simple_food_budget:
            print("you can buy our simple food for cats")
        else:
            print("you can't buy any food for cats")
    elif pet_type == Pet.Parrot.value:
        if budget >= parrot_best_food_budget:
            print("you can buy our best food for parrots")
        elif budget >= parrot_better_food_budget:
            print("you can buy our better food for parrots")
        elif budget >= parrot_simple_food_budget:
            print("you can buy our simple food for parrots")
        else:
            print("you can't buy any food for parrots")
else:
    print("you don't have enough for any food")

