def fnCezar(cistopis, kljuc, razdeljeno):
    rezultat = ""

    for c in cistopis:
        if razdeljeno:
            if c.islower():
                # male crke: a–z (ASCII 97–122)
                nova_koda = ((ord(c) - ord("a") + kljuc) % 26) + ord("a")
                rezultat += chr(nova_koda)
            elif c.isupper():
                # velike črke: A–Z (ASCII 65–90)
                nova_koda = ((ord(c) - ord("A") + kljuc) % 26) + ord("A")
                rezultat += chr(nova_koda)
            elif c.isdigit():
                # stevilke: 0–9 (ASCII 48–57)
                nova_koda = ((ord(c) - ord("0") + kljuc) % 10) + ord("0")
                rezultat += chr(nova_koda)
            else:
                rezultat += c
        else:
            if 32 <= ord(c) <= 126:
                nova_koda = ((ord(c) - 32 + kljuc) % 95) + 32
                rezultat += chr(nova_koda)
            else:
                rezultat += c

    return rezultat


def fnCezarBruteForce(word, length, razdelejno=0):
    print(f"\nword={word}, length={length}")
    x = 1
    while x <= length:
        print(
            f"x={x}: {word} --> {fnCezar(cistopis=word, kljuc=x, razdeljeno=razdelejno)}"
        )
        x = x + 1


## TODO: Fix it
def fnVigener(cistopis, kljuc, smer=True):
    sifropis = ""
    k_ind = 0

    for c in cistopis:
        if c.isalpha():
            zamik = ord(kljuc[k_ind] - ord("A"))

            if smer == False:
                zamik *= -1
            sifropis = sifropis + fnCezar(cistopis=c, kljuc=k_ind, razdeljeno=0)
            k_ind = (k_ind + 1) % len(kljuc)
        else:
            sifropis = sifropis + c

    return sifropis


import random
import string

# Globalna naključna abeceda (lahko jo definiraš tudi znotraj funkcije)
# Npr. A-Z zmešamo v nov vrstni red
nakljucna_abeceda = list(string.ascii_uppercase)
random.seed(42)  # Za ponovljivost – odstrani za pravo naključnost
random.shuffle(nakljucna_abeceda)

# Ustvariš mape za šifriranje in dešifriranje
standard_abeceda = list(string.ascii_uppercase)

mapa_sifriranje = {
    standard: nadomestek
    for standard, nadomestek in zip(standard_abeceda, nakljucna_abeceda)
}
mapa_desifriranje = {v: k for k, v in mapa_sifriranje.items()}


def fnSubstitucija(cistopis, smer):
    rezultat = ""

    for c in cistopis:
        if c in " .,":
            rezultat += c
        elif c.isupper():
            if smer == 1:
                rezultat += mapa_sifriranje.get(c, c)
            else:
                rezultat += mapa_desifriranje.get(c, c)
        elif c.islower():
            velika = c.upper()
            if smer == 1:
                sifr = mapa_sifriranje.get(velika, velika)
                rezultat += sifr.lower()
            else:
                desifr = mapa_desifriranje.get(velika, velika)
                rezultat += desifr.lower()
        else:
            rezultat += c

    return rezultat


def specialNaloga():
    rezultat = ""
    key = ""

    return rezultat


if __name__ == "__main__":

    # 1. naloga
    key = -10
    print(f"Cezar code for key '{key}': {fnCezar("tolk", key, razdeljeno=0)}")

    # 2. naloga
    # brute force
    # fnCezarBruteForce("szwo", 26, 1)

    # fnCezarBruteForce("Hzgxkcdhi", 26, 1)

    # fnCezarBruteForce("l#,9b-zz|9g~1.)(9$~9(z*)0~}z&9%)(~|9-0~.z94z9&~.)9KIOIG ", 26, 1)

    print(f"Halo --> {fnSubstitucija(cistopis="Halo", smer=1)}")
    print(f"{fnSubstitucija(cistopis="Halo", smer=0)} --> Halo")
