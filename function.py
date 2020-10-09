def get_table_width(title,data):
    longest = len(title)
    additional_spacing = 2
    for item in data:
        if len(item) > longest:
            longest = len(item)
    return longest + additional_spacing

def print_table_body(contents):
    for item in contents:
        print(f" | {item}")

def print_divider(length):
    print(f'+ {"=" * length}+')

def print_table_header(title,width):
    print_divider(width)
    print(f' | {title.upper()}')
    print_divider(width)

def print_table_footer(width):
    print_divider(width)

def print_table(title, contents):
    width = get_table_width(title, contents)
    print_table_header(title,width)
    print_table_body(contents)
    print_table_footer(width)



class Order():
    def __init__(self,owner):
        self.owner = owner
        self.orders = {}

    def add_to_order(self,name, drink):
        if drink:
            self.name= name
            self.drink = drink
            self.orders[name]= drink

    def print_order(self):
        items =[]
        for name, drink in self.orders.items():
            items.append(f'{name}: {drink} ')
        print_table(f"\nIt is {self.owner}'s round...\n|", items)
        for names in items:
            print(names)
        print('.................................................................\n')
        print('Thank you, your round has been saved\n')

    def save_rounds_to_file(self):
        global favourite_drinks_file
        favourite_drinks_file = open('./favourites.txt', 'w')
        for x, y in self.orders.items():
            favourite_drinks_file.write(f'{x} - {y}' + '\n' )
        favourite_drinks_file.close()

