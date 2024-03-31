#!/usr/bin/env python3

import sys
# Create a dictionary to store input sentences
dictionary = {}
# Initialize a user ID counter
user_id = 0 



# Read input lines from standard input and store them in the dictionary
for line in sys.stdin:
    dictionary[user_id] = line.strip() # Remove leading/trailing whitespaces
    user_id += 1 

# Initialize an empty set to store unique words (vocabulary)
vocabulary = set()

# Loop through each sentence in the dictionary and update the vocabulary with its words
for sen in dictionary.values():
    vocabulary.update(sen.split())

# Convert the vocabulary set into a sorted list
vocabulary = sorted(list(vocabulary))

# Enumerate the vocabulary to get index-word pairs
i_vocabulary = list(enumerate(vocabulary))

# Create a list of word indices
idvocabulary = [x for x in range(len(vocabulary))]

# Initialize an empty list to store tuples of (word_index, count) for each sentence
tup = []

# Loop through each sentence in the dictionary
for phrase, sen in dictionary.items():
    tup_sentence = []
    sen = sen.split()
    
    # Loop through each word in the vocabulary and check if it's in the sentence
    for idd, word in i_vocabulary:
        if word in sen:
            # If the word is present, add a tuple of (word_index, 1) to the sentence tuple
            tup_sentence.append((idd, 1))
    # Append the sentence tuple to the list of tuples
    tup.append(tup_sentence)

# Calculate Inverse Document Frequency (Inverse_Frequence) for each word
id_freq = [] 
for w in vocabulary: 
    total = 0  	
    for phrase, sen in dictionary.items():
        sen = sen.split()
        if w in sen: 
            total = total +  1 
    id_freq.append(total)    

# Combine word indices and their Inverse_Frequence values into tuples
Inverse_Frequence = list(zip(idvocabulary, id_freq))   

# Initialize an empty list to store TF-Inverse_Frequence values for each document
tdf = []

# Loop through each document (sentence) and its word counts
for document, w_counts in enumerate(tup):
    document_id_freq = []
    # Loop through each word and its count in the document
    for Word, total in w_counts:
        # Find the corresponding Inverse_Frequence value for the word
        matching_tuple = next((tpl for tpl in Inverse_Frequence if tpl[0] == Word), None )
        Inverse_FrequenceCount = matching_tuple[0+1]
        # Calculate TF-Inverse_Frequence score for the word in the document
        temp = total / Inverse_FrequenceCount
        tf_id_freq = temp
        # Append the word index and its TF-Inverse_Frequence score to the document's list
        document_id_freq.append((Word, tf_id_freq))
    # Append the TF-Inverse_Frequence values of the document to the main list
    tdf.append(document_id_freq)	

# Print the calculated TF-Inverse_Frequence values
print(tdf)