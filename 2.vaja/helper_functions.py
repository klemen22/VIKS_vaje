import random
import string

# ------------------------------------------------------------------------------#
#                                     Vaja 1                                   #
# ------------------------------------------------------------------------------#


def fnSubstitucija(cistopis, smer):
    rezultat = ""

    nakeyna_abeceda = list(string.ascii_uppercase)
    random.seed(42)
    random.shuffle(nakeyna_abeceda)

    standard_abeceda = list(string.ascii_uppercase)

    mapa_sifriranje = {
        standard: nadomestek
        for standard, nadomestek in zip(standard_abeceda, nakeyna_abeceda)
    }
    mapa_desifriranje = {v: k for k, v in mapa_sifriranje.items()}

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
