import pyqrcode
def qrgen(s):
    qr = pyqrcode.create(s)
    qr.png(str('yakkub')+'.png',scale = 4)
