import os
import logging
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

# Add predefined questions and answers
PREDEFINED_QA = {
    "What are Apple’s primary sources of revenue, and what is driving growth?":
        "Apple’s primary revenue sources are product sales (iPhone, iPad, Mac, etc.) and services (App Store, iCloud, Apple Music, etc.). iPhone contributes over 50% of total revenue, while services are the fastest-growing segment, with a year-over-year growth of 15%-20%.",

    "What is the trend in Apple’s R&D spending, and does it align with its innovation strategy?":
        "In fiscal year 2023, Apple’s R&D spending reached $30.6 billion, a 9% year-over-year increase, representing 6.3% of total revenue. The increased spending highlights Apple’s focus on emerging technologies like AR/VR (Apple Vision Pro) and AI applications.",

    "How is Apple’s profitability evolving?":
        "In 2023, Apple maintained a gross margin of 43.5% and a net profit margin of around 25%. High-margin service revenue and cost optimization supported its stable profitability.",

    "How does Apple manage its cash flow and capital allocation?":
        "Apple generated $90 billion in free cash flow in 2023. It allocated $55 billion to stock buybacks, $15 billion to dividend payments, and invested in renewable energy and supply chain diversification.",

    "What are the highlights of Apple’s sustainability strategy?":
        "Apple aims to achieve carbon neutrality by 2030. Over 300 suppliers are part of its 100% renewable energy program, and the iPhone 15 incorporates more recycled materials, reducing its carbon footprint.",

    "What is Apple’s position in the global market compared to competitors?":
        "Apple holds a 20% global market share in smartphones and dominates the premium segment (> $400) with over 50% share. Competitors like Samsung, Huawei, and Xiaomi challenge Apple, but it remains a leader in high-end markets.",

    "How financially healthy is Apple in terms of debt and cash reserves?":
        "Apple has $110 billion in total debt but holds $166 billion in cash reserves, reflecting strong financial health. Its debt-to-equity ratio is a low 1.8x, supported by its top-tier credit rating.",
    "What is in Apple's 10K report in 2023？":
        "Apple's 2023 10K report highlights strong revenue from iPhone and services, growing R&D investment in AI and AR/VR, solid profitability, sustainability efforts toward carbon neutrality by 2030, and a dominant position in the premium smartphone market."
}


# API route: Process input and return predefined answers
@app.route("/process_input", methods=["POST"])
def process_user_input():
    data = request.json
    user_input = data.get("input")

    if not user_input:
        return jsonify({"error": "Input is required."}), 400

    # Return predefined answers
    if user_input == "predefined":
        return jsonify(PREDEFINED_QA)

    # Check if user_input matches any predefined question
    answer = PREDEFINED_QA.get(user_input)
    if answer:
        return jsonify({"question": user_input, "answer": answer})
    else:
        return jsonify({"error": "Question not found in predefined list."})


# Home route
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
