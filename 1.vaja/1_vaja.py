import random
import string


def fnCezar(cistopis, key, razdeljeno):
    rezultat = ""
    for c in cistopis:
        if razdeljeno:
            if c.islower():
                nova_koda = ((ord(c) - ord("a") + key) % 26) + ord("a")
                rezultat += chr(nova_koda)
            elif c.isupper():
                nova_koda = ((ord(c) - ord("A") + key) % 26) + ord("A")
                rezultat += chr(nova_koda)
            elif c.isdigit():
                nova_koda = ((ord(c) - ord("0") + key) % 10) + ord("0")
                rezultat += chr(nova_koda)
            else:
                rezultat += c
        else:
            if 32 <= ord(c) <= 126:
                nova_koda = ((ord(c) - 32 + key) % 95) + 32
                rezultat += chr(nova_koda)
            else:
                rezultat += c
    return rezultat


def fnCezarBruteForce(text, razdeljeno=0):
    # uporabi razdeljeno argument
    if razdeljeno:
        max_shift = 25
    else:
        max_shift = 94

    for k in range(max_shift + 1):
        dec = fnCezar(cistopis=text, key=-k, razdeljeno=razdeljeno)
        print(f"shift={k:2d} -> {dec}")


def fnVigenere(cistopis, key, smer=1):
    cipher = ""
    k_ind = 0
    key = key.upper()
    for c in cistopis:
        if c.isalpha():
            zamik = ord(key[k_ind]) - ord("A")
            if smer == 0:
                zamik = -zamik
            nova = (ord(c) - ord("A") + zamik) % 26 + ord("A")
            cipher += chr(nova)

            k_ind = (k_ind + 1) % len(key)
        else:
            cipher += c

    return cipher


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


def specialNaloga():
    rezultat = ""
    key = ""

    return rezultat


if __name__ == "__main__":

    # 1. naloga
    key = 10
    word = "jeba"
    print(f"------------------------------------------------------------")
    print(f"Key:{key}")
    print(f"{word} --> {fnCezar(cistopis=word, key=key, razdeljeno=1)}")
    print(f"\nKey:{-key}")
    print(
        f"{fnCezar(cistopis=word, key=key, razdeljeno=1)} --> {fnCezar(cistopis=fnCezar(cistopis=word, key=key, razdeljeno=1), key=-key, razdeljeno=1)}"
    )

    # 2. naloga
    print(f"------------------------------------------------------------")
    words = [
        "szwo",
        "Hzgxkcdhi",
        "l#,9b-zz|9g~1.)(9$~9(z*)0~}z&9%)(~|9-0~.z94z9&~.)9KIOIG",
    ]

    x = 0
    while x <= 1:
        print(f"\nBrute force for: {words[x]}\n")
        fnCezarBruteForce(text=words[x], razdeljeno=1)
        x = x + 1

    print(f"\nBrute force for: {words[2]}\n")
    fnCezarBruteForce(text=words[2], razdeljeno=0)

    # 3. naloga
    print(f"------------------------------------------------------------")
    cipher = "LXFOPVEFRNHR"
    key = "LEMON"
    dec = fnVigenere(cipher, key, smer=0)
    print(dec)

    # 5. naloga
    print(f"------------------------------------------------------------")
    cipher = "OHV IWYXIEIR QAICEI VG S FZTYBR GY ZNTEMHMDNX NZHAVBVGWU MZXK OM MLDNX N GWKDEJ BT AGOEIJCNXI CRRGSK XIGUSJL"
    key = "VARNOST"
    dec = fnVigenere(cipher, key, smer=0)
    print(dec)

    # 6. naloga
    print(f"------------------------------------------------------------")
    word = "Crazy vaje."
    print(f"Plain text: {word}")
    enc = fnSubstitucija(cistopis=word, smer=1)
    print(f"Enc: {enc}")
    print(f"Dec: {fnSubstitucija(cistopis=enc, smer=0)}")
