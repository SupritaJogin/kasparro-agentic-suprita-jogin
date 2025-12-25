"""
FAQ Template
------------
Builds FAQ page JSON using questions and product data.
"""

def build_faq_page(questions: dict, product: dict) -> dict:
    faq_items = []

    for category, qs in questions.items():
        for q in qs[:5]:  # limit per category
            faq_items.append({
                "category": category,
                "question": q,
                "answer": f"{product['name']} information related to: {q}"
            })

    return {
        "page_type": "FAQ",
        "product_name": product["name"],
        "faqs": faq_items[:5]
    }
