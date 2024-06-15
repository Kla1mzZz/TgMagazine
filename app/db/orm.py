from .database import engine, Base, session_factory
from .models import Brands, Items, Order, Users, VereficationOrder


class Orm:
    @staticmethod
    def create_tables():
        Base.metadata.create_all(engine)

    def add_user(self, id):
        with session_factory() as session:
            users = Users(user_id=id)

            session.add(users)
            session.commit()

    def add_brand(self, brand):
        with session_factory() as session:
            brands = Brands(brandName=brand)

            session.add(brands)
            session.commit()

    def get_brands(self):
        with session_factory() as session:
            brands = session.query(Brands).all()

            return [brand.brandName for brand in brands]

    def delete_brand(self, brandName):
        with session_factory() as session:
            brand = session.query(Brands).filter(Brands.brandName == brandName).first()

            if brand:
                session.delete(brand)
                session.commit()
            else:
                return False

    def add_item(self, item, brand, modelName, size, photo, price):
        with session_factory() as session:
            item = Items(item=item.lower(),brand=brand.lower(),modelName=modelName,size=size,photo=photo,price=price)

            session.add(item)
            session.commit()
    
    def get_items_for_brand_and_item(self, brandName, item):
        with session_factory() as session:
            items = session.query(Items).filter(
                Items.brand == brandName.lower(),
                Items.item == item.lower()
            ).all()

            if items:
                return items
            else:
                return None
    
    def get_id(self, item, brandName, modelName):
        with session_factory() as session:
            item = session.query(Items).filter(
                Items.item == item.lower(),
                Items.brand == brandName.lower(),
                Items.modelName == modelName
            ).first()

        if item:
            return item.id
        else:
            return None
    
    def get_item_for_id(self, id):
        with session_factory() as session:
            item = session.query(Items).filter(
                Items.id == id
            ).first()

            if item:
                return item
            else: 
                return None
    
    def add_order(self, item, brand, modelName, size, price, photo, fullName, phoneNumber,address,username):
        with session_factory() as session:
            order = Order(item=item,brand=brand,modelName=modelName,
                          size=size,price=price,photo=photo,fullName=fullName,phoneNumber=phoneNumber,address=address,username=username)
            
            session.add(order)
            session.commit()
    
    def get_orders(self, username):
        with session_factory() as session:
            order = session.query(Order).filter(
                Order.username == username
            ).all()

            return order
    
    def add_verefication_order(self, item, brand, modelName, size, price, photo, address, fullName, phoneNumber, payment,user_id, username):
        with session_factory() as session:
            order = VereficationOrder(item=item,brand=brand,modelName=modelName,
                          size=size,price=price,photo=photo,fullName=fullName,address=address,
                          phoneNumber=phoneNumber,payment=payment,user_id=user_id, username=username)
            
            session.add(order)
            session.commit()
    
    def get_verefication_order(self, user_id):
        with session_factory() as session:
            order = session.query(VereficationOrder).filter(VereficationOrder.user_id == user_id).first()

            if order:
                return order
            else:
                return None
    
    def delete_verefication_order(self, user_id):
        with session_factory() as session:
            order = session.query(VereficationOrder).filter(VereficationOrder.user_id == user_id).first()

            session.delete(order)
            session.commit()


orm = Orm()