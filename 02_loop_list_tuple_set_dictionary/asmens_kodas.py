while True:
    asmens_kodas = input("Įveskite asmens kodą arba 0 kad išeiti: ")
    if asmens_kodas == '0':
        print('viso gero :)')
        break
    # ar visi skaičiai ir ar jų 11?
    if not asmens_kodas.isnumeric() or len(asmens_kodas) != 11:
        print('Neteisingas: turi būti 11 skaitmenų skaičius.')
        continue
    menuo = int(asmens_kodas[3:5])
    print('menuo:', menuo)
    if menuo < 1 or menuo > 12:
        print('Neteisingas: mėmnuo gimimo datoje negali būti didesnis už 12 arba lygus 0.')
        continue
    diena = int(asmens_kodas[5:7])
    print('diena', diena)
    # TODO: patikrini priklausomai nuo mėnesio
    if diena < 1 or diena > 31:
        print('Neteisingas: diena gimimo datoje negali būti didesnė už 31 arba lygus 0.')
        continue
    # Paskutinio skaičiaus tikrinimas
    daugikliai = '1234567891'
    kiti_daugikliai = '3456789123'
    kontrolinis = 0
    for daugiklio_nr, skaitmuo in enumerate(asmens_kodas[:10]):
        kontrolinis += int(skaitmuo) * int(daugikliai[daugiklio_nr])
    print('kontorlinis:', kontrolinis, kontrolinis % 11)
    if kontrolinis % 11 == 10:
        kontrolinis = 0
        for daugiklio_nr, skaitmuo in enumerate(asmens_kodas[:10]):
            kontrolinis += int(skaitmuo) * int(kiti_daugikliai[daugiklio_nr])
        print('kitas kontorlinis:', kontrolinis, kontrolinis % 11)
    tikrinamas = kontrolinis % 11
    if tikrinamas == 10:
        tikrinamas = 0
    paskutinis = int(asmens_kodas[10])
    if paskutinis != tikrinamas:
        print('Neteisingas: paskutinis skaičius klaidingas.')
        continue
    print('TEISINGAS')
