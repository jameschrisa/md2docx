# md2docx.py

md2docx.py is a Python script that converts Markdown (.md) files to Microsoft Word (.docx) format. It preserves basic formatting such as headers, paragraphs, and lists.

## Features

- Converts Markdown to Word document format
- Preserves basic Markdown formatting (headers, paragraphs, lists)
- Easy-to-use command-line interface
- Automatically installs required dependencies

## Requirements

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone this repository or download the `md2docx.py` file.

2. (Optional but recommended) Create a virtual environment:
   ```
   python -m venv md2docx_env
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     md2docx_env\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source md2docx_env/bin/activate
     ```

4. The script will automatically install required dependencies when run for the first time. If you prefer to install them manually, use:
   ```
   pip install markdown python-docx beautifulsoup4
   ```

## Usage

1. Ensure your virtual environment is activated (if you're using one).

2. Run the script:
   ```
   python md2docx.py
   ```

3. Follow the prompts to enter the paths for your input Markdown file and desired output Word document.

4. The script will convert your Markdown file and save the resulting Word document at the specified location.

## Example

```
$ python md2docx.py
Enter the path to the input Markdown file: /path/to/your/input.md
Enter the path for the output Word document: /path/to/your/output.docx
Conversion complete. Output saved to /path/to/your/output.docx
```

## Limitations

- The script currently supports basic Markdown formatting. Advanced features like tables, code blocks, or inline HTML are not fully supported.
- Images in the Markdown file are not included in the Word document.

## Troubleshooting

- If you encounter any "module not found" errors, ensure that you've activated your virtual environment (if using one) and that all dependencies are installed.
- For permission-related errors, make sure you have read access to the input file and write access to the output directory.

## Contributing

Contributions to improve md2docx.py are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
