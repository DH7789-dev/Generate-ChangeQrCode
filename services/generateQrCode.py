import qrcode
from qrcode import ERROR_CORRECT_L


def QrCode(name_qrcode,data, color_fill, color_back):
    qr = qrcode.QRCode(
        version=5,
        error_correction=ERROR_CORRECT_L,
        box_size=3,
        border=5
    )

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color_fill, back_color=color_back)
    img.save(f'download/{name_qrcode}.png')


