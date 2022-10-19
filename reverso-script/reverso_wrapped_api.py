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
