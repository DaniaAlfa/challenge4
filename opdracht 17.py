while True:

 print("Lootbox!")
 import random
 randomize=("Common","Uncommon","Rare","Epic","Legendary")

 begin = input("Wil je de lootbox openen? : ")
 if begin == "ja":
    print("Je hebt een! :")
    print(random.choice(randomize))
 else:
    print("Lootbox denied.")
    break