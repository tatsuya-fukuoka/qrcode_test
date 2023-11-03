import qrcode

text = 'https://chantastu.hatenablog.com/'
img = qrcode.make(text)

img.save('qrcode_make_test1.jpg')