Text Extractor from Images
The Text Extractor from Images project is a Python-based tool designed to extract text from image files. Using the powerful Tesseract OCR engine, this program simplifies the process of converting visual text into machine-readable text. Whether you're working with scanned documents, photos, or other text-based images, this tool efficiently processes .jpg and .png files and provides clean, readable output.


## Features
- **Text Extraction**: Extracts text from images with high accuracy.
- **Preprocessing**: Converts images to grayscale and applies thresholding for better OCR results.
- **Dynamic Input**: Users can specify the file path of the image, supporting files from any directory.
- **Formatted Output**: Displays the extracted text in a clean and readable format.

---

## Requirements
To run this project, you need the following:

1. **Python 3.7 or later**
2. **Libraries**:
   - `pytesseract`
   - `opencv-python`
   - `Pillow`
3. **Tesseract OCR**:
   - Download and install

---

## Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/text-extractor.git
   cd text-extractor
