

Regex_Pattern = r'wikipedia'	# Do not delete 'r'.

import re
Test_String = raw_input()


match = re.findall(Regex_Pattern,Test_String)

print match

print "Number of matches :", len(match)