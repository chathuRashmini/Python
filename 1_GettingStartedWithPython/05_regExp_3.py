# REGULAR EXPRESSIONS PART 03

import re

mail = 'From stephen.marquard@uct.ac.za Sat stephen.king@uct.ac.lk Jan  5 09:14:16 2008'
email1 = re.findall('\S+@\S+', mail)
print(email1)

email2 = re.findall('^From (\S+@\S+)', mail)
#gives only the mails starts by "From", but does not print 'From'
print(email2)
print(type(email2))

email3 = re.findall('@([^ ]*)', mail)
#starts by @, single non-blank character and many of them
print(email3)
