individual_weight=input("Enter your weight in kg/lb: " )
weight_kgorlb=input("Select K or L:  ")

if weight_kgorlb == "L":
    final_weight= float(individual_weight)%0.454
elif  weight_kgorlb == "K":
    final_weight= individual_weight
else:
  print (f"{weight_kgorlb} is neither K or L, please select the right options")
  sys.exit()

def heightt(num=0):
  
  individual_height=input("Enter your height in Meters or Inches:  ")


  height_morinch=input("Select M or I:  ")
 

  if  height_morinch == "I":
    final_height= float(individual_height)/39.37
    return final_height

  elif height_morinch == "M":
    final_height= individual_height
    return final_height
     
  else:
    print (f"{individual_height} is neither M or I, please select the right options")
    num+=1
    if num < 3:
      heightt(num)
    else:
      print("You already tried 3 times exiting ")
      sys.exit()

final_height=heightt()
final_BMI= int(final_weight)/ (int(final_height)**2)


if final_BMI < 18.5:
  print("your BMI is : ",final_BMI, "and you are underweight!")
elif final_BMI > 18.5 and final_BMI < 25 :
  print("your BMI is : ",final_BMI, "and you are normal weight!")

elif final_BMI > 25 and final_BMI < 30 :
  print("your BMI is : ",final_BMI, "and you are overweight")

elif final_BMI > 30 and final_BMI < 35 :
  print("your BMI is : ",final_BMI, "and you are OBESE")

elif final_BMI > 35 :
  print("your BMI is : ",final_BMI, "and you are clinically obese")
