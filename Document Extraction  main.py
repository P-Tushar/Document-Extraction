#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import unittest 
import pytesseract
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
from docx import Document
from PIL import Image
from io import BytesIO


class ExtractInformation:
    def __init__(self, file_path):
        self.file_path = file_path

    def __call__(self):
        _, file_extension = os.path.splitext(self.file_path)

        if file_extension == '.html':
            with open(self.file_path, 'r') as file:
                html_content = file.read()
                text = self.extract_text_from_html(html_content)
        elif file_extension in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']:
            text = self.extract_text_from_image(self.file_path)
        elif file_extension == '.pdf':
            text = self.extract_text_from_pdf(self.file_path)
        elif file_extension == '.docx':
            text = self.extract_text_from_docx(self.file_path)
        elif self.file_path.startswith('http') or self.file_path.startswith('https'):
            response = requests.get(self.file_path)
            if response.status_code == 200:
                html_content = response.content
                text = self.extract_text_from_html(html_content)
            else:
                text = f"Error accessing URL: {self.file_path}"
                print(text)
        else:
            text = f"Unsupported file type: {file_extension}"
            print(text)

        return text
    
    def get_file_extension(self):
        _, file_extension = os.path.splitext(self.file_path)
        return file_extension

    @classmethod
    def extract_text_from_html(cls, file_content):
        soup = BeautifulSoup(file_content, 'html.parser')
        text = soup.get_text()
        return text

    @classmethod
    def extract_text_from_image(cls, file_path):
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return text

    @classmethod
    def extract_text_from_pdf(cls, file_path):
        with open(file_path, 'rb') as file:
            pdf = PdfReader(file)
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
        return text

    @classmethod
    def extract_text_from_docx(cls, file_path):
        doc = Document(file_path)
        paragraphs = [p.text for p in doc.paragraphs]
        text = '\n'.join(paragraphs)
        return text



file_path = r"https://www.w3schools.com/"
extractor = ExtractInformation(file_path)
text = extractor()
print(text)


# In[ ]:




