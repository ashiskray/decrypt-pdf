import PyPDF2
with open(r"C:\Users\ashis\OneDrive\Desktop\Data Automation\pdf_automation\encrypt pdf\protected_output.pdf","rb") as file:
    reader =PyPDF2.PdfReader(file)
    if reader.is_encrypted :
        try:
            reader.decrypt("Ashis")   # password will be provide in ("here")
            print ("decryption successful")
        except exception as e :
            print("task fail")
    writer= PyPDF2.PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
with open ("decrypt.pdf","wb") as output:
    writer.write(output)



