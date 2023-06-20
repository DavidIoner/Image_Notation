import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Carregar a imagem do documento
image_path = "texto.jpeg"
image = Image.open(image_path)

# Extrair o texto da imagem usando OCR
extracted_text = pytesseract.image_to_string(image, lang="pt-br")

# Salvar o texto extraído em um arquivo de saída
output_file = "output.txt"
with open(output_file, "w") as file:
    file.write(extracted_text)

print("Texto extraído e salvo com sucesso no arquivo", output_file)
