# history-plotter
Plots your ~/.zsh_history file to see what 10 commands you use the most.

## Getting Started
Issue the following to see command line options
```
$ python3 main.py --help
```

If no arguments are supplied, the program runs assuming your history dotfile is in your home directory and generates a plot file in your current directory.

### Prerequisites
This project was built using Python 3.7.6 and requires a few additional libraries
```
matplotlib 3.1.3
pandas 1.0.0
```
Though it is most simple to just install the latest version of the libraries.
```
$ pip3 install matplotlib
$ pip3 install pandas
```
