def calculate(weight,height):
    if height<=0:
        return "Error:Height cannot be zero or negative"
    bmi= weight/(height**2)
    return round(bmi,2)

def interpret_bmi(bmi_value):
    if isinstance(bmi_value,str):
        return  bmi_value
    elif bmi_value<18.5:
        return "underweight"
    elif 18.5<= bmi_value < 25:
        return "Normal weight"
    elif 25 <= bmi_value < 30:
        return "Overweight"
    else:
        return "obese"
    
try:
    weight=float(input ("Enter your weight(kg):"))
    height=float(input ("Enter your height(m):"))

    result= calculate(weight,height)
    bmi_interpretation= interpret_bmi(result)

    if isinstance(result,str):
        print(result)
    else:
        print("your BMI is:",result)
        print("Health level:",bmi_interpretation)

except ValueError:
    print("Invalid input")




