import cv2
from qrcode import ERROR_CORRECT_L
import qrcode
from PIL import Image

def QrCodeChange(name_qrcode,data,color_fill, color_back,nameOpen):

    #detecte data and decode

    d = cv2.QRCodeDetector()
    val,point,Qrcode = d.detectAndDecode(cv2.imread(nameOpen))

    if data == '':
        data = val

    #create qrcode
    qr = qrcode.QRCode(
        version=5,
        error_correction=ERROR_CORRECT_L,
        box_size=3,
        border=5
    )

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color_fill, back_color=color_back)
    img.save(f'download/change/{name_qrcode}.png')

    #open image
    im = Image.open(f'download/change/{name_qrcode}.png')
    im.show()

def valQrcode(file):
    print(file)
    d = cv2.QRCodeDetector()
    val, point, Qrcode = d.detectAndDecode(cv2.imread(file))
    return val

