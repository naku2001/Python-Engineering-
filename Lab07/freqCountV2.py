# Author: Perfect Makuwerere
# Date: March 9, 2026
# Description: Counts word frequencies while excluding words found in a stopword set.

import os

def readStopWordsFile(stop_set):
    """
    Reads stopwords from a file into a set.
    :param stop_set: Set to store stopwords
    :type stop_set: set
    """
    filename = input("Please enter the name of the stopwords file: ")
    while not os.path.exists(filename):
        print(f"{filename} does not exist!")
        filename = input("Please enter the name of the stopwords file: ")
    
    with open(filename, 'r') as file:
        for line in file:
            stop_set.add(line.strip().lower()) # [cite: 74]

def readTextFile(word_dict, stop_set):
    """
    Reads text file and counts words only if they are NOT in the stop_set.
    :param word_dict: Dictionary for counts
    :param stop_set: Set of words to ignore
    """
    filename = input("Please enter the name of the file to analyze: ")
    while not os.path.exists(filename):
        print(f"{filename} does not exist!")
        filename = input("Please enter the name of the file to analyze: ")
    
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().lower().split()
            for word in words:
                if word not in stop_set: # [cite: 79]
                    word_dict[word] = word_dict.get(word, 0) + 1
                # [cite: 80] If in set, do nothing

def outputFreq(word_dict):
    print(f"The file contained {len(word_dict)} unique words.")
    for word, count in word_dict.items():
        print(f"{word}:{count}")

def main():
    stop_words = set() # [cite: 82]
    word_counts = {}
    readStopWordsFile(stop_words) # [cite: 84]
    readTextFile(word_counts, stop_words) # [cite: 85]
    outputFreq(word_counts)

if __name__ == "__main__":
    main()