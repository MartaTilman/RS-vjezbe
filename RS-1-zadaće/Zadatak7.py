#prviZad
def provjeri_lozinku():
    lozinka = input("Unesite lozinku: ")
    if len(lozinka) < 8 or len(lozinka) > 15:
        print("Lozinka mora sadržavati između 8 i 15 znakova.")
  
    if not any(char.isupper() for char in lozinka) or not any(char.isdigit() for char in lozinka):
      print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj.")
      if lozinka == "password" or lozinka == "lozinka":
        print("Lozinka ne smije biti 'password' ili 'lozinka'.")
    else :
      print("Lozinka je jaka!")
provjeri_lozinku()

input("Pritisnite Enter za izlaz...")
