import json
import logging
import re
from datetime import datetime
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

NOTES_FILES = Path("notes.json")

def load_notes():
    if not NOTES_FILES.exists():
        logging.warning(f"Notes file {NOTES_FILES} not found")
        return []

    with open(NOTES_FILES,'r',encoding="utf-8") as f:
        logging.info(f"Notes file {NOTES_FILES} loaded")
        return json.load(f)

def save_notes(text:str)->None:

    notes = load_notes()
    note = {"time":datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),"text": text}
    notes.append(note)

    with open(NOTES_FILES,"w",encoding="utf-8") as f:
        json.dump(notes,f,indent=4)
    logging.info(F"Note saved to {NOTES_FILES}")

def search_notes(keyword: str)-> list:
    notes = load_notes()

    matches = []
    # for note in notes:
    #     text = note["text"]

    #     match = re.search(keyword, text, re.IGNORECASE)
    #     matches.append(match)

    return [note for note in notes if re.search(keyword, note["text"], re.IGNORECASE)]



if __name__ == "__main__":
    # save_notes("This is my daily routing notebook")
    # save_notes("My mobile number is 2892385299")
    # save_notes("This is my personal notebook so if you opended then please close it.")
    
    search_result = search_notes("2892385299")
    print(search_result)