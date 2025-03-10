import qrcode

# taking UPI ID
upi_id = input("Enter your UPI ID = ")
name = input("Enter the recipient's name: ")
amount = input("Enter the amount: ")
currency = input("Enter the currency code (e.g., INR): ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

# Deffining the payment URLbased on the UPI ID and the payment app
# You can modify these urls based on the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=REcipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=REcipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=REcipient%20Name&mc=1234'

# create qr codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# save the qr code to image file 
phonepe_qr.save('phone_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay.png')

# Display qr codes (by pillow lib)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

