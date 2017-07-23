import re
def palindrome_or_not(phrase):
    """
    This function tests whether or not a given phrase is a palindrome.

    :param phrase: the desired phrase that is to be tested
    :returns: boolean
    """
    # strip non-alphanumeric
    phrase = re.sub('[\W_]+', '', phrase)
    # convert to lowercase
    phrase = phrase.lower()
    return (phrase == phrase[::-1])
