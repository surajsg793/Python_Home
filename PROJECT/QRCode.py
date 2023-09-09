# import qrcode as qr
# img = qr.make("https://github.com/surajsg793/Python_Home/blob/main/PROJECT/QRCode.py")
# img.save("Project _QR.png")

# import QRCode 
# from PIL import Image
# qr = QRCode.QRCode(version =1,
#                     error_correction = QRCode.constants.ERROR_CORRECT_L,
#                     box_size = 10, border = 4)
# qr.add_data("https://github.com/surajsg793/Python_Home/blob/main/PROJECT/QRCode.py")
# qr.make(fit=True)
# img = qr.make_image(fill_color = "blue", back_color = "yellow")
# img.save("GitHub_Project.png")


import qrcode

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # QR code version (1 to 40, or None for auto)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L, M, Q, or H)
    box_size=10,  # Size of each box in the QR code
    border=4,  # Border size (number of boxes)
)

# Data you want to encode in the QR code
data = "https://github.com/surajsg793/Python_Home/blob/main/PROJECT/QRCode.py"

# Add data to the QR code
qr.add_data(data)

# Generate the QR code as a PIL Image object
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="yellow")

# Save the QR code image to a file
img.save("GitHub_Project.png")

# Display the QR code (optional)
img.show()


