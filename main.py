# -*- coding: utf-8 -*-

from kivymd.app import MDApp
from math import pow
from kivy.config import Config
from kivymd.toast.kivytoast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDThemePicker
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_hex_from_color
from kivy.uix.screenmanager import Screen

# TODO: Comment before build apk!!!
# from kivy.core.window import Window
# Window.size = (430, 650)

# Turn on android keyboard
Config.set("kivy", "keyboard_mode", "systemanddock")


class ContentNavigationDrawer(BoxLayout):
    pass


class MainScreen(Screen):
    pass


class BMIApp(MDApp):
    title = "Индекс массы тела"
    menu_items = []

    # def __init__(self, **kwargs):
    #     super(BMIApp, self).__init__(**kwargs)

    def build(self):
        self.theme_cls.primary_palette = "Teal"
        # self.ti_height = self.root.ids["_ti_height"]
        # self.ti_weight = self.root.ids["_ti_weight"]
        # self.lbl_bmi = self.root.ids["_lbl_bmi"]
        # self.nav_drawer = self.root.ids["_nav_drawer"]
        self.menu_items = [
            # {"viewclass": "MDMenuItem",
            #  "text": "Сменить тему",
            #  # "text_color": (1, 0, 0, 1),
            #  "icon": "theme-light-dark",
            #  "callback": self.show_themepicker},
            {
                "viewclass": "MDMenuItem",
                "text": "Приветствия",
                # "text_color": (1, 0, 0, 1),
                "icon": "human-greeting",
                "callback": self.greetings
            },

            {
                "viewclass": "MDMenuItem",
                "text": "Об авторе",
                # "text_color": (1, 0, 0, 1),
                "icon": "account",
                "callback": self.about_author
            },

            {
                "viewclass": "MDMenuItem",
                "text": "Выход",
                # "text_color": (0, 1, 0, 1),
                "icon": "exit-to-app",
                "callback": lambda x: self.stop()
            }
        ]
        return MainScreen()

    def show_themepicker(self, *args):
        picker = MDThemePicker()
        picker.open()

    def greetings(self, *args):
        dialog = MDDialog(
            title="Приветствия",
            size_hint=(.7, .5),
            text_button_ok="Всем привет",
            auto_dismiss=False,
            text="Огромное спасибо разработчикам Kivy и KivyMD, "
            "благодаря которым, есть возможность "
            "писать мобильные приложения на Python."
            "\nТакже огромное спасибо разработчикам утилиты Buildozer "
            "за возможность получить заветную apk-шечку."
            "\n\n[color={}][b]Привет моей дорогой семье.[/b][/color]"
            "\n\nПривет моему коллеге Владу Илюшникову.".format(get_hex_from_color(self.theme_cls.primary_color)))

        dialog.open()

    def about_author(self, *args):
        dialog = MDDialog(
            title="Об авторе",
            size_hint=(.7, .4),
            text_button_ok="Спасибо автору",
            # text_button_cancel=None,
            auto_dismiss=False,
            text="Александр Костючков"
             "\n[color={}][b]alkostuchkov@gmail.com[/b][/color]"
             "\n\nЭто мое первое мобильное приложение на Python "
             "c использованием KivyMD. "
             "Не судите сильно строго.".format(get_hex_from_color(self.theme_cls.primary_color)))

        dialog.open()

    def calculate(self):
        """Calculate BMI."""
        if (self.root.ti_height.text.strip() != "" and
                self.root.ti_weight.text.strip() != ""):
            try:
                height = float(self.root.ti_height.text)
                weight = float(self.root.ti_weight.text)
            except:
                height = 0
                weight = 0
            if height <= 0 or weight <= 0:
                toast("Рост и масса\nдолжны быть больше 0.")
                self.root.lbl_bmi.text = ""
                # self.lbl_advice.text = "Рост и масса\nдолжны быть больше 0."
            else:
                bmi = (weight / (height * height)) * pow(10, 4)
                result_string = self.get_result_string(bmi)
                normal_weight_arrange = self.get_normal_weight_arrange(height)
                self.root.lbl_bmi.text = "Ваш индекс массы тела: {:.2f}\n{}\n\n{}".format(bmi, result_string, normal_weight_arrange)
        else:
            self.root.lbl_bmi.text = ""
            toast("Введите данные")

    def get_result_string(self, bmi):
        """Returns result depends on bmi."""
        if bmi < 16:
            return "Выраженный дефицит массы тела."
        # elif 18.5 > bmi >= 16:  # and bmi < 18.5:
        elif 16 <= bmi < 18.5:  # and bmi < 18.5:
            return "Недостаточная масса тела"
        # elif 25 > bmi >= 18.5:  # and bmi < 25:
        elif 18.5 <= bmi < 25:  # and bmi < 25:
            return "Нормальная масса тела"
        # elif 30 > bmi >= 25:  # and bmi < 30:
        elif 25 <= bmi < 30:  # and bmi < 30:
            return "Избыточная масса тела (предожирение)"
        # elif 35 > bmi >= 30:  # and bmi < 35:
        elif 30 <= bmi < 35:  # and bmi < 35:
            return "Ожирение 1-ой степени"
        # elif 40 > bmi >= 35:  # and bmi < 40:
        elif 35 <= bmi < 40:  # and bmi < 40:
            return "Ожирение 2-ой степени"
        elif bmi >= 40:
            return "Ожирение 3-ой степени"

    def get_normal_weight_arrange(self, height):
        """Give an advice to gain or lose weight."""
        min_normal_bmi = 18.5
        max_normal_bmi = 24.99
        min_normal_weight = height * height * min_normal_bmi * pow(10, -4)
        max_normal_weight = height * height * max_normal_bmi * pow(10, -4)

        return "Ваша нормальная масса тела\nнаходится в диапазоне:\n {:.2f}кг - {:.2f}кг".format(min_normal_weight, max_normal_weight)


if __name__ == "__main__":
    BMIApp().run()
