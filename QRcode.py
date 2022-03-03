import qrcode

img = qrcode.make('http://www.yahoo.com.br')
print(type(img))
print(img.size)

img.save('qrcode_yahoo.png')
