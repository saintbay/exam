import psycopg2
from psycopg2 import sql
import pandas as pd

class Product:
    def __init__(self, name, description, price, availability):
        self.name = name
        self.description = description
        self.price = price
        self.availability = availability

class Marketplace:
    def __init__(self, db_name, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cur = self.conn.cursor()

    def insert(self, name, description, price, availability):
        query = sql.SQL("INSERT INTO onlinerukodel (name, description, price, availability) VALUES (%s, %s, %s, %s)")
        self.cur.execute(query, (name, description, price, availability))
        self.conn.commit()

    def select(self, product_id):
        query = sql.SQL("SELECT * FROM onlinerukodel WHERE id = %s")
        self.cur.execute(query, (product_id,))
        return self.cur.fetchone()

    def update(self, product_id, name, description, price, availability):
        query = sql.SQL("UPDATE onlinerukodel SET name = %s, description = %s, price = %s, availability = %s WHERE id = %s")
        self.cur.execute(query, (name, description, price, availability, product_id))
        self.conn.commit()

    def delete(self, product_id):
        query = sql.SQL("DELETE FROM onlinerukodel WHERE id = %s")
        self.cur.execute(query, (product_id,))
        self.conn.commit()

    # def purchase(self, product_id, customer_balance, price_product):
    #     price_product = self.select(product_id)
    #     if customer_balance > price_product:
    #     # хотел сделать чек но не смог изза времени
    #     #     if product[3] <= customer_balance:
    #     #         self.update(product_id, product[1], product[2], product[3], product[4] - 1)
    #     #         print("Purchase successful!")
    #     #         invoice_data = {
    #     #             'Product Name': product[1],
    #     #             'Price': product[3]
    #     #         }
    #     #         invoice_df = pd.DataFrame([invoice_data])
    #     #         invoice_df.to_excel('invoice.xlsx', index=False)
    #     #     else:
    #     #         print("Insufficient balance! Choose something else.")
    #     # else:
    #     #     print("Product not found!")

if __name__ == "__main__":
    # user_type = input("Enter user type (admin/customer): ").lower()
    
    if user_type == "admin":
        marketplace = Marketplace(
            db_name='postgres',
            user='postgres',
            password='postgres',
            host='localhost',
            port='5432'
        )

        while True:
            print("Hello, this is DBMS system. What do you want to do?\n")
            choice = int(input("1.Insert\n2.Select\n3.Update\n4.Delete\n5.Exit\n"))

            if choice == 1:
                name = input("Enter name: ")
                description = input("Enter description: ")
                price = int(input("Enter price: "))
                availability = int(input("Enter availability: "))
                marketplace.insert(name, description, price, availability)
            elif choice == 2:
                product_id = int(input("Enter ID you want to select: "))
                result = marketplace.select(product_id)
                print(result)
            elif choice == 3:
                product_id = int(input("Enter ID you want to update: "))
                name = input("Enter name: ")
                description = input("Enter description: ")
                price = int(input("Enter price: "))
                availability = int(input("Enter availability: "))
                marketplace.update(product_id, name, description, price, availability)
            elif choice == 4:
                product_id = int(input("Enter ID you want to delete: "))
                marketplace.delete(product_id)
            elif choice == 5:
                break
        marketplace.cur.close()
        marketplace.conn.close()
        
#     elif user_type == "customer":
#         marketplace = Marketplace(
#             db_name='postgres',
#             user='postgres',
#             password='postgres',
#             host='localhost',
#             port='5432'
#     )

#         balance = float(input("Enter your balance: "))

#         while True:
#                 print("Hello, this is DBMS system. What do you want to do?\n")
#                 choice = int(input("1.Purchase\n2.Exit\n"))

#                 if choice == 1:
#                     product_id = int(input("Enter ID of the product you want to purchase: "))
                    
#                 elif choice == 2:
#                     break

#         marketplace.cur.close()
#         marketplace.conn.close()
        
# else:
#     print("Invalid user type!")
