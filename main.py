import qrcode
import image

qr = qrcode.QRCode(
    version= 15,
    box_size= 10, # this is for the qr box size
    border= 5 # this is for the border for the qr
)

data = 'https://www.youtube.com/channel/UCc1EI37ezbALvdaj5ai8Gpw'

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('demo.png')