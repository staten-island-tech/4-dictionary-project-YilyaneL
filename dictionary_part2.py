def itemlist():
        items = [
            {
            "id": 6650,
            "name": "AMD RX 6650 XT",
            "price": 249.99,
            "description": "CUTTING EDGE NEW GPU TECHNOLOGIES AND AMD BEST",
            },
            {
            "id": 5090,
            "name": "Nvidia 5090",
            "price": 3699.99,
            "description": "best of best gpu with ai upscaling and frame gen"
            },
            {
            "id": 64,
            "name": "64gb ram",
            "price": 799.99,
            "description": "ram prices really gone up nowadays"
            },
        ]
        for index, item in enumerate(items):
            print(index, ":", item["name"])
        done = False
        cart = []
        while done == False:
            purchase = int(input("which product do you want to buy (number): "))
            cart.append(items[purchase]["name"])
            ask = input("are you done (yes/no)? ")
            if ask == "yes":
                done = True
                print("this is what you purchased: ")
                for i in cart:
                     print(i,)
            elif ask == "no":
                done = False
            else:
                print("invalid input kid")
itemlist()