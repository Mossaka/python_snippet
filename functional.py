from itertools import compress, cycle
from functools import reduce
import string

class Functional:
    def get_even_letters():
        """
        get the even letters using `compress` and `cycle`. 
        """
        letters = string.ascii_uppercase
        even_letters = compress(letters, cycle([0,1]))
        print(list(even_letters))
