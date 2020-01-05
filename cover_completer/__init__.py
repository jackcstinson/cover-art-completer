import os
import pylast
import cover_completer.config
import wget
from tinytag import TinyTag
import re

testroot = "D:\Music\King Crimson"
root = testroot
network = pylast.LastFMNetwork(api_key=config.API_KEY, api_secret=config.API_SECRET)
IMAGE_TYPES = [".png", ".jpg", ".gif", ".tiff", ".svg", ".jpeg"]
MUSIC_TYPES = [".m4a", ".flac", ".mp3", ".mp4", ".wav", ".pcm", ".aiff", ".aac", ".wma", ".alac"]

# artist = network.get_artist("Brian Eno")
# print(artist)

def do_the_thing(path):
    # recursion, baby
    print("Searching...")
    for root, subdirs, files in os.walk(path):
        if has_filetype(files, MUSIC_TYPES): # in a dir that has music in it
            if not has_filetype(files, IMAGE_TYPES): # with no images
                any_old_audio = get_audiotrack(files)
                track_name = os.path.join(root,any_old_audio) # just grab the first track
                (artist_name, album_name) = get_metadata(track_name)
                get_cover(artist_name, album_name, root)


def has_filetype(files, filetypes):
    for f in files:
        if any(x in f for x in filetypes):
            return True
    return False

def get_audiotrack(files):
    for f in files:
        if any(x in f for x in MUSIC_TYPES):
            return f   

def get_metadata(track_name):
    # TODO this has to look at the format and decide how to get it
    artist_name = ""
    album_name = ""

    try:
        tag = TinyTag.get(track_name)
        artist_name = tag.artist.rstrip('\x00')
        album_name = tag.album.rstrip('\x00')
        album_name = re.sub("\[.+\]", '', album_name).rstrip() # remove shit like '[Stereo Remaster]'
    except:
        print("Tinytag couldn't parse " + track_name)

    return (artist_name, album_name) 

def get_cover(artist_name, album_name, directory):
    try:
        album = network.get_album(artist_name, album_name)
        image_url = album.get_cover_image(size=4)
        wget.download(image_url, os.path.join(directory, "cover.png"), False)
    except:
        if "(" in album_name:
            print("Could not get art for album " + album_name, "  will try removing brackets")
            album_name = re.sub("\(.+\)", '', album_name).rstrip()
            print(album_name)
            get_cover(artist_name, album_name, directory)
        else:
            print("Could not get art for album " + album_name)

if __name__ == "__main__":
    do_the_thing(root)


