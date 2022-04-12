from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, ParseMode, InlineKeyboardButton
from keyboards import client_kb

from config import bot


async def python_quiz_1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Next question",
                                         callback_data="button_call_1")
    markup.add(button_call_1)
    code_snippets = '''*Option one*\n```python def list_extender(input_list):
    input_list.extend(input_list)```*Option two*```python def list_adder(input_list):
    return input_list+input_list```'''
    question = "Which one of the above functions will return a list extended by itself? "
    answers = [
        "1", "2", "Both options", "None of them"
    ]
    await bot.send_message(call.message.chat.id, code_snippets, parse_mode='MarkdownV2')

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Both seems right but work differently",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )


async def python_quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("Next question",
                                         callback_data="button_call_2")
    markup.add(button_call_2)
    question = "How do you insert COMMENTS in Python code?"
    answers = [
        "# Comment",
        "// Comment",
        "/* Comment */",
        "None of above",
        "All",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="\# Used for comments in Python\. You can also use triple quotes for multiline comments",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )


async def python_quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("Final question",
                                         callback_data="button_call_3")
    markup.add(button_call_3)
    question = "What is the correct file extension for Python files?"
    answers = [
        ".py",
        ".pyt",
        ".pyth",
        ".pie"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="py extension is for source code",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def python_quiz_4(call: types.CallbackQuery):
    question = 'In Python, \'Hello\', is the same as "Hello"?'
    answers = [
        "True",
        "False"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Strings in python are surrounded by either single quotation marks or double quotation marks",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )
    await bot.send_message(call.message.chat.id,
                           f"Want to try again?",
                           reply_markup=client_kb.quiz_menu_markup)


async def good_bye(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id,
                           f"Bye! See you soon")


def register_handlers_client(dp: Dispatcher):
    dp.register_callback_query_handler(python_quiz_1,
                                       lambda call: call.data == "python_quiz")
    dp.register_callback_query_handler(python_quiz_2,
                                       lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(python_quiz_3,
                                       lambda call: call.data == "button_call_2")
    dp.register_callback_query_handler(python_quiz_4,
                                       lambda call: call.data == "button_call_3")
    dp.register_callback_query_handler(good_bye,
                                       lambda call: call.data == "cancel_quiz")