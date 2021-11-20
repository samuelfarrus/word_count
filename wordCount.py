import pandas


# custom error class definition
class Error(Exception):
    pass


class UnknownCmd(Error):  # custom error
    def __init__(self, msg):
        self.msg = msg


# word count function
def word_count(entry):
    txt = entry
    result = []  # generic variable, resulting words of the word counting process
    amount = []  # generic variable, amount result of the word counting process

    # dealing with á, è and others

    # cleaning text
    for x in '.,;:+-—*/=!?#$£¢@&()[]{}“"\'\n':
        txt = txt.replace(x, ' ')  # replacing all punctuation and line breaks with whitespaces

    # splitting text
    words = txt.split()

    # counting words
    for word in words:
        if len(word) <= 1:  # do not consider single letters
            pass
        else:
            if word in result:  # word already considered
                z = result.index(word)
                amount[z] += 1
            else:  # first time appearance
                result.append(word)
                amount.append(1)

    # returns a list
    return [result, amount]


# dictionary to work as a DataFrame structure
df_structure = {
    'WORD': None,
    'AMOUNT': None
}

# exe
if __name__ == '__main__':

    print('\nWelcome to the Word Count by samuelfarrus.\nType the \'.txt\' file to be analysed.')

    while True:  # selecting and validating file
        try:
            user_input = input('WC> ')

            if '.txt' not in user_input:
                user_input = user_input + '.txt'

            text_handling = open(user_input, 'r', encoding='utf_8')  # trying to open given file name

        except FileNotFoundError as fnf:
            print('No such file or directory: {}'.format(user_input))
        else:
            break

    # convert all chars to lower case to avoid misunderstandings
    text = text_handling.read().lower()

    # counting words
    word_counting = word_count(text)
    text_handling.close()

    # dictionary creation
    df_structure['WORD'] = word_counting[0]
    df_structure['AMOUNT'] = word_counting[1]

    # DataFrame creation
    df = pandas.DataFrame(df_structure)

    # asking the user how to sort
    print('\nChoose the sorting method. \
    \nType \'wa\' to sort by words (ascending). \
    \nType \'wd\' to sort by words (descending). \
    \nType \'aa\' to sort by amount of appearances (low to high). \
    \nType \'ad\' to sort by amount of appearances (high to low). \
    \nOr leave empty to sort by order of appearance.')

    while True:
        try:
            sort_input = input('WC> ')  # inserting sorting method

            if bool(sort_input) is True and sort_input not in ('wa', 'wd', 'aa', 'ad'):  # validating sort method
                raise UnknownCmd('Unknown method. Insert again.')

        except UnknownCmd as uc:
            print(uc)
        else:
            break

    # sorting definition
    if sort_input == 'wa':
        df = df.sort_values(by='WORD')  # sort by word ascending
    elif sort_input == 'wd':
        df = df.sort_values(by='WORD', ascending=False)  # sort by word descending
    elif sort_input == 'aa':
        df = df.sort_values(by='AMOUNT')  # sort starting from word with fewest appearances
    elif sort_input == 'ad':
        df = df.sort_values(by='AMOUNT', ascending=False)  # sort starting from word with most appearances
    else:
        pass

    # exporting to csv and ending the process
    df.to_csv('word_count_result.csv', index=False)
    print('Words counted. Process ended.')
