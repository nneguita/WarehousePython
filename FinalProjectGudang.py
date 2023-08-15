from tabulate import tabulate #For stocks, so it shows in a good table

#Static value dictionary for the running code
dict_warehouse = {
    1 : {
        'name' : 'GTX1660S',
        'manufacturer' : 'NVIDIA',
        'stock' : 100,
        'price' : 3000000,
        'section' : 'N',
        'division' : '16S'
    },
    2 : {
        'name' : 'RX6600',
        'manufacturer' : 'AMD',
        'stock' : 100,
        'price' : 4000000,
        'section' : 'A',
        'division' : '66'
    },
    3 : {
        'name' : 'RTX3090',
        'manufacturer' : 'NVIDIA',
        'stock' : 100,
        'price' : 6000000,
        'section' : 'N',
        'division' : '39'
    },
    4 : {
        'name' : 'RTX4090',
        'manufacturer' : 'NVIDIA',
        'stock' : 100,
        'price' : 12000000,
        'section' : 'N',
        'division' : '49'
    },
}

# Showing Menu and taking inputs
def menu():
    global lemenu
    while True:
        lemenu = input('''
            Purwa's Graphic Card Warehouse

            Menu :
            1. Warehouse List
            2. Add Product
            3. Modify Product
            4. Delete Product
            5. Cashier Mode
            6. Exit

            Choose Menu : \n\t''')
        try:
            lemenu = int(lemenu)
            break
        except ValueError:
             print("Not within the given choices, Try Again!")
    return lemenu

# Defining table's row for tabulate
heads = ['SID','Name', 'Manufacturer', 'Stock', 'Price', 'Section', 'Division']

# Showing Stocks Function
def show(self):
        # name is a variable to call in the key of the dictionary
        # inner is a variable to call in the key within the nested dictionary
        # the * before inner.values means all positional arguments, in this case, the nested key are captured and
        #   stored within the inner variable, after that, the function inner.values already knows every position
        #   of the key, thus, the values are printed out as a tuple without annotation from the system and readable
        #   for the tabulate

        # alternative of the below code are
        # levalu = []
        # for name, inner in dict_warehouse.items():
        #     levalu.append([name, *inner.values()])
        # print(tabulate(levalu, headers=heads, tablefmt='outline'))
        global values

        values = [[name, *inner.values()] for name, inner in self.items()] 
        print("\n\t\tLe Stocks\n")
        print(tabulate(values, headers=heads, tablefmt='outline'))
# show(dict_warehouse)

def side():
    global stock_SID
    for stock_SID in dict_warehouse.keys():
        stock_SID += 1
    return stock_SID

def manufacturern():
     global stock_manufacturerc
     global stock_manufacturer
     while True:
        stock_manufacturerc = input("Choose Product Manufacturer:\n1. NVIDIA\n2. AMD\n")
        try:
            stock_manufacturerc = int(stock_manufacturerc)
        except ValueError:
            print("Not within the given choices, Try Again!")
        if stock_manufacturerc == 1:
            stock_manufacturer = 'NVIDIA'
            break
        elif stock_manufacturerc == 2:
            stock_manufacturer = 'AMD'
            break
        elif stock_manufacturerc > 3 or stock_manufacturerc <=0:
            print('Not within the given choices, Try Again')
        return stock_manufacturer

def stocka():
    global stock_amount
    while True:
        stock_amount = input('Stock Amount: ')
        try:
            stock_amount = int(stock_amount)
            break
        except:
            print("Not a number! Please input with numbers")
    return stock_amount

def p_tag():
    global price_tag
    while True:
        price_tag = input('Price Tag: ')
        try:
            price_tag = int(price_tag)
            break
        except:
            print("Not a number! Please input with numbers")
    return price_tag

def add():
        side()
        stock_name = input('Product Name: ')
        manufacturern()
        stocka()
        p_tag()
        section = stock_manufacturer[0]
        if stock_manufacturer == 'AMD':
            division = stock_name[2:4]
        elif stock_manufacturer == 'NVIDIA':
            if stock_name[-1].isalpha():
                if stock_name[-2].isalpha():
                    division = stock_name[3:6:2] + stock_name[-2:]
                elif stock_name[-2].isdigit():
                    division = stock_name[3:6:2] + stock_name[-1]
            elif stock_name[-1].isdigit():
                division = stock_name[3:6:2]
        stocklist = (stock_name,stock_manufacturer,stock_amount,price_tag,section,division)
        new_head = ['name', 'manufacturer', 'stock', 'price', 'section', 'division']
        stockdict = {}
        stockdict = dict(zip(new_head,stocklist))
   
        for i in (stock_SID,stock_SID):
            dict_warehouse[i] = stockdict

        print("\n\t\tUpdated Data of")
        show(dict_warehouse)

def delete():
    warningcont = input("Warning! This function deletes the object permanently\nDo you really want to continue?\n")
    if warningcont.lower() == 'y' or warningcont.lower() == 'yes':
        AdminPass = input('Please input administrator password!\n')
        try: 
            AdminPass = int(AdminPass)
        except ValueError:
            print("Incorrect, Throwing you back into main menu!")
        if AdminPass == 123:
            show(dict_warehouse)
            # values = []
            stockdelID = int(input('ID to be deleted : \n\t'))
            del dict_warehouse[stockdelID]
        else:
            print("Incorrect, Throwing you back into main menu!")
    elif warningcont.lower() == 'n' or warningcont.lower() == 'no':
        print("Throwing you back into the main menu")
    else:
        print("You are not serious!\nThrowing you back into the main menu")
    show(dict_warehouse)

def modifypush():
    stockmodcol = input('Which Column do you want to modify?\n\t')
    place = stockmodcol.lower()
    if place == 'name':
        modname = input('New Name: \n')
        dict_warehouse[stockmodID][place] = modname
        if dict_warehouse[stockmodID]['manufacturer'] == 'AMD':
            dict_warehouse[stockmodID]['division'] = modname[2:4]
        elif dict_warehouse[stockmodID]['manufacturer'] == 'NVIDIA':
            if modname[-1].isalpha():
                if modname[-2].isalpha():
                    dict_warehouse[stockmodID]['division'] = modname[3:6:2] + modname[-2:]
                elif modname[-2].isdigit():
                    dict_warehouse[stockmodID]['division'] = modname[3:6:2] + modname[-1]
            elif modname[-1].isdigit():
                dict_warehouse[stockmodID]['division'] = modname[3:6:2]
    elif place == 'stock':
        modstock = input('Updated Stock: \n')
        dict_warehouse[stockmodID][place] = modstock
    elif place == 'price':
        modprice = input('New Price: \n')
        dict_warehouse[stockmodID][place] = modprice
    else:
        print("That's not modifiable!")

def modify():
    show(dict_warehouse)
    global stockmodID
    stockmodID = int(input('ID to be modified : \n\t'))
    levalu = []
    for name, inner in dict_warehouse.items():
        if name == stockmodID:
            levalu.append([name, *inner.values()])
    print(tabulate(levalu, headers=heads, tablefmt='outline'))  
    modifypush()
    show(dict_warehouse)

cart = []
cashierHead = ['SID','Name', 'Quantity', 'Price/Qty', 'Total Price']

def cashier():
    global v_cash
    v_cash = False
    while not v_cash:
        v_cash = True
        show(dict_warehouse)
        while True :
            buyIndex = int(input('SID : '))
            boughtQty = int(input('Input quantity : '))
            if(boughtQty > dict_warehouse[buyIndex]['stock']) :
                print(f"Stock Quantity is not enough!\n{dict_warehouse[buyIndex]['name']} has {dict_warehouse[buyIndex]['stock']} left")
            else :
                cart.append([buyIndex, dict_warehouse[buyIndex]['name'], boughtQty, dict_warehouse[buyIndex]['price'],boughtQty*dict_warehouse[buyIndex]['price']])
            print(tabulate(cart, headers=cashierHead, tablefmt='outline'))
            checker = input('Continue adding? (y/n) = ')
            if(checker.lower() == 'n' or checker.lower() == 'no' or checker.lower() == 'nein') :
                break
            else:
                print("Yes is assumed, continuing the addition")
        print('Shopping List :')
        print(tabulate(cart, headers=cashierHead, tablefmt='outline'))
        totalHarga = 0
        for item in cart :  
            totalHarga += item[4] 
        while True :
            print(f'Amount to be paid = {totalHarga}')
            jmlUang = int(input('Payment amount : \n'))
            if(jmlUang > totalHarga) :
                change = jmlUang - totalHarga
                print(f'Thank You for shopping with us! \n\nYour Change : {change}')
                for item in cart :
                    dict_warehouse[item[0]]['stock'] -= item[2]
                cart.clear()
                break
            elif(jmlUang == totalHarga) :
                print('Thank You for shopping with us!')
                for item in cart :
                    dict_warehouse[item[0]]['stock'] -= item[2]
                cart.clear()
                break
            else :
                kekurangan = totalHarga - jmlUang
                print(f'Invalid amount! You are short by: {kekurangan}')
    cont = input('Do you wish to continue cashier mode?\n')
    if(cont.lower() == 'y' or cont.lower() == 'yes'):
        v_cash = False
    elif(cont.lower() == 'n' or cont.lower() == 'no' or cont.lower() == 'nein'):
        print('Throwing you back into the main menu')
    else:
        print("No is assumed, throwing you back into the main menu!")

#The Running Program below
valid = False

while not valid:
    valid = True
    menu()
    if lemenu == 1:
        show(dict_warehouse)
    elif lemenu == 2:
        add()
    elif lemenu == 3:
        modify()
    elif lemenu == 4:
        delete()
    elif lemenu == 5:
        cashier()
    elif lemenu == 6:
        print("Goodbye, See you tomorrow!")
        break
    else:
        print("Not within the given choices, Try Again!")
    valid = False
