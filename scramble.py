#
#    This could be used to create random
#    passwords from sentences that could
#    be saved in a file somewhere.
#    Password length is set by the
#    string length in the print statement.
#    The final variable strips spaces from the
#    sentence. It's best not to start them
#    with a capitol, as it will always be
#    used first and is obvious.
#
# The next 2 lines are need to keep pylint quiet.
# pylint: disable=invalid-name
from __future__ import print_function
import sys
print(sys.executable)
print(sys.version, "\n")

string1 = 'i like 1 4 all and such'
string2 = 'they are gr8 mottos'
string_comb = ''.join([''.join(x) for x in zip(string1, string2)])
string_final = string_comb.replace(' ', '')
print(string_final[:26])
