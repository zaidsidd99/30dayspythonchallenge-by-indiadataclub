# Validate gmail addresses using regex ?

import re
pattern= "[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|edu|net)"
user_input=input()
if (re.search(pattern,user_input)):
    print("valid_email")
else:
 print ("invalid email")


