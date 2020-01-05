import os
import mutagen 
import pylast
import config
import wget
import time

"""
PARSING AUDIO FILES

# Looks like we can use mutagen
album_name = mutagen.File(trackname)['album'][0]

# although it looks like sometimes 'album' is not quite right, might have to 
use something like
for key in file.keys():
    if key.contains('alb'):
        album_name = file[key]

# or something like that, plus the same for the artist

GETTING ARTWORK

# Looks like we create the network object, 
# then grab the album object
# then grab the cover image

network = pylast.LastFMNetwork(api_key...)..
album = network.get_album(album_name)
image_uri = album.get_cover_image(size=SIZE_EXTRA_LARGE)
"""

testroot = "D:\MusicTest"
root = testroot
network = pylast.LastFMNetwork(api_key=config.API_KEY, api_secret=config.API_SECRET)
IMAGE_TYPES = [".png", ".jpg", ".gif", ".tiff", ".svg", ".jpeg"]

# artist = network.get_artist("Brian Eno")
# print(artist)

def do_the_thing(path):
    # recursion, baby
    for root, subdirs, files in os.walk(path):
        if files: # in a dir that has music in it
            if not has_art(files):
                track = os.path.join(root,files[0]) # just grab the first track
                get_cover(track)

def has_art(files):
    for f in files:
        if any(x in f for x in IMAGE_TYPES):
            return True
    return False     

def get_cover(track_name):
    f = open("shitballs.txt","a")
    print(track_name)
    metadata = mutagen.File(track_name).tags
    f.write(str(metadata) + "\n\n")
    # artist_name = 
    # album = network.get_album(artist_name, album_name)
    # image_url = album.get_cover_image(size=4)
    # wget.download(image_url, "cover.png")

# get_cover(network,"Julia Jacklin","Crushing")
do_the_thing(root)
print(root)


