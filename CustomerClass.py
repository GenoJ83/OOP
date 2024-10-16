class Customer:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def __str__(self):
        return f'Customer Information: \nName: {self.name}\nAddress: {self.address}'


if __name__ == '__main__':
    customer1 = Customer('Geno Joshua', 'Kampala')
    print(customer1)
