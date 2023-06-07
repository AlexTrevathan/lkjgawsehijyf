import tkinter as tk
from tkinter import *
root = Tk()


class Windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Test Application")
        container = tk.Frame(self, height=10, width=10)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (Menu, BurgerMenu, DrinksMenu, KidsMenu, Cart):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Menu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Menu")
        label.pack(padx=10, pady=10)
        switch_window_button = tk.Button(self, text="BurgerMenu", command=lambda: controller.show_frame(BurgerMenu),)
        switch_window_button.pack(side="top", fill=tk.X)
        switch_window_button = tk.Button(self, text="DrinksMenu", command=lambda: controller.show_frame(DrinksMenu), )
        switch_window_button.pack(side="top", fill=tk.X)
        switch_window_button = tk.Button(self, text="KidsMenu", command=lambda: controller.show_frame(KidsMenu), )
        switch_window_button.pack(side="top", fill=tk.X)
        switch_window_button = tk.Button(self, text="Cart", command=lambda: controller.show_frame(Cart), )
        switch_window_button.pack(side="top", fill=tk.X)



class KidsMenu(tk.Frame):
    def __init__(self, parent, controller):
        global cart # tring to make a global cart so i can change from other classes.
        tk.Frame.__init__(self, parent)
        nugget_pack = 3.50
        kids_meal = 5.25
        supreme_meal = 6.50
        label = tk.Label(self, text="Kids Menu")
        label.pack(padx=10, pady=10)
        menu = tk.Message(self, text=("Nugget Pack", "|$", nugget_pack))
        menu.pack(padx=10, pady=10)
        menu = tk.Message(self, text=("Kids Meal", "|$", kids_meal))
        menu.pack(padx=10, pady=10)
        menu = tk.Message(self, text=("Supreme Meal", "|$", supreme_meal))
        menu.pack(padx=10, pady=10)
        switch_window_button = tk.Button(self, text="Return to menu", command=lambda: controller.show_frame(Menu))
        switch_window_button.pack(side="bottom", fill=tk.X)


class DrinksMenu(tk.Frame):
    def __init__(self, parent, controller):
        global cart
        tk.Frame.__init__(self, parent)
        soda = 4.50
        cola = 5.20
        fanta = 4.00
        label = tk.Label(self, text="Drinks")
        label.pack(padx=10, pady=10)
        menu = tk.Message(self, text=("Soda", "|$", soda))
        menu.pack(padx=10, pady=10)
        menu = tk.Message(self, text=("Cola", "|$", cola))
        menu.pack(padx=10, pady=10)
        menu = tk.Message(self, text=("Fanta", "|$", fanta))
        menu.pack(padx=10, pady=10)
        switch_window_button = tk.Button(self, text="Return to menu", command=lambda: controller.show_frame(Menu))
        switch_window_button.pack(side="bottom", fill=tk.X)


class BurgerMenu(tk.Frame):
    def __init__(self, parent, controller):
        global cart
        global listbox
        tk.Frame.__init__(self, parent)
        cheeseburger = 10.99
        hamburger = 8.50
        veggieburger = 11.30
        label = tk.Label(self, text="Burgers")
        label.pack(padx=10, pady=10)
        menu = tk.Message(self, text=("cheeseburger", "|$"))
        menu.pack(padx=10, pady=10)
        menu = tk.Message(self, text=("veggieburger", "|$", veggieburger))
        menu.pack(padx=10, pady=10)
        menu = tk.Message(self, text=("hamburger", "|$", hamburger))
        menu.pack(padx=10, pady=10)
        switch_window_button = tk.Button(self, text="Return to menu", command=lambda: controller.show_frame(Menu))
        switch_window_button.pack(side="bottom", fill=tk.X)


class Cart(tk.Frame):
    def __init__(self, parent, controller):
        def add():
            global cart
        cart = [] # need a .append to add to the list but don't know how to.
        price = 0
        # burger Prices
        cheeseburger = 10.99
        veggieburger = 11.30
        hamburger = 8.50
        # Drinks Prices
        soda = 4.50
        cola = 5.20
        fanta = 4.00
        # Kids Meals Prices
        nugget_pack = 3.50
        kids_meal = 2.25
        supreme_meal = 6.50
        # These prices are for the calculations to find out the total price.
        tk.Frame.__init__(self, parent)
        def add_to_list(text):
            global listbox
            listbox.insert(0, text)
        entry = tk.Entry(self)
        entry.pack(padx=1)
        text = tk.Button(self, text="Add Item", command=lambda: add_to_list(entry))
        # this should put the variable that is inputted into the entry into the list
        text.pack(pady=5)
        listbox = tk.Listbox(self, listvariable=cart)
        listbox.pack(pady=15)
        if entry == "cheeseburger" or entry == "Cheeseburger":
            cart.append("Cheeseburger")
            price = price + cheeseburger

        message = tk.Message(self, text=("$", price))
        message.pack(padx=1)
        switch_window_button = tk.Button(self, text="Return to menu", command=lambda: controller.show_frame(Menu))
        switch_window_button.pack(side="bottom", fill=tk.X)

if __name__ == "__main__":
    testObj = Windows()
    testObj.mainloop()