#!/usr/bin/env python3
import string
from collections import Counter
from tabulate import tabulate

#function that reads a text file, processes it, and returns a list of words

def load_text(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
            text = text.translate(str.maketrans('', '', string.punctuation))
            return text.split()
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
        return []

#function that counts the occurrences of each word in a list

def get_word_counts(words):
    return Counter(words)

# function that finds common words between two word count dictionaries

def find_common_words(counter1, counter2):
    common = set(counter1) & set(counter2)
    table = []
    for word in sorted(common):
        table.append([word, counter1[word], counter2[word]])
    return table

# function that searches for a specific word in two word count dictionaries

def search_word(word, counter1, counter2):
    word = word.lower()
    in_essay1 = counter1.get(word, 0)
    in_essay2 = counter2.get(word, 0)
    if in_essay1 == 0 and in_essay2 == 0:
        return False
    return [[word, in_essay1, in_essay2]]

#function that calculates the plagiarism percentage based on two lists of words

def calculate_plagiarism_percentage(words1, words2):
    set1, set2 = set(words1), set(words2)
    intersection = set1 & set2
    union = set1 | set2
    if not union:
        return 0
    return (len(intersection) / len(union)) * 100

#function that serves as the main entry point for the plagiarism checker program
def main():
    print("=====================================================")
    print("Welcome to the Plagiarism Checker!")
    print("Before you start,enter the filenames of the two essays you want to compare.")
    file1=input("Enter the first essay filename (e.g., 'essay1.txt'): ")
    file2=input("Enter the second essay filename (e.g., 'essay2.txt'): ")
    words1 = load_text(file1)
    words2 = load_text(file2)

    if not words1 or not words2:
        print("Cannot proceed without both essay files.")
        return

    counter1 = get_word_counts(words1)
    counter2 = get_word_counts(words2)

    while True:
        print("=================================================")
        print("\n=========Plagiarism Checker Menu===============")
        print("1. Show common words and their frequencies")
        print("2. Search for a specific word")
        print("3. Calculate plagiarism percentage")
        print("4. Exit")
        print("=================================================")


        choice = input("Enter your choice (1-4): ")
# Process the user's choice and call the appropriate function
        if choice == '1':
            common_table = find_common_words(counter1, counter2)
            if common_table:
                print(tabulate(common_table, headers=["Word", "Essay 1 Count", "Essay 2 Count"], tablefmt="fancy_grid"))
            else:
                print("No common words found.")

        elif choice == '2':
            word = input("Enter the word to search: ")
            result = search_word(word, counter1, counter2)
            if result:
                print(tabulate(result, headers=["Word", "Essay 1 Count", "Essay 2 Count"], tablefmt="fancy_grid"))
            else:
                print(f"'{word}' not found in either essay.")

        elif choice == '3':
            percentage = calculate_plagiarism_percentage(words1, words2)
# Display the plagiarism percentage and result using tabulate            
            print(tabulate([[f"{percentage:.2f}%", "Plagiarism" if percentage >= 50 else "No Plagiarism"]],
                           headers=["Plagiarism %", "Result"], tablefmt="fancy_grid"))

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

# The main function that runs the program. 
if __name__ == "__main__":
    main()
