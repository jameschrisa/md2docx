from flask import Flask, request, send_file, render_template
import os
from md2docx import convert_md_to_docx
import tempfile

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file and file.filename.endswith('.md'):
        # Create temporary files for input and output
        with tempfile.NamedTemporaryFile(delete=False, suffix='.md') as temp_input:
            file.save(temp_input.name)
        temp_output = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
        temp_output.close()

        # Convert the file
        convert_md_to_docx(temp_input.name, temp_output.name)

        # Send the file
        return send_file(temp_output.name, as_attachment=True, download_name=file.filename.rsplit('.', 1)[0] + '.docx')
    return 'Invalid file type', 400

if __name__ == '__main__':
    app.run(debug=True)
