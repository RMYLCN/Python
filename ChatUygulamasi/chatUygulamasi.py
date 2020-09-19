import kullanici
from datetime import date
import os
temizle=("cls" if  os.name == "nt" else "clear")

#-*-*-*-*-*-#
def mesajListele(kullaniciAdi):

	try:
		dosya = open("mesajlar.txt","r")
		satirlar = dosya.readlines()

		print("")
		print("    MESAJ KUTUSU")

		kontrol=0
		for satir in satirlar:

			mesaj = satir.split("||")

			if mesaj[1] == kullaniciAdi:
				kontrol += 1
				print("-"*80)
				print("")
				print(" ! {}. {}: {}'dan Mesaj Var '{}'".format(kontrol, mesaj[3], mesaj[0].capitalize(), mesaj[2] ))
				print("")
				print("-"*80)

			elif mesaj[0] == kullaniciAdi:
				kontrol += 1
				print("-"*80)
				print("")
				print("{}. {}: {}'a Gönderilen Mesaj '{}'".format(kontrol, mesaj[3], mesaj[1].capitalize(), mesaj[2] ))
				print("")
				print("-"*80)

		if kontrol==0:
			print("---- Yeni Mesajınız Bulunmamaktadır ----")
	
		input("Yeni Bir Mesaj Yazmak İçin Bir Tuşa Basın")

	except FileNotFoundError:
		print("____ Hiç Kimsenin Mesajı Yok Ki, Ne Sessiz Bir Dünya ___")
		print()
		input("Hadi İlk Adımı Sen Atmak İçin Bir Tuşa Bas")

def mesajGonder(**kwargs):
	dosya = open("mesajlar.txt","a")
	dosya.write( kwargs["kullaniciAdi"].lower() + "||" + kwargs["hedef"].lower() + "||" + kwargs["mesaj"] + "||" + str(kwargs["tarih"]) + "||" + "\n" )
	input("{},{} kişisine mesaj gönderdi.".format(kwargs["kullaniciAdi"],kwargs["hedef"]))

def arkadasEkle(**kwargs):

	ben=kwargs["ben"].lower()
	arkadas=kwargs["arkadas"]

	dosya=open("arkadasliklar.txt","a")
	dosya.write(kwargs["ben"].lower() + " " + kwargs["arkadas"].lower() + " " +"\n")
	dosya.close()

	print("^^^ {ben} isimli kişi {arkadas} isimli kullanıcıyı arkadaş olarak ekledi ^^^".format(ben=kwargs["ben"].title(),arkadas=kwargs["arkadas"].title()))
	print("")
	input("Devam Etmek İçin Bir Tuşa Basınız")

def arkadasListesiGoster(kullaniciAdi):

	try:
		dosya=open("arkadasliklar.txt","r")
		satirlar = dosya.readlines()

		arkadasKontrol=0
		print("{}, Arkadaş Listeniz".format(kullaniciAdi))

		for arkadas in satirlar:

			arkadaslar = arkadas.split()
			if arkadaslar[0] == kullaniciAdi:
				print(arkadaslar[1])
				arkadasKontrol += 1

			elif arkadaslar[1] == kullaniciAdi:
				print(arkadaslar[0])
				arkadasKontrol += 1

		if arkadasKontrol==0:
			print("---- Herhangi Bir Arkadaşınız Henüz Yok ----")

		input("Devam Etmek İçin Bir Tuşa Basınız")

	except FileNotFoundError:
		print("____ Hiç Kimsenin Arkadaşı Yok Ki, Ne Sessiz Bir Dünya ___")
		print()
		input("Hadi İlk Adımı Sen Atmak İçin Bir Tuşa Bas")

def kisiselMenu(kullaniciAdi):
	while kullanici.cevrimIci:

		os.system(temizle)

		print("""

				[1] Arkadaş Listemi Getir
				[2] Arkadaş Ekle
				[3] Mesaj Gönder
				[4] Mesaj Kutusu
				[0] Çıkış

			""")

		secim = int(input("Seciminiz..:"))

		if secim==1:
			arkadasListesiGoster(kullaniciAdi)

		elif secim==2:
			arkadas = input("Eklemek İstediğiniz kullanıcının Adı..:")
			arkadasEkle(ben=kullaniciAdi,arkadas=arkadas)

		elif secim == 3:
			hedef = input("Mesajı Göndermek İstediğiniz Kişi..:")
			mesaj = input("Göndermek İstediğiniz Mesaj..:")
			mesajGonder(kullaniciAdi=kullaniciAdi, hedef=hedef, mesaj=mesaj, tarih=date.today())

		elif secim==4:
			mesajListele(kullaniciAdi)

		elif secim == 0:
			#quit()
			kullanici.cevrimIci = False

#-*-*-*-*-*-#

if __name__ == "__main__":
	while True:

		os.system(temizle)

		print("""
				[1] Kayıt Ol
				[2] Giriş Yap
				[0] Çıkış
			""")
		secim = int(input("Seciminiz..:"))

		if secim == 1:
			kullanici.kayitOl()

		elif secim == 2:
			kullanici.girisYap()
			if kullanici.cevrimIci:
				kisiselMenu(kullanici.cevrimIci)
		elif secim==0:
			quit()

