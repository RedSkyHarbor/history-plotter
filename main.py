import argparse
import os

def mkdir(path):
    try:
        os.makedirs(path)
    except:
        pass

if __name__ == "__main__":
    parser = argparse.ArguementParser()
    home_dir = os.environ.get("HOME","~")
    parser.add_argument("--plot-file", type=str, default="history_plots", help="provide path to where you want plot files saved")
    parser.add_argument("--hist-file", type=str, default="%s/.zsh_history" % home_dir, help="provide path to your history dotfile") 
    args = parser.parse_args()

def main():
    pass


