# PDF to Markdown Conversion Using `llama_parse`

## Overview
This project demonstrates how to use the `llama_parse` package to convert a PDF document into Markdown format. The program connects to the Llama Cloud API, processes the PDF file, and saves the converted Markdown content into a file.

## Features
- Extract text from a PDF document using `llama_parse`.
- Convert the extracted text to Markdown format.
- Save the converted content into a Markdown file.

## Requirements
- Python 3.x
- Llama Cloud API Key
- `llama_parse` package

## Installation

1. Install the `llama_parse` package:
   ```bash
   %pip install llama_parse
Clone this repository and navigate to the project directory:
bash
Copy code
git clone <repository-url>
cd <repository-directory>

##Setup

Llama Cloud API Key: You will need to sign up for access to the Llama Cloud API and obtain an API key. Replace the placeholder API key in the code with your actual key:
```python

import os
os.environ["LLAMA_CLOUD_API_KEY"] = "your-api-key-here"
```
PDF File: Update the path in the load_data function to the PDF document you want to convert:
```python
document = LlamaParse(result_type="markdown").load_data("/path/to/your/pdf/file")
```
Usage

Once the necessary dependencies are installed and API credentials are configured, you can run the program to convert your PDF document into Markdown format.

```bash

python main.py
```
The following code demonstrates how to convert a PDF into Markdown format and save it as a file:

```python

import nest_asyncio
nest_asyncio.apply()

import os
os.environ["LLAMA_CLOUD_API_KEY"] = "your-api-key-here"

from llama_parse import LlamaParse
```
# Load PDF and convert to markdown
```
document = LlamaParse(result_type="markdown").load_data("/path/to/your/pdf/file")
```
# Output the result
```
print(document[0])
```
# Save the markdown content to a file
```
file_name = "alfa.md"
with open(file_name, 'w') as file:
    file.write(document[0].text)
```
After running the program, you should find the extracted content from the PDF saved as a Markdown file (alfa.md).

Code Overview

Functions
```
LlamaParse(result_type="markdown").load_data(pdf_path): Loads the PDF file and extracts its content in Markdown format.

```
# Convert a PDF to Markdown and save to file
```python
document = LlamaParse(result_type="markdown").load_data("/path/to/your/pdf/file")
```
# Save the markdown content to a file
```
file_name = "output.md"
with open(file_name, 'w') as file:
    file.write(document[0].text)
```
Notes

Make sure that your Llama Cloud API key is kept secure and not exposed in public repositories.
Test the code with different PDFs to verify performance and formatting.

