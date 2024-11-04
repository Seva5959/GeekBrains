import json
import os
import csv
class Product:
    data = {}
    def __init__(self,name,category,price,stock):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.all_items(self.name,self.category,self.price,self.stock)
    @staticmethod
    def all_items(prod_name,category,price,stock):
        Product.data[prod_name] = [category,price,stock]
        return Product.data

    def __str__(self):
        return f'СТР метод. Товар: {self.name} стоит: {self.price} На складе: {self.stock} штук.'

    def __eq__(self,other):
        return self.name == other.name and self.category == other.category

    def __repr__(self):
        return f'RePR метод. Товар: {self.name} стоит: {self.price}'

    def update_stock(self,quantity,action):
        if action == "+":
            return f'Теперь на складе: {self.stock + quantity} вещей.'
        return f'Теперь на складе: {self.stock - quantity} вещей.'

tishort = Product('Tishort Superma','footbolka',700,21459)
palto = Product('Balansiaga Palto','palto',4500,2)
sapogi = Product('Nike 228','obuBi',3500,400)
o4ki = Product('black_o4ko','o4ki',478,590)

class Customer:
    def __init__(self,name,email,orders):
        self.name = name
        self.email = email
        self.orders = orders  #список заказов, сделанных покупателем

    def __str__(self):
        return f' Клиент: {self.name} Почта: {self.email} Список заказов: {self.orders}'

oleg = Customer('Oleg','lolkek@gmail.cum',[tishort,palto])
matbek = Customer('Matbek','olyh3000@gmail.ry',[o4ki,sapogi,palto])
ivan = Customer('Ivan','IvanIvanov2015@mail.com',[palto,sapogi])


class Order:
    def __init__(self,customer):
        self.customer = customer
        self.products = [prod for prod in self.customer.orders]
        self.products_name = [prod.name for prod in self.customer.orders]
        self.total_price = 0
        self.add_products()
    def add_products(self):
        for i in self.products:
            self.total_price += i.price
        return self.total_price

    def info(self):
        return [self.customer.name, self.products_name, self.total_price]

    def __lt__(self, other):
        return self.total_price < other.total_price

    def __gt__(self, other):
        return self.total_price > other.total_price

    def __eq__(self, other):
        return self.total_price == other.total_price


order_1 = Order(oleg)
order_2 = Order(ivan)
order_3 = Order(matbek)

class Store:
    def __init__(self,order,products = None,customers= None,file_name_orders = "info_about_orders.csv"):
        self.products = products
        self.customers = customers
        self.order = order.info()
        self.file_name_orders = file_name_orders

    @staticmethod
    def find_file(file_name):
        current_directory = os.getcwd()
        for file in os.listdir(current_directory):
            if os.path.isfile(file) and file == file_name:
                return True
        return False

    @staticmethod
    def find_product_by_name(name, file_name='warehouse.json'):
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return name in data

    def create_to_json(self,file_name="warehouse.json"):
        if self.find_file(file_name):
            with open(file_name,'r',encoding='utf-8') as f:
                infa = json.load(f)
                infa.update(Product.data)
            with open(file_name,'w',encoding='utf-8')as f:
                json.dump(infa,f,ensure_ascii=False,indent=4)
        else:
            with open(file_name,'w',encoding='utf-8')as f:
                json.dump(Product.data,f,ensure_ascii=False,indent=4)

    def load_products_from_csv(self,file_path):
        with open(file_path,'r', encoding='utf-8')as file:
            data = csv.reader(file)
            for i in data:
                return i

    def save_orders_to_csv(self):
        if not self.find_file(self.file_name_orders):
            self.headers_to_csv(self.file_name_orders)
        with open(self.file_name_orders,'a',newline='', encoding='utf-8')as f:
            if len(self.order[1]) > 1:  # Проверяю, что покупатель купил больше одной вещи
                self.order[1] = ', '.join(i for i in self.order[1]) # Это чисто для красоты. Обычное форматирование
            else:
                self.order[1] = ''.join(self.order[1])
            csv_write = csv.writer(f)
            csv_write.writerow(self.order)
    def headers_to_csv(self,file_name_orders):
        headers_to_orders = ['customer_name', 'products_name', 'total_price']
        with open(file_name_orders,'w',newline='',encoding='utf-8')as f:
                csv_write = csv.writer(f)
                csv_write.writerow(headers_to_orders)



mtc = Store(order_3)
#mtc.headers_to_csv("info_about_orders.csv")
#mtc.save_orders_to_csv()
mtc.create_to_json()
mtc.create_to_json()

