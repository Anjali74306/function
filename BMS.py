# Q7.Write function bmi that calculates body mass index (bmi = weight / height2).

# if bmi <= 18.5 return "Underweight"

# if bmi <= 25.0 return "Normal"

# if bmi <= 30.0 return "Overweight"

# if bmi > 30 return "Obese"

height=float(input("enter height "))
weight=float(input("enter weight"))
def bmi(height,weight):
  bmi=weight/height**2
  if bmi<=18.5:
    print("underweight")
    if bmi<=25.0:
      print("normal")
      if bmi<=30.0:
        print("overweight")
      else:
        print("obese")
  print("your body mass index ia:",weight/height**2)
bmi(6,65)

# def fun(n):
#   if n==0:
#     print (n)
#     return
#   elif n==1:
#     print (n)
#     return
#   else:
#     print(fun(n-1)+fun-2)
#     return
# fun(5)

# def fun(num,result):
#   if num==0:
#     return result
#   result=str(num%2)+result
#   return fun(num//2,result)
# n=int(input("enter ur number u want to convert to binary: "))
# print(fun(n," "))



