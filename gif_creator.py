#Python imports.
import glob
from boxx import *
from boxx.ylimg.ylimgVideoAndGif import *

#Main class.
class Giff_creator:
    def __init__(self, gif_path):
        
        #Values.
        self.gif_names = ["loga", "show", "tree"]
        #self.gif_path = "/downloaded_gifs/"
        self.gif_path = gif_path
        self.fps = 24
        self.spatial_down_sample = 1
        self.time_down_sample = 1

    #Public functions.
    #Returns path.
    def get_path(self):
        pass
    
    #Create merge gif.
    def merge_gifs(self):

        _read_gifs = []
        _gif_files = glob(self.gif_path + "*.gif")
        
        for gifname in _gif_files:
            formated_gifname = gifname.split("/downloaded_gifs/")
            print("'" + formated_gifname[1] + "', ")
            _current_gif = imread(self.gif_path + formated_gifname[1])[::]
            _read_gifs += [_current_gif]
            
        ss = npa(map(x_.shape, _read_gifs))

        print(ss)
        fs = ss[:,0]
        shape = ss.max(0)[[1, 2]]
        news = []
        for i, gif in enumerate(_read_gifs):
            n , w, h, c = gif.shape
            print('%sth GIF has'%i,n,'pics')
            new =  np.zeros((n, *shape, c), np.uint8)
            new[:,:w,:h,:] = gif
            news.extend(new)
            news.extend(np.zeros((3, *shape, c), np.uint8))
        newgif = npa-news

        gifSave(newgif[::time_down_sample,::spatial_down_sample,::spatial_down_sample,::],'./Downloads/gifs/one.gif',fps)
