import gspread


class Gsheet_Api():
    def __init__(self, credentials="credentials.json"):
        self.gc = gspread.service_account(filename=credentials)

    def write_on_sheet(self, file_id, word, traductions):
        self.sh = self.gc.open_by_key(file_id)
        self.sh.sheet1.append_row([word, traductions])
