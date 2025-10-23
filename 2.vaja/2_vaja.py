from collections import Counter
import string, random
from pypdf import PdfReader

ciphertext = """HPBKVLZRSOVGZYLBGBDMFDRHRMRHSPBKHZY VBHDBGBJ RYSNBSUB 
PKSNHPOBFLBQYHKYBMPHRDBSUBZAGHPR WRBGV BV ZAGK NBQHRYBKHZY VR 
WRBGKKSVNHPOBRSBGBV OMAGVBDLDR JBRY BMPHRDBJGLBF BDHPOA BA RR VDBRY 
BJSDRBKSJJSPBZGHVDBSUBA RR VDBRVHZA RDBSUBA RR VDBJHWRMV DBSUBRY BGFSI 
BGPNBDSBUSVRYBRY BV K HI VBN KHZY VDBRY BR WRBFLBZ VUSVJHPOBGPBHPI VD 
BDMFDRHRMRHSP"""

clean_text = """JERMAN KAKŠNA JE BILA BESEDA KI STE JO REKLI KAJ STE IZNAŠLI DA BI ME DO DNA RANILI HLAPCI 
ZA HLAPCE ROJENI ZA HLAPCE VZGOJENI USTVARJENI ZA HLAPČEVANJE GOSPODAR SE MENJA BIČ PA 
OSTANE IN BO OSTAL NA VEKOMAJ ZATO KER JE HRBET SKRIVLJEN BIČA VAJEN IN ŽELJAN GLAS OD 
OKNA ALI STE MOŽJE DA POSLUŠATE GLASOVI VSIVPREK LAKOT TI NAS BOŠ ZMERJAL NA CESTO 
UDARITE JERMAN STOPI Z ENO NOGO NA STOL Z DRUGO NA MIZO HLAPCI MED VAS BI KRISTUS NE 
PRIŠEL Z BESEDO PRIŠEL BI Z BIČEM NOREC KI SE JE NAPRAVIL DA BI VAM ODKLEPAL TO PAMET 
DEVETKRAT ZAKLENJENO GLASOVI ZADOSTI JE KDO JE HLAPEC ŽENSKI GLASOVI ALI STE MOŽJE ALI 
NISTE ALI DA GA ME RAZPRASKAMO"""

ciphertext = ciphertext.replace("\n", "")
clean_text = clean_text.replace("\n", "")


def fnSubstitucija(cistopis, smer, abeceda):
    rezultat = ""

    nakeyna_abeceda = list(abeceda)
    random.seed(42)
    random.shuffle(nakeyna_abeceda)

    standard_abeceda = list(abeceda)

    mapa_sifriranje = {s: n for s, n in zip(standard_abeceda, nakeyna_abeceda)}
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
                rezultat += mapa_sifriranje.get(velika, velika).lower()
            else:
                rezultat += mapa_desifriranje.get(velika, velika).lower()
        else:
            rezultat += c

    return rezultat


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


def fnAnaliza(text: str):

    text_temp = text
    frek_char = Counter(text_temp)
    start_char = []

    start_char.append(text[0])
    for i in range(len(text) - 1):
        if text[i] == " ":
            start_char.append(text[i + 1])

    bigrami = [text_temp[i : i + 2] for i in range(len(text_temp) - 1)]
    frek_bigrami = Counter(bigrami)

    trigrami = [text_temp[i : i + 3] for i in range(len(text_temp) - 1)]
    frek_trigrami = Counter(trigrami)

    print("\n-----Frekvenca_posameznih_crk-----")

    for char, num in frek_char.most_common():
        print(f"Crka {char}: {num}")

    print("\n-----Frekvenca_bigramov-----")
    for bigr, num in frek_bigrami.most_common():
        print(f"Bigram {bigr}: {num}")

    print("\n-----Frekvenca_trigramov-----")
    for trig, num in frek_trigrami.most_common():
        print(f"Trigram {trig}: {num}")

    return frek_char, frek_bigrami, frek_trigrami


def clean_besedilo(text):
    return "".join([c.upper() if c.isalpha() or c == " " else "" for c in text])


if __name__ == "__main__":
    # 1. naloga
    # fnAnaliza(ciphertext)
    char, _, _ = fnAnaliza(text=ciphertext)

    print(f"Char: {char}")

    key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    abc = "L_-S-BAIVMCYUDGNWTO-FRX-HPE"

    # ciphertext = fnVigenere(ciphertext, key=key, smer=1)

    # print(fnSubstitucija(ciphertext, smer=0, abeceda=abc))

    with open("2.vaja/Na_klancu.txt", encoding="utf-8") as f:
        besedilo = f.read()

    clean = clean_besedilo(besedilo)
    print(clean)

    abeceda = list("A B C Č D E F G H I J K L M N O P R S Š T U V Z Ž".replace(" ", ""))
    permutacija = abeceda.copy()
    random.shuffle(permutacija)
    kljuc = dict(zip(abeceda, permutacija))

    print(permutacija)

    char1, bigr1, tri1 = fnAnaliza(clean_text)
    char2, bigr2, tri2 = fnAnaliza(clean)

    print(char1)
    print(char2)
