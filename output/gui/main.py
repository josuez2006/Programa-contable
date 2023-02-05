from pdf_to_text_converter import pdf_to_text_convert
from entry.entry_search import get_entries
from data_to_excel_converter import data_to_excel_convert

from tkinter.filedialog import askopenfilename, askdirectory


paths = {}

def find_input_path():
    paths["input_path"] = askopenfilename(filetypes=(("pdf files", "*.pdf"),("all files", "*.*")))
    return paths["input_path"]
    
def find_output_path():
    paths["output_path"] = askdirectory()
    return paths["output_path"]


def convert_file():
    text = pdf_to_text_convert(paths["input_path"])
    entries = get_entries(text)
    data_to_excel_convert(entries, paths["output_path"])