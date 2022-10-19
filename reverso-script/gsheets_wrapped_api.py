import gspread


class Gsheet_Api():
    def __init__(self, credentials="credentials.json"):
        self.gc = gspread.service_account(filename=credentials)

    def create_sheet(self, title):
        self.sh = self.gc.create(title)
        return self.sh

    def is_a_g_sheet(self, link_type, file_id):
        # link type can be key, url or title
        try:
            if link_type == "key":
                self.sh = self.gc.open_by_key(file_id)
            elif link_type == "url":
                self.sh = self.gc.open_by_url(file_id)
            elif link_type == "title":
                self.sh = self.gc.open(file_id)
            return True
        except:
            return False

    def write_on_sheet(self, link_type, file_id, word, traductions):
        if self.is_a_g_sheet(link_type, file_id):
            self.sh.sheet1.append_row([word, traductions])
            return True
        else:
            print("Error: the link is not a google sheet")
            return False
