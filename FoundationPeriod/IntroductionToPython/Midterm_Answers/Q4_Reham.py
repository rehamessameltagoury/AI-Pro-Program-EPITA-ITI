def multiplication_or_sum(num1,num2):
    multi =num1*num2 # calculate their multiplication
    if multi>500:
        return num1+num2
    else:
        return multi
    

print(multiplication_or_sum(20, 30))
