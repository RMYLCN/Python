import time
import os
temizle=("cls" if  os.name == "nt" else "clear")


cevrimIci=False

def kayitOl():

	kullaniciAdi = input("Kullanıcı Adı Girin..:")

	if KullaniciAdiKontrolEt(kullaniciAdi):
		sifre = input("Sifrenizi Giriniz..:")
		sifreKontrol = input("Sifrenizi Tekrar Giriniz..:")

		if sifre == sifreKontrol:

			mail = input("Mail Adresinizi Giriniz..:")

			kayıtEt(kullaniciAdi,sifre,mail)
			print("^^^  Kullanıcı Kayıt Edildi  ^^^")
			time.sleep(3)

		else:
			print("")
			print("----Şifreler Eşleşmedi-----")
			time.sleep(3)
			return kayitOl()

	else:
		print("")
		print("______Kullanıcı Adı Zaten Mevcut____")
		time.sleep(3)
		return kayitOl()

def kayıtEt(kullaniciAdi,sifre,mail):

			#dosya = open("kullanicilar.txt","r")
			#icerik = dosya.read()
			#dosya.close()

			dosya = open("kullanicilar.txt","a")
			#dosya.write(icerik)
			dosya.write(kullaniciAdi + " " + sifre + " " + mail + "\n")
			dosya.close()

def KullaniciAdiKontrolEt(kullaniciAdi):

	try:
		if kullaniciAdi in open("kullanicilar.txt","r").read():
			return False
		else:
			return True

	except FileNotFoundError:
		return True

def girisYap():

	kullaniciAdi = input("Kullanıcı Adınızı Giriniz..:")
	sifre = input("Sifrenizi Giriniz..:")

	dosya = open("kullanicilar.txt","r")
	satirlar = dosya.readlines()

	kontrol=False
	global cevrimIci
	
	for kullanici in satirlar:
		gercekKullanici = kullanici.split(" ")

		if kullaniciAdi == gercekKullanici[0]:

			if sifre == gercekKullanici[1]:
				kontrol = True
				cevrimIci = kullaniciAdi
				print("Giriş Yapılıyor...")
				time.sleep(0.5)
				break
			else:
				print("")
				print("---- Yanlış Şifre Girdiniz ----")
				time.sleep(3)
				return girisYap()

	if not kontrol:
		print("")
		print("---- Yanlış Kullanıcı Adı Girdiniz ----")
		time.sleep(3)
		return girisYap()


menu="""

		[1] Yeni Kullanıcı Ekle
		[2] Giriş Yap
		[0] Çıkış

"""

if __name__ == "__main__":
	while True:

		os.system(temizle)

		print(menu)
		secim = int(input("Seciminiz..:"))

		if secim == 1:
			kayitOl()
			input()

		elif secim == 2:
			girisYap()

		elif secim == 0:
			quit()



#if _name__ == "__main==":
#	print("Program Direk Çağırıldı, Modül Değil :)")
#else:
#	print("Bir Modüldür,Direk Başlatılmadı! :(")