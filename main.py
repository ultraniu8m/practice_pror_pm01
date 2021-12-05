from tkinter import *
import requests
from bs4 import BeautifulSoup
try:
    headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    r = requests.get(url = 'https://ru.investing.com/currencies/usd-jpy', headers=headers)
    with open ('actual_course.htlm','w', encoding='utf-8')as file:
        file.write(r.text)
    with open('actual_course.htlm', encoding='utf-8')as file:
        src=file.read()
    soup = BeautifulSoup(src,'lxml')
    actual_course = float(soup.find('div',class_="top bold inlineblock" ).find('span').text.replace(',','.'))
except:
    print(sys.exc_info()[1])
    actual_course = 113
def get_actuall_course():
    len_usdt = int((len(entry_for_usdt.get())))
    len_jpy = int((len(entry_for_jpy.get())))
    print(len_jpy)
    print(len_usdt)

    if len_usdt != 0 and len_jpy!= 0 or len_usdt == 0 and len_jpy==0:
        pass
    elif len_usdt!= 0 and len_jpy== 0:
        entry_for_jpy.delete(0, 'end')
        swapped =entry_for_jpy.insert(INSERT,float(entry_for_usdt.get())*actual_course)
        swap = entry_for_usdt.get()
        print(swapped)
        print(swap)
        with open('history.txt', 'a') as file:
            file.write(f'User swapped {swap} USDT to {float(entry_for_usdt.get())*actual_course} JPY, actuall course is {actual_course}\n')
    elif len_jpy!= 0 and len_usdt== 0 :
        entry_for_usdt.delete(0, 'end')
        swapped = entry_for_usdt.insert(INSERT, float(entry_for_jpy.get()) / actual_course)
        swap = entry_for_jpy.get()
        print(swapped)
        print(swap)
        with open('history.txt', 'a') as file:
            file.write(
                f'User swapped {swap} JPY to {float(entry_for_usdt.get()) / actual_course} USDT, actuall course is {actual_course}\n')
window = Tk()
window.title("Обменник")
window.geometry('320x80')
window.resizable(width=1, height=1)
usdt = Label(window,text = 'USDT(Доллары)')
usdt.place(relx=.1)
yean = Label(window, text='JPY(Иена)')
yean.place(relx=.6)
entry_for_usdt = Entry(window,width=17)
entry_for_usdt.place(relx=.1,rely=.3)
entry_for_jpy = Entry(window,width=17)
entry_for_jpy.place(relx=.6, rely=.3)
button = Button(window, text="рассчитать",command=get_actuall_course,padx="15",pady="6")
button.pack(side=BOTTOM)
window.mainloop()



