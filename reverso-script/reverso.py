import argparse
import sys 
import os
sys.path.append(os.getcwd() + os.path.abspath("/api/"))
from api.reverso_wrapped_api import *
from api.gsheets_wrapped_api import *

parser = argparse.ArgumentParser(
    description='A simple reverso translator and google sheet automatic appender', epilog="Example: python3 reverso.py --source=en --dest=it --word=Unabashed --depth=6 --write=y --file_id=...")
parser.add_argument(
    "--source", help="Source language of the selected word (e.g. en stands for english)", default="en", required=False)
parser.add_argument("--dest",
                    help="Language of destination for the traduction (e.g. it stands for italian)", default="it", required=False)
parser.add_argument("--word", help="Word you want to traduce", required=True)
parser.add_argument(
    "--depth", help="Depth of the traduction, aka how many different traduction you want", default=5, required=False)
parser.add_argument("--file_id", help="Google sheet file id", required=False)
parser.add_argument(
    "--write", help="If you want to write the traductions on the google sheet file please type y, otherwise the default setting is no", required=False)
args = vars(parser.parse_args())

source_lang = args["source"]
destination_lang = args["dest"]
word = args["word"]
write_on_sheet = args["write"]
file_id = args["file_id"]
sheet_buffer = ""
try:
    print(
        f"\nTranslating from {source_lang} to {destination_lang} the word: {word}\n")

    reverso_api = Reverso_Api(
        source_lang, destination_lang)
    client = reverso_api.get_client()
    translated_words = reverso_api.get_translations(word, int(args["depth"]))
    if len(translated_words) == 0:
        print("No traduction available")
    else:
        for i in translated_words[:int(args["depth"])]:
            print(i)
            if write_on_sheet == "y":
                sheet_buffer += i + " / "
        if write_on_sheet == "y":
            sheet_buffer = sheet_buffer[:len(sheet_buffer)-2]
            if file_id != None:
                pass
                gsheet = Gsheet_Api()
                if gsheet.is_a_g_sheet("key", file_id):
                    if gsheet.write_on_sheet(word, sheet_buffer):
                        print("\nTraductions written on the google sheet")
                else:
                    raise Exception("No valid gsheet")
            else:
                raise Exception("No file id provided")


except Exception as e:
    print(f"Error: {e}")
