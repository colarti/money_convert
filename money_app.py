import tkinter as tk
import customtkinter as ctk
import money


FONT= ('Arial', 30, 'bold')


class baseValue(tk.Frame):
    def __init__(self, parent, varList, baseList, value=1):
        super().__init__(parent, background='black')
        self.rowconfigure((0), uniform='a', weight=1)
        self.columnconfigure((0,1), weight=1)
        lblOne = ctk.CTkLabel(self, text=str(value), font=FONT, text_color='white')
        lblOne.grid(row=0, column=1)
        listValue = ctk.CTkOptionMenu(self, variable=varList, values=baseList, height=40, font=FONT, width=100)
        listValue.grid(row=0, column=0, padx=10)

class convertValue(tk.Frame):
    def __init__(self, parent, varList, baseList, exchangeValue):
        super().__init__(parent, background='black')

        self.rowconfigure((0), uniform='a', weight=1)
        self.columnconfigure((0,1), weight=1)
        lblValue = ctk.CTkLabel(self, textvariable=exchangeValue, font=FONT, text_color='white')
        lblValue.grid(row=0, column=1)
        listValue = ctk.CTkOptionMenu(self, variable=varList, values=baseList, height=40, font=FONT, width=100)
        listValue.grid(row=0, column=0, padx=10)

class entryBaseValue(tk.Frame):
    def __init__(self, parent, entryVarBase, varList):
        super().__init__(parent, background='black')

        self.rowconfigure((0), uniform='a', weight=1)
        self.columnconfigure((0,1), weight=1)
        entryValue = ctk.CTkEntry(self, textvariable=entryVarBase, justify='center', font=FONT)
        entryValue.grid(row=0, column=0, padx=20, sticky='ew')
        lblValue = ctk.CTkLabel(self, textvariable=varList, font=FONT, text_color='white')
        lblValue.grid(row=0, column=1)

class MoneyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Money Converter App')
        self._set_appearance_mode('dark')
        self._geo(500, 300)

        self.convert = money.currency_exchange()

        self.varBase = tk.StringVar(value=self.convert.get_base_list()[0])
        self.varConvert = tk.StringVar(value=self.convert.get_base_list()[0])
        self.exchangeValue = tk.StringVar()
        self.convertValue = tk.StringVar()
        self.currencyValue = tk.StringVar()

        self.varBase.trace('w', self.optionChange)
        self.varConvert.trace('w', self.optionChange)

        self.convertValue.trace('w', self.currencyChange)
        self.currencyValue.trace('w', self.currencyChange)

        self.rowconfigure((0,1), weight=1, uniform='a')
        self.columnconfigure((0,1), weight=1, uniform='a')

        m = baseValue(self, self.varBase, self.convert.get_base_list())
        m.grid(row=0, column=0, sticky='news')

        c = convertValue(self, self.varConvert, self.convert.get_base_list(), self.exchangeValue)
        c.grid(row=0, column=1, sticky='news')

        e = entryBaseValue(self, self.convertValue, self.varBase)
        e.grid(row=1, column=0, sticky='news')

        d = entryBaseValue(self, self.currencyValue, self.varConvert)
        d.grid(row=1, column=1, sticky='news')


        self.optionChange(None)

        self.bind('<Shift-Escape>', quit)
        self.mainloop()

    def _geo(self, w, h):
        pWidth = w
        pHeight = h
        sWidth = self.winfo_screenwidth()
        sHeight = self.winfo_screenheight()
        mWidth = sWidth//2-pWidth//2
        mHeight = sHeight//2-pHeight//2

        self.minsize(pWidth, pHeight)
        self.geometry(f'{pWidth}x{pHeight}+{mWidth}+{mHeight}')
    
    def optionChange(self, *args):
        self.exchangeValue.set(self.convert.get_exchange(self.varConvert.get(), self.varBase.get()))
        # print(f'optionChange[{self.varBase.get()}, {self.varConvert.get()}]: {self.exchangeValue.get()}')
        self.convertValue.set('')
        self.currencyValue.set('')


    def currencyChange(self, *args):
        # print(f'ARGS: {args}')

        if args[0] == 'PY_VAR3':
            try:
                data = float(self.convertValue.get()) * float(self.exchangeValue.get())
                # print(f'pyvar3 data: {round(data,2)}')
                self.currencyValue.set(round(data,4))
            except:
                pass
        if args[0] == 'PY_VAR4':
            try:
                data = float(self.currencyValue.get()) / float(self.exchangeValue.get())
                # print(f'pyvar4 data: {round(data,2)}')
                self.convertValue.set(round(data,4))
            except:
                pass

if __name__ == '__main__':
    money = MoneyApp()