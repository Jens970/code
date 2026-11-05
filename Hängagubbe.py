import random


ord_lista = ["sam", "vide",  "johannes", "isak", "vilmer", "jens", "junior", "gustav", "arvid", "hektor", "colin", "oliver", "nellie", "jose", "emmett"]
hemligt_ord = random.choice(ord_lista) 
gissade_bokstäver = []
felaktiga_gissningar = 0
max_fel = 6


print("Välkommen till Hänga gubbe!")

while felaktiga_gissningar < max_fel:
  
    visat_ord = ""
    for bokstav in hemligt_ord:
        if bokstav in gissade_bokstäver:
            visat_ord += bokstav + " "
        else:
            visat_ord += "_ "

    print("\nOrd:", visat_ord.strip())
    print(f"Felaktiga gissningar kvar: {max_fel - felaktiga_gissningar}")

    
    if all(bokstav in gissade_bokstäver for bokstav in hemligt_ord):
        print(f"\nGrattis! Du klarade det. Ordet var '{hemligt_ord}'.")
        break

   
    gissning = input("Gissa en bokstav: ").lower()

    if len(gissning) != 1 or not gissning.isalpha():
        print("Vänligen skriv en enda bokstav.")
        continue

    if gissning in gissade_bokstäver:
        print("Du har redan gissat den bokstaven.")
        continue

    gissade_bokstäver.append(gissning)

    if gissning not in hemligt_ord:
        felaktiga_gissningar += 1
        print(f"Fel! '{gissning}' finns inte i ordet.")

else:
    print(f"\nGame Over! Hängd! Ordet var '{hemligt_ord}'.")
 
                 