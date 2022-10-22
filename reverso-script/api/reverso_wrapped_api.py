from reverso_context_api import Client


class Reverso_Api():
    MAX_DEPTH = 100

    def __init__(self, source_lang="en", destination_lang="it"):
        self.source_lang = source_lang
        self.destination_lang = destination_lang
        self.client = Client(source_lang, destination_lang)

    def create_client(self, source_lang="en", destination_lang="it"):
        self.client = Client(source_lang, destination_lang)

    def get_client(self):
        return self.client

    def get_translations(self, word, depth=MAX_DEPTH):
        return list(self.client.get_translations(word))[:depth]

    def print_translations(self, word, depth=MAX_DEPTH):
        for i in self.get_translations(word, depth):
            print(i)

    def get_separated_translations(self, word, depth=MAX_DEPTH):
        # output like: "a / b / c "
        self.sheet_buffer = ""
        for i in self.get_translations(word, depth):
            self.sheet_buffer += i + " / "
        self.sheet_buffer = self.sheet_buffer[:len(self.sheet_buffer)-2]
        return self.sheet_buffer
