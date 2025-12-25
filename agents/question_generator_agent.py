"""
QuestionGeneratorAgent
----------------------
Responsibility:
- Generate categorized user questions from product data
"""

class QuestionGeneratorAgent:

    def generate(self, product: dict) -> dict:
        """
        Generates categorized questions based on product attributes.
        Returns a dictionary of categories -> list of questions.
        """

        questions = {
            "Informational": [
                f"What is {product['name']}?",
                f"What does {product['concentration']} mean in this serum?",
                "What are the key ingredients used?",
                "What skin types is this product suitable for?"
            ],
            "Usage": [
                "How should this serum be applied?",
                "Can this serum be used daily?",
                "Should it be used before or after sunscreen?",
                "How much product should be applied each time?"
            ],
            "Safety": [
                "Are there any side effects?",
                "Is this product suitable for sensitive skin?",
                "Can it cause irritation?",
                "Is a patch test required?"
            ],
            "Purchase": [
                "What is the price of this serum?",
                "Is this product value for money?",
                "How long does one bottle last?"
            ],
            "Comparison": [
                "How does this serum compare with other Vitamin C serums?",
                "Is this better than lower concentration Vitamin C products?"
            ]
        }

        return questions
