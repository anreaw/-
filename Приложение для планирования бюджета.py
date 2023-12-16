from tkinter import *
from tkinter import messagebox
import sqlite3
import os
import csv


class Base:
    def __init__(self):
        self.connection = sqlite3.connect("budget.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS budget (id INTEGER PRIMARY KEY, data TEXT, price TEXT, name TEXT)")
        self.connection.commit()

    def __del__(self):
        self.connection.close()

    def view(self):
        self.cursor.execute("SELECT * FROM budget")
        rashod_base = self.cursor.fetchall()
        return rashod_base

    def insert(self, data, price, name):
        self.cursor.execute("INSERT INTO budget VALUES (NULL,?,?,?)", (data, price, name))
        self.connection.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM budget WHERE id=?", (id,))
        self.connection.commit()


db = Base()


class Zaimbase:
    def __init__(self):
        self.conn = sqlite3.connect("zaim.db")
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS give (id INTEGER PRIMARY KEY, data TEXT, name TEXT, summa TEXT, com TEXT)")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def view(self):
        self.cur.execute("SELECT * FROM give")
        zaim = self.cur.fetchall()
        return zaim

    def insert(self, data, name, summa, com):
        self.cur.execute("INSERT INTO give VALUES (NULL,?,?,?,?)", (data, name, summa, com,))
        self.conn.commit()

    def update(self, id, data, name, summa, com):
        self.cur.execute("UPDATE give SET data=?, name=?, summa=?, com=? WHERE id=?", (data, name, summa, com, id,))
        self.conn.commit()

    def delete(self, id):
        self.cur.execute("DELETE FROM give WHERE id=?", (id,))
        self.conn.commit()


zb = Zaimbase()


class Window:
    def __init__(self, width, height, title='Копилка', resizable=(False, False)):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+550+130')
        self.root.resizable(resizable[0], resizable[1])
        self.root.config(bg='white')

        self.ostatok = Label(self.root, width=36, height=3, text=('Остаток:' + str(0)),
                             bg='#71C671', font=('Arial', 15))
        self.ostatok.place(x=0, y=0)

        self.all_rashodi = Label(text=('Расходы:' + str(0)), font=('Arial', 14), bg='white')
        self.all_rashodi.place(x=15, y=195)

        self.all_dohodi = Label(text=('Доходы:' + str(0)), font=('Arial', 14), bg='white')
        self.all_dohodi.place(x=200, y=195)

        self.dobavit_rashodi = Label(text='Добавить расходы', bg='white', font=('Arial', 10))
        self.dobavit_rashodi_vvod = Entry()
        self.dobavit_rashodi.place(x=20, y=250)
        self.dobavit_rashodi_vvod.place(x=140, y=250)

        self.add1 = Button(self.root, text='Добавить', command=self.dobavlen_rashod)
        self.add1.place(x=270, y=245)

        self.dobavit_dohodi = Label(text='Добавить доходы', bg='white', font=('Arial', 10))
        self.dobavit_dohodi_vvod = Entry()
        self.dobavit_dohodi.place(x=20, y=280)
        self.dobavit_dohodi_vvod.place(x=140, y=280)

        self.add2 = Button(self.root, text='Добавить', command=self.dobavlen_dohod)
        self.add2.place(x=270, y=275)

        self.supermarket = Label(text='Супермаркеты', bg='white', font=('Arial', 10))
        self.supermarket.place(x=20, y=335)
        self.supermarket_sum = Label(text=0, bg='white', font=('Arial', 10))
        self.supermarket_sum.place(x=280, y=335)

        self.clothes = Label(text='Одежда', bg='white', font=('Arial', 10))
        self.clothes.place(x=20, y=365)
        self.clothes_sum = Label(text=0, bg='white', font=('Arial', 10))
        self.clothes_sum.place(x=280, y=365)

        self.beauty = Label(text='Красота и здоровье', bg='white', font=('Arial', 10))
        self.beauty.place(x=20, y=395)
        self.beauty_sum = Label(text=0, bg='white', font=('Arial', 10))
        self.beauty_sum.place(x=280, y=395)

        self.fun = Label(text='Развлечения и хобби', bg='white', font=('Arial', 10))
        self.fun.place(x=20, y=425)
        self.fun_sum = Label(text=0, bg='white', font=('Arial', 10))
        self.fun_sum.place(x=280, y=425)

        self.child = Label(text='Детские товары', bg='white', font=('Arial', 10))
        self.child.place(x=20, y=455)
        self.child_sum = Label(text=0, bg='white', font=('Arial', 10))
        self.child_sum.place(x=280, y=455)

        self.edu = Label(text='Образование', bg='white', font=('Arial', 10))
        self.edu.place(x=20, y=515)
        self.edu_sum = Label(text=0, bg='white', font=('Arial', 10))
        self.edu_sum.place(x=280, y=515)

        self.cafe = Label(text='Кафе и рестораны', bg='white', font=('Arial', 10))
        self.cafe.place(x=20, y=485)
        self.cafe_sum = Label(text=0, bg='white', font=('Arial', 10))
        self.cafe_sum.place(x=280, y=485)

        self.other = Label(text='Прочее', bg='white', font=('Arial', 10))
        self.other.place(x=20, y=545)
        self.other_sum = Label(text=0, bg='white', font=('Arial', 10))
        self.other_sum.place(x=280, y=545)

        self.story = Button(
            self.root, text='История расходов', width=17, height=2, font=('Arial', 10), command=self.story_window_open)
        self.story.place(x=47, y=140)

        self.zaim = Button(self.root, text='Займы', width=17, height=2, font=('Arial', 10), command=self.zaim_open)
        self.zaim.place(x=47, y=90)

        self.delete_all = Button(
            self.root, text='Обновить', width=17, height=2, font=('Arial', 10), command=self.delete_all)
        self.delete_all.place(x=200, y=90)

        self.change1 = Button(self.root, width=2, text='+', command=self.change1)
        self.change1.place(x=340, y=330)
        self.change2 = Button(self.root, width=2, text='+', command=self.change2)
        self.change2.place(x=340, y=360)
        self.change3 = Button(self.root, width=2, text='+', command=self.change3)
        self.change3.place(x=340, y=390)
        self.change4 = Button(self.root, width=2, text='+', command=self.change4)
        self.change4.place(x=340, y=420)
        self.change5 = Button(self.root, width=2, text='+', command=self.change5)
        self.change5.place(x=340, y=450)
        self.change6 = Button(self.root, width=2, text='+', command=self.change6)
        self.change6.place(x=340, y=480)
        self.change7 = Button(self.root, width=2, text='+', command=self.change7)
        self.change7.place(x=340, y=510)
        self.change8 = Button(self.root, width=2, text='+', command=self.change8)
        self.change8.place(x=340, y=540)

        self.separate = Button(
            self.root, text='Отдельная категория', width=17, height=2, font=('Arial', 10), command=self.separate_open)
        self.separate.place(x=200, y=140)

        self.load()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def load(self):
        if os.path.exists('leave.csv'):
            with open('leave.csv', newline='') as leave:
                reader = list(csv.reader(leave))
                self.ostatok.config(text=(str(",".join(reader[0]))))
                self.all_rashodi.config(text=(str(",".join(reader[2]))))
                self.all_dohodi.config(text=(str(",".join(reader[4]))))
                self.supermarket_sum.config(text=(str(",".join(reader[6]))))
                self.clothes_sum.config(text=(str(",".join(reader[8]))))
                self.beauty_sum.config(text=(str(",".join(reader[10]))))
                self.fun_sum.config(text=(str(",".join(reader[12]))))
                self.child_sum.config(text=(str(",".join(reader[14]))))
                self.edu_sum.config(text=(str(",".join(reader[16]))))
                self.cafe_sum.config(text=(str(",".join(reader[18]))))
                self.other_sum.config(text=(str(",".join(reader[20]))))
                self.supermarket.config(text=(str(",".join(reader[22]))))
                self.clothes.config(text=(str(",".join(reader[24]))))
                self.beauty.config(text=(str(",".join(reader[26]))))
                self.fun.config(text=(str(",".join(reader[28]))))
                self.child.config(text=(str(",".join(reader[30]))))
                self.edu.config(text=(str(",".join(reader[32]))))
                self.cafe.config(text=(str(",".join(reader[34]))))
                self.other.config(text=(str(",".join(reader[36]))))
                self.separate.config(text=(str(",".join(reader[38]))))

    def save(self):
        least = [[str(self.ostatok.cget('text'))],
                 [str(self.all_rashodi.cget('text'))],
                 [str(self.all_dohodi.cget('text'))],
                 [str(self.supermarket_sum.cget('text'))],
                 [str(self.clothes_sum.cget('text'))],
                 [str(self.beauty_sum.cget('text'))],
                 [str(self.fun_sum.cget('text'))],
                 [str(self.child_sum.cget('text'))],
                 [str(self.edu_sum.cget('text'))],
                 [str(self.cafe_sum.cget('text'))],
                 [str(self.other_sum.cget('text'))],
                 [str(self.supermarket.cget('text'))],
                 [str(self.clothes.cget('text'))],
                 [str(self.beauty.cget('text'))],
                 [str(self.fun.cget('text'))],
                 [str(self.child.cget('text'))],
                 [str(self.edu.cget('text'))],
                 [str(self.cafe.cget('text'))],
                 [str(self.other.cget('text'))],
                 [str(self.separate.cget('text'))]]
        with open('leave.csv', 'w') as leave:
            writer = csv.writer(leave)
            writer.writerows(least)

    def last_change(self):
        last_change_r = self.ostatok.cget('text')
        last_change_r = int(last_change_r.strip('Остаток:'))
        return last_change_r

    def dobavlen_rashod(self):
        add_rashod = self.dobavit_rashodi_vvod.get()
        add_rashod = int(add_rashod)
        last = self.last_change()
        new_znach = last - add_rashod
        new_znach = str(new_znach)

        choose_type = Toplevel(self.root)
        choose_type.geometry('350x260+860+410')
        choose_type.title('Категория')

        Label(choose_type, text='Название').place(x=200, y=7)
        name_text = StringVar()
        e2 = Entry(choose_type, textvariable=name_text)
        e2.place(x=200, y=35)
        Label(choose_type, text='Цена').place(x=200, y=63)
        price_text = StringVar()
        e3 = Entry(choose_type, textvariable=price_text)
        e3.place(x=200, y=91)
        Label(choose_type, text='Дата').place(x=200, y=119)
        data_text = StringVar()
        e1 = Entry(choose_type, textvariable=data_text)
        e1.place(x=200, y=147)

        def select_type():
            type = choose_type_var.get()
            if type == 1:
                last_change_supermarket = self.supermarket_sum.cget('text')
                last_change_supermarket = int(last_change_supermarket)
                self.supermarket_sum.config(text=str(last_change_supermarket + add_rashod))
            if type == 2:
                last_change_clothes = self.clothes_sum.cget('text')
                last_change_clothes = int(last_change_clothes)
                self.clothes_sum.config(text=str(last_change_clothes + add_rashod))
            if type == 3:
                last_change_beauty = self.beauty_sum.cget('text')
                last_change_beauty = int(last_change_beauty)
                self.beauty_sum.config(text=str(last_change_beauty + add_rashod))
            if type == 4:
                last_change_fun = self.fun_sum.cget('text')
                last_change_fun = int(last_change_fun)
                self.fun_sum.config(text=str(last_change_fun + add_rashod))
            if type == 5:
                last_change_child = self.child_sum.cget('text')
                last_change_child = int(last_change_child)
                self.child_sum.config(text=str(last_change_child + add_rashod))
            if type == 6:
                last_change_cafe = self.cafe_sum.cget('text')
                last_change_cafe = int(last_change_cafe)
                self.cafe_sum.config(text=str(last_change_cafe + add_rashod))
            if type == 7:
                last_change_edu = self.edu_sum.cget('text')
                last_change_edu = int(last_change_edu)
                self.edu_sum.config(text=str(last_change_edu + add_rashod))
            if type == 8:
                last_change_other = self.other_sum.cget('text')
                last_change_other = int(last_change_other)
                self.other_sum.config(text=str(last_change_other + add_rashod))

        def add_command():
            db.insert(data_text.get(), price_text.get(), name_text.get())

        def the_end_of_rashod():
            self.dobavit_rashodi_vvod.delete(0, 'end')
            self.ostatok.config(text=('Остаток:' + new_znach))
            last_change_r = int(self.all_rashodi.cget('text').strip('Расходы:'))
            self.all_rashodi.config(text=('Расходы:' + str(last_change_r + add_rashod)))
            select_type()
            add_command()
            choose_type.destroy()

        choose_type_var = IntVar()

        choose1 = Radiobutton(choose_type, text='Супермаркеты', font=('Arial', 9), variable=choose_type_var, value=1)
        choose1.place(x=4, y=7)

        choose2 = Radiobutton(choose_type, text='Одежда', font=('Arial', 9), variable=choose_type_var, value=2)
        choose2.place(x=4, y=35)

        choose3 = Radiobutton(choose_type, text='Красота и здоровье', font=('Arial', 9), variable=choose_type_var,
                              value=3)
        choose3.place(x=4, y=63)

        choose4 = Radiobutton(choose_type, text='Развлечения и хобби', font=('Arial', 9), variable=choose_type_var,
                              value=4)
        choose4.place(x=4, y=91)

        choose5 = Radiobutton(choose_type, text='Детские товары', font=('Arial', 9), variable=choose_type_var, value=5)
        choose5.place(x=4, y=119)

        choose6 = Radiobutton(choose_type, text='Кафе и рестораны', font=('Arial', 9), variable=choose_type_var,
                              value=6)
        choose6.place(x=4, y=147)

        choose7 = Radiobutton(choose_type, text='Образование', font=('Arial', 9), variable=choose_type_var, value=7)
        choose7.place(x=4, y=175)

        choose8 = Radiobutton(choose_type, text='Прочее', font=('Arial', 9), variable=choose_type_var, value=8)
        choose8.place(x=4, y=203)

        ok = Button(choose_type, text='Ok', font=('Arial', 9), command=the_end_of_rashod)
        ok.place(x=160, y=231)

        choose_type.mainloop()

    def dobavlen_dohod(self):
        add_dohod = self.dobavit_dohodi_vvod.get()
        add_dohod = int(add_dohod)
        last = self.last_change()
        new_znach = last + add_dohod
        new_znach = str(new_znach)
        self.ostatok.config(text=('Остаток:' + new_znach))
        last_change_r = int(self.all_dohodi.cget('text').strip('Доходы:'))
        self.all_dohodi.config(text=('Доходы:' + str(last_change_r + add_dohod)))
        self.dobavit_dohodi_vvod.delete(0, 'end')

    def separate_open(self):
        separate = Toplevel(self.root)
        separate.geometry('300x280+800+350')

        def ok1():
            self.separate.config(text=(str(name_vvod.get())))
            name_vvod.delete(0, 'end')
            save()

        def limit_f():
            limit = limit_vvod.get()
            limit_znach.config(text=(str(limit)))
            limit_vvod.delete(0, 'end')
            ostalos_znach.config(text=(
                'Осталось:' + str(int(limit_znach.cget('text')) - int(rashodi_znach.cget('text')))))
            save()

        def rashodi_f():
            b = int(add_rashodi.get())
            a = int(rashodi_znach.cget('text'))
            rashodi_znach.config(text=(str(a+b)))
            ostalos_znach.config(text=(
                'Осталось:' + str(int(limit_znach.cget('text')) - int(rashodi_znach.cget('text')))))
            add_rashodi.delete(0, 'end')
            save()

        def delete_all():
            limit_znach.config(text=0)
            ostalos_znach.config(text=('Осталось:' + '0'))
            rashodi_znach.config(text=0)
            self.separate.config(text='Отдельная категория')
            save()

        Label(separate, text='Изменить название категории:', font=('Arial', 10)).place(x=20, y=10)
        name_vvod = Entry(separate)
        name_vvod.place(x=20, y=40)
        Button(separate, text='Ok',  command=ok1).place(x=150, y=35)

        Label(separate, text='Изменить лимит:', font=('Arial', 10)).place(x=20, y=100)
        limit_vvod = Entry(separate)
        limit_vvod.place(x=20, y=130)
        Button(separate, text='Ok', command=limit_f).place(x=150, y=125)

        Label(separate, text='Лимит:', font=('Arial', 10)).place(x=20, y=70)
        limit_znach = Label(separate, text=0, font=('Arial', 10))
        limit_znach.place(x=65, y=70)

        Label(separate, text='Расходы:', font=('Arial', 10)).place(x=20, y=160)
        rashodi_znach = Label(separate, text=0, font=('Arial', 10))
        rashodi_znach.place(x=85, y=160)

        ostalos_znach = Label(separate, text=('Осталось:' + '0'), font=('Arial', 10))
        ostalos_znach.place(x=150, y=70)

        Label(separate, text='Добавить расходы:', font=('Arial', 10)).place(x=20, y=190)
        add_rashodi = Entry(separate)
        add_rashodi.place(x=20, y=220)
        Button(separate, text='Ok', command=rashodi_f).place(x=150, y=215)
        Button(separate, text='Обновить', command=delete_all).place(x=115, y=250)

        def load():
            if os.path.exists('leave1.csv'):
                with open('leave1.csv', newline='') as leave:
                    reader = list(csv.reader(leave))
                    limit_znach.config(text=(str(",".join(reader[0]))))
                    ostalos_znach.config(text=(str(",".join(reader[2]))))
                    rashodi_znach.config(text=(str(",".join(reader[4]))))

        def save():
            least = [[str(limit_znach.cget('text'))],
                     [str(ostalos_znach.cget('text'))],
                     [str(rashodi_znach.cget('text'))]]
            with open('leave1.csv', 'w') as leave:
                writer = csv.writer(leave)
                writer.writerows(least)

        load()
        save()
        separate.mainloop()

    def zaim_open(self):
        zaim = Toplevel(self.root)
        zaim.geometry('550x300+800+400')
        zaim.title('Займы')

        list2 = Listbox(zaim, height=18, width=45)
        list2.grid(row=2, column=0, rowspan=6, columnspan=2)
        sb2 = Scrollbar(zaim)
        sb2.grid(row=2, column=2, rowspan=6)
        Label(zaim, text='Дата', font=('Arial', 10)).place(x=300, y=30)
        data_txt = StringVar()
        data = Entry(zaim, textvariable=data_txt)
        data.place(x=300, y=55)
        Label(zaim, text='Имя', font=('Arial', 10)).place(x=300, y=80)
        name_txt = StringVar()
        name = Entry(zaim, textvariable=name_txt)
        name.place(x=300, y=105)
        Label(zaim, text='Сумма', font=('Arial', 10)).place(x=300, y=130)
        summa_txt = StringVar()
        summa = Entry(zaim, textvariable=summa_txt)
        summa.place(x=300, y=155)
        Label(zaim, text='Комментарий', font=('Arial', 10)).place(x=300, y=180)
        com_txt = StringVar()
        com = Entry(zaim, textvariable=com_txt)
        com.place(x=300, y=205)

        def get_selected_row(event):
            global selected_tuple
            index = list2.curselection()[0]
            selected_tuple = list2.get(index)
            data.delete(0, END)
            data.insert(END, selected_tuple[1])
            name.delete(0, END)
            name.insert(END, selected_tuple[2])
            summa.delete(0, END)
            summa.insert(END, selected_tuple[3])
            com.delete(0, END)
            com.insert(END, selected_tuple[4])

        def view_command():
            list2.delete(0, END)
            for row in zb.view():
                list2.insert(END, row)

        def delete_command():
            zb.delete(selected_tuple[0])
            data.delete(0, 'end')
            name.delete(0, 'end')
            summa.delete(0, 'end')
            com.delete(0, 'end')
            view_command()

        def update_command():
            zb.update(selected_tuple[0], data_txt.get(), name_txt.get(), summa_txt.get(), com_txt.get())
            data.delete(0, 'end')
            name.delete(0, 'end')
            summa.delete(0, 'end')
            com.delete(0, 'end')
            view_command()

        def add_command():
            zb.insert(data_txt.get(), name_txt.get(), summa_txt.get(), com_txt.get())
            data.delete(0, 'end')
            name.delete(0, 'end')
            summa.delete(0, 'end')
            com.delete(0, 'end')
            view_command()

        list2.bind('<<ListboxSelect>>', get_selected_row)

        Button(zaim, text='Добавить', command=add_command).place(x=450, y=80)
        Button(zaim, text='Удалить', command=delete_command).place(x=450, y=180)
        Button(zaim, text='Обновить', command=update_command).place(x=450, y=130)

        view_command()
        zaim.mainloop()

    def story_window_open(self):
        story = Toplevel(self.root)
        story.geometry('500x400+700+300')
        story.title('История')

        list1 = Listbox(story, height=25, width=65)
        list1.grid(row=2, column=0, rowspan=6, columnspan=2)
        sb1 = Scrollbar(story)
        sb1.grid(row=2, column=2, rowspan=6)
        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)

        def get_selected_row(event):
            global selected_tuple
            index = list1.curselection()[0]
            selected_tuple = list1.get(index)

        def view_command():
            list1.delete(0, END)
            for row in db.view():
                list1.insert(END, row)

        def delete_command():
            db.delete(selected_tuple[0])
            view_command()

        list1.bind('<<ListboxSelect>>', get_selected_row)

        Button(story, text='Удалить', command=delete_command).place(x=420, y=190)

        view_command()
        story.mainloop()

    def delete_all(self):
        self.all_rashodi.config(text=('Расходы:' + str(0)))
        self.all_dohodi.config(text=('Доходы:' + str(0)))
        self.supermarket_sum.config(text=0)
        self.clothes_sum.config(text=0)
        self.beauty_sum.config(text=0)
        self.fun_sum.config(text=0)
        self.child_sum.config(text=0)
        self.edu_sum.config(text=0)
        self.cafe_sum.config(text=0)
        self.other_sum.config(text=0)

    def change1(self):
        change1 = Toplevel(self.root)
        change1.geometry('270x180+800+400')
        change1.title('Информация')

        def apply():
            a = str(change_name.get())
            if a.islower():
                a = a.title()
            self.supermarket.config(text=a)
            change_name.delete(0, 'end')

        Label(change1, text='Поменять название категории:', font=('Arial', 10)).place(x=20, y=10)
        change_name = Entry(change1)
        change_name.place(x=20, y=45)
        Button(change1, text='Ok', command=apply).place(x=150, y=40)

        Label(change1, text='Изменить лимит:', font=('Arial', 10)).place(x=20, y=100)
        limit_vvod = Entry(change1)
        limit_vvod.place(x=20, y=135)

        def limit_d():
            limit = limit_vvod.get()
            a = int(limit)
            b = int(lim_get)
            ostalos_znach.config(text=('Остаток:' + (str(a - b))))
            limit_znach.config(text=limit)
            limit_vvod.delete(0, 'end')
            save()

        Label(change1, text='Лимит:', font=('Arial', 10)).place(x=20, y=70)
        lim_get = str(window.supermarket_sum.cget('text'))
        limit_znach = Label(change1, text='0', font=('Arial', 10))
        limit_znach.place(x=65, y=70)
        ostalos_znach = Label(change1, text=('Осталось:' + '0'), font=('Arial', 10))
        ostalos_znach.place(x=150, y=70)
        Button(change1, text='Ok', command=limit_d).place(x=150, y=130)

        def openning():
            limit = limit_znach.cget('text')
            a = int(limit)
            b = int(lim_get)
            ostalos_znach.config(text=('Остаток:' + (str(a - b))))

        def load():
            if os.path.exists('leave2.csv'):
                with open('leave2.csv', newline='') as leave:
                    reader = list(csv.reader(leave))
                    limit_znach.config(text=(str(",".join(reader[0]))))

        def save():
            least = [[str(limit_znach.cget('text'))]]
            with open('leave2.csv', 'w') as leave:
                writer = csv.writer(leave)
                writer.writerows(least)
        load()
        openning()

    def change2(self):
        change2 = Toplevel(self.root)
        change2.geometry('270x180+800+400')
        change2.title('Информация')

        def apply():
            a = str(change_name.get())
            if a.islower():
                a = a.title()
            self.clothes.config(text=a)
            change_name.delete(0, 'end')

        Label(change2, text='Поменять название категории:', font=('Arial', 10)).place(x=20, y=10)
        change_name = Entry(change2)
        change_name.place(x=20, y=45)
        Button(change2, text='Ok', command=apply).place(x=150, y=40)

        Label(change2, text='Изменить лимит:', font=('Arial', 10)).place(x=20, y=100)
        limit_vvod = Entry(change2)
        limit_vvod.place(x=20, y=135)

        def limit_d():
            limit = limit_vvod.get()
            a = int(limit)
            b = int(lim_get)
            ostalos_znach.config(text=('Остаток:' + (str(a - b))))
            limit_znach.config(text=limit)
            save()
            limit_vvod.delete(0, 'end')

        Label(change2, text='Лимит:', font=('Arial', 10)).place(x=20, y=70)
        lim_get = str(window.clothes_sum.cget('text'))
        limit_znach = Label(change2, text='0', font=('Arial', 10))
        limit_znach.place(x=65, y=70)
        ostalos_znach = Label(change2, text=('Осталось:' + '0'), font=('Arial', 10))
        ostalos_znach.place(x=150, y=70)
        Button(change2, text='Ok', command=limit_d).place(x=150, y=130)

        def openning():
            limit = limit_znach.cget('text')
            a = int(limit)
            b = int(lim_get)
            ostalos_znach.config(text=('Остаток:' + (str(a - b))))

        def load():
            if os.path.exists('leave3.csv'):
                with open('leave3.csv', newline='') as leave:
                    reader = list(csv.reader(leave))
                    limit_znach.config(text=(str(",".join(reader[0]))))

        def save():
            least = [[str(limit_znach.cget('text'))]]
            with open('leave3.csv', 'w') as leave:
                writer = csv.writer(leave)
                writer.writerows(least)
        load()
        openning()

    def change3(self):
        change3 = Toplevel(self.root)
        change3.geometry('270x180+800+400')
        change3.title('Информация')

        def apply():
            a = str(change_name.get())
            if a.islower():
                a = a.title()
            self.beauty.config(text=a)
            change_name.delete(0, 'end')

        Label(change3, text='Поменять название категории:', font=('Arial', 10)).place(x=20, y=10)
        change_name = Entry(change3)
        change_name.place(x=20, y=45)
        Button(change3, text='Ok', command=apply).place(x=150, y=40)

        Label(change3, text='Изменить лимит:', font=('Arial', 10)).place(x=20, y=100)
        limit_vvod = Entry(change3)
        limit_vvod.place(x=20, y=135)

        def limit_d():
            limit = limit_vvod.get()
            a = int(limit)
            b = int(lim_get)
            ostalos_znach.config(text=('Остаток:' + (str(a - b))))
            limit_znach.config(text=limit)
            save()
            limit_vvod.delete(0, 'end')

        Label(change3, text='Лимит:', font=('Arial', 10)).place(x=20, y=70)
        lim_get = str(window.beauty_sum.cget('text'))
        limit_znach = Label(change3, text='0', font=('Arial', 10))
        limit_znach.place(x=65, y=70)
        ostalos_znach = Label(change3, text=('Осталось:' + '0'), font=('Arial', 10))
        ostalos_znach.place(x=150, y=70)
        Button(change3, text='Ok', command=limit_d).place(x=150, y=130)

        def openning():
            limit = limit_znach.cget('text')
            a = int(limit)
            b = int(lim_get)
            ostalos_znach.config(text=('Остаток:' + (str(a - b))))

        def load():
            if os.path.exists('leave4.csv'):
                with open('leave4.csv', newline='') as leave:
                    reader = list(csv.reader(leave))
                    limit_znach.config(text=(str(",".join(reader[0]))))

        def save():
            least = [[str(limit_znach.cget('text'))]]
            with open('leave4.csv', 'w') as leave:
                writer = csv.writer(leave)
                writer.writerows(least)
        load()
        openning()

    def change4(self):
        change4 = Toplevel(self.root)
        change4.geometry('270x180+800+400')
        change4.title('Информация')

        def apply():
            a = str(change_name.get())
            if a.islower():
                a = a.title()
            self.fun.config(text=a)
            change_name.delete(0, 'end')

        Label(change4, text='Поменять название категории:', font=('Arial', 10)).place(x=20, y=10)
        change_name = Entry(change4)
        change_name.place(x=20, y=45)
        Button(change4, text='Ok', command=apply).place(x=150, y=40)

        Label(change4, text='Изменить лимит:', font=('Arial', 10)).place(x=20, y=100)
        limit_vvod = Entry(change4)
        limit_vvod.place(x=20, y=135)

        def limit_d():
            limit = limit_vvod.get()
            a = int(limit)
            b = int(lim_get)
            ostalos_znach.config(text=('Остаток:' + (str(a - b))))
            limit_znach.config(text=limit)
            save()
            limit_vvod.delete(0, 'end')

        Label(change4, text='Лимит:', font=('Arial', 10)).place(x=20, y=70)
        lim_get = str(window.fun_sum.cget('text'))
        limit_znach = Label(change4, text='0', font=('Arial', 10))
        limit_znach.place(x=65, y=70)
        ostalos_znach = Label(change4, text=('Осталось:' + '0'), font=('Arial', 10))
        ostalos_znach.place(x=150, y=70)
        Button(change4, text='Ok', command=limit_d).place(x=150, y=130)

        def openning():
            limit = limit_znach.cget('text')
            a = int(limit)
            b = int(lim_get)
            ostalos_znach.config(text=('Остаток:' + (str(a - b))))

        def load():
            if os.path.exists('leave5.csv'):
                with open('leave5.csv', newline='') as leave:
                    reader = list(csv.reader(leave))
                    limit_znach.config(text=(str(",".join(reader[0]))))

        def save():
            least = [[str(limit_znach.cget('text'))]]
            with open('leave5.csv', 'w') as leave:
                writer = csv.writer(leave)
                writer.writerows(least)
        load()
        openning()

    def change5(self):
        change5 = Toplevel(self.root)
        change5.geometry('270x180+800+400')
        change5.title('Информация')

        def apply():
            a = str(change_name.get())
            if a.islower():
                a = a.title()
            self.child.config(text=a)
            change_name.delete(0, 'end')

        Label(change5, text='Поменять название категории:', font=('Arial', 10)).place(x=20, y=10)
        change_name = Entry(change5)
        change_name.place(x=20, y=45)
        Button(change5, text='Ok', command=apply).place(x=150, y=40)

        Label(change5, text='Изменить лимит:', font=('Arial', 10)).place(x=20, y=100)
        limit_vvod = Entry(change5)
        limit_vvod.place(x=20, y=135)

        def limit_d():
            limit = limit_vvod.get()
            a = int(limit)
            b = int(lim_get)
            ostalos_znach.config(text=('Остаток:' + (str(a - b))))
            limit_znach.config(text=limit)
            save()
            limit_vvod.delete(0, 'end')

        Label(change5, text='Лимит:', font=('Arial', 10)).place(x=20, y=70)
        lim_get = str(window.child_sum.cget('text'))
        limit_znach = Label(change5, text='0', font=('Arial', 10))
        limit_znach.place(x=65, y=70)
        ostalos_znach = Label(change5, text=('Осталось:' + '0'), font=('Arial', 10))
        ostalos_znach.place(x=150, y=70)
        Button(change5, text='Ok', command=limit_d).place(x=150, y=130)

        def openning():
            limit = limit_znach.cget('text')
            a = int(limit)
            b = int(lim_get)
            ostalos_znach.config(text=('Остаток:' + (str(a - b))))

        def load():
            if os.path.exists('leave6.csv'):
                with open('leave6.csv', newline='') as leave:
                    reader = list(csv.reader(leave))
                    limit_znach.config(text=(str(",".join(reader[0]))))

        def save():
            least = [[str(limit_znach.cget('text'))]]
            with open('leave6.csv', 'w') as leave:
                writer = csv.writer(leave)
                writer.writerows(least)
        load()
        openning()

    def change6(self):
        change6 = Toplevel(self.root)
        change6.geometry('270x180+800+400')
        change6.title('Информация')

        def apply():
            a = str(change_name.get())
            if a.islower():
                a = a.title()
            self.edu.config(text=a)
            change_name.delete(0, 'end')

        Label(change6, text='Поменять название категории:', font=('Arial', 10)).place(x=20, y=10)
        change_name = Entry(change6)
        change_name.place(x=20, y=45)
        Button(change6, text='Ok', command=apply).place(x=150, y=40)

        Label(change6, text='Изменить лимит:', font=('Arial', 10)).place(x=20, y=100)
        limit_vvod = Entry(change6)
        limit_vvod.place(x=20, y=135)

        def limit_d():
            limit = limit_vvod.get()
            a = int(limit)
            b = int(lim_get)
            ostalos_znach.config(text=('Остаток:' + (str(a - b))))
            limit_znach.config(text=limit)
            save()
            limit_vvod.delete(0, 'end')

        Label(change6, text='Лимит:', font=('Arial', 10)).place(x=20, y=70)
        lim_get = str(window.edu_sum.cget('text'))
        limit_znach = Label(change6, text='0', font=('Arial', 10))
        limit_znach.place(x=65, y=70)
        ostalos_znach = Label(change6, text=('Осталось:' + '0'), font=('Arial', 10))
        ostalos_znach.place(x=150, y=70)
        Button(change6, text='Ok', command=limit_d).place(x=150, y=130)

        def openning():
            limit = limit_znach.cget('text')
            a = int(limit)
            b = int(lim_get)
            ostalos_znach.config(text=('Остаток:' + (str(a - b))))

        def load():
            if os.path.exists('leave7.csv'):
                with open('leave7.csv', newline='') as leave:
                    reader = list(csv.reader(leave))
                    limit_znach.config(text=(str(",".join(reader[0]))))

        def save():
            least = [[str(limit_znach.cget('text'))]]
            with open('leave7.csv', 'w') as leave:
                writer = csv.writer(leave)
                writer.writerows(least)
        load()
        openning()

    def change7(self):
        change7 = Toplevel(self.root)
        change7.geometry('270x180+800+400')
        change7.title('Информация')

        def apply():
            a = str(change_name.get())
            if a.islower():
                a = a.title()
            self.cafe.config(text=a)
            change_name.delete(0, 'end')

        Label(change7, text='Поменять название категории:', font=('Arial', 10)).place(x=20, y=10)
        change_name = Entry(change7)
        change_name.place(x=20, y=45)
        Button(change7, text='Ok', command=apply).place(x=150, y=40)

        Label(change7, text='Изменить лимит:', font=('Arial', 10)).place(x=20, y=100)
        limit_vvod = Entry(change7)
        limit_vvod.place(x=20, y=135)

        def limit_d():
            limit = limit_vvod.get()
            a = int(limit)
            b = int(lim_get)
            ostalos_znach.config(text=('Остаток:' + (str(a - b))))
            limit_znach.config(text=limit)
            save()
            limit_vvod.delete(0, 'end')

        Label(change7, text='Лимит:', font=('Arial', 10)).place(x=20, y=70)
        lim_get = str(window.cafe_sum.cget('text'))
        limit_znach = Label(change7, text='0', font=('Arial', 10))
        limit_znach.place(x=65, y=70)
        ostalos_znach = Label(change7, text=('Осталось:' + '0'), font=('Arial', 10))
        ostalos_znach.place(x=150, y=70)
        Button(change7, text='Ok', command=limit_d).place(x=150, y=130)

        def openning():
            limit = limit_znach.cget('text')
            a = int(limit)
            b = int(lim_get)
            ostalos_znach.config(text=('Остаток:' + (str(a - b))))

        def load():
            if os.path.exists('leave8.csv'):
                with open('leave8.csv', newline='') as leave:
                    reader = list(csv.reader(leave))
                    limit_znach.config(text=(str(",".join(reader[0]))))

        def save():
            least = [[str(limit_znach.cget('text'))]]
            with open('leave8.csv', 'w') as leave:
                writer = csv.writer(leave)
                writer.writerows(least)
        load()
        openning()

    def change8(self):
        change8 = Toplevel(self.root)
        change8.geometry('270x180+800+400')
        change8.title('Информация')

        def apply():
            a = str(change_name.get())
            if a.islower():
                a = a.title()
            self.other.config(text=a)
            change_name.delete(0, 'end')

        Label(change8, text='Поменять название категории:', font=('Arial', 10)).place(x=20, y=10)
        change_name = Entry(change8)
        change_name.place(x=20, y=45)
        Button(change8, text='Ok', command=apply).place(x=150, y=40)

        Label(change8, text='Изменить лимит:', font=('Arial', 10)).place(x=20, y=100)
        limit_vvod = Entry(change8)
        limit_vvod.place(x=20, y=135)

        def limit_d():
            limit = limit_vvod.get()
            a = int(limit)
            b = int(lim_get)
            ostalos_znach.config(text=('Остаток:' + (str(a - b))))
            limit_znach.config(text=limit)
            save()
            limit_vvod.delete(0, 'end')

        Label(change8, text='Лимит:', font=('Arial', 10)).place(x=20, y=70)
        lim_get = str(window.other_sum.cget('text'))
        limit_znach = Label(change8, text='0', font=('Arial', 10))
        limit_znach.place(x=65, y=70)
        ostalos_znach = Label(change8, text=('Осталось:' + '0'), font=('Arial', 10))
        ostalos_znach.place(x=150, y=70)
        Button(change8, text='Ok', command=limit_d).place(x=150, y=130)

        def openning():
            limit = limit_znach.cget('text')
            a = int(limit)
            b = int(lim_get)
            ostalos_znach.config(text=('Остаток:' + (str(a - b))))

        def load():
            if os.path.exists('leave9.csv'):
                with open('leave9.csv', newline='') as leave:
                    reader = list(csv.reader(leave))
                    limit_znach.config(text=(str(",".join(reader[0]))))

        def save():
            least = [[str(limit_znach.cget('text'))]]
            with open('leave9.csv', 'w') as leave:
                writer = csv.writer(leave)
                writer.writerows(least)
        load()
        openning()

    def create_beginning(self, width, height, title='Начало работы', resizable=(False, False)):
        Beginning(self.root, width, height, title, resizable)

    def run(self):
        self.root.mainloop()

    def on_closing(self):
        if messagebox.askokcancel("", "Закрыть программу?"):
            self.save()
            self.root.destroy()


class Beginning:
    def __init__(self, parent, width, height, title='Начало работы', resizable=(False, False)):
        self.root = Toplevel(parent)
        self.window = Window
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+600+300')
        self.root.resizable(resizable[0], resizable[1])
        self.grab_focus()
        self.label_beginning = Label(self.root, text='Пожалуйста, укажите остаток средств на счёте.',
                                     font=('Arial', 10))
        self.label_beginning.place(x=3, y=5)
        self.entry_vvod = Entry(self.root)
        self.entry_vvod.place(x=89, y=35)
        self.button_ok = Button(self.root, text='Ok', font=('Arial', 10), command=self.beginning_ok)
        self.button_ok.place(x=132, y=60)

    def beginning_ok(self):
        data = self.entry_vvod.get()
        window.ostatok.config(text=('Остаток:' + data))
        self.root.destroy()

    def grab_focus(self):
        self.root.grab_set()


if __name__ == '__main__':
    window = Window(400, 600, 'Копилка')
    if (
            window.last_change() == 0 and int(window.supermarket_sum.cget('text')) == 0
            and int(window.clothes_sum.cget('text')) == 0 and int(window.beauty_sum.cget('text')) == 0
            and int(window.fun_sum.cget('text')) == 0 and int(window.child_sum.cget('text')) == 0
            and int(window.cafe_sum.cget('text')) == 0 and int(window.edu_sum.cget('text')) == 0
            and int(window.other_sum.cget('text')) == 0):
        window.create_beginning(300, 100, 'Начало')
    window.run()
