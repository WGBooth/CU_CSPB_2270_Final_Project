from PyPDF2 import PdfReader
import os
# this file was found on Github and assists in parsing the pdfs
from scripts.pymupdf_rag import to_markdown
import fitz
import xml.etree.ElementTree as ET

# From the screenplays folder gather up the names of each screenplay
collection = os.listdir("screenplays")
collection.sort()
print(collection)
name_set = set([])

# For each screenplay, parse the text and extract the character names
# returns a set of characters from the screenplays in the batch with their name and title of screenplay
def collect_character_names():
    def loop_collection():
        for screenplay in collection:
            character_position = []
            
            print(f"Parsing {screenplay}...")

            #skips over dot files (e.g. .DS_STORE if a mac user)
            if screenplay.startswith('.'):
                continue

            reader = PdfReader(f"screenplays/{screenplay}")
            num_pages = len(reader.pages)
            doc = fitz.open(f"screenplays/{screenplay}")
            out = open(f"{screenplay}.txt", "wb")
            
            def get_character_position():
                character_position = 0
                for block in root:
                    for line in block:
                        for v in line.attrib.values():
                            if round(float(v.partition(' ')[0]), 0) > character_position:
                                character_position = round(float(v.partition(' ')[0]), 0)
                        return character_position

            # Goes line-by-line through the script and identifies the position where a character's name
            # is and adds it to the set
            def go_through_script(character_position):
                for block in root:
                    for line in block:
                        character_name = ""
                        for v in line.attrib.values():
                            # should work for any modern screenplay format
                            if round(float(v.partition(' ')[0]), 0) == character_position:
                                for x in line:
                                    for a in x:
                                        character_name += a.attrib['c'].upper()
                                    # Avoids duplicate characters incurred by script directions
                                    if '(' in character_name:
                                        continue
                                    # Added the screenplay for clarity and to avoid overwriting character with same name
                                    # from two screenplays (e.g. "Buzz" from "Toy Story" and "Buzz" from "A Bug's Life")
                                    name_set.add(f"{character_name.strip()}......{screenplay}")

            # iterates through each page of the screenplay and calls the go_through_script function
            # to extract the character names
            
            # Skip title page to find location of character on page
            for page in range(1,num_pages):
                my_page = doc.load_page(page_id=page)
                texts = my_page.get_text("xml")
                tree = ET.ElementTree(ET.fromstring(texts))
                tree.write(f"{screenplay}.xml")
                parsed = ET.parse(f"{screenplay}.xml")
                root = parsed.getroot()
                character_position.append(get_character_position())
            
            # Go through the script and extract character names
            for page in range(num_pages):
                my_page = doc.load_page(page_id=page)
                texts = my_page.get_text("xml")
                tree = ET.ElementTree(ET.fromstring(texts))
                tree.write(f"{screenplay}.xml")
                parsed = ET.parse(f"{screenplay}.xml")
                root = parsed.getroot()
                go_through_script(max(character_position))

            # Closes the text file that was created
            out.close()

            # Deletes the xml and txt file after it's been used (we not longer need them)
            os.remove(f"{screenplay}.xml")
            os.remove(f"{screenplay}.txt")
    loop_collection()
    return name_set