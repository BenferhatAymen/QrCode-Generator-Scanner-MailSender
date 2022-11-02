import qrcode 
from PIL import Image 
def generate(mail :str):
    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=20,border=2)
    qr.add_data(mail)
    img=qr.make_image(fill_color="black",back_color="white")
    img.save(f'db/images/{mail}.png')
    print(f"{mail}.png generated")
    
