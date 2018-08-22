# import glob
# foo = glob.glob("Documents/Python/Giffername/downloaded_gifs/*.gif")

# for f in foo:
#     fl = f.split("/downloaded_gifs/")
#     print(fl[1])

from boxx import *
from boxx.ylimg.ylimgVideoAndGif import *
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'downloaded_gifs/')

#gif_paths = ["1. hello_my_name_is_sticker", "1. ksfe", "1. bank-myna-6",]
gif_paths = ['loga','show','tree',]
fps = 24
spatial_down_sample = 1
time_down_sample = 1


a=0
a=1
if a:
    gifs = []
    for pp in gif_paths:
        gif = pp+'.gif')[::]
        gifs += [gif]
#        break
    ss = npa(map(x_.shape, gifs))
    print(ss)
#else:
    fs = ss[:,0]
    shape = ss.max(0)[[1, 2]]
    news = []
    for i,gif in enumerate(gifs):
        n , w, h, c = gif.shape
        print('%sth GIF has'%i,n,'pics')
        new =  np.zeros((n, *shape, c), np.uint8)
        new[:,:w,:h,:] = gif
        news.extend(new)
        news.extend(np.zeros((3, *shape, c), np.uint8))
    newgif = npa-news
    print('save to merged_one.gif....')
    gifSave(newgif[::time_down_sample,::spatial_down_sample,::spatial_down_sample,::],'merged_one.gif',fps)
print('OK')
