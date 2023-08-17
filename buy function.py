

with open ("inventory_list.txt","r") as f:
    all_products = f.readlines()
    #print(*all_products, sep="\n")

def buy(all_products):
    inp = int(input("Which brand are you looking for?:\n1. Adidas\n2. Nike "))
    if inp == 1:
        inp2 = int(input("Which section are you interested in?:\n1. Male\n2. Female"))
        if inp2 == 1:
            inp3 = int(input("How many Adidas male t-shirts do you wanna buy?:"))
            print("Added to your cart. Your total is: HKD ", inp3 * 300)
        else:
            inp3 = int(input("How many Adidas female t-shirts do you wanna buy?:"))
            print("Added to your cart. Your total is: HKD ", inp3 * 350)
    elif inp == 2:
        inp2 = int(input("Which section are you interested in?:\n1. Male\n2. Female"))
        if inp2 == 1:
            inp3 = int(input("How many Nike male t-shirts do you wanna buy?:"))
            print("Added to your cart. Your total is: HKD ", inp3 * 350)
        else:
            inp3 = int(input("How many Nike female t-shirts do you wanna buy?:"))
            print("Added to your cart. Your total is: HKD ", inp3 * 250)

buy(all_products)