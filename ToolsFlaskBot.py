from typing import List, Tuple

from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def list_of_lists_to_keyboards(buttons: List[List[str]]) :
    return ReplyKeyboardMarkup(keyboard=buttons)


def list_of_lists_to_inline_keyboard(buttons: List[List[Tuple[str, str]]]) :
    if not buttons :
        return None
    for i in range(len(buttons)) :
        for j in range(len(buttons[i])) :
            item = buttons[i][j]
            buttons[i][j] = InlineKeyboardButton(text=item[0], url=item[1])
    return InlineKeyboardMarkup(inline_keyboard=buttons)
