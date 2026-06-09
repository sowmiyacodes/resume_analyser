import PyPDF2

def extract_text_from_pdf(filepath):
    text = ""
    with open(filepath,'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text