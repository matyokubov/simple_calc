# ——— @python_dasturlash_darslari
#Eng sodda kalkulyator yasaymiz
#Oynani sozlash
from tkinter import Tk, ttk, StringVar
main_win = Tk()
main_win.title("Kalkulyator")
main_win.geometry("285x130")

#Text joylash
label = ttk.Label(main_win, text="Misol yozing")
label.place(x=10, y=10)

#Ma'lumot kiritish
i = StringVar()
input_cp = ttk.Entry(main_win, width=30, textvariable=i)
input_cp.place(x=85, y=10)

#Natijani olish uchun yozuv
res = ttk.Label(main_win, text="...")
res.place(x=20, y=75)

#Hisoblovchi funksiya
def calc(inp):
    global res
    #Noto'g'ri ma'lumot kiritilganda dastur to'xtamasligi uchun
    try:
        res.configure(text=eval(inp))
    except:
        pass

#Tugmalar joylab chiqamiz
ttk.Button(main_win, text="Hisoblash", command = lambda: calc(i.get())).place(x=40, y=40, width=80)
ttk.Button(main_win, text="Tozzala", command = lambda: i.set("")).place(x=130, y=40, width=80)

#Va har doim ishlaydigan qilamiz
main_win.mainloop()
