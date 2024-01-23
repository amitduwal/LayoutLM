import os
from PIL import Image
import pytesseract
import json

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def process_images(input_dir, output_file):
    results = []

    for filename in os.listdir(input_dir):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            image_path = os.path.join(input_dir, filename)
            result = process_image(image_path)
            results.append(result)

    with open(output_file, 'w') as output:
        json.dump(results, output, indent=2)

def process_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='eng')

    result = {
        "id": os.path.basename(image_path),
        "data": {
            "image": {
                "valued": image_path,
                "original_width": image.width,
                "original_height": image.height
            },
            "text": {
                "value": text
            }
        }
    }

    return result

if __name__ == "__main__":
    input_directory = "data/"
    output_json_file = "output_label_studio.json"

    process_images(input_directory, output_json_file)
