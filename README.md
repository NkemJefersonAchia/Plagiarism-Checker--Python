# Plagiarism Checker

A simple Python-based tool that helps detect potential plagiarism between two text documents by analyzing word frequency and calculating similarity percentages.

## Features

- Compare two text files for common words and their frequencies
- Search for specific words across both documents
- Calculate plagiarism percentage based on word overlap
- User-friendly menu-driven interface
- Clean tabular output for easy reading

## Requirements

- Python 3.x
- tabulate library for formatted table output

## Installation

### Step 1: Install Python
Make sure you have Python 3 installed on your system. You can check by running:
- bash
- python3 --version

### Step 2: Install Required Library
Install the tabulate library using the following command:
- bash
- sudo apt install python3-tabulate

### Step 3: Download the Program
Save the plagiarism checker code as `plagiarism_checker.py` on your computer.

## How to Use

### Step 1: Prepare Your Text Files
Create two text files that you want to compare for plagiarism. For example:
- essay1.txt
- essay2.txt

Make sure these files are in the same directory as your `plagiarism_checker.py` file.

### Step 2: Run the Program
Open your terminal or command prompt, navigate to the directory containing the program, and run:
- bash
- python3 plagiarism_checker.py

### Step 3: Enter File Names
When prompted, enter the names of your two essay files:

- Enter the first essay filename (e.g., 'essay1.txt'): essay1.txt
- Enter the second essay filename (e.g., 'essay2.txt'): essay2.txt


### Step 4: Choose from the Menu
The program will display a menu with four options:

#### Option 1: Show Common Words
- Displays all words that appear in both essays
- Shows the frequency count for each word in both documents
- Results are presented in a neat table format

#### Option 2: Search for Specific Word
- Allows you to search for a particular word
- Shows how many times the word appears in each essay
- Helpful for checking specific terms or phrases

#### Option 3: Calculate Plagiarism Percentage
- Calculates the similarity percentage between the two documents
- Uses a threshold of 50% to determine if plagiarism is detected
- Shows the result in a clear table format

#### Option 4: Exit
- Closes the program safely

## Example Usage


=====================================================
Welcome to the Plagiarism Checker!
Before you start,enter the filenames of the two essays you want to compare.
Enter the first essay filename (e.g., 'essay1.txt'): sample1.txt
Enter the second essay filename (e.g., 'essay2.txt'): sample2.txt

=================================================

=========Plagiarism Checker Menu===============
1. Show common words and their frequencies
2. Search for a specific word
3. Calculate plagiarism percentage
4. Exit
=================================================
Enter your choice (1-4): 3

╒══════════════╤════════════════╕
│ Plagiarism % │ Result         │
╞══════════════╪════════════════╡
│ 65.43%       │ Plagiarism     │
╘══════════════╧════════════════╛


## Understanding the Results

### Plagiarism Percentage
- **Above 50%**: Indicates potential plagiarism
- **Below 50%**: Suggests the documents are sufficiently different
- The calculation is based on the ratio of common unique words to total unique words

### Word Frequency Analysis
- Shows exact counts of how often words appear in each document
- Helps identify the most commonly shared terms
- Useful for understanding the nature of similarities

## Troubleshooting

### File Not Found Error
If you see "Error: 'filename' not found", make sure:
- The file exists in the same directory as the program
- You spelled the filename correctly
- The file has the correct extension (e.g., .txt)

### Empty Files
If your text files are empty, the program will display "Cannot proceed without both essay files."

### Installation Issues
If the tabulate library doesn't install with the apt command, try:
- bash
- pip3 install tabulate


## Limitations

- The program only analyzes individual words, not phrases or sentences
- Punctuation is removed during analysis
- Case sensitivity is ignored (all text is converted to lowercase)
- Only supports plain text files

## Tips for Best Results

1. Use properly formatted text files with clear content
2. Ensure both files contain substantial text for meaningful comparison
3. Remember that high similarity doesn't always mean plagiarism - it could indicate proper citation or common topic vocabulary
4. Use this tool as a starting point for plagiarism detection, not as the final authority

## Programming Concepts Used in Implementation

This plagiarism checker demonstrates several important programming concepts:

**Data Structures:**
- **Lists**: Used to store words from text files (`words1`, `words2`) and table data for display
- **Dictionaries**: Counter objects act as dictionaries to store word frequencies
- **Sets**: Used for finding intersections and unions when calculating plagiarism percentage

**Control Structures:**
- **While loops**: Main program loop for the menu system that continues until user chooses to exit
- **For loops**: Used in `find_common_words()` to iterate through common words and build the table
- **Conditional statements (if/elif/else)**: Menu choice processing and error handling throughout the program

**Functions and Modular Programming:**
- **Function definitions**: Six well-defined functions each handling specific tasks (`load_text`, `get_word_counts`, `find_common_words`, `search_word`, `calculate_plagiarism_percentage`, `main`)
- **Function parameters and return values**: Functions accept parameters and return processed data
- **Main function pattern**: Using `if __name__ == "__main__"` for proper program entry point

**File I/O Operations:**
- **File reading**: Opening and reading text files using `open()` and `file.read()`
- **Exception handling**: Try-catch blocks to handle file not found errors

**String Processing:**
- **String methods**: `.lower()` for case normalization, `.split()` for word separation
- **String translation**: Using `str.maketrans()` and `.translate()` to remove punctuation

**Built-in Libraries and Modules:**
- **Collections module**: Using `Counter` for efficient word counting
- **String module**: Using `string.punctuation` for punctuation removal
- **External library**: `tabulate` for formatted table output

**Set Operations:**
- **Set intersection (`&`)**: Finding common elements between two sets
- **Set union (`|`)**: Combining all unique elements from both sets

**Mathematical Operations:**
- **Percentage calculations**: Computing plagiarism percentage using division and multiplication
- **Dictionary methods**: `.get()` with default values for safe key access

**User Interface Design:**
- **Input/output operations**: Using `input()` and `print()` for user interaction
- **Menu-driven programming**: Structured menu system with numbered options
- **Formatted output**: Using tabulate library for professional-looking tables

---

**Note**: This tool is designed for educational purposes and should be used as part of a comprehensive plagiarism detection strategy, not as the sole method for determining academic misconduct.
