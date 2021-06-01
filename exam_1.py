#1.Password generate
import random
import string

#Set sambol
text = string.ascii_lowercase + string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#Start program
print('Exam_1 : Password Generator')

#Function convert list to string

def listtostring(list):
    new_num = ""
    for i in list:
        new_num += str(i)

#Get input data
def password_generate():
    total_length = int(input('\nEnter the minimum text length : '))
    special_char_length = int(input('\nEnter the minimum special charactor length : '))
    num_length = int(input('\nEnter the minimum number length : '))
    
    #calculate text length
    length_cha = total_length-special_char_length-num_length
    
    #Merge text
    all_text1 = (random.sample(text,length_cha)+random.sample(num,num_length)+random.sample(symbols,special_char_length))
    all_text2 = (random.sample(text,length_cha)+random.sample(num,num_length)+random.sample(symbols,special_char_length))
    all_text3 = (random.sample(text,length_cha)+random.sample(num,num_length)+random.sample(symbols,special_char_length))
    
    #convert vowels to numbers
    for index, i in enumerate(all_text1):
        if ( i == "a" or i =="e" or i =="i" or i =="o" or i =="u" or
            i =="A" or i =="E" or i =="I" or i =="O" or i =="U"):
            num_list = random.sample(num,1)
            new_num = ""
            for i in num_list:
                new_num += str(i)
            
            all_text1[index] = new_num
    
    #shuffle text
    random.shuffle(all_text1)
    
    #merge list  
    all_text1 = ''.join([str(elem) for elem in all_text1])
    password1 = ''.join(all_text1)

    ##################
    #convert vowels to numbers
    for index, i in enumerate(all_text2):
        if ( i == "a" or i =="e" or i =="i" or i =="o" or i =="u" or
            i =="A" or i =="E" or i =="I" or i =="O" or i =="U"):
            num_list = random.sample(num,1)
            new_num = ""
            for i in num_list:
                new_num += str(i)
            
            all_text2[index] = new_num
    
    #shuffle text
    random.shuffle(all_text2)
    
    #merge list  
    all_text2 = ''.join([str(elem) for elem in all_text2])
    password2 = ''.join(all_text2)
    
    #################
    #convert vowels to numbers
    for index, i in enumerate(all_text3):
        if ( i == "a" or i =="e" or i =="i" or i =="o" or i =="u" or
            i =="A" or i =="E" or i =="I" or i =="O" or i =="U"):
            num_list = random.sample(num,1)
            new_num = ""
            for i in num_list:
                new_num += str(i)
            
            all_text3[index] = new_num
    
    #shuffle text
    random.shuffle(all_text3)
    
    #merge list  
    all_text3 = ''.join([str(elem) for elem in all_text3])
    password3 = ''.join(all_text3)
    
    #Result
    print("You can choose password below.")
    print("First password : " + str(password1)) 
    print("Second password : " + str(password2))
    print("Third password : " + str(password3))

password_generate()
