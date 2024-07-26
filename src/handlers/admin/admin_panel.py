from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from ...FSM.states import BrandForm, DeleteBrandForm, AddNewItemForm
from ...db.orm import Orm

from ...settings.settings import Settings
from app.keyboards.admin_kb import admin_kb

router = Router()

settings = Settings()

orm = Orm()



@router.message(F.text == 'Админ-панель')
async def admin_panel(message: Message):
    await message.answer('Админ-панель',reply_markup=admin_kb.webapp_builder())

@router.message(F.text == 'Добавить новый бренд')
async def addNewBrand(message: Message, state: FSMContext):
    if message.from_user.id in settings.getAdminIds():
        await state.set_state(BrandForm.brandName)

        await message.answer('Введите название бренда:')

@router.message(BrandForm.brandName)
async def brandNameForm(message: Message, state: FSMContext):
    await state.update_data(brandName=message.text)

    orm.add_brand(message.text)

    await message.answer(f'Бренд {message.text} добавлен')

    await state.clear()


@router.message(F.text == 'Удалить бренд')
async def deleteBrand(message: Message, state: FSMContext):
    if message.from_user.id in settings.getAdminIds():
        await state.set_state(DeleteBrandForm.brandName)

        allBrands = orm.get_brands()

        brands = ''


        for brand in allBrands:
            brands += f'{brand}\n'

        await message.answer(f'Все бренды:\n\n{brands}')
        await message.answer('Введите название бренда которого удалить:')

@router.message(DeleteBrandForm.brandName)
async def deleteBrandName(message: Message, state: FSMContext):
    await state.update_data(brandName=message.text)

    brands = orm.get_brands()

    if message.text in brands:
        await message.answer(f'Бренд {message.text} удален')
        orm.delete_brand(message.text)
    else:
        await message.answer(f'Такого бренда нету в списке', reply_markup=admin_kb.adminPanel)

    await state.clear()


@router.message(F.text == 'Все Бренды')
async def getAllBrands(message: Message):
    allBrands = orm.get_brands()

    brands = ''


    for brand in allBrands:
        brands += f'{brand}\n'

    
    await message.answer(f'Все бренды:\n\n{brands}')


@router.message(F.text == 'Добавить новую вещь')
async def addNewItem(message: Message, state: FSMContext):
    if message.from_user.id in settings.getAdminIds():
        await state.set_state(AddNewItemForm.brand)
        await message.answer('Введите название бренда', reply_markup=admin_kb.brandItemKb())


@router.message(AddNewItemForm.brand)
async def addBrandName(message: Message, state: FSMContext):


    if message.text in orm.get_brands():
        await state.set_state(AddNewItemForm.item)
        await state.update_data(brand=message.text)

        await message.answer('Введите название вещи',reply_markup=admin_kb.nameItemKb)
    else:
        await message.answer('Такого бренда нету',reply_markup=admin_kb.adminPanel)



@router.message(AddNewItemForm.item)
async def addBrandModel(message: Message, state: FSMContext):
    await state.set_state(AddNewItemForm.modelName)
    await state.update_data(item=message.text)

    allItems = ['T-shirts','Hoodies', 'Sneakers', 'Jackets','Longsleeves']

    if message.text in allItems:
        await message.answer('Введите модель', reply_markup=admin_kb.adminPanel)
    else:
        await message.answer('Такой вещи нету',reply_markup=admin_kb.adminPanel)


@router.message(AddNewItemForm.modelName)
async def addBrandSize(message: Message, state: FSMContext):
    await state.set_state(AddNewItemForm.size)
    await state.update_data(modelName=message.text)

    await message.answer('Введите размер вещи')


@router.message(AddNewItemForm.size)
async def addBrandPhoto(message: Message, state: FSMContext):
    await state.set_state(AddNewItemForm.photo)
    await state.update_data(size=message.text)

    await message.answer('Отправьте фото вещи')


@router.message(AddNewItemForm.photo, F.photo)
async def addBrandVerification(message: Message, state: FSMContext):
    await state.set_state(AddNewItemForm.price)
    await state.update_data(photo=message.photo[-1].file_id)

    await message.answer('Введите цену в USD:')


@router.message(AddNewItemForm.price)
async def addBrandPrice(message: Message, state: FSMContext):
    await state.set_state(AddNewItemForm.like)
    await state.update_data(price=message.text)

    data = await state.get_data()
    
    item = []

    for key in data.values():
        item.append(key)
    
    
    await message.answer_photo(item[4],f'Бренд: {item[0]}\nМодель: {item[2]}\nРазмер: {item[3]}\nЦена: {item[5]}')

    await message.answer('Все правильно?',reply_markup=admin_kb.addItemKb)

@router.message(AddNewItemForm.like, F.text == 'Да')
async def likeAddItem(message: Message, state: FSMContext):
        data = await state.get_data()
        item = []

        for key in data.values():
            item.append(key)

        
        orm.add_item(item[1],item[0],item[2],item[3],item[4],item[5])

        await message.answer('Вещь добавлена',reply_markup=admin_kb.adminPanel)

        await state.clear()


@router.message(AddNewItemForm.like, F.text == 'Нет')
async def unLikeAddItem(message: Message, state: FSMContext):
        await state.clear()

        await message.answer('Вещь не добавлена',reply_markup=admin_kb.adminPanel)