"""
Создание круговой клавиатуры

"""


# Проверка является ли последним
def is_tail(n, index):
    n_ful = n//9
    check = n_ful * 9
    if index <= check:
        return False
    return True


# Проверка является ли одним
def is_alone(n):
    if n <= 9:
        return True
    else:
        return False


# Кнопка отмены
def stop_del():
    back = InlineKeyboardButton('отмена', callback_data='stop_del')
    return back


# Первый (без кнопки "<")
def is_first(index):
    if index == 1:
        return True
    return False


def empty_btn():
    btn = InlineKeyboardButton(' ', callback_data=' ')
    return btn


def make_round_keyboard(n, index, istail=False):
    """
    n - длина списка элементов
    index - индекс элемента с которого начинается меню

    """
    markup = InlineKeyboardMarkup(row_width=3)
    number = 9
    n_full = 2
    tail = is_tail(n, index)
    alone = is_alone(n)
    first = is_first(index)

    if tail:
        for i in range(index, n+1):
            num = str(i)
            btn1 = InlineKeyboardButton(num, callback_data=num)
            markup.insert(btn1)
        if not alone:
            left = InlineKeyboardButton('<', callback_data='<'+str(index - 9))
            markup.row(left)
        else:
            markup.row(empty_btn())
        markup.insert(stop_del())
        markup.insert(empty_btn())

    else:
        end = index + 9
        i = index
        while i < end:

            btn1 = InlineKeyboardButton(str(i), callback_data=str(i))
            i += 1
            btn2 = InlineKeyboardButton(str(i), callback_data=str(i))
            i += 1
            btn3 = InlineKeyboardButton(str(i), callback_data=str(i))
            markup.add(btn1, btn2, btn3)
            i += 1
        if not first:
            left = InlineKeyboardButton('<', callback_data='<'+str(index - 9))
            markup.insert(left)
        else:
            markup.insert(empty_btn())
        markup.insert(stop_del())
        if not alone:
            right = InlineKeyboardButton('>', callback_data='>'+str(index+9))
            markup.insert(right)
        else:
            markup.insert(empty_btn())

    return markup
