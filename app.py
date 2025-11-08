from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['resume']
    if file and file.filename.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()

        keywords = ["python", "java", "sql", "machine learning", "data"]
        matched = [kw for kw in keywords if kw.lower() in text.lower()]
        if matched:
            return f"Resume shortlisted! Found: {', '.join(matched)}"
        else:
            return "Resume not shortlisted. No relevant keywords found."
    return "Upload a valid PDF file."

if __name__ == '__main__':
    app.run(debug=True)