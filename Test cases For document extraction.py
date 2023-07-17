#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import unittest
from Extraction_Test_Cases import ExtractInformation

def get_file_extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension

def test_extract_text_from_html():
    file_path = r"C:\Users\TusharPatil\Documents\index.html"
    extractor = ExtractInformation(file_path)
    text = extractor()
    expected_keyword = "My name is unknown"
    unittest.TestCase().assertIn(expected_keyword, text)

def test_extract_text_from_image():
    file_path = r"C:\Users\TusharPatil\Downloads\ocr-tesseract-sample-text.png"
    extractor = ExtractInformation(file_path)
    text = extractor()
    expected_keyword = "This is a sample text for Tesseract to recognize"
    unittest.TestCase().assertIn(expected_keyword, text)

def test_extract_text_from_pdf():
    file_path = r"C:\Users\TusharPatil\Downloads\docc.pdf"
    extractor = ExtractInformation(file_path)
    text = extractor()
    expected_keyword = "I love to play football"
    unittest.TestCase().assertIn(expected_keyword, text)

def test_extract_text_from_docx():
    file_path = r"C:\Users\TusharPatil\Documents\docc.docx"
    extractor = ExtractInformation(file_path)
    text = extractor()
    expected_keyword = "I love to play football"
    unittest.TestCase().assertIn(expected_keyword, text)

def test_extract_text_from_url_html():
    file_path = r"C:\Users\TusharPatil\Documents\index.html"
    extractor = ExtractInformation(file_path)
    text = extractor()
    expected_keyword ="My name is unknown"
    unittest.TestCase().assertIn(expected_keyword, text)

def test_unsupported_file_type():
    file_path = r"C:\Users\TusharPatil\Downloads\sample (1).webp"
    extractor = ExtractInformation(file_path)
    text = extractor()
    expected_message = None
    unittest.TestCase().assertEqual(text, expected_message)

def test_get_file_extension():
    file_path = r"C:\Users\TusharPatil\Documents\index.html"
    file_extension = get_file_extension(file_path)
    expected_extension = ".html"
    unittest.TestCase().assertEqual(file_extension, expected_extension)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.FunctionTestCase(staticmethod(test_extract_text_from_html)))
    suite.addTest(unittest.FunctionTestCase(staticmethod(test_extract_text_from_image)))
    suite.addTest(unittest.FunctionTestCase(staticmethod(test_extract_text_from_pdf)))
    suite.addTest(unittest.FunctionTestCase(staticmethod(test_extract_text_from_docx)))
    suite.addTest(unittest.FunctionTestCase(staticmethod(test_extract_text_from_url_html)))
    suite.addTest(unittest.FunctionTestCase(staticmethod(test_unsupported_file_type)))
    suite.addTest(unittest.FunctionTestCase(staticmethod(test_get_file_extension)))

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.failures or result.errors:
        exit(1)


# In[ ]:





# In[ ]:




