from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
from tkinter import messagebox
import sys

def main():
    win = Tk()
    app = GirişSayfasi(win)
    win.mainloop()

class GirişSayfasi:
    def __init__(self, win):
        self.win = win
        self.win.geometry("1350x750+0+0")
        self.win.title("Restoran Yönetim Sistemi")

        self.title_label = Label(self.win, text="Restoran Yönetim Sistemi", font=('Arial', 35, 'bold'), bg="lightgrey", bd=8, relief=GROOVE)
        self.title_label.pack(side=TOP, fill=X)  # fill=X olarak düzelttim

        self.main_frame = Frame(self.win, bg="lightgrey", bd=6, relief=GROOVE)
        self.main_frame.place(x=300, y=150, width=800, height=450)

        self.login_lbl = Label(self.main_frame, text="Giriş", bd=6, relief=GROOVE, anchor=CENTER, bg="lightgrey", font=('sans-serif', 25, 'bold'))
        self.login_lbl.pack(side=TOP, fill=X)

        self.entry_frame = LabelFrame(self.main_frame, text="Detayları Giriniz", bd=6, relief=GROOVE, bg="lightgrey", font=('sans-serif', 18))
        self.entry_frame.pack(fill=BOTH, expand=TRUE)

        self.entus_lbl = Label(self.entry_frame, text="Kullanıcı Adı Giriiniz: ", bg="lightgrey", font=('sans-serif', 15))
        self.entus_lbl.grid(row=0, column=0, padx=2, pady=2)

        username = StringVar()
        password = StringVar()

        self.entus_ent = Entry(self.entry_frame,font=('sans-serif',15),bd=6, textvariable=username)
        self.entus_ent.grid(row=0,column=1,padx=2,pady=2)


        self.enpass_lbl=Label(self.entry_frame, text="Şifre Giriniz:",  bg="lightgrey", font=('sans-serif', 15))
        self.enpass_lbl.grid(row=1, column=0, padx=2, pady=2)

        self.entpass_ent=Entry(self.entry_frame,font=('sans-serif',15),bd=6, textvariable=password,show="*")
        self.entpass_ent.grid(row=1,column=1,padx=2,pady=2)

        def check_login():
            ''' Bu fonksiyon girişi kontrol edecek'''
            if username.get() == "kasa" and password.get() == "1234":
                self.billing_btn.config(state="normal")
            else:
                pass

        def reset():
            username.set("")
            password.set("")

        def billing_sect():
            self.newWindow = Toplevel(self.win)
            self.app = Window2(self.newWindow)


        self.button_frame =LabelFrame(self.entry_frame,text="Seçenekler",font=('Arial',15),bg="lightgrey",bd=7,relief=GROOVE)
        self.button_frame.place(x=20,y=100,width=730,height=85)

        self.login_btn= Button(self.button_frame,text="Giriş",font=('Arial',12),bd=5,width=15,command=check_login)
        self.login_btn.grid(row=0,column=0,padx=20,pady=2)

        self.billing_btn= Button(self.button_frame,text="Menü",font=('Arial',12),bd=5,width=15,command=billing_sect)
        self.billing_btn.grid(row=0,column=1,padx=20,pady=2)
        self.billing_btn.config(state="disabled")

        self.reset_btn = Button(self.button_frame,text="Reset",font=('Arial',12),bd=5,width=15,command=reset)
        self.reset_btn.grid(row=0,column=2,padx=20,pady=2)


class Window2:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1300x750+0+0")
        self.win.title("Restoran Yönetim Sistemi")

        self.title_label = Label(self.win, text="Restoran Yönetim Sistemi", font=('Arial', 35, 'bold'), bg="lightgrey", bd=8, relief=GROOVE)
        self.title_label.pack(side=TOP, fill=X)  # fill=X olarak düzelttim

        self.win.resizable(0,0)

        bill_no = random.randint(100,9999)
        bill_no_tk = IntVar()
        bill_no_tk.set(bill_no)

        hesaplama_var = StringVar()

        musteri_no = StringVar()
        garson_no = StringVar()
        tarih_pr = StringVar()
        siparis = StringVar()
        siparis_adet = StringVar()
        adet_fiyat = StringVar()

        tarih_pr.set(datetime.now())

        total_list =[]
        self.grd_total = 0


        self.entry_frame = LabelFrame(self.win,text = "Detayları Giriniz", background="lightgrey",font=('Arial',20),bd=7,relief=GROOVE)
        self.entry_frame.place(x=20,y=95,width=500,height=650)

        self.bill_no_lbl = Label(self.entry_frame,text="Fiş Numarası",font=('Arial,15'),bg="lightgrey")
        self.bill_no_lbl.grid(row=0,column=0,padx=2,pady=2)

        self.bill_no_ent = Entry(self.entry_frame,bd=5,font=('Arial',15),textvariable=bill_no_tk)
        self.bill_no_ent.grid(row=0,column=1,padx=2,pady=2)
        self.bill_no_ent.config(state="disabled")

        self.musteri_no_lbl = Label(self.entry_frame,text="Müşteri Numarası",font=('Arial,15'),bg="lightgrey")
        self.musteri_no_lbl.grid(row=1,column=0,padx=2,pady=2)

        self.musteri_no_ent = Entry(self.entry_frame,bd=5,textvariable=musteri_no,font=('Arial',15))
        self.musteri_no_ent.grid(row=1,column=1,padx=2,pady=2)

        self.garson_no_lbl = Label(self.entry_frame,text="Garson Numarası",font=('Arial,15'),bg="lightgrey")
        self.garson_no_lbl.grid(row=2,column=0,padx=2,pady=2)

        self.garson_no_ent = Entry(self.entry_frame,bd=5,textvariable=garson_no,font=('Arial',15))
        self.garson_no_ent.grid(row=2,column=1,padx=2,pady=2)

        self.tarih_lbl = Label(self.entry_frame,text="Tarih",font=('Arial,15'),bg="lightgrey")
        self.tarih_lbl.grid(row=3,column=0,padx=2,pady=2)

        self.tarih_ent = Entry(self.entry_frame,bd=5,textvariable=tarih_pr,font=('Arial',15))
        self.tarih_ent.grid(row=3,column=1,padx=2,pady=2)

        self.siparis_lbl = Label(self.entry_frame,text="Siparişler",font=('Arial,15'),bg="lightgrey")
        self.siparis_lbl.grid(row=4,column=0,padx=2,pady=2)

        self.siparis_ent = Entry(self.entry_frame,bd=5,textvariable=siparis,font=('Arial',15))
        self.siparis_ent.grid(row=4,column=1,padx=2,pady=2)

        self.siparis_adet_lbl = Label(self.entry_frame,text="Sipariş Adedi",font=('Arial,15'),bg="lightgrey")
        self.siparis_adet_lbl.grid(row=5,column=0,padx=2,pady=2)

        self.siparis_adet_ent = Entry(self.entry_frame,bd=5,textvariable=siparis_adet,font=('Arial',15))
        self.siparis_adet_ent.grid(row=5,column=1,padx=2,pady=2)

        self.adet_fiyat_lbl = Label(self.entry_frame,text="Adet Fiyatı",font=('Arial,15'),bg="lightgrey")
        self.adet_fiyat_lbl.grid(row=6,column=0,padx=2,pady=2)

        self.adet_fiyat_ent = Entry(self.entry_frame,bd=5,textvariable=adet_fiyat,font=('Arial',15))
        self.adet_fiyat_ent.grid(row=6,column=1,padx=2,pady=2)

        def default_bill():
            self.bill_txt.insert(END,"\t\t\t\tEGEMYO RESTORANT")
            self.bill_txt.insert(END,"\n\t\t\t9. Sokak, Kazım Dirik Mahallesi,Bornova")
            self.bill_txt.insert(END,"\n\t\t\t\tİletişim = +0232 023 2203")
            self.bill_txt.insert(END,"\n============================================================================")
            self.bill_txt.insert(END, f"\nFiş Numarası: {bill_no_tk.get()}")

        def genbill():
            if musteri_no.get() == "" or (garson_no.get() == ""):
                messagebox.showerror("Hata", "Lütfen tüm boşlukları doğru şekilde doldurunuz.", parent=self.win)
            else:
                self.bill_txt.insert(END,f"\nMüşteri Numarası: {musteri_no.get()}")
                self.bill_txt.insert(END, f"\nGarson Numarası: {garson_no.get()}")
                self.bill_txt.insert(END, f"\nTarih: {tarih_pr.get()}")
                self.bill_txt.insert(END,"\n============================================================================")
                self.bill_txt.insert(END, "\nÜrün Adı\t\t       Miktar\t\t       Adet Fiyatı\t\t      Total")
                self.bill_txt.insert(END,"\n============================================================================")

                self.ekle_btn.config(state="normal")
                self.total_btn.config(state="normal")

        def ekle_func():
            if siparis.get() == "" or siparis_adet.get() == "":
                messagebox.showerror("Hata!", "Lütfen tüm boşlukları doğru şekilde doldurunuz." ,parent=self.win)
            else:
                adet = int(siparis_adet.get())
                fiyatlar = int(adet_fiyat.get())
                total = adet * fiyatlar
                total_list.append(total)
                self.bill_txt.insert(END,f"\n{siparis.get()}\t\t       {siparis_adet.get()}\t\t     TL.  {adet_fiyat.get()}\t\t     TL. {total}")


        def total_func():
            for item in total_list:
                self.grd_total = self.grd_total + siparis
            self.bill_txt.insert(END,"\n============================================================================")
            self.bill_txt.insert(END,"\t\t\t\t\tToplam Ücret : {self.grd_total}")
            self.bill_txt.insert(END,"\n============================================================================")
            self.kaydet_btn.config(state="normal")

        def clear_func():
            musteri_no.set("")
            garson_no.set("")
            siparis.set("")
            siparis_adet.set("")
            adet_fiyat.set("")

        def reset_func():
            total_list.clear()
            self.grd_total = 0
            self.ekle_btn.config(state="disabled")
            self.total_btn.config(state="disabled")
            self.kaydet_btn.config(state="disabled")
            self.bill_txt.delete("1.0",END)
            default_bill()

    
        def kaydet_func():
            kullanici_tercihi = messagebox.askyesno("Onaylayınız.", f"Fişi kaydetmek ister misiniz {bill_no_tk.get()}", parent = self.win)
            if kullanici_tercihi > 0:
                self.fis_icerigi = self.bill_txt.get("1.0",END)
                try:
                    con = open(f"{sys.path[0]}/fişler/"+str(bill_no_tk.get())+".txt","w")
                except Exception as  e:
                    messagebox.showerror("Hata!", f"{e} Nedeniyle hata", parent= self.win)
                con.write(self.fis_icerigi)
                con.close()
                messagebox.showinfo("Başarılı!", f"Fiş {bill_no_tk.get()} başarıyla kaydedildi.", parent=self.win)
            else:
                return
            


        self.button_frame = LabelFrame(self.entry_frame,bd=5,text="Seçenekler",bg="lightgrey",font=('Arial',25))
        self.button_frame.place(x=20,y=300,width=392,height=300)

        self.ekle_btn = Button(self.button_frame,bd=3,text="Ekle",font=('Arial',12),width=12,height=3, command= ekle_func)
        self.ekle_btn.grid(row=0,column=0,padx=4,pady=2)

        self.generate_btn = Button(self.button_frame,bd=3,text="Generate",font=('Arial',12),width=12,height=3,command=genbill)
        self.generate_btn.grid(row=0,column=1,padx=4,pady=2)

        self.temizle_btn = Button(self.button_frame,bd=3,text="Temizle",font=('Arial',12),width=12,height=3,command=clear_func)
        self.temizle_btn.grid(row=0,column=2,padx=4,pady=2)

        self.total_btn = Button(self.button_frame,bd=3,text="Total",font=('Arial',12),width=12,height=3, command=total_func)
        self.total_btn.grid(row=1,column=0,padx=4,pady=2)

        self.reset_btn = Button(self.button_frame,bd=3,text="Reset",font=('Arial',12),width=12,height=3, command= reset_func)
        self.reset_btn.grid(row=1,column=1,padx=4,pady=2)

        self.kaydet_btn =  Button(self.button_frame,bd=3,text="Kaydet",font=('Arial',12),width=12,height=3, command= kaydet_func)
        self.kaydet_btn.grid(row=1,column=2,padx=4,pady=2)

        self.hesaplama_frame = Frame(self.win, bd=8, background= "lightgrey",relief=GROOVE)
        self.hesaplama_frame.place(x=585,y=110,width=656,height=295)

        self.num_ent = Entry(self.hesaplama_frame,bd=15,background="lightgrey",textvariable=hesaplama_var,font=('Arial',15),width=54,justify='right')
        self.num_ent.grid(row=0,column=0,columnspan=11)

        def press_btn(event):
            text = event.widget.cget("text")
            if text == "=":
                if hesaplama_var.get().isdigit():
                    value = int(hesaplama_var.get())
                else:
                    try:
                        value = eval(self.num_ent.get())
                    except:
                        print("Hata")
                hesaplama_var.set(value)
                self.num_ent.update()
            elif text == "C":
                pass
            else:
                hesaplama_var.set(hesaplama_var.get() + text)
                self.num_ent.update()


        self.btn7 = Button(self.hesaplama_frame,bg="lightgrey",text="7",bd=8,width=12,height=1,font=('Arial',15))
        self.btn7.grid(row=1,column=0,padx=2,pady=2)
        self.btn7.bind("<Button-1>", press_btn)

        self.btn8 = Button(self.hesaplama_frame,bg="lightgrey",text="8",bd=8,width=12,height=1,font=('Arial',15))
        self.btn8.grid(row=1,column=1,padx=2,pady=2)
        self.btn8.bind("<Button-1>", press_btn)

        self.btn9 = Button(self.hesaplama_frame,bg="lightgrey",text="9",bd=8,width=12,height=1,font=('Arial',15))
        self.btn9.grid(row=1,column=2,padx=2,pady=2)
        self.btn9.bind("<Button-1>", press_btn)

        self.btnekle = Button(self.hesaplama_frame,bg="lightgrey",text="+",bd=8,width=12,height=1,font=('Arial',15))
        self.btnekle.grid(row=1,column=3,padx=2,pady=2)
        self.btnekle.bind("<Button-1>", press_btn)

        self.btn4 = Button(self.hesaplama_frame,bg="lightgrey",text="4",bd=8,width=12,height=1,font=('Arial',15))
        self.btn4.grid(row=2,column=0,padx=2,pady=2)
        self.btn4.bind("<Button-1>", press_btn)

        self.btn5 = Button(self.hesaplama_frame,bg="lightgrey",text="5",bd=8,width=12,height=1,font=('Arial',15))
        self.btn5.grid(row=2,column=1,padx=2,pady=2)
        self.btn5.bind("<Button-1>", press_btn)

        self.btn6 = Button(self.hesaplama_frame,bg="lightgrey",text="6",bd=8,width=12,height=1,font=('Arial',15))
        self.btn6.grid(row=2,column=2,padx=2,pady=2)
        self.btn6.bind("<Button-1>", press_btn)

        self.btncikart = Button(self.hesaplama_frame,bg="lightgrey",text="-",bd=8,width=12,height=1,font=('Arial',15))
        self.btncikart.grid(row=2,column=3,padx=2,pady=2)
        self.btncikart.bind("<Button-1>", press_btn)

        self.btn1 = Button(self.hesaplama_frame,bg="lightgrey",text="1",bd=8,width=12,height=1,font=('Arial',15))
        self.btn1.grid(row=3,column=0,padx=2,pady=2)
        self.btn1.bind("<Button-1>", press_btn)

        self.btn2 = Button(self.hesaplama_frame,bg="lightgrey",text="2",bd=8,width=12,height=1,font=('Arial',15))
        self.btn2.grid(row=3,column=1,padx=2,pady=2)
        self.btn2.bind("<Button-1>", press_btn)

        self.btn3 = Button(self.hesaplama_frame,bg="lightgrey",text="3",bd=8,width=12,height=1,font=('Arial',15))
        self.btn3.grid(row=3,column=2,padx=2,pady=2)
        self.btn3.bind("<Button-1>", press_btn)

        self.btncarp = Button(self.hesaplama_frame,bg="lightgrey",text="*",bd=8,width=12,height=1,font=('Arial',15))
        self.btncarp.grid(row=3,column=3,padx=2,pady=2)
        self.btncarp.bind("<Button-1>", press_btn)

        self.btnnokta = Button(self.hesaplama_frame,bg="lightgrey",text=".",bd=8,width=12,height=1,font=('Arial',15))
        self.btnnokta.grid(row=4,column=0,padx=2,pady=2)
        self.btnnokta.bind("<Button-1>", press_btn)

        self.btn0 = Button(self.hesaplama_frame,bg="lightgrey",text="0",bd=8,width=12,height=1,font=('Arial',15))
        self.btn0.grid(row=4,column=1,padx=2,pady=2)
        self.btn0.bind("<Button-1>", press_btn)

        self.btnclear = Button(self.hesaplama_frame,bg="lightgrey",text="=",bd=8,width=12,height=1,font=('Arial',15))
        self.btnclear.grid(row=4,column=2,padx=2,pady=2)
        self.btnclear.bind("<Button-1>", press_btn)

        self.btnbol = Button(self.hesaplama_frame,bg="lightgrey",text="/",bd=8,width=12,height=1,font=('Arial',15))
        self.btnbol.grid(row=4,column=3,padx=2,pady=2)
        self.btnbol.bind("<Button-1>", press_btn)

        self.bill_frame = LabelFrame(self.win,text="Fiş Bölümü",font=('Arial',18),background="lightgrey",bd=8,relief=GROOVE)
        self.bill_frame.place(x=585,y=420,width=650,height=320)

        self.ekle_btn.config(state="disabled")
        self.total_btn.config(state="disabled")
        self.kaydet_btn.config(state="disabled")


        self.y_scroll=Scrollbar(self.bill_frame,orient="vertical")
        self.bill_txt=Text(self.bill_frame,bg="white",yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.bill_txt.pack(fill=BOTH,expand=TRUE)

        default_bill()

       

























if __name__ == "__main__":
    main()
