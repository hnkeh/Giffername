#Local imports.
from parse_username import *
from gif_downloader import *

#Main class.
class Giffername:
    def __init__(self, username, dictionary_language = "en_US", gif_download_path = "Documents/Python/RedditBot/downloaded_gifs/"):
        #Values.
        self.username = username
        self.dictionary_language = dictionary_language
        self.gif_download_path = gif_download_path
        
        #Objects.
        self.username_parser = UsernameParser(self.username, self.dictionary_language)

    #Public functions.
    #Returns url of uploaded gif.
    def get_imgur_url(self):
        pass

    #Start Giffername.
    def start(self):
        _keywords = self.username_parser.get_words_in_username()
        giffloader = Giffloader(_keywords, self.gif_download_path)
        giffloader.download_gifs()


foo = Giffername(username = "himynameis")
foo.start()
    
