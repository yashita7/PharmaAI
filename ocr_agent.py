import easyocr

class OCRAgent:
    def __init__(self):
        self.reader = easyocr.Reader(['en'])

    def extract_text(self, image_path):
        result = self.reader.readtext(image_path, detail=0)
        return result

# Example usage
if __name__ == "__main__":
    ocr_agent = OCRAgent()
    text = ocr_agent.extract_text("prescription1.jpg")  # Replace with your image path
    print("Extracted Text:", text)
