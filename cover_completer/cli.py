import cover_completer
import argparse

def get_args():
    parser = argparse.ArgumentParser('Downloads all cover art recursively for given directory')
    parser.add_argument('root', type=str, help="Your music directory")
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    cover_completer.do_the_thing(args.root)
