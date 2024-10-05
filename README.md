# MD to DOCX Converter

This project provides both a command-line tool and a web-based interface for converting Markdown (.md) files to Microsoft Word (.docx) format.

## Features

- Command-line interface for quick conversions
- Web-based user interface with drag-and-drop functionality
- Converts Markdown to Word document format
- Preserves basic Markdown formatting (headers, paragraphs, lists)

## Requirements

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone this repository or download the project files.

2. If you haven't already, create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Unix or MacOS
   # OR
   venv\Scripts\activate  # On Windows
   ```

3. Install the required dependencies:
   ```
   pip install markdown python-docx beautifulsoup4 flask
   ```

## Usage

### Command-line Interface

1. Ensure your virtual environment is activated.

2. Run the script:
   ```
   python md2docx.py
   ```

3. Follow the prompts to enter the paths for your input Markdown file and desired output Word document.

### Web-based Interface

1. Ensure your virtual environment is activated.

2. Run the Flask application:
   ```
   python app.py
   ```

3. Open a web browser and go to `http://localhost:5000`.

4. Drag and drop a Markdown file onto the designated area, or click to select a file.

5. Click the "Convert to DOCX" button to start the conversion.

6. The converted file will be automatically downloaded once the conversion is complete.

## Project Structure

- `md2docx.py`: The core Python script that performs the Markdown to DOCX conversion.
- `app.py`: The Flask server that handles file conversion and serves the web application.
- `templates/index.html`: The HTML file containing the user interface for the web application.

## Limitations

- The converter currently supports basic Markdown formatting. Advanced features like tables, code blocks, or inline HTML are not fully supported.
- Images in the Markdown file are not included in the Word document.

## Troubleshooting

- If you encounter any module import errors, ensure that you've activated your virtual environment and that all dependencies are installed.
- For permission-related errors, make sure you have read access to the input file and write access to the output directory.
- If the web page doesn't load, check that the Flask server is running and that you're using the correct URL.

## Contributing

Contributions to improve the MD to DOCX Converter are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
