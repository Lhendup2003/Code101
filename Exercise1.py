print("""HELLO!!! WELCOME TO THE CSTERIAN CINEMA HALL !!!
                        0 REGISTRATION  0
      ----->  Please enter the deteils below!!!! """)
name_ =str(input("Can you enter your name??"))
print ("Okay NIce to meet you",name_)
std_ = int(input("""Are You a Student ??
                # If Yes Enter--> (1)
                # If No Enter-->  (2)
                 ------->>>"""))
a= name_
if std_==1:
    print("proceed with the deteils!!")
    age_= int(input("How old are you??"))
    b=age_
    if age_ <=12 :
        print("""Registration succesfull!!
              --> You are a student age below (12) so,therefore
              we offer you a discount of 50%
              (Below is your Ticket!!) """)
        print(f"""-----------------------------------------------
                 |----------CSTerian CINEMA HALL-------(50%) |
                 |       Name:Mr./Mrs {a}                      |
                 |       Age:{b}                               |
                 |       STUDENT DISCOUNT OFFER!!              |
                 -----------------------------------------------""")
    elif age_>13<18:
      print("""Registration succesfull!!
              --> You are a student age below (18) so,therefore
              we offer you a discount of 30%
              (Below is your Ticket!!) """)
      print(f"""-----------------------------------------------
                 |----------CSTerian CINEMA HALL-------(30%)   |
                 |       Name:Mr./Mrs {a}                    |
                 |       Age: {b}                               |
                 |  STUDENT DISCOUNT OFFER!!                   |
                 -----------------------------------------------""")
    else:
        print("""Registration succesfull!!
              --> You are a student age above (19) so,therefore
              we offer you a discount of 10%
              (Below is your Ticket!!) """)
        print(f"""-----------------------------------------------
                 |----------CSTerian CINEMA HALL-------(10%)   |
                 |       Name:Mr./Mrs  {a}                     |
                 |       Age: {b}                              |
                 |  STUDENT DISCOUNT OFFER!!                   |
                 -----------------------------------------------""")
else:
    print(f"""|-----------------------------------|
              |    Mr./Mrs:-   {a}                |
              |         ACCESS DENIED!!           |
              |    PLEASE TAKE ANOTHER SITE       |
              |THIS IS ESPECIALLY FOR STUDENTS!!! |
              -------------------------------------""")
   
 

