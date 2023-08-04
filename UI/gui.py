from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivymd.uix.label import MDLabel
from kivy.metrics import dp
from Domain.main import text_preprocessing
from data import gold_and_wax
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine, MDExpansionPanelTwoLine
from kivy.core.clipboard import Clipboard
from kivymd.uix.boxlayout import MDBoxLayout
from datetime import datetime
from kivy.core.window import Window


class AI(MDApp):
    title = "Amharic Gold and Wax(ቅኔ) Identifier"

    def build(self):
        LabelBase.register("AmharicFont", "./PGUNICODE1.ttf")
        self.theme_cls.theme_style_switch_animation = False
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('main.kv')

    # def switch_theme(self):
    #     if self.theme_cls.theme_style == "Dark":
    #         self.theme_cls.theme_style = "Light"
    #     else:
    #         self.theme_cls.theme_style = "Dark"

    def open_tab(self, tab_name, question, incoming=False):

        bottom_navigation = self.root.ids.bottom_navigation
        bottom_navigation.switch_tab(tab_name)


    def copy_to_clipboard(self, label):
        text = label.text
        Clipboard.copy(text)


    def send_message(self, incoming=False, incoming_text=None):
        if not incoming:
            text_input = self.root.ids.text_input
            message = text_input.text
            if not message.isspace():
                label = Builder.load_string('''
MDCard:
    size_hint: 0.5, None
    height: self.minimum_height
    padding: dp(10)
    md_bg_color: "#023C35"
    pos_hint: {'center_x': .7}
    MDLabel:
        text: 'question'
        theme_text_color: "Custom"
        text_color: "#C7D7D7"
        adaptive_height: False,
        padding_x: '15dp'
        font_name: 'AmharicFont'
        halign: 'right'
        '''.replace('question', message.strip()))

                self.root.ids.chat_messages.add_widget(label)
                text_input.text = ""
                api_answer = text_preprocessing(message.strip())
                if api_answer.get("success") is True:
                    self.send_message(True, f"---> {api_answer.get('word')} ---> {api_answer.get('wax')} ---> {api_answer.get('gold')}")

                else:
                    self.send_message(True, api_answer.get('response'))


            else:
                text_input.text = ""
        else:
            label = Builder.load_string("""
MDCard:
    size_hint: 0.5, None
    height: self.minimum_height
    padding: dp(10)
    md_bg_color: "#2B2C36"
    pos_hint: {'center_x': .3}
    MDLabel:
        text: 'ai_answer'
        theme_text_color: "Custom"
        text_color: "#C7D7D7"
        adaptive_height: True,
        padding_x: '15dp'
        font_name: 'AmharicFont'
        halign: 'left'
        """.replace('ai_answer', incoming_text.strip()))
            self.root.ids.chat_messages.add_widget(label)

#     def on_start(self):
#         Window.set_icon('ai_icon.ico')
#         for text in [item.get('phrase') for item in gold_and_wax]:
#             card = """
# MDCard:
#     md_bg_color: "#2A3030"
#     size_hint: None, None
#     size: "250dp", "180dp"
#     pos_hint: {'center_x': .5}
#
#     BoxLayout:
#         orientation: 'vertical'
#         padding: '10dp'
#         spacing: '10dp'
#
#         MDLabel:
#             id: question_1
#             font_name: 'AmharicFont'
#             text: "gold_and_wax_text"
#             theme_text_color: "Custom"
#             text_color: "#C7D7D7"
#
#         MDRelativeLayout:
#             size_hint_y: None
#             height: dp(48)
#             spacing: '10dp'
#             pos_hint: {'left': 1}
#
#             MDIconButton:
#                 icon: 'help-circle'
#                 theme_text_color: "Secondary"
#                 on_release: app.open_tab('screen 2', "gold_and_wax_text", False)
#                 md_bg_color: "#3B474A"
#
#             MDIconButton:
#                 icon: 'content-copy'
#                 theme_text_color: "Secondary"
#                 on_release: app.copy_to_clipboard(root.ids.question_1)
#                 pos_hint: {'center_x': .8}
#                 halign: "right"
#                 md_bg_color: "#3B474A"
# """.replace("gold_and_wax_text", text)
#
#             self.root.ids.question_container.add_widget(Builder.load_string(card))


AI().run()
