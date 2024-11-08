class Skolotajs:
    def __init__(self, vards, uzvards, stundu_sk_nedela, tips, tipssk):
        self.vards = vards
        self.uzvards = uzvards
        self.stundu_sk_nedela = stundu_sk_nedela
        self.tips = tips
        #self.tipssk = tipssk

    def idrukat(self):
        pass


class SakumskolasSkolotajs:
    def __init__(self, uzvards, tips, pasniektu_stundu_sk, skolotaja_klase):
        self.uzvards = uzvards
        self.tips = tips
        self.pasniektu_stundu_sk = pasniektu_stundu_sk
        self.skolotaja_klase = skolotaja_klase

    def izdrukat1():
        return ("Sākumskolas skolotājs: {} {} pasniedz {} stundas {} klasei").format(tips, uzvards, pasniektu_stundu_sk, skolotaja_klase)

print("\n")

class VidusskolasSkolotajs:
    def __init__(self, uzvards, pirmtips, pirmst, otrstips, otrsst, kopst, skolotaja_klase,):
        self.uzvards = uzvards
        self.pirmtips = pirmtips
        self.pirmst = pirmst
        self.otrtips = otrstips
        self.otrsst = otrsst
        self.kopst = kopst
        self.skolotaja_klase = skolotaja_klase

    def izdrukat2():
        return ("Vidusskolas skolotājs: {} pasniedz {} {} stundas un {} {} nedēļā {} klasei, kopā {} stundas").format(uzvards, primst, pirmtips, otrsst, otrtips, skolotaja_klase, kopst)

tipssk = input("Izvēlieties skolotāja tipu (tips 1 =  sākumskola), (tips 3 =  vidusskola): ")

if tipssk=="1":
    uzvards = input("Ievadiet sākumskolas skolotaja uzvārdu: ")
    tips = input("Ievadiet sākumskolas skolotāja priekšmetu: ")
    pasniektu_stundu_sk = int(input("Ievadiet pasniekto stundu skaitu: "))
    skolotaja_klase = input("Ievadiet sākumskolas skolotāja klasi: ")
    print("\n")
    print(SakumskolasSkolotajs.izdrukat1())

elif tipssk=="3":
    uzvards = input("Ievadiet vidusskolas skolotāja uzvārdu: ")
    pirmtips = input("Ievadiet vidusskolas skolotāja pirmo priekšmetu: ")
    primst = int(input("Ievadiet primā priekšmeta stundu skaitu nedēļā: "))
    otrtips = input("Ievadiet vidusskolas skolotāja otro priekšmetu: ")
    otrsst = int(input("Ievadiet otrš priekšmeta stundu skaitu nedēļā: "))
    skolotaja_klase = input("Ievadiet klase ko skolotājs māca: ")
    kopst = primst + otrsst
    print("\n")
    print(VidusskolasSkolotajs.izdrukat2())

else:
    print("Šāda tipa nepastāv")




