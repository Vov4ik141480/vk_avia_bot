# coding: utf-8
from vk_utils import start_keyboard
from vk_methods import VkMethods
from template_messages import welcome_text, wrong_data, hint_to_begin


class BotSendMethod:
    def __init__(self):
        self.welcome_message = welcome_text
        self.wrong_message = wrong_data
        self.hint_for_begin = hint_to_begin

    def send_welcome(self, user_id):
        """Отправляет юзеру информацию как взаимодействовать с ботом"""
        keyboard = start_keyboard.get_keyboard()
        VkMethods().send_message(user_id, self.welcome_message, keyboard)

    def send_hint(self, user_id):
        """Отправляет юзеру подсказку как начать поиск"""
        VkMethods().send_message(user_id, self.hint_for_begin, keyboard=None)

    def send_warning(self, user_id, text):
        """Отправляет юзеру предупреждения если что-то пошло не так"""
        VkMethods().send_message(user_id, self.wrong_message.format(text), keyboard=None)        

    def send_message(self, user_id, message, keyboard):
        """Отправляет юзеру сообщение от бота"""
        VkMethods().send_message(user_id, message, keyboard=keyboard)