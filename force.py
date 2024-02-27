print("Newtons's second law of motion!")
print("-------------------------------------------")
print("""INSTRUCTION (select 1,2,3 from below for your result!!)
      1. Mass (m)
      3. Acceleration (a)
      3. Force (f)""")
missing_value_choice=input("Enter the option for the missing value: ")
if missing_value_choice=="1":
    a = float(input("Enter acceleration (a):"))
    f = float(input("Enter Force (f):" ))
    m = f / a
    print (f"Mass(m)={m}")
elif missing_value_choice=="2":
    f = float(input("Enter Force(f):"))
    m = float(input("Enter mass(m):"))
    a = f / m 
    print (f"Acceleration(a) = {a}")
elif missing_value_choice=="3":
    a = float(input("Enter Acceleration(a):"))
    m = float(input("Enter mass(m ):"))
    f = m*a
    print(f"Force (f)={f}")
else:
    print ("Invalid option enter!!!COMMAND NOT RECOGNIZED!!")