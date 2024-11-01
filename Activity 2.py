Height=int(input("Enter Height"))
Weight=int(input("Enter Weight"))

BMI=Weight/(Height/100)

if BMI<=18.4:
    print("Eat more,you are underweight")
elif BMI<=24.9:
    print("You're good, keep it up")
elif BMI<=34.9:
    print("You are over weight, maintain a diet")
elif BMI<=39.9:
    print("Start working out your extremely over weight")
elif BMI<=40.0:
    print("you are Obese!, get help")
else:
    print("Call 911")
   