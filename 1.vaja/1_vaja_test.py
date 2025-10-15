import re

index = [
    52,
    62,
    72,
    123,
    125,
    135,
    142,
    152,
    177,
    178,
    185,
    200,
    204,
    210,
    216,
    315,
    321,
    322,
    358,
    373,
    376,
    377,
    378,
    405,
    432,
    464,
    468,
    470,
    489,
    641,
    650,
    667,
    701,
]


def popravi_sumnike(besedilo: str) -> str:
    # Slovenski šumniki z znakom ˇ pred črko
    nadomestitve = {"c": "č", "s": "š", "z": "ž", "C": "Č", "S": "Š", "Z": "Ž"}

    # Poišče vzorce ˇ + črka (lahko ima presledek vmes)
    popravljeno = re.sub(
        r"ˇ\s*([cszCSZ])", lambda m: nadomestitve.get(m.group(1), m.group(1)), besedilo
    )

    return popravljeno


# --- Primer uporabe ---
besedilo = """
 ˇ
 Zivimovinformacijski druˇzbi, v kateri se veˇc kot polovica bruto druˇzbenega proizvoda ustvari
 z ustvarjanjem, prenosom, obdelavo in prodajo informacij oziroma informacijskih storitev.
 Informacijsko komunikacijski sistemi (IKSi) so postali nujen del vsakodnevnega ˇzivljenja. Z
 njimi se sreˇcujemo, ko telefoniramo, gledamo televizijo, plaˇcujemo z banˇcno kartico, dvigamo
 denar na bankomatu, poˇsljemo elektronsko poˇsto, brskamo po svetovnem spletu inˇse pri mnogih
 drugih vsakodnevnih opravilih. ˇ Zivljenja brez IKS si praktiˇcno ne znamo veˇc predstavljati.
 Uporaba informacijsko komunikacijskih tehnologij (IKT) na vseh podroˇcjih ˇzivljenja je zago
tovo precej olajˇsala ˇzivljenje in dvignila njegovo kvaliteto, vendar je hkrati s tem prinesla tudi
 nevarnost njihove zlorabe. Z ozirom na veliko vrednost, ki jo imajo informacije v informacijski
 druˇzbi, je postala kraja informacij izredno privlaˇcna. Z vdorom v IKS nekega podjetja je mogoˇce
 priti do vseh informacij o poslovanju, trˇzni strategiji, novih produktih in podobno, kar lahko
 izkoristi konkurenca. Z vdorom v banˇcni je mogoˇce prenaˇsati denar iz enega raˇcuna na drug
 raˇcun oziroma ustvarjati nov denar, ki je v informacijski druˇzbi zgolj informacija v banˇcnem
 informacijskem sistemu, in na ta naˇcin neupraviˇceno pridobiti premoˇzenje. V vojaˇskem infor
macijskem sistemu lahko nasprotnik pridobi informacije, ki mu prinesejo taktiˇcno in strateˇsko
 prednost, kar lahko odloˇca o zmagi ali porazu. Vdor v na osebni raˇcunalnik lahko omogoˇci
 dostop do osebnih podatkov, dostop do banˇcnega raˇcuna in tudi krajo identitete, kar lahko last
niku povzroˇci nepopravljivo ˇskodo. Veliko ˇskodo lahko povzroˇci tudi izguba doloˇcenih podatkov
 zaradi neprevidnega upravljanje z njimi oziroma z informacijsko komunikacijskim sistemom, na
 katerem se hranijo.
 Zaradi velike vrednosti , ki jo imajo lahko doloˇceni podatki, in zardi velike ˇskode, ki jo
 lahko povzroˇci njihova izguba ali zloraba, jih je potrebno zaˇsˇcititi, ne glede na to ali gre za
 pomembne podatke drˇzavnih ustanov in podjetij ali pa za osebne podatke uporabnikov IKSa. V
 nadaljevanju bomo, zaradi preprostosti loˇcevali zgolj med podjetji in fiziˇcnimi osebami. Pod pod
jetje bomo razumeli tako podjetja kot tudi drˇzavne ustanove, druˇstva, organizacije in podobno,
 medtem ko bomo s pojmom fiziˇcne osebe oznaˇcevali uporabnike nekega zasebnega ali javno
 dostopnega IKSa za svoje osebne namene.
 Klasiˇcno so bili podatki shranjeni oziroma so se prenaˇsali veˇcinoma v tiskani obliki na pa
pirju. Z razvojem IKT se danes veˇcina podatkov shranjuje in prenaˇsa v elektronski obliki, zato
 se bomo v nadaljevanju posvetili le zaˇsˇciti podatkov v elektronski obliki. Za zaˇsˇcito podatkov
 v elektronski obliki je potrebno pravilno naˇcrtovati in tudi pravilno uporabljati IKSe v katerih
 se shranjujejo oziroma prenaˇsajo podatki. V nadaljevanju bomo spoznali razliˇcne postopke, ki
"""
beseda = ""

for x in index:
    beseda = beseda + besedilo[x]
print(popravi_sumnike(besedilo))

print(beseda)
