import fitz
import re


def is_english(s):
    return bool(re.fullmatch(r'[a-zA-Z\s]+', s))


def is_digits(s):
    return bool(re.fullmatch(r'\d+', s))


def extract_words_from_pdf(pdf_path):
    words = []
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text("text")
        lines = text.strip().split('\n')
        for i, line in enumerate(lines):
            if i > 5000:
                break
            if is_english(line):
                word = line
                if word.strip() == '': continue
                transcription = lines[i + 1]
                translation = lines[i + 2]
                # print((word, transcription, translation))
                words.append((word, transcription, translation))
    return words


