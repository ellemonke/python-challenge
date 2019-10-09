import os
import re

# Ask the user for which file to analyze
text_file = input("Which text file would you like to analyze? ")
absolute_path = os.path.abspath(text_file)


with open(absolute_path) as input_file:

    # Converts the text file into a string
    paragraph = input_file.read()

    # Remove problematic characters
    paragraph = paragraph.replace('"',' ')
    paragraph = paragraph.replace('\n','')

    # Find Word Count
    words = []
    words = paragraph.split()
    word_count = len(words)

    # Find Sentence Count
    sentences = []
    sentences = re.split("(?<=[.!?])", paragraph)
    sentences = list(filter(None, sentences))
    sentence_count = len(sentences)

    # Find Average Letter Count (per word) 
    letter_count = []
    for word in words:
        letter_count.append(len(word))
    ave_letter_count = sum(letter_count)/len(letter_count)

    # Find Average Sentence Length (split by words)
    sentence_length = []
    for sentence in sentences:
        sentence_length.append((len(sentence.split())))
    ave_sentence_length = sum(sentence_length)/len(sentence_length)


# Print results    
print("Paragraph Analysis\n-----------------\n")
print(f"Approximate Word Count: {word_count}")
print(f"Approximate Sentence Count: {sentence_count}")
print(f"Average Letter Count: {round(ave_letter_count,1)}")
print(f"Average Sentence Length: {round(ave_sentence_length,1)}")
