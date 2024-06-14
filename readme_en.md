# Japanese Learning Tool

## Introduction
This is a tool designed to help users memorize Japanese syllabaries. Users can practice Hiragana and Katakana by inputting the corresponding Romaji.

## Usage
1. Ensure the CSV file is formatted correctly with columns such as `index`, `hira`, `kata`, `roma`, `weight`.
2. Run the script and input command-line arguments as prompted.

### Command-line Arguments
- `-f`, `--file`: Specify the path to the data file, default is `data.csv`.
- `-r`, `--reset`: Reset all weights to 1.
- `-i`, `--input`: Specify the attribute to input, default is `roma`.
- `-d`, `--display`: Specify the attribute to display, default is `hira`.

### Interactive Operations
- Input the correct Romaji to match the displayed syllabary.
- Enter `?` to reveal the answer.
- Enter `q` to quit the program.

### Data Saving
- Upon exiting the program, all data will be saved to the specified CSV file.

## Example
```
python script.py -f mydata.csv -r
```
This command will load the `mydata.csv` file, reset all weights to 1, and then start the learning tool.

