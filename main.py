# import to count words
from collections import Counter
# list of popular conjunctions which are we not going to count (articles included)
popular_conjunctions = ['and', 'for', 'or', 'yet', 'but', 'nor', 'so'
                        , 'after', 'as', 'before', 'if', 'since', 'that'
                        , 'till', 'whether', 'where', 'because', 'how'
                        , 'than', 'when', 'the', 'a', 'an']


# Function to open and count the most frequent word from text
def open_count_txt():
    # open the text file and make it lowercase for easier interaction
    with open('bumajka.txt') as my_text:
        my_text_str = my_text.read()
    lowercase = my_text_str.lower()
    word_list = lowercase.split()

    # get rid of all conjunctions
    for i in word_list:
        for j in popular_conjunctions:
            if i == j:
                word_list.remove(i)

    # count and print most common words in the text
    word_count = Counter(word_list)
    print(word_count.most_common(5))


# writing the amount of words into the text file
def write_into_txt():
    command = input('would you like to input your words one by one (y/n): ')
    # if we want to write words one by one
    if command == 'y':
        # we just input words until the stop word
        # and write len of the list into file
        stop_word = input('enter your stop word: ')
        new_list = []
        word = input()

        while word != stop_word:
            word = input()
            new_list.append(word)
            new_count = Counter(new_list)

            # write into file most common words and the amount of them
        with open('write_here.txt', 'w') as my_text:
            my_text.write('The amount of inputted words is: ' + str(len(new_list))+'\n')
            my_text.write('Most common of which are: ' + str(new_count.most_common(5)))

    elif command == 'n':
        # we just input a string of word with commas
        input_string = input('input your words with commas: ')
        new_list = input_string.split()
        new_count = Counter(new_list)

        # write into file the amount of words and which are more common
        with open('write_here.txt', 'w') as my_text:
            my_text.write('The amount of inputted words is: ' + str(len(new_list)) + '\n')
            my_text.write('Most common of which are: ' + str(new_count.most_common(5)))
    # if none of the commands were entered we do nothing
    else:
        print('wrong command value!')

def main():
    command = input('would you like to read or to write: ')
    if command == 'read':
        open_count_txt()
    elif command == 'write':
        write_into_txt()
    else:
        print('wrong command value!')
main()