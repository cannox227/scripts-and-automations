import random
import gspread

# To be coherent with Gsheet style
# it is used the same shitty way to enumate the indexes
# so the first index is marked with 1 instead of 0 
# (contrasting the normal programmers common sense)
# sorry :(

class Gsheet_Api():
    def __init__(self, credentials="credentials.json", cred_type="filename"):
        if(cred_type == "filename"):
            self.gc = gspread.service_account(filename=credentials)
        elif(cred_type == "dict"):
            self.gc = gspread.service_account_from_dict(credentials)
        else:
            print("Error: supported credential types are 'filename' and 'dict'")
            raise ValueError("Error: supported credential types are 'filename' and 'dict'")
        self.first_row_index = 1
        self.sh = None
    
    def get_first_row_index(self):
        return self.first_row_index
    
    def set_first_row_index(self, index):
        self.first_row_index = index

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

    def open_sheet(self, link_type, file_id):
        if self.is_a_g_sheet(link_type, file_id):
            return True
        else:
            return False

    def get_sheet_url(self):
        if self.sh != None:
            return self.sh.url
        else:
            return None
    
    def get_sheet_title(self):
        if self.sh != None:
            return self.sh.title
        else:
            return None
    
    def get_sheet_id(self):
        if self.sh != None:
            return self.sh.id
        else:
            return None

    def write_on_sheet(self, word, traductions):
        if self.sh != None:
            self.sh.sheet1.append_row([word, traductions])
            return True
        else:
            print("Error: google sheet not found")
            return False

    def write_custom_row(self, row: list):
        if self.sh != None:
            self.sh.sheet1.append_row(row)
            return True
        else:
            print("Error: google sheet not found")
            return False
    
    def find_word(self, word):
        # return False wheter not found
        # otherwise return a tuple with True and the cell object
        if self.sh != None:
            cell = self.sh.sheet1.find(word)
            if cell:
                return (True,cell)
            else:
                return False
        else:
            print("Error: google sheet not found")
            return False
    
    def get_cell_row(self, cell):
        if self.sh != None:
            return cell.row
        else:
            return None

    def get_cell_col(self, cell):
        if self.sh != None:
            return cell.col
        else:
            return None

    def get_rows_number(self):
        # get_last_row_index
        if self.sh != None:
            return len(self.sh.sheet1.get_all_values())
        else:
            return None

    def get_cols_number(self):
        # get_last_column_index
        if self.sh != None:
            return len(self.get_sheet_header())
        else:
            return None
    
    def get_row(self, row):
        # return just the raw value without the headers
        if self.sh != None:
            return self.sh.sheet1.row_values(row)
        else:
            return None

    def get_sheet_header(self):
        if self.sh != None:
            return self.sh.sheet1.row_values(self.first_row_index)
        else:
            return None
    
    def get_row_complete(self, row):
        #return a string made as a dict
        if self.sh != None:
            values = self.sh.sheet1.row_values(row)
            keys = self.sh.sheet1.row_values(self.first_row_index)
            dict = ""
            for i in range(0, len(values)):
                dict += f"{keys[i]}: {values[i]}, "
            dict = dict[:-2] # remove the last ", "
            return dict
        else:
            return None
    
    def get_column(self, column):
        if self.sh != None:
            try:
                if column > 0:
                    return self.get_sheet_header()[column-self.first_row_index]
            except:
                return IndexError
        else:
            return None
    
    def get_cell(self, row, column):
        if self.sh != None:
            # check if the column index exists
            if column <= len(self.sh.sheet1.row_values(row)):
                return self.sh.sheet1.cell(row, column).value
            else:
                return None
        else:
            return None

    def get_random_row(self):
        if self.sh != None:
            rand = random.randint(self.first_row_index,self.get_rows_number())
            return self.get_row_complete(rand)
        else:
            return None

    def get_random_column(self):
        if self.sh != None:
            rand = random.randint(self.first_row_index,len(self.get_sheet_header()))
            return self.get_column(rand)
        else:
            return None

    def get_all_records(self):
        # return a list of dictionaries
        if self.sh != None:
            return self.sh.sheet1.get_all_records()
        else:
            return None
    
    def get_all_records_parsed(self):
        if self.sh != None:
            raw_records = self.sh.sheet1.get_all_records()
            parsed_records = ""
            for i in raw_records:
                keys = list(i.keys())
                for j in keys:
                    if i[j] == "":
                        cell = "empty cell"
                        parsed_records += f"{j}: {cell}, "
                    else:
                        parsed_records += f"{j}: {i[j]}, "
                parsed_records += "\n"
            parsed_records = parsed_records[:-3] # remove the last \n and the last ,
            return parsed_records
                   
        else:
            return None