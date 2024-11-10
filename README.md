# IsNowConverter

**IsNowConverter** is a Python script that uses Optical Character Recognition ( OCR ) to extract text from images and saves the result in a text file. The script leverages the **Tesseract OCR** engine to process images, and it automatically names the output text file based on the current date.

This project is ideal for automating the process of converting scanned documents, screenshots, or any image containing text into machine-readable text.

## Features

- **OCR Processing** : Uses Tesseract OCR to convert text in images to machine-readable text.
- **Automatic File Naming** : The output text file is automatically named with the current date in the format `YYYY-MM-DD.txt`.
- **Flexible Input** : Accepts any image file ( PNG, JPEG, etc. ) as input.
- **Tesseract Installation Check** : The script checks if Tesseract is installed and prompts the user to install or configure it if not found.

## Prerequisites

- **Python 3.x** : This script is written in Python and requires Python 3.x or higher.
- **Tesseract OCR** : The Tesseract OCR engine must be installed on your machine.

### Install Tesseract OCR

You can install Tesseract by following the instructions on its official GitHub repository : [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract)

Alternatively, you can manually specify the path to the Tesseract executable if it’s already installed.

## Installation

1. Clone this repository to your local machine :

```bash
git clone https://github.com/yourusername/IsNowConverter.git
```

2. Navigate to the project directory :

```bash
cd IsNowConverter
```

3. Install the required Python dependencies :

```bash
pip install -r requirements.txt
```

## Usage

1. Make sure **Tesseract OCR** is installed and available in your system's PATH.
   
2. Run the script with the path to the image you want to process as a command-line argument :

```bash
python script.py path/to/your/image.png
```

3. The script will :
   - Extract the text from the provided image.
   - Print the extracted text to the console.
   - Save the extracted text into a `.txt` file named with the current date ( e.g., `2024-11-10.txt` ).

## Example

```bash
python script.py path/to/your/image.png
```

### Example Output :

- Extracted text will be displayed in the terminal.
- A text file named `2024-11-10.txt` will be generated with the extracted text.

## Tesseract Not Found ?

If Tesseract is not found in your system's PATH, the script will prompt you with two options :

1. Install Tesseract by visiting the official [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract).
2. Manually provide the path to the Tesseract executable on your system.

## Contributing

Feel free to contribute to **IsNowConverter** by submitting issues or pull requests. If you have any ideas or improvements, we welcome your contributions.

### How to contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Made with ❤️ by [snowyhiker](https://github.com/sn0wyhik3r)
