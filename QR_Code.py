import qrcode

data = input("Enter the text or URL to generate QR code: ")

qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    box_size=10,  
    border=4,  
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

save_path = r"C:\Users\SOUMYA DAS\OneDrive\Desktop\Program\Python Practical\Qr Code\user_qrcode.png"
img.save(save_path)

print(f"QR code saved successfully as: {save_path}")
