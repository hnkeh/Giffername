#Python imports.
from google_images_download import google_images_download

#Main class.
class Giffloader:
    def __init__(self, keywords, download_path):
        #Values:
        self.keywords = keywords
        self.download_path = download_path

        #Objects.
        self.response = google_images_download.googleimagesdownload()


    #Private functions.
    #Download single gif.
    def _download_gif(self, search_word):
        self.arguments = {"keywords":search_word,
                          "limit":1,
                          "language":"English",
                          "no_directory":True,
                          "format":"gif",
                          "output_directory":self.download_path}

        self.response.download(self.arguments)

    
    #Public functions.
    #Download multiple gifs.
    def download_gifs(self):
        for word in self.keywords:
            self._download_gif(word)

