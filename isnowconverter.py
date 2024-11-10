import pytesseract
from PIL import Image
import os
import sys
import shutil
from datetime import datetime

def tesseract_installed():
    tesseract_path = shutil.which("tesseract")
    return tesseract_path is not None

def propose_installation():
    print("Tesseract is not installed or not found in the PATH.")
    print("1. Install Tesseract : You can download Tesseract here : https://github.com/tesseract-ocr/tesseract")
    print("2. Manually add the path to the Tesseract executable.")
    choice = input("Enter 1 to install or 2 to add the path manually : ")

    if choice == "1":
        print("You can install Tesseract by following the instructions on the provided URL.")
        sys.exit(0)
    elif choice == "2":
        path = input("Please enter the full path to the Tesseract executable ( e.g., C:/Program Files/Tesseract-OCR/tesseract.exe ) : ")
        if os.path.exists(path):
            pytesseract.pytesseract.tesseract_cmd = path
            print(f"The path to Tesseract has been updated : {path}.")
        else:
            print("The provided path is not valid. Please try again.")
            sys.exit(1)
    else:
        print("Invalid choice, please restart the program.")
        sys.exit(1)

def image_to_text(png_path):
    try:
        img = Image.open(png_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Error: {e}."

def write_to_file(text):
    today_date = datetime.now().strftime("%Y-%m-%d")
    output_filename = f"{today_date}.txt"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"The text has been written to the file {output_filename}.")

if not tesseract_installed():
    propose_installation()

if len(sys.argv) < 2:
    print("Please specify an image file as an argument to the script.")
    sys.exit(1)

png_file = sys.argv[1]
extracted_text = image_to_text(png_file)

print("Extracted text :")
print(extracted_text)

write_to_file(extracted_text)