# Exercise 1
def calculate_bmi(height, weight) :
    print("Height = " + str(height))
    print ("Weight = " + str(weight))

    # Calculate BMI
    bmi = weight / (height * height)
    # Display BMI
    print("BMI = " + str(bmi))
    if bmi < 18.5:
        print("Under Weight")
    elif 18.5 <= bmi and bmi <= 25.0:
        print("Normal Weight")
    elif bmi > 25.0:
        print("Over Weight")



calculate_bmi(height= 1.73, weight = 57)