# TESTPASS PASSWORd01

import re
entrada = ()
intentos = 1
special = ['@','#','$','&']
while True:
 entrada=(input("Introduce un password: "))
 if (len(entrada)<=6):
       print("No")
 elif (len(entrada)>=20):
       print("No")
 elif re.search('[0-9]',entrada) is None:
      print("No")
 elif re.search('[A-Z]',entrada) is None :
         print("No")
 elif re.search('[a-z]',entrada) is None :
         print("No")
 elif re.search('special', entrada)is None :
         print("No")
 else:
         print("Yes")
         break




