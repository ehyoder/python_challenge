# Dependencies 
import string
import sys
import re

# Files to load and output
input_file = "paragraph_1.txt" 
output_file = "paragraph_analysis.txt"

# Read text file  
paragraph_text = open(input_file, 'r')
paragraph_data = paragraph_text.read()

# Find the number of words in the text file
character_count = len(paragraph_data) 
spaces = paragraph_data.count(' ')
character_count_no_spaces = character_count - spaces 
word_count = len(paragraph_data.split())

# Find the number of sentences by feeding text into findall(); it returns a list of all the found strings
sentence_count = len(re.findall(r'\.', paragraph_data))

# Find the average letter count
average_letter_count = character_count_no_spaces/word_count

# Find average sentence length
average_sentence_len = word_count/sentence_count

# Store paragraph analysis as variable, round down results to 3 decimal places, and print to terminal 
paragraph_analysis = (
    f"\nParagraph Analysis\n"
    f"--------------------\n"
    f"Approximate word count is: {word_count}\n"
    f"Approximate sentence count is: {sentence_count}\n"
    f"Average letter count (per word) is: {average_letter_count:.3f}\n"
    f"Average sentence length is: {average_sentence_len:.0f} words \n")
print(paragraph_analysis, end="")

# Export the paragraph analysis to a text file  
sys.stdout = open(output_file, 'w')
print(paragraph_analysis)

