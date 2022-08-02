import qrcode


def make(url):
    img = qrcode.make(url)
    img.save("qrcode.jpg")


url = input("Enter your URL: ")

make(url)
