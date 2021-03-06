""" We study words from the hills dictionary that form a different word when read backwards.

>>> is_reword('reward')
True

No palindromes allowed this time.

>>> is_reword('rotor')
False

Case will be ignored.

>>> is_reword('Pat')
True
>>> is_reword('turtle')
False


How many rewords of length eight?

>>> len(rewordset(8))
10

"""

from words import HILLSDICTFILE
from words import is_word, wordset



def is_reword(s):
    """Returns True only if s and s backwards are different words in the hills dictionary.
    """

    # REPLACE THE pass BELOW WITH YOUR OWN CODE.
    
    if is_word(s) and is_word(s[::-1]) and s != s[::-1]:
        return True
    else:
        return False
        


def rewordset(size):
    """Returns a set with all 'rewords' of that size from the hills dictionary.
    All words are in lower-case and none are palindromes.
    """
    
    # REPLACE THE pass BELOW WITH YOUR OWN CODE.
    mywordset = set()
    words = wordset(size)
    for word in words:
        if word[::-1] in words:
            mywordset.add(word)    
    return mywordset

