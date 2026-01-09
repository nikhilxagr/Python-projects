import qrcode

upi_id = input("Enter Your UPI ID: ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE
#Defining the payment URL based on the UPI ID and the payment app
#You can modify these URLs based on the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Generating QR codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#Saving the QR codes as image files
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#Displaying a message to indicate that the QR codes have been generated
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
print("QR codes generated and saved as 'phonepe_qr.png', 'paytm_qr.png', and 'google_pay_qr.png'.")