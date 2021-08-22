import tkinter as tk
from fileinput import filename
from tkinter import filedialog
from tkinter import filedialog as fd
from services.changeQrCode import QrCodeChange, valQrcode


def changeQr(self):



    # choice qrcode
    text_name = "1."
    tk.Label(self, text=text_name).place(x=40, y=75, width=20, height=20)
    filename = filedialog.askopenfilename()
    #fileQrcode = tk.Button(self, text='Open', command=UploadAction)
    #fileQrcode.pack()





    ## name of QRcode
    text_name = "2."
    tk.Label(self, text=text_name).place(x=40, y=75, width=20, height=20)
    name_qrcode = tk.StringVar()
    name_qrcode.set("Renomé le Qrcode")
    entree = tk.Entry(self, textvariable=name_qrcode, width=30)
    entree.place(x=80, y=70)

    ## data of QRcode
    text_data = "3."
    tk.Label(self, text=text_data).place(x=40, y=125, width=20, height=20)
    data = tk.StringVar()
    valueqrcode = valQrcode(filename)
    data.set(valueqrcode)
    entree2 = tk.Entry(self, textvariable=data, width=30)
    entree2.place(x=80, y=120)

    ## color_fill of QRcode
    text_color_fill = "4."
    tk.Label(self, text=text_color_fill).place(x=40, y=175, width=20, height=20)
    color_fill = tk.StringVar()
    color_fill.set("black")
    entree3 = tk.Entry(self, textvariable=color_fill, width=30)
    entree3.place(x=80, y=170)

    ## color_fill of QRcode
    text_color_back = "5."
    tk.Label(self, text=text_color_back).place(x=40, y=225, width=20, height=20)
    color_back = tk.StringVar()
    color_back.set("white")
    entree4 = tk.Entry(self, textvariable=color_back, width=30)
    entree4.place(x=80, y=220)

    displaySendButton(self, entree, entree2, entree3, entree4, filename)



def displaySendButton(self, entree, entree2, entree3, entree4, qrCodeFile):
    sendButton = tk.Button(self, text="changer votre QrCode", width=30,
                           command=lambda: changeQrCode(entree, entree2, entree3, entree4, qrCodeFile))
    sendButton.place(x=80, y=350)


def changeQrCode(entree, entree2, entree3, entree4, qrCodeFile):
    QrCodeChange(entree.get(), entree2.get(), entree3.get(), entree4.get(), qrCodeFile)


def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    return filename