# Python imports.
from google_images_download import google_images_download
from request import * 

# Main class.
class Giffloader:
    def __init__(self, keywords, download_path):
        # Values:
        self.keywords = keywords
        self.download_path = download_path

        # Objects.
        self.response = google_images_download.googleimagesdownload()

        self.response.search = self._search

    # Private functions.
    # Download single gif.
    def _download_gif(self, search_word):
        self.arguments = {"keywords":search_word,
                          "limit":1,
                          "language":"English",
                          "no_directory":True,
                          "format":"gif",
                          "output_directory":self.download_path}
    

        self.response.search(self.arguments)

    # Suited search.
    def _search(self, search_word):

        #Values.
        search_term = search_word
        main_directory = "downloads"
        paths = {}
        i = 0

        print("Evaluating...")
        
        dir_name = "sub_dir_name"

        #create directories in OS.
        self.response.create_directories(main_directory,dir_name, "foo")

        url = 'https://www.google.com/search?as_st=y&tbm=isch&as_q=' + quote(search_term) + '&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=imgur.com&safe=images&tbs=isz:m,itp:animated,ic:trans,iar:s,ift:gif#imgrc=ZCwd24HS3ksnbM:'

        raw_html = self.response.download_page(url)

        print("Starting Download...")
        
        items, errorCount, abs_path = self.response._get_all_items(raw_html,main_directory,dir_name, 1)    #get all image items and download images

    #Public functions.
    #Download multiple gifs.
    def download_gifs(self):
        for word in self.keywords:
            self._download_gif(word)

