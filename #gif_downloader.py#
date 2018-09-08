# Python imports.
from google_images_download import google_images_download

# Main class.
class Giffloader:
    def __init__(self, keywords, download_path):
        # Values:
        self.keywords = keywords
        self.download_path = download_path

        # Adding fixed search function.
        #google_images_download.googleimagesdownload.suited_search = self._search        
        # Objects.
        self.response = google_images_download.googleimagesdownload()

        setattr(google_images_download.googleimagesdownload, "suited_download", self._search)

        
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

        # Values.
        main_directory = "downloads"

        print("Evaluating...")
        
        dir_name = "sub_dir_name"
        limit = 1

        # Create directories in OS.
        self.response.create_directories(main_directory, dir_name, "foo")

        url = 'https://www.google.com/search?as_st=y&tbm=isch&as_q=' + search_word + '&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=imgur.com&safe=images&tbs=isz:m,itp:animated,ic:trans,iar:s,ift:gif#imgrc=ZCwd24HS3ksnbM:'

        raw_html = self.response.download_page(url)

        items, errorCount, abs_path = self.response._get_all_items(raw_html, main_directory, dir_name, limit)
        
        print("dl done")
         
    # Public functions.
    # Download multiple gifs.
    def download_gifs(self):
        for word in self.keywords:
            self.response.suited_download(word)

