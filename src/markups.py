from telebot import types


main_markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
btn_new_request = types.KeyboardButton('/Новая_заявка🗣')
btn_user_request = types.KeyboardButton('/Мои_заявки🔍')
btn_contacts = types.KeyboardButton('/Контакты📜')
btn_user_review = types.KeyboardButton('/Оставить_отзыв📫')
main_markup.add(btn_new_request, btn_user_request, btn_contacts, btn_user_review)

organization_markup = types.ReplyKeyboardMarkup()
btn_first_organization = types.KeyboardButton(text = 'First organization')
btn_second_organization = types.KeyboardButton(text = 'Second organization')
btn_third_organization = types.KeyboardButton(text = 'Third_organization')
btn_fourth_organization = types.KeyboardButton(text = 'Fourth organization')
organization_markup.add(btn_first_organization, btn_second_organization, btn_third_organization, btn_fourth_organization)

cancel_markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
btn_cancel = types.KeyboardButton('Отмена')
cancel_markup.add(btn_cancel)

admin_markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
btn_get_users = types.KeyboardButton('/get_users')
btn_get_orders = types.KeyboardButton('/get_orders')
btn_get_reviews = types.KeyboardButton('/get_reviews')
btn_tell_to_user = types.KeyboardButton('/tell_to_user')
btn_tell_everyone = types.KeyboardButton('/tell_everyone')
admin_markup.add(btn_get_users, btn_get_orders, btn_get_reviews, btn_tell_to_user, btn_tell_everyone)

task_markup = types.InlineKeyboardMarkup()
btn_done = types.InlineKeyboardButton(text = 'Принять',callback_data = 'done')
btn_refusal = types.InlineKeyboardButton(text = 'Отказ',callback_data ='refusal')
task_markup.add(btn_done, btn_refusal)

lets_done_markup = types.InlineKeyboardMarkup()
btn_lets_done_request = types.InlineKeyboardButton(text = 'Выполнить',callback_data = 'done_request')
lets_done_markup.add(btn_lets_done_request)

done_markup = types.InlineKeyboardMarkup()
btn_done_request = types.InlineKeyboardButton(text = 'Выполнено', callback_data = 'pass')
done_markup.add(btn_done_request)

refusal_markup = types.InlineKeyboardMarkup()
btn_refusal_request = types.InlineKeyboardButton(text = 'Отказано', callback_data = 'pass')
refusal_markup.add(btn_refusal_request)
