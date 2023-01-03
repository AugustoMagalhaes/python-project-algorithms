def is_palindrome_iterative(word):
    try:
        if not word or type(word) is not str:
            return False
        word_as_list = list(word)
        reversed_word_list = word_as_list[-1::-1]

        return word_as_list == reversed_word_list
    except TypeError:
        return None
