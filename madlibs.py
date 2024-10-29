# Assignment 3 Question 2
# Author: Aryan Chaturvedi 260976059

import random
import pickle

def capitalize_sentences(string_sentence):
    """(str) -> str
    Returns a string with the first letter of each sentence capitalized
    
    >>> capitalize_sentences("hello. hello! hello???? HI!")
    'Hello. Hello! Hello???? HI!'
    >>> capitalize_sentences(" good morning! or is it afternoon already? Today we will be learning.... ")
    'Good morning! Or is it afternoon already? Today we will be learning....'
    >>> capitalize_sentences("....this statement won't be capitalised. but this one will be!")
    "....this statement won't be capitalised. But this one will be!"
    """
    # removes any whitespaces from the start and end of string
    string_sentence = string_sentence.strip()
    capitalized_sentence = string_sentence[0].upper() # First letter capitalized
    end_mark_list = ['.', '!', '?']
    
    for index in range(1, len(string_sentence)):
        
        # if character before current index is a space, and the character before that ends a previous sentence
        if string_sentence[index - 1] == ' ' and string_sentence[index - 2] in end_mark_list:
            
            # add a capitalised character to the string
            capitalized_sentence += string_sentence[index].upper()
        else:
            # add regular character to the string
            capitalized_sentence += string_sentence[index]
        
    return capitalized_sentence

def capitalize_sentence_grid(nested_list):
    """(list) -> list
    Returns a nested list sentences with the first character of each new sentece capitalised
    
    >>> grid = [["you", "might", "think"], ["these", "are", "separate", "sentences"], ["but", "they", "are", "not!", "ok,", "this"], ["one", "is."]]
    >>> capitalize_sentence_grid(grid)
    [['You', 'might', 'think'], ['these', 'are', 'separate', 'sentences'], ['but', 'they', 'are', 'not!', 'Ok,', 'this'], ['one', 'is.']]
    
    >>> grid = [['are', 'you', 'ready'], ['to', 'rumble???', 'come', 'down'], ['to', 'the', 'monster', 'truck', 'showdown', 'tomorrow', 'night!'],['tickets', 'now', 'up', 'for', 'sale!']]
    >>> capitalize_sentence_grid(grid)
    [['Are', 'you', 'ready'], ['to', 'rumble???', 'Come', 'down'], ['to', 'the', 'monster', 'truck', 'showdown', 'tomorrow', 'night!'], ['Tickets', 'now', 'up', 'for', 'sale!']]
    
    >>> grid = [['holy!', 'cow!', 'you', 'have'],['to', 'come', 'see', 'this!'], ['this', 'is', 'soooooo', 'exciting!!!']]
    >>> capitalize_sentence_grid(grid)
    [['Holy!', 'Cow!', 'You', 'have'], ['to', 'come', 'see', 'this!'], ['This', 'is', 'soooooo', 'exciting!!!']]
    """
    capital_outer_list = []
    # starts the loop with previous index pre-set so that first character of list can be capitalised
    previous_index = '.'
    end_mark_list = ['.', '!', '?']
    
    # looping through the outer list of the grid
    for inner_list in nested_list:
        capital_inner_list = []
        
        # looping through the inner list of grid
        for word in inner_list:
            if previous_index in end_mark_list:
                capital_inner_list.append(capitalize_sentences(word))
            else:
                capital_inner_list.append(word)
            
            # change previous index to last character of each word for next iteration
            previous_index = word[-1]
                
        capital_outer_list.append(capital_inner_list)
    
    return capital_outer_list

def fill_in_madlib(madlib_string, parts_of_speech):
    """(str, dict) -> str
    Returns the madlib string with the word replacement filled in
    >>> random.seed(1)
    
    >>> dictionary = {'ADJECTIVE': ['exciting', 'amazing', 'boring'], 'VERB': ['hiking', 'canoeing', 'surfing']}
    >>> madlib_string = 'yesterday, we went [VERB], and it felt so [ADJECTIVE]'
    >>> fill_in_madlib(madlib_string, dictionary)
    'Yesterday, we went hiking, and it felt so boring'
    
    >>> dictionary = {'PAST-TENSE-VERB': ['pondered', 'scribbled', 'snoozled'], 'ADJECTIVE': ['dreamy', 'weary', 'starry', 'lazy']}
    >>> madlib_string = "once upon a midnight [ADJECTIVE_1], while I [PAST-TENSE-VERB], [ADJECTIVE_2] and [ADJECTIVE_3]"
    >>> fill_in_madlib(madlib_string, dictionary)
    'Once upon a midnight dreamy, while I scribbled, weary and lazy'
    
    >>> dictionary = {'ADJECTIVE': ['amazing', 'boring']}
    >>> madlib_string = 'i found the concert [ADJECTIVE_1]! but jake found it [ADJECTIVE_2]. did you find it [ADJECTIVE_1] or [ADJECTIVE_2]?'
    >>> fill_in_madlib(madlib_string, dictionary)
    'I found the concert boring! But jake found it amazing. Did you find it boring or amazing?'
    
    >>> dictionary = {'VERB': ['jump']}
    >>> madlib_string = ''
    >>> fill_in_madlib(madlib_string, dictionary)
    ''
    
    >>> madlib_string = True
    >>> dictionary = ['amazing', 'boring']
    >>> fill_in_madlib(madlib_string, dictionary)
    Traceback (most recent call last):
    AssertionError: first argument is not of type 'str' or second argument is not of type 'dict'
    
    >>> madlib_string = 'Yesterday, we went [[VERB], and it felt so [ADJECTIVE'
    >>> dictionary = {'ADJECTIVE': 'exciting', 'VERB': 'jump'}
    >>> fill_in_madlib(madlib_string, dictionary)
    Traceback (most recent call last):
    AssertionError: square brackets are not paired
    
    >>> madlib_string = 'Yesterday, we went [VERB], and it felt so [ADJECTIVE]'
    >>> dictionary = {'ADJECTIVE': 'exciting', 'VERB': 'jump'}
    >>> fill_in_madlib(madlib_string, dictionary)
    Traceback (most recent call last):
    AssertionError: corresponding dictionary value is not of type 'list'
    
    >>> madlib_string = "Once upon a midnight [ADJECTIVE_1], while I [PAST-TENSE-VERB], [ADJECTIVE_2] and [ADJECTIVE_3]"
    >>> dictionary = {'PAST-TENSE-VERB': ['pondered', 'scribbled', 'snoozled'], 'ADJECTIVE': ['dreamy', 'weary']}
    >>> fill_in_madlib(madlib_string, dictionary)
    Traceback (most recent call last):
    AssertionError: corresponding dictionary value has not been provided with sufficient synonymous words
    
    >>> madlib_string = "Once upon a midnight [ADVERB], while I [VERB], [ADJECTIVE_1] and [ADJECTIVE_2]"
    >>> dictionary = {'PAST-TENSE-VERB': ['pondered', 'scribbled', 'snoozled'], 'ADJECTIVE': ['dreamy', 'weary']}
    >>> fill_in_madlib(madlib_string, dictionary)
    Traceback (most recent call last):
    AssertionError: annotated blank word is not in a key in the provided dictionary
    """
    # condition validates whether input type is invalid
    if (type(madlib_string) != str) or (type(parts_of_speech) != dict):
        raise AssertionError("first argument is not of type 'str' or second argument is not of type 'dict'")
        
    if madlib_string == '':
        return ''
    # condition check for any open square brackets
    elif madlib_string.count('[') != madlib_string.count(']'):
        raise AssertionError("square brackets are not paired")
    
    # deep copying the input dictionary
    word_replacement_dict = {}
    for key, value in parts_of_speech.items():
        if type(value) != list:
            raise AssertionError("corresponding dictionary value is not of type 'list'")
        # slice entire list and replace word_replacement_dict's key's corresponding values
        value_list = value[:]
        word_replacement_dict[key] = value_list
    
    # converts all '[' and ']' in string to '§' and splits into lists at each interval
    madlib_string = madlib_string.replace('[', '§')
    madlib_string = madlib_string.replace(']', '§')
    string_list = madlib_string.split('§')
    
    
    annotated_words = {}
    # new dictionary stores every second element of list as keys
    for i in range(1, len(string_list), 2):
        annotated_words[string_list[i]] = 0
    
    for key in annotated_words:
        # condition checks if annotated word is followed by an integer
        if key[-1].isdigit() == True:
            
            # slice string until index of '_'
            index = key.find('_')
            word = key[:index]
            
            # checks if word is a key in the dictionary and that it's corresponding value has sufficient number of synonyms
            if (word in word_replacement_dict) and (len(word_replacement_dict[word]) > 0):
                choice = random.choice(word_replacement_dict[word])
                # picks a synonyms from list and remove that synonym for the next iteration
                word_replacement_dict[word].remove(choice)
                
                # add choice to the annotated_words dictionary as a value
                annotated_words[key] = choice
            
            # word is a key, but corresponding dict value doesn't have sufficient number of synonyms
            elif word in word_replacement_dict:
                raise AssertionError("corresponding dictionary value has not been provided with sufficient synonymous words")
            
            # word is not a key in the dictionary
            else:
                raise AssertionError("annotated blank word is not in a key in the provided dictionary")
        
        # if no integers follow the annotated word, then no slicing string or removing choice from list is required
        else:
            if key in word_replacement_dict  and (len(word_replacement_dict[key]) > 0):
                annotated_words[key] = random.choice(word_replacement_dict[key])
            elif key in word_replacement_dict:
                raise AssertionError("corresponding dictionary value has not been provided with sufficient synonymous words")
            else:
                raise AssertionError("annotated blank word is not in a key in the provided dictionary")
    
    # loop replaces every annotated blank space with corresponding key-value from annotated_words
    for j in range(1, len(string_list), 2):
        string_list[j] =  annotated_words[string_list[j]]
     
    # join list back into a string and capitalize it
    rejoined_string = ''.join(string_list)
    filled_string = capitalize_sentences(rejoined_string)
    
    return filled_string

def load_and_process_madlib(filename):
    """(str) -> NoneType
    Void function that fills in madlib string and appends it to a different file
    
    >>> random.seed(0)
    >>> load_and_process_madlib('madlib1.txt')
    >>> f = open('madlib1_filled.txt', 'r')
    >>> s = f.read()
    >>> f.close()
    >>> s
    'Once upon a midnight weary, while I snoozled, dreamy and lazy,'
    
    >>> random.seed(1)
    >>> load_and_process_madlib('madlib2.txt')
    >>> f = open('madlib2_filled.txt', 'r')
    >>> s = f.read()
    >>> f.close()
    >>> s
    'Yesterday, we went hiking, and it felt so exciting'
    
    >>> random.seed(9)
    >>> load_and_process_madlib('madlib3.txt')
    >>> f = open('madlib3_filled.txt', 'r')
    >>> s = f.read()
    >>> f.close()
    >>> s
    'I found the concert amazing! But jake found it boring. Did you find it amazing or boring?'
    """
    # read content from the given file name
    madlib_object = open(filename, 'r')
    madlib_string = madlib_object.read()
    madlib_object.close()
    
    # read content from the dictionary pickle file
    word_object = open('word_dict.pkl', 'rb')
    word_dict = pickle.load(word_object) # using the load() method
    word_object.close()
    
    # fill in the annotated blank spaces in the madlib_string
    filled_string = fill_in_madlib(madlib_string, word_dict)
    
    # creating new filename by splittnig string and inserting '_filled.' in between
    filename_list = filename.split('.')
    new_filename = '_filled.'.join(filename_list)
    
    # write filled_string into a new corresponding file
    madlib_filled = open(new_filename, 'w')
    madlib_filled.write(filled_string)
    madlib_filled.close()
    
    
# Assignment 3 Question 3
def generate_comment():
    """(None) -> str
    Returns filled in madlib_string from randomly selected madlib[k].txt file
    >>> random.seed(1)
    >>> generate_comment()
    "Elsa IfStatement is so circumstantial and detailed when it comes to procedures planning. Maybe that should be her department instead of president. She'd make a great right hand for Dee Bug-Her."
    
    >>> random.seed(2)
    >>> generate_comment()
    "In my opinion Transparency is key in running any organization. I don't know how he managed to get elected last time, but clearly his management has gotten the CSSSMU into wreckage. I side with Dee Bug-Her on this one! You go!"
    
    >>> random.seed(3)
    >>> generate_comment()
    'How is Dee Bug-Her lowering the passing grade down to 40% not disdainful to you? I would totally not approve this. Come on, give me a platform and a hurdle to prove myself instead of making me take the lazy river.'
    """
    # variable k is randomly selected between 1 to 10
    k = str(random.randint(1, 10))
    # inserted into a list
    filename_list = ['madlib', k , '.txt']
    # joined using the .join() method
    filename = ''.join(filename_list)
    
    # generates randomly filled in madlib_string
    load_and_process_madlib(filename)
    
    # obtain the saved string from the _filled.txt file
    new_filename_list = filename.split('.')
    new_filename = '_filled.'.join(new_filename_list)
    madlibk_object = open(new_filename, 'r')
    madlibk_string = madlibk_object.read()
    madlibk_object.close()
    
    return madlibk_string