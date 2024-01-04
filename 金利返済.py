karita = int(input("借りたお金:"))
kinri = int(input("金利:"))
hensai = int(input("毎月の返済額:"))

def zangaku(zankin, kinri, hensai):
  geturi = kinri/12/100
  risi = int(zankin * geturi)
  hensaigaku = hensai - risi
  return zankin - hensaigaku

zankin = karita
zengetu = 0
month = 0

risi = karita * kinri/12/100
print("利子 : ", int(risi), ", 返済額 : ", hensai)

while zankin >0:
  if hensai <= risi:
    break
  zengetu = zankin
  zankin = zangaku(zankin, kinri, hensai)
  month = month + 1

if hensai > risi:
  print("返済の前月残金 : " + str(zengetu) + "円")
  print("返済月 : " + str(month) + "か月目 = " + str(month//12) + "年" +str(month%12) +"か月")
else:
  print("利子 :" + str(risi) + "円 >= 返済額 :" + str(hensai) + "円のため返済できません")