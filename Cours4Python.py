# COURS 4 : Les chaines de caractères en python
import os
def remove_content(directory):
          for dirpath , dirnames , filenames in os.walk(directory, topdown =True):
                    for file in filenames:
                              file_path = os.path.join(directory , file)
                              os.remove(file_path) 
                    for dirname in dirnames :
                              dirname_path = os.path.join(directory , dirname)
                              os.remove(dirname_path)

def cesar_cipher (message , cle=3):
          cipher = ""
          for element in message:
                    if(element.islower()):
                              cipher +=chr((ord(element)-97 +cle)%26 + 97)
                    elif( element.isupper()):
                              cipher += chr((ord(element)-65 +cle)%26 + 65)
                    else:
                              cipher += element
          return cipher     
                   
          	
		
