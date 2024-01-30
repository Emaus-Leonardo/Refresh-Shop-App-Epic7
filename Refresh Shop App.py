import pyautogui as pg
import time
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.core.window import Window

import threading

pg.PAUSE = 0.5

mystic_image = 'images/mystic.png'
buy_mystic_image = 'images/buy_mystic.png'

bm_image = 'images/bm.png'
buy_bm_image = 'images/buy_bm.png'

refresh_image = 'images/refresh.png'
confirm_image = 'images/confirm.png'

# Variáveis globais
num_refreshes = 0
refresh_count = 0
bm_count = 0
mystic_count = 0
running = True


class RefreshShopApp(MDApp):
    def build(self):
        Window.size = (300, 300)  # Define o tamanho da janela
        self.theme_cls.theme_style = "Dark"
        self.root = BoxLayout(orientation='vertical', spacing=10, padding=[10, 10, 10, 10])

        self.root.add_widget(MDLabel(text="Welcome to Refresh Shop"))

        # Adiciona um campo de entrada para o número de refresh
        self.input_refreshes = MDTextField(hint_text="Amount of Refresh")
        self.root.add_widget(self.input_refreshes)

        button_refresh = MDFlatButton(
            text="Refresh Shop", on_release=self.start_refresh, md_bg_color=(0, 0.7, 0.7, 1)) 
        self.root.add_widget(button_refresh)

        button_stop = MDFlatButton(
            text="Stop Refresh", on_release=self.stop_refresh, md_bg_color=(0.9, 0.2, 0.2, 1))
        self.root.add_widget(button_stop)

        self.text_completed = MDLabel(text="")
        self.root.add_widget(self.text_completed)

        return self.root

    def start_refresh(self, instance):
        global num_refreshes, running, refresh_count, bm_count, mystic_count
        try:
            num_refreshes = int(self.input_refreshes.text)
            refresh_count = 0
            bm_count = 0
            mystic_count = 0
            running = True
            threading.Thread(target=self.refresh_shop).start()
        except ValueError:
            self.text_completed.text = "Please enter a valid number."

    def stop_refresh(self, instance):
        global running, refresh_count, bm_count, mystic_count
        running = False
        self.text_completed.text = f"Stopped after {refresh_count} refresh. Bought {bm_count} BMs and {mystic_count} Mystics."

    def find_mystic(self):
        global mystic_count
        while True:
            try:
                mystic = pg.locateOnScreen(mystic_image, confidence=0.6)
                if mystic is not None:
                    pg.moveTo(mystic)
                    pg.moveRel(700, 30)
                    pg.click()
                    buy_mystic = pg.locateOnScreen(
                        buy_mystic_image, confidence=0.6)
                    pg.click(buy_mystic)
                    time.sleep(1)
                    mystic_count += 1
                    break
            except pg.ImageNotFoundException:
                break

    def find_bm(self):
        global bm_count
        while True:
            try:
                bm = pg.locateOnScreen(bm_image, confidence=0.6)
                if bm is not None:
                    pg.moveTo(bm)
                    pg.moveRel(700, 30)
                    pg.click()
                    buy_bm = pg.locateOnScreen(buy_bm_image, confidence=0.6)
                    pg.click(buy_bm)
                    time.sleep(1)
                    bm_count += 1
                    break
            except pg.ImageNotFoundException:
                self.find_mystic()
                break

    def refresh_shop(self):
        global num_refreshes, refresh_count
        time.sleep(3)
        print('Looking for BM and Mystic')
        for _ in range(num_refreshes):
            if not running:
                break
            self.find_bm()
            pg.scroll(-250)

            time.sleep(1)
            self.find_bm()

            refresh = pg.locateOnScreen(refresh_image, confidence=0.6)
            pg.click(refresh)

            confirm = pg.locateOnScreen(confirm_image, confidence=0.6)
            pg.click(confirm)
            time.sleep(1)
            refresh_count += 1

        if running:
            self.text_completed.text = f"Completed {refresh_count} Refreshes. Bought {bm_count} BMs and {mystic_count} Mystics."


Config.set('graphics', 'width', '300')  # Define a largura da janela
Config.set('graphics', 'height', '300')  # Define a altura da janela

if __name__ == "__main__":
    RefreshShopApp().run()
