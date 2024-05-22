from aiogram import types, Bot, Router
from aiogram.filters.command import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from bot.middlewares.logging import TEstMiddleware

from bot.config.settings import GROUP_ID, SEND_ME, TEXT_DATA, VALIDATION_OUPUT_TEXT, SUCCESS_INPUT_DATA


router = Router()

router.message.middleware(TEstMiddleware())

class SendMe(StatesGroup):
    message = State()


@router.message(Command(commands=SEND_ME))
async def send_message_on_group_admin(message: types.Message, state: FSMContext) -> None:
    """Start send my group"""
    await state.set_state(SendMe.message)
    await message.answer(VALIDATION_OUPUT_TEXT)
    

@router.message(SendMe.message)
async def send_message(message: types.Message, state: FSMContext, bot: Bot) -> None: 
    """Sending message my group (Group admin) chat"""   
    if message.text:
        await state.update_data(message = message.text)

        data = await state.get_data()
        
        # Send Group
        await bot.send_message(GROUP_ID, TEXT_DATA(message.from_user.first_name, 
                                                message.from_user.last_name, 
                                                message.from_user.username, 
                                                data['message']))
        state.clear()
        
        await message.answer(SUCCESS_INPUT_DATA)
        
    else:
        await message.answer(VALIDATION_OUPUT_TEXT)
        return send_message