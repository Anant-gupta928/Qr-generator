import qrcode
from PIL import Image

# Define URLs for each application
urls = {
    "1": ("Google", "https://www.google.com"),
    "2": ("YouTube", "https://www.youtube.com"),
    "3": ("Facebook", "https://www.facebook.com"),
    "4": ("Chrome", "https://www.google.com/chrome/"),
    "5": ("WhatsApp", "https://www.whatsapp.com")

}

# Display menu
print("Select an option to generate a QR code:")
for key, (name, _) in urls.items():
    print(f"{key}: {name}")

# Get user choice
choice = input("Enter the number of your choice: ")

# Validate user choice
if choice in urls:
    app_name, url = urls[choice]
    
    # Generate and save QR code
    qr = qrcode.make(url)
    file_name = f'{app_name.lower()}_qr.png'
    qr.save(file_name)
    
    # Display QR code image
    Image.open(file_name).show()
    
    print(f"QR code for {app_name} generated and displayed successfully.")
else:
    print("Invalid choice. Please run the script again and select a valid option.")
