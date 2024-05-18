import re
def chuanhoacau(sentence):
   
    cau = sentence.capitalize()

   
    cau = ' '.join(cau.split())

  
    if cau[-1] not in ['.','!','?']:
        cau+='.'
    
    if cau[-1]=='!' or cau[-1]=='?':
        cau=cau[:-2]+cau[-1]
    return cau


s = []

while True: 
    try : s.append(input())
    except EOFError : break
for i in s:
    print(chuanhoacau(i))