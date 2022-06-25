#install the module 'qrcode'

import qrcode

# define the dimensions of qr code

qr=qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

#put the data which you have to scan

data="Hello, Welcome to Diya's QR."
qr.add_data(data)
qr.make(fit=True)

#define the color combination of qr code

img=qr.make_image(fill="black",back_color="white")

#save the image

img.save("qrcode.png")
