from customtkinter import *
import pygame
import math
import tkinter
pygame.mixer.init()

def play_click():
    try:
        sound = pygame.mixer.Sound("click.wav")
        sound.set_volume(1.0)
        sound.play()
    except Exception as e:
        print("Error playing sound:", e)

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.columnconfigure((0,1,2,3),weight=1)
        self.rowconfigure((0,1,2,3),weight=1)
        self.font = CTkFont(family="Bank Gothic light bt", size=26, weight="bold")
        self.history = []

        self.values=CTkEntry(self,fg_color="dark green",
                        text_color="black",
                        placeholder_text_color="black",
                        placeholder_text="Enter the value",
                        font=self.font)
        self.values.grid(row=0,column=0,columnspan=4,sticky="nsew")

        self.btn1=CTkButton(self,text="1",command=lambda:self.g_num("1"),fg_color="chartreuse4",
                            hover_color="#556B2F",font=self.font)
        self.btn1.grid(row=3,column=0,pady=5,padx=10,sticky="nsew")

        self.btn2 = CTkButton(self, text="2", command=lambda: self.g_num("2"), fg_color="chartreuse4",
                              hover_color="#556B2F",font=self.font)
        self.btn2.grid(row=3, column=1, pady=5, padx=10,sticky="nsew")

        self.btn3 = CTkButton(self, text="3", command=lambda: self.g_num("3"), fg_color="chartreuse4",
                              hover_color="#556B2F",font=self.font)
        self.btn3.grid(row=3, column=2, pady=5, padx=10,sticky="nsew")

        self.btn4 = CTkButton(self, text="4", command=lambda: self.g_num("4"), fg_color="chartreuse4",
                              hover_color="#556B2F",font=self.font)
        self.btn4.grid(row=2, column=0, pady=5, padx=10,sticky="nsew")

        self.btn5 = CTkButton(self, text="5", command=lambda: self.g_num("5"), fg_color="chartreuse4",
                              hover_color="#556B2F",font=self.font)
        self.btn5.grid(row=2, column=1, pady=5, padx=10, sticky="nsew")

        self.btn6 = CTkButton(self, text="6", command=lambda: self.g_num("6"), fg_color="chartreuse4",
                              hover_color="#556B2F",font=self.font)
        self.btn6.grid(row=2, column=2, pady=5, padx=10, sticky="nsew")

        self.btn7 = CTkButton(self, text="7", command=lambda: self.g_num("7"), fg_color="chartreuse4",
                              hover_color="#556B2F",font=self.font)
        self.btn7.grid(row=1, column=0, pady=5, padx=10, sticky="nsew")

        self.btn8 = CTkButton(self, text="8", command=lambda: self.g_num("8"), fg_color="chartreuse4",
                              hover_color="#556B2F",font=self.font)
        self.btn8.grid(row=1, column=1, pady=5, padx=10, sticky="nsew")

        self.btn9 = CTkButton(self, text="9", command=lambda: self.g_num("9"), fg_color="chartreuse4",
                              hover_color="#556B2F",font=self.font)
        self.btn9.grid(row=1, column=2, pady=5, padx=10, sticky="nsew")

        self.btn0 = CTkButton(self, text="0", command=lambda: self.g_num("0"), fg_color="chartreuse4",
                             hover_color="#556B2F",font=self.font)
        self.btn0.grid(row=4, column=2, pady=5, padx=10, sticky="nsew")

        self.pls=CTkButton(self,text="+",command=lambda:self.operating("+"),fg_color="chartreuse4",
                           hover_color="#556B2F",font=self.font)
        self.pls.grid(row=1,column=3,pady=5, padx=10,sticky="nsew")

        self.ngt = CTkButton(self, text="-", command=lambda: self.operating("-"), fg_color="chartreuse4",
                             hover_color="#556B2F",font=self.font)
        self.ngt.grid(row=2, column=3, pady=5, padx=10, sticky="nsew")

        self.div = CTkButton(self, text="/", command=lambda: self.operating("/"), fg_color="chartreuse4",
                             hover_color="#556B2F",font=self.font)
        self.div.grid(row=3, column=3, pady=5, padx=10, sticky="nsew")

        self.mul = CTkButton(self, text="*", command=lambda: self.operating("*"), fg_color="chartreuse4",
                             hover_color="#556B2F",font=self.font)
        self.mul.grid(row=4, column=3, pady=5, padx=10, sticky="nsew")

        self.equal=CTkButton(self,text="=",command=self.equalation,hover_color="#556B2F",
                             fg_color="#6B8E23" ,font=self.font)
        self.equal.grid(row=5, column=3, pady=5, padx=10, sticky="nsew")

        self.clear=CTkButton(self, text="Clear", command=self.delet, hover_color="#556B2F",
                               fg_color="#6B8E23",font=self.font )
        self.clear.grid(row=6, column=3, pady=5, padx=10, sticky="nsew")

        self.dot=CTkButton(self,text=".",command=lambda: self.g_dot(), fg_color="#6B8E23",
                           font=self.font,
                           hover_color="#556B2F")
        self.dot.grid(row=7, column=3, pady=5, padx=10, sticky="nsew")

        self.sing=CTkButton(self,text="+,-",command=self.toggle_sing,fg_color="#6B8E23",hover_color="#556B2F",
                            font=self.font)
        self.sing.grid(row=5,column=2,pady=5, padx=10, sticky="nsew")

        self.percent = CTkButton(self, text="%", command=self.percentage,
                                 hover_color="#556B2F", fg_color="#6B8E23", font=self.font)
        self.percent.grid(row=6, column=2, pady=5, padx=10, sticky="nsew")

        self.x=CTkButton(self,text="x²",command=self.square,fg_color="#6B8E23",
                         hover_color="#556B2F",font=self.font)
        self.x.grid(row=7, column=2, pady=5, padx=10, sticky="nsew")

        self.h=CTkButton(self, text="√", command=self.square_root, fg_color="#6B8E23",
                  hover_color="#556B2F",font=self.font)
        self.h.grid(row=4, column=1, pady=5, padx=10, sticky="nsew")

        self.option=CTkOptionMenu(self,values=["dark","light"],command=self.val,fg_color="#6B8E23",
                                  button_color="dark green",font=self.font)
        self.option.grid(row=5, column=1, pady=5, padx=10, sticky="nsew")

        history_btn = CTkButton(self, text="HISTORY", command=self.show_history, fg_color="dark green",
                                   font=self.font,hover_color="#6B8E23")
        history_btn.grid(row=6, column=1, padx=10, pady=5, sticky="nsew")

    def g_num(self, n):
        play_click()
        new_n = self.values.get() + n
        self.values.delete(0, END)
        self.values.insert(0, new_n)

    def delet(self):
        play_click()
        self.values.delete(0, END)

    def toggle_sing(self):
        play_click()
        try:
            c = self.values.get()
            if c :
                if c.startswith("-"):
                    self.values.delete(0, END)
                    self.values.insert(0, c[1:])
                else:
                    self.values.delete(0, END)
                    self.values.insert(0,"-"+c)
        except:
            pass

    def percentage(self):
        play_click()
        try:
            c = float(self.values.get())
            self.values.delete(0, END)
            self.values.insert(0, c / 100)
        except:
            pass

    def operating(self, o):
        play_click()
        try:
            self.f_num = float(self.values.get())
            self.op = o
            self.values.delete(0, END)
        except ValueError:
            self.values.delete(0, END)
            self.values.insert(0, "Error")

    def equalation(self):
        play_click()
        try:
            self.s_num = float(self.values.get())
            expression = f"{self.f_num} {self.op} {self.s_num}"

            if self.op == "+":
                result = self.f_num + self.s_num
            elif self.op == "-":
                result = self.f_num - self.s_num
            elif self.op == "*":
                result = self.f_num * self.s_num
            elif self.op == "/":
                if self.s_num == 0:
                    result = "Error"
                else:
                    result = self.f_num / self.s_num
            else:
                result = "Error"

            self.values.delete(0, END)
            self.values.insert(0, result)
            history_item = f"{expression} = {result}"
            self.history.append(history_item)

        except Exception as e:
            self.values.delete(0, END)
            self.values.insert(0, "Error")
            print("Error in equalation:", e)

    def g_dot(self):
        play_click()
        current = self.values.get()
        if "." not in current:
            self.values.insert(END, ".")

    def square(self):
        play_click()
        try:
            c = float(self.values.get())
            result = c ** 2
            self.values.delete(0,END)
            self.values.insert(0,result)
        except:
            pass

    def square_root(self):
        play_click()
        try:
            c = float(self.values.get())
            if c >=0:
                result = math.sqrt(c)
                self.values.delete(0,END)
                self.values.insert(0,result)
            else:
                self.values.delete(0, END)
                self.values.insert(0, "Error")
        except:
            pass

    def val(self,choice):
        set_appearance_mode(choice)

    def show_history(self):
        history_window = CTkToplevel(self)
        history_window.title("History")
        history_window.geometry("300x400")

        text = CTkTextbox(history_window, width=280, height=380)
        text.pack(padx=10, pady=10)

        for item in reversed(self.history):
            text.insert("end", item + "\n")
        text.configure(state="disabled")


if __name__ == '__main__':
    app = App()
    app.mainloop()
