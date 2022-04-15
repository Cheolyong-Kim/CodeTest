animation = {
    "Pokemon" : "Pikachu",
    "Digimon" : "Agumon",
    "Yugioh" : "Black Magician"
    }

name = input()

print(animation.get(name) if animation.get(name) else "I don't know")