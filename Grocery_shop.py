
grocery = {}

def display_menu():
    print('Options:')
    print('1. Add product')
    print('2. Remove product')
    print('3. Search for product')
    print('4. Quit')

def add_product():
    product_name = input('Enter product name: ')
    price = float(input('Enter price: '))
    quantity = int(input('Enter quantity: '))
    grocery[product_name] = {'price': price, 'quantity': quantity}
    print(f'Added {product_name} to the grocery shop.')

def remove_product():
    product_name = input('Enter product name: ')
    if product_name in grocery:
        del grocery[product_name]
        print(f'Removed {product_name} from the grocery shop.')
    else:
        print(f'Sorry, {product_name} is not in the grocery shop.')

def search_product():
    product_name = input('Enter product name: ')
    if product_name in grocery:
        print(f'{product_name} costs ${grocery[product_name]["price"]:.2f} and there are {grocery[product_name]["quantity"]} in stock.')
    else:
        print(f'Sorry, {product_name} is not in the grocery shop.')

while True:
    display_menu()
    choice = input('Enter choice (1-4): ')
    if choice == '1':
        add_product()
    elif choice == '2':
        remove_product()
    elif choice == '3':
        search_product()
    elif choice == '4':
        break
    else:
        print('Invalid choice. Please try again.')
