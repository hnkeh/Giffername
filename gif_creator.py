# USING FOR IMAGES.
# import os
# import imageio

# gif_dir = './Downloads/gifs/'
# images = []
# for file_name in os.listdir(gif_dir):
#     if file_name.endswith('.gif'):
#         file_path = os.path.join(gif_dir, file_name)
#         images.append(imageio.imread(file_path))
# imageio.mimsave('./Downloads/gifs/movie.gif', images)

#Python imports.
import glob
from boxx import *
from boxx.ylimg.ylimgVideoAndGif import *

#Main class.
class Giffeator:
    def __init__(self):
        
        #Values.
        self.gif_names = ["ddd", "lol", "sss"]
        self.gif_path = "/downloaded_gifs/"
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
        for gif_name in gif_names:
            _current_gif = imread(gif_path + gif_name + '.gif')[::]
            _read_gifs += [_current_gif]

        ss = npa(map(x_.shape, _read_gifs))
    
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

        gifSave(newgif[::time_down_sample,::spatial_down_sample,::spatial_down_sample,::],'./Downloads/gifs/merged_one.gif',fps)
