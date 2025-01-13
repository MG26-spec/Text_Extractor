import pytesseract
from PIL import Image
import cv2
import os



def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img_thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
    return img_thresh

def extract_text_from_image(image_path):
    preprocessed_image = preprocess_image(image_path)
    text = pytesseract.image_to_string(preprocessed_image, config="--psm 6 --oem 3")
    return text

if __name__ == "__main__":
    file_path = input("Enter the full path to the image file (.jpg or .png): ")
    if os.path.exists(file_path):
        extracted_text = extract_text_from_image(file_path)
        print("\n" + "="*40)
        print("        Extracted Text from Image")
        print("="*40)
        print(extracted_text.strip())
        print("="*40)
    else:
        print("\n" + "="*40)
        print(f"File not found: {file_path}")
        print("Please ensure the file path is correct.")
        print("="*40)
