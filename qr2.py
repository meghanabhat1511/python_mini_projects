import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4
                 )
qr.add_data("https://notebooklm.google.com/notebook/2af35e32-0167-4d11-89d2-0ddd2f455ef4")
qr.make("fit=True")
img=qr.make_image(fill_color="black",back_color="red")
img.save("notebookllm.png")