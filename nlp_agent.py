import spacy

class NLPAgent:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def analyze_text(self, text):
        """
        Analyzes extracted text for key medical terms.
        :param text: Extracted text from OCR.
        :return: Identified medical terms.
        """
        doc = self.nlp(text)
        medicines = [token.text for token in doc if token.ent_type_ == "DRUG"]
        return {
            "original_text": text,
            "medicines_identified": medicines if medicines else ["No medicines detected."]
        }
