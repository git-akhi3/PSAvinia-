from transformers import BartForConditionalGeneration, BartTokenizer
import pandas as pd
from docx import Document

# Load pre-trained BART model and tokenizer
model_name = "facebook/bart-large-cnn"
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer = BartTokenizer.from_pretrained(model_name)

def generate_summary(text):
    inputs = tokenizer([text], max_length=1024, return_tensors="pt", truncation=True)
    summary_ids = model.generate(inputs["input_ids"], num_beams=4, min_length=50, max_length=200, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def export_summary(summary, format):
    if format == "Word":
        doc = Document()
        doc.add_paragraph(summary)
        doc.save("summary.docx")
    elif format == "Excel":
        df = pd.DataFrame({"Summary": [summary]})
        df.to_excel("summary.xlsx", index=False)
