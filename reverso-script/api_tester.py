import sys
import os
import argparse

sys.path.append(os.getcwd() + os.path.abspath("/api/"))
from api.reverso_wrapped_api import *
from api.gsheets_wrapped_api import *

parser = argparse.ArgumentParser(
    description='GSheet api wrapper tester script')
parser.add_argument("--file_id", help="Google sheet file id", required=True)
parser.add_argument("--row", help="Row number you want to get", required=False)
parser.add_argument("--col", help="Col number you want to get based on the row", required=False)
parser.add_argument("--find", help="Find a w", required=False)

args = vars(parser.parse_args())

if (args["file_id"] == None):
    print("File id not giben!")
else:
    gsheet = Gsheet_Api()
    if(gsheet.open_sheet("key",args["file_id"]) == False):
        print("Not a valid google sheet file id")
    else:
        print(f"""Sheet opened, here some infos:\r\n
        Url: {gsheet.get_sheet_url()}\r
        id: {gsheet.get_sheet_id()}\r
        title: {gsheet.get_sheet_title()}\r
        Total rows: {gsheet.get_rows_number()}\r
        Total cols: {gsheet.get_cols_number()}\r
        Header: {gsheet.get_sheet_header()}\n""")

        #gsheet.write_custom_row(["en","it","meaning"])
        if(args["find"]!=None):
            print(f"Searching for {args['find']}...")
            res = (gsheet.find_word(args["find"]))
            if res[0]:
                print(f"Found word:{args['find']} at row {gsheet.get_cell_row(res[1])} and col {gsheet.get_cell_col(res[1])}")
            else:
                print("Word not found")
        if(args["row"] == None):
            print(f'Printing a random row: {gsheet.get_random_row()}')
            print(f'Print a random column: {gsheet.get_random_column()}')
            print("\nNo row number given, printing all the sheet")
            print(gsheet.get_all_records_parsed())
        else:
            print(f'Print row [{args["row"]}]: {gsheet.get_row_complete(int(args["row"]))}')
            if(args["col"] != None):
                print(f'Selected row: {args["row"]} and col: {args["col"]} ({gsheet.get_column(int(args["col"]))})')
                print(f'Value: {gsheet.get_cell(int(args["row"]),int(args["col"]))}')
