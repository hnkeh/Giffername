# Python imports.
from google_images_download import google_images_download

# Main class.
class Giffloader:
    def __init__(self, keywords, download_path):
        # Values:
        self.keywords = keywords
        self.download_path = download_path
        self.arguments = {"keywords":self.keywords,
                          "limit":1,
                          "output_directory":self.download_path}

        # Objects.
        self.response = google_images_download.googleimagesdownload()
        
        # Adding fixed search function.
        setattr(google_images_download.googleimagesdownload, "suited_download", self._suited_search)
        
    # Private functions.
    # Suited search.
    def _suited_search(self, search_word):

        # Adding arguments for google_images_download.
        for arg in google_images_download.args_list:
            if arg not in self.arguments:
                self.arguments[arg] = None

        # Values.
        _sub_dir = "gifs"
        _url = 'https://www.google.com/search?as_st=y&tbm=isch&as_q=' + search_word + '&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=imgur.com&safe=images&tbs=isz:m,itp:animated,ic:trans,iar:s,ift:gif#imgrc=ZCwd24HS3ksnbM:'
        
        # Create directories in OS.
        self.response.create_directories(self.download_path, _sub_dir, "foo")
        # Downloading images.
        _raw_html = self.response.download_page(_url)
        items, errorCount, abs_path = self.response._get_all_items(_raw_html, self.download_path, _sub_dir, 1, self.arguments)
         
    # Public functions.
    # Download multiple gifs.
    def download_gifs(self):
        for word in self.keywords:
            self.response.suited_download(word)
