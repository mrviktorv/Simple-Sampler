import os.path
import tkinter as tk
import sys
import os

from .keyboard_keys_view import KeyboardKeysView
from .lfo_view import LfoView

#DIR_NAME = os.path.dirname(__file__)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class MainView(tk.Frame):
    def __init__(self, window, rompler, *a, **kw):
        super(MainView, self).__init__(window, *a, **kw)

        self._window = window

        # Set up the main window
        window.title("Crazy Sampler")
        window.geometry("800x760+360+20")
        window.config(bg="#ffffff")
        window.resizable(0,0)

        self._canvas = tk.Canvas(window)
        self._canvas.pack()

        self._background_image = self._create_background_image()
        self._logo = self._create_logo()

        self._keyboard_keys_view = KeyboardKeysView(self._canvas)

        self._lfo_view = LfoView(self._canvas, rompler.lfo)

    def on_key_pressed(self, key):
        self._keyboard_keys_view.on_key_pressed(key)

    def on_key_released(self, key):
        self._keyboard_keys_view.on_key_released(key)

    def _create_background_image(self):
        image_path = resource_path("images/keyboard.ppm")
        background_image = tk.PhotoImage(file=image_path)

        self._canvas.configure(
            width=background_image.width(),
            height=background_image.height(),
        )
        self._canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

        return background_image

    def _create_logo(self):
        image_path = resource_path("images/logo.ppm")
        image = tk.PhotoImage(file=image_path)
        self._logo_label = tk.Label(None, image=image)

        self._canvas.create_window(555, 155, anchor=tk.NW, window=self._logo_label)

        return image
