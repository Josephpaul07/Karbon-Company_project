from flask import Flask, render_template, request, redirect, url_for
import json
from model import financial_analysis  # Ensure model.py is in the same directory

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/submit', methods=['POST'])
def submit_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)

    # Save the uploaded file
    file.save('data.json')

    # Perform financial analysis using model.py
    with open('data.json', 'r') as f:
        data = json.load(f)
    
    analysis_result = financial_analysis(data)

    return render_template('results.html', results=analysis_result)

if __name__ == '__main__':
    app.run(debug=True)
