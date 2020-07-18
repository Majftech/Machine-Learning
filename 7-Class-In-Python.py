class Shirt:
    def __init__(self, color, size, style, price):
        self.color = color
        self.size = size
        self.style = style
        self.price = price

    def change_price(self, price):
        self.price = price
    def discount(self, discount):
        return self.price * (1-discount)

new_shirt = Shirt('red', 'M', 'collored', '100')
print(new_shirt.color)
print(new_shirt.size)
print(new_shirt.style)
print(new_shirt.price)

new_shirt.change_price(110)
print(new_shirt.price)
