from handlers import*

if __name__ == '__main__':
    while True:
        customer_input = input('>>>')\
            .strip()\
            .lower();
        if customer_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif customer_input == 'hello':
            print("How can I help you?")
        elif customer_input[0:3] == 'add':
            add_handling(customer_input[3::])
            if add_handling(customer_input[3::]) != False:
                print("Contact added")
            else:
                print("Incorrect input, please write name and phone number")
        elif customer_input[0:6] == 'change':
            change_handling(customer_input[6::])
            if change_handling(customer_input[6::]) != False:
                print("Contact changed")
            else:
                print("Incorrect input, please write name and phone number")
        elif customer_input[0:5] == 'phone':
            phone = phone_handling(customer_input[5::])
            if phone != False:
                print(f'The phone is {phone}')
            else:
                print("Incorrect input, please write name")
        elif customer_input == 'show all':
            for i in dict_contacts:
                print(i.title(), dict_contacts[i])

