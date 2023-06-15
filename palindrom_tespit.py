# Palindrom tespit eden bir fonksiyon tanımlayalım
def palindrom_mu(metin):
  # Metni küçük harflere dönüştürelim ve boşlukları silelim
  metin = metin.lower().replace(" ", "")
  # Metnin tersten yazılışını alalım
  ters_metin = metin[::-1]
  # Metin ile ters metin eşitse palindromdur
  if metin == ters_metin:
    return True
  else:
    return False

# Kullanıcıdan bir metin girmesini isteyelim
metin = input("Bir metin giriniz: ")

# Palindrom olup olmadığını kontrol edelim
if palindrom_mu(metin):
  print("Girdiğiniz metin bir palindromdur.")
else:
  print("Girdiğiniz metin bir palindrom değildir.")
