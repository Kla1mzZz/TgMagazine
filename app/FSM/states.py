from aiogram.fsm.state import StatesGroup, State

class BrandForm(StatesGroup):
    brandName = State()

class DeleteBrandForm(StatesGroup):
    brandName = State()

class AddNewItemForm(StatesGroup):
    item = State()
    brand = State()
    modelName = State()
    size = State()
    photo = State()
    price = State()
    like = State()

class AddOrderForm(StatesGroup):
    fullName = State()
    phoneNumber = State()
    address = State()