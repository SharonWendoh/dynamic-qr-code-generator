import qrcode
from PIL import Image


def generate_qr_code(till_number, amount):
    url = f"qrpesa://pay?till={till_number}&amount={amount}"
    qr = qrcode.make(url)
    filename = f"{till_number}_{amount}.png"
    qr.save(filename)
    return filename

def display_qr_code(filename):
    image = Image.open(filename)
    image.show()

filename = generate_qr_code("8811788", "1500")
display_qr_code(filename)