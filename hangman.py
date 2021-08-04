import random
#take a random word from the text File
with open("secret.txt", 'r') as magic_words:
  read_file=magic_words.readlines()
#secret_word="championc"
secret_word=random.choice(read_file).rstrip()

entered_char=[]
found_string=[]
sec_list=list(secret_word)
n=0
updated_list=["_  "for i in sec_list]
print("_ "*len(secret_word))
while True:
  myinput=input("Enter your choice: ")
  if myinput in entered_char:
    print(f"{myinput} This has already been used")
  else: 
    entered_char.append(myinput)
    if myinput in secret_word:
      print(f"{myinput}")
      indexes=[ i for i,value in enumerate(sec_list) if value == myinput]
      for i in indexes:
        updated_list[i]=myinput
      print(" ".join(updated_list))
      if updated_list == sec_list:
        break
      
    else:
      if n < 7:
        print(f"myinput not in secret_word")
        if n == 0:
          print("""
          |
          |
          |
          |
          """)
          print(" ".join(updated_list))
        elif n == 1:
                    print("""
          |
          |
          |
          |
          |
          |
          |
          """)
        elif n == 2:
          print("""
          -----------
          |
          |
          |
          |
          |
          |
          |
          """)
          print(" ".join(updated_list))
        elif n == 3:
          print("""
          ------------
          |/
          |
          |
          |
          |
          |
          |
          """)
          print(" ".join(updated_list))
        elif n == 4:
          print("""
          ------------
          |/          |
          |           |
          |
          |
          |
          |
          |
          """)
          print(" ".join(updated_list))
        elif n == 5:
          print("""
          ------------
          |/          |
          |           |
          |           0
          |
          |
          |
          |
          """)
          print(" ".join(updated_list))


        elif n == 6:
          print("""
           ------------
          |/          |
          |           |
          |           0
          |           | 
          |
          |
          |           
          """)
          print(" ".join(updated_list))
        n=n+1
        print(n)
      else:
        print("""
           ------------
          |/          |
          |           |
          |           0
          |           /\ 
          |            |
          |            /\
          |           
          """)
        print("u r hanged!")
        break

    


