def naam_en_leeftijd():
	    naam = input("Wat is jouw naam?")
	    leeftijd = input("Wat is jouw leeftijd?")
	    print("Jouw naam is", naam, "en jouw leeftijd is", leeftijd)
	    leeftijd_binnen_jaar = leeftijd + 1
	    print(leeftijd_binnen_jaar)


def naam_leeftijd_plaats_schooljaar():
    naam = input("Geef jouw naam")
    leeftijd = input("Geef je leeftijd")
    plaats = input("Geef je favoriete plaats")
    schooljaar = input("Welk school jaar zit je")
    
    story  = print("Er was eens een kind met de naam", naam, "Hij was", leeftijd, "jaar en zat in het", schooljaar, ".", "Zijn lievelings plaats was", plaats, "."
