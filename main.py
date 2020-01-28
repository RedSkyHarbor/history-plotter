import argparse
import os

def main(args):
    print(args)

def mkdir(path):
    try:
        os.makedirs(path)
    else:
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    home_dir = os.environ.get("HOME","~")
    parser.add_argument("--plot-file", type=str, default="history_plots", help="provide path to where you want plot files saved")
    parser.add_argument("--hist-file", type=str, default="%s/.zsh_history" % home_dir, help="provide path to your history dotfile") 
    args = parser.parse_args()
    main(args)



