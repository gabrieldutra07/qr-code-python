import qrcode

url = input("Enter your URL: ")

img = qrcode.make(url)
img.save("qrcode.jpg")