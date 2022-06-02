# Bill Splitter

The Bill Splitter is a simple and interactive command-line Python application that evenly divides a bill amount among friends. It also includes an optional "Who is lucky?" feature that allows one randomly chosen friend to have their share of the bill covered by the others.

## Features

- Input the total number of people sharing the bill (must be a positive number).
- Enter the name of each participant.
- Input the total bill amount.
- Decide whether to use the "Who is lucky?" feature to exempt a random friend from paying.
- If "Who is lucky?" is used, the bill is split evenly among all other participants, and the lucky one pays nothing.
- If "Who is lucky?" is not used, the bill is split evenly among all participants.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/bill-splitter.git
```

## How to Run

To run the program, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using Python:

```
python main.py
```

## Example Usage

```
$ python bill_splitter.py
Enter the number of friends joining (including you):
4
Enter the name of every friend (including you), each on a new line:
Alice
Bob
Charlie
David
Enter the total bill value:
100
Do you want to use the "Who is lucky?" feature? Write Yes/No:
Yes
Charlie is the lucky one!
{'Alice': 33.33, 'Bob': 33.33, 'Charlie': 0, 'David': 33.33}
```

## License

This project is licensed under the [MIT License](LICENSE.txt).
