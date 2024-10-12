import string
import keyword
from bdb import Breakpoint

sumbols =  ['_', '__', '___', 'x', 'get_value', 'get value', 'get!value', 'some_super_puper_value', 'Get_value',
             'get_Value', '3m', 'm3', 'assert', 'assert_exception']
for test_sumbols in sumbols:
    if len(test_sumbols()) > 0:
        if test_sumbols in keyword.kwlist:
                print(f"ERROR  {test_sumbols} Found")
            elif not test_sumbols[0].isnumeric() and test_sumbols.islower() and test_sumbols.count(" ") == 0:
                is_ok = True
                for sumbols in string.punctuation.replace("_", ""):
                    if sumbols in test_sumbols:
                        is_Good = False
                        print(f"ERROR {test_sumbols} Found")
                        break

            if is_ok:
                print(f"Keyword {test_sumbols} is OK")
        else:
            print(f"ERROR {test_sumbols} Found")
    else:
        print("Incorrect variable length!")