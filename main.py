import argparse
import shutil
import os
import pandas as pd

def main(args):
    shutil.copyfile(args.hist_file, os.path.join(args.hist_dir, 'history'))
    history = pd.read_csv('./history/history', sep="\n", names=['raw_history'], header=None)
    history[['timestamp','command']] = history['raw_history'].str.split(';', 1, expand=True)
    print(history)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    home_dir = os.environ.get("HOME","~")
    parser.add_argument("--hist-dir", type=str, default="history", help="provide path to where you want your history dotfile copied to")
    parser.add_argument("--plot-dir", type=str, default="plots", help="provide path to where you want plot files saved")
    parser.add_argument("--hist-file", type=str, default=f"{home_dir}/.zsh_history", help="provide path to your history dotfile")
    args = parser.parse_args()

    def mkdir(path):
        try:
            os.makedirs(path)
        except:
            pass

    mkdir(args.hist_dir)
    mkdir(args.plot_dir)

    main(args)

