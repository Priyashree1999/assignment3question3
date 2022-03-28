def counting_letters(a):
    upper_case=0 
    lower_case=0
    for i in a:
        if i.isupper():
            upper_case+=1
        elif i.islower():
            lower_case+=1
    print("No of upper case characters:",upper_case)  
    print("No of lower case characters :",lower_case)
    return   

string ='The quick Brow Fox '
counting_letters(string)

