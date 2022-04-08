from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from config import bot, dp


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Hello {message.from_user.first_name}. Type /quiz to start quiz.")


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
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
    await bot.send_message(message.from_user.id, code_snippets, parse_mode='MarkdownV2')

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Both seems right but work differently",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
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


@dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quiz_3(call: types.CallbackQuery):
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


@dp.callback_query_handler(lambda call: call.data == "button_call_3")
async def quiz_4(call: types.CallbackQuery):
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


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
