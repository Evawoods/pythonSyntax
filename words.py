def print_upper_words(words):
    """"Print each word on a separate line in all caps
    
     # example 

     print_upper_words(['hey', 'hi'])

     HEY
     HI
    """

    for word in words:
        print(word.upper())

# change the function so that it only prints words that start with the letter 'e'

def print_upper_words_2(words):
    """Print each word on a separate line in all caps, as long as
    it starts with the letter e
    
    #example
    
    print_upper_words_two(['hello', 'elf', 'elephant', 'apple'])

    ELF
    ELEPHANT
    """

    for word in words:
        if word.startswith('e') or word.startswith("E"):
            print(word.upper())

# make the functions more general. pass in a set of letters and it only prints words that start with one of those letters

def print_upper_words_3(words, letters):
    """Print each word on a separate line in all case, if it starts with a designated letter
    
    # example
    
    print_upper_words_3(['hello', 'hey', 'goodbye', 'yo', 'yes'], letters={'h', 'y'})

    HELLO
    HEY 
    YO
    YES
    """

    for word in words:
        for letter in letters:
            if word.startswith(letter):
                print(word.upper())


