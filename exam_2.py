
prod = {
  "products" : [
    {"name": "widget", "price": 25.00, "quantity": 5 },
    {"name": "thing", "price": 15.00, "quantity": 5 },
    {"name": "doodad", "price": 5.00, "quantity": 10 }
  ]
}

def update(name):
    if input("Product name : " +str(name) + " is out stock.If you want update your product stock information>Press Yes : ").lower() == "yes":
        #Input data from user
        prod_name = input("Please input your new product name : ").lower()
        prod_price = input("Please input your new product price : ").lower()
        prod_quan = input("Please input your new product quantity : ").lower()
        
        #Merge text
        product_dict = "name " + str(prod_name) +"\n\
price "+ str(prod_price) +"\n\
quantity "+ str(prod_quan)  
    
        #convert str to dict format
        product_new_add = dict(x.split() for x in product_dict.splitlines())
        
        #Update
        prod['products'].append(product_new_add)
        print("Thank you for your new information \n\
You can search any product.")
    else:
        print("Thank you.Please try again.")
    
def search():
    #print("Welcome.Press start for start program or exit for exit program")
    input_text = input("Welcome.Press start for start program or exit for exit program : ").lower()
    while True:
        printed = True
        print("Welcome to exam2.")
        input_text = input("Please input your product : ").lower()
        if input_text.lower() == 'exit':
            print("Thany for using programe.See you again")
            pass
        else:
            check_f = []
            if input_text != "":
                for i in prod['products']:
                    check = input_text in i.values()
                    check_f.append(check)
                    if check:
                        print("Name : " +str(i['name']) + "\n\
price : " +str(i['price']) + "\n\
Quantity on hand : " +str(i['quantity']))
                        pass
                    elif check == False and not printed:
                        update(input_text)
                        printed = False
                if not any(check_f) == True:
                    update(input_text)
            elif input_text.lower() != "exit":
                break
            else:
                print("Product can't empty.Please add your product name.")
search()