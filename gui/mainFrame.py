
import tkinter as tk
from tkinter import ttk

from gui.view.changeQrFrame import changeQr
from gui.view.createQrcodeFrame import createQrcode


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        master.title("Generate your QrCode")
        master.geometry("500x500")
        master.resizable(False, False)

        tab_control = ttk.Notebook(master)

        # init onglet
        changeqRcode = ttk.Frame(tab_control)
        createqrcode = ttk.Frame(tab_control)


        # Create onglet
        tab_control.add(changeqRcode, text='Changer votre Qrcode')
        tab_control.add(createqrcode, text='crée votre Qrcode')

        changeQr(changeqRcode)
        createQrcode(createqrcode)


        tab_control.pack(expand=1, fill='both')

def launchApp():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


