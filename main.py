from customtkinter import *
from CTkScrollableDropdown import CTkScrollableDropdown
from PIL import Image

set_appearance_mode("dark")
root = CTk(fg_color="#111")
root.geometry("900x600")
root.resizable(False, False)
root.title("Currency Converter")

image_path = os.path.join(os.path.dirname(os.path.relpath(__file__)), "images")
interchange_img = CTkImage(Image.open(os.path.join(image_path, "interchange.png")), size=(40, 40))

exchange_rates = {
        "USD": 1.0,
        "EUR": 0.85,
        "JPY": 110.0,
        "GBP": 0.75,
        "AUD": 1.4,
        "CAD": 1.25,
        "CNY": 6.5,
        "INR": 74.0,
        "BRL": 5.25,
        "KRW": 1150.0
    }

class CurrencyConverter:
    def __init__(self, master):
        self.root = master

        self.main = CTkFrame(self.root, fg_color="#333")
        CTkLabel(self.main, text="Currency Converter", text_color="white", font=("Canbera", 40)).pack(side=TOP, pady=20, fill=X,  padx=10)
        
        self.amount_frame = CTkFrame(self.main, fg_color="transparent")
        
        CTkLabel(self.amount_frame, text="Enter Amount", font=("Consolas Light", 20), text_color="white").pack(side=TOP, anchor="nw", padx=22, pady=10)
        
        self.amount_entry = CTkEntry(self.amount_frame, font=("IBM Plex Sans", 30))
        self.amount_entry.pack(side=BOTTOM, fill=X, padx=20, ipady=10)
        self.amount_entry.insert(0, "100")
        
        self.amount_frame.pack(side=TOP, fill=X, padx=50)

        value = [
            "USD", "CNY", "JPY", "EUR", "INR", "GBP", "BRL", "AUD", 
            "CAD", "KRW"
        ]
        value2 = [
            "INR", "CNY", "JPY", "EUR", "USD", "GBP", "BRL", "AUD", 
            "CAD", "KRW"]

        self.from_to_frame = CTkFrame(self.main, fg_color="transparent")
        
        self.from_frame = CTkFrame(self.from_to_frame, fg_color="transparent")
        CTkLabel(self.from_frame, text="From", font=("Consolas Light", 20), text_color="white").pack(side=TOP, anchor="nw", padx=22, pady=5)
        self.option_from = CTkOptionMenu(self.from_frame, values=value, font=("Poppins", 20), height=40)
        self.option_from.pack(side=BOTTOM, padx=22)
        CTkScrollableDropdown(self.option_from, values=value, width=200, button_height=40, button_color="#222", fg_color="#111", text_color="white", 
                              font=("IBM Plex Sans", 15), scrollbar=True)

        self.from_frame.pack(side=LEFT, fill=Y, padx=0, pady=10)
        
        self.interchange_frame = CTkFrame(self.from_to_frame,  fg_color="transparent")
        CTkButton(self.interchange_frame, text="", image=interchange_img, width=0, fg_color="transparent", command=self.interchange_amount).pack(side=BOTTOM, anchor="ne")
        self.interchange_frame.pack(side=LEFT, fill=Y, padx=1, pady=10)

        self.to_frame = CTkFrame(self.from_to_frame, fg_color="transparent")
        CTkLabel(self.to_frame, text="To", font=("Consolas Light", 20), text_color="white").pack(side=TOP, anchor="nw", padx=22, pady=5)
        self.option_to = CTkOptionMenu(self.to_frame, font=("Poppins", 20), height=40, values=value2)
        self.option_to.pack(side=BOTTOM, padx=22)

        CTkScrollableDropdown(self.option_to, values=value, width=200, button_height=40, button_color="#222", fg_color="#111", text_color="white", 
                              font=("IBM Plex Sans", 15), scrollbar=True)

        self.to_frame.pack(side=RIGHT, fill=Y, padx=0, pady=10)

        self.from_to_frame.pack(side=TOP, fill=X, padx=50, pady=15)

        self.get_rate = CTkButton(self.main, text="Get Exchange Rate", font=("IBM Plex Sans", 25), fg_color="#e8e8e8", text_color="black", hover_color="white", command=self.get_exchange_rate)
        self.get_rate.pack(side=TOP, fill=X, padx=65, ipady=15, pady=15)

        self.result = CTkLabel(self.main, fg_color="#555", text_color="white", font=("IBM Plex Sans", 25, "bold"), corner_radius=10, text="1 USD = 83745.93 INR")
        self.result.pack(side=TOP, pady=10, ipady=25, ipadx=40, fill=X, padx=65)

        self.main.pack(fill=BOTH, expand=True, padx=180, pady=25, ipady=20)

        like_that_entry = CTkEntry(self.root, fg_color="transparent", border_color="#111", text_color="#111")
        like_that_entry.pack(side=BOTTOM, padx=1, pady=0)

        self.main.bind("<Button-1>", lambda event: like_that_entry.focus())

    def get_exchange_rate(self):
        amount = self.amount_entry.get()
        from_currency = self.option_from.get()
        to_currency = self.option_to.get()

        try:
            amount = float(amount)
        except ValueError:
            self.result.configure(text="Invalid amount entered")
            return

        if from_currency in exchange_rates and to_currency in exchange_rates:
            rate_from = exchange_rates[from_currency]
            rate_to = exchange_rates[to_currency]
            usd_amount = amount / rate_from
            converted_amount = usd_amount * rate_to

            self.result.configure(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            self.result.configure(text="Currency not supported")

    def interchange_amount(self):
        from_ = self.option_from.get()
        to_ = self.option_to.get()
        self.option_from.set(to_)
        self.option_to.set(from_)

CurrencyConverter(root)

root.mainloop()