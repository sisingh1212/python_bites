def int_check():
  while True:

    try:
      ans = input( "Enter interger: ")
      answer=int(ans)
      if answer == 4:
        return answer
      else:
        return 8

    except ValueError as e:
      print(f"{ans} is Not an Interger")


number_final=int_check()
print(number_final)
