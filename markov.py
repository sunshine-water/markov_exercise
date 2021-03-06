from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    f = open(file_path)
    text = f.read()
    f.close() 
    return text


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    text = text_string.split()


    for i in range(len(text) -2):
        # if i + 1 < range(len(text) -1):
        my_tuple = (text[i], text [i + 1])
        value = text [i+2]
       #assign bi-gram tuples as dictionary keys
        if chains.get(my_tuple) == None:
            chains[my_tuple] = []

    # Set value to list of  all words to right of tuple
        chains[my_tuple].append(value)        
    
    return chains

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    # Selects random key from chains dict
    current_key = choice(chains.keys())
    text = [current_key[0],current_key[1]]

    # while the current key from chains is not none (still exists):

    while current_key in chains:        
        chosen_word = choice(chains[current_key])
        current_key = (current_key[1], chosen_word)
        text.append(chosen_word)
            # if text is none, don't print <-- Not necessary when you return instead of printing final thing
            # do print initial current_key value
    return " ".join(text) 



input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
