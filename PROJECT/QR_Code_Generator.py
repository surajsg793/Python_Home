import qrcode

# Define the data you want to encode in the QR code
data = "Hello, World!"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # QR code version (1-40, where 1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L, M, Q, H)
    box_size=10,  # Size of each box in pixels
    border=4,  # Border size (number of boxes around the QR code)
)

# Add data to the QR code
qr.add_data(data)

# Generate the QR code as a PIL Image object
qr.make(fit=True)
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the QR code to a file
qr_image.save("my_qr_code.png")

# Display the QR code
qr_image.show()
