from flask import Flask, render_template, request
from PyPDF2 import PdfReader

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['resume']
    if file and file.filename.endswith('.pdf'):
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

        # Keywords to check in resume
        keywords = ["python", "machine learning", "data", "java", "sql"]

        # Match keywords
        matched = [kw for kw in keywords if kw.lower() in text.lower()]
        if matched:
            return f"✅ Resume shortlisted! Found: {', '.join(matched)}"
        else:
            return "❌ Resume not shortlisted. No relevant keywords found."
    else:
        return "Please upload a valid PDF file."

if __name__ == '__main__':
    app.run(debug=True)