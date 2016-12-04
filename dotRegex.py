import re
regex_pattern = r"abc\.\def\.ghi\.jkx"	# Do not delete 'r'.


test_string= raw_input()

match=re.match(regex_pattern,test_string) is None
print re.search(regex_pattern,test_string)

