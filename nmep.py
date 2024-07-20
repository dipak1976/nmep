from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
#from time import time#
import mysql.connector
from tkinter import messagebox



win = Tk()
win.title("NMEP")
win.geometry('1100x650+50+5')
win.resizable(0,0)
win.iconbitmap("C:/Users/Hp/Downloads/microscope icon file.ico")

#variable for styles
bg_color = "white"
fg_color = "black"
font_family_regular = ("arial",12,"bold")
font_family_heading = ("arial",20,"bold")

#variable for fixed data
villages = ["Rinchhvani","Damavav","Albeta","Jorapura","Khilodi","Ranipura","Shaniyada","Vangarava","Mullakuva"]
rin_flya = ["bava","borani","bhuval","tadavi","bhayala patel","virsing patel"]
dam_flya = ["Patel"]
alb_flya = ["gam"]
jor_flya = ["samidhas"]
khi_flya = ["patel"]
ran_flya = ["patel"]
sha_flya = ["champa"]
van_flya = ["patel"]
muk_flya = ["nayak"]
agency = ["ACTIVE","FHW","ASHA","CLINIC","CHO","OTHER"]
agency_code_active = ["A1","A2","A3","A4","A5","A6","A7"]
agency_code_fhw = ["P1","P2","P3","P4","P5","P6","P7"]
agency_code_cho = ["C1","C2","C3","C4","C5","C6","C7"]
agency_code_asha = ["F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","F13","F14","F15","F16","F17","F18","F19","F20","F21"]
agency_code_clinic = "P"

#variable for getting data
id_num = IntVar()
rcv_date = StringVar()
agency = StringVar()
agency_code = StringVar()
village = StringVar()
falya = StringVar()
coll_date = StringVar()
exam_date = StringVar()
rdt_test = IntVar()
rdt_pv = IntVar()
rdt_pf = IntVar()
bs_test = IntVar()
bs_pv = IntVar()
bs_pf = IntVar()
mf8_agency = StringVar()
mf8_agency_code = StringVar()
mf8_from_date = StringVar()
mf8_to_date = StringVar()

#fun for geting agency code as per selected agency
def pick_code(e):
	if ent_agency.get() == "ACTIVE":
		ent_agency_code.config(value=agency_code_active)
		ent_agency_code.current(0)
	if ent_agency.get() == "FHW":
		ent_agency_code.config(value=agency_code_fhw)
		ent_agency_code.current(0)
	if ent_agency.get() == "ASHA":
		ent_agency_code.config(value=agency_code_asha)
		ent_agency_code.current(0)
	if ent_agency.get() == "CLINIC":
		ent_agency_code.config(value=agency_code_clinic)
		ent_agency_code.current(0)
	if ent_agency.get() == "CHO":
		ent_agency_code.config(value=agency_code_cho)
		ent_agency_code.current(0)
	if ent_agency.get() == "OTHER":
		ent_agency_code.config(value="Other")
		ent_agency_code.current(0)		

#fun for geting falya as per selected village		
def pick_falya(e):
	if ent_village.get() == "Rinchhvani":
		ent_falya.config(value=rin_flya)
		ent_falya.current(0)
	if ent_village.get() == "Damavav":
		ent_falya.config(value=dam_flya)
		ent_falya.current(0)
	if ent_village.get() == "Albeta":
		ent_falya.config(value=alb_flya)
		ent_falya.current(0)
	if ent_village.get() == "Jorapura":
		ent_falya.config(value=jor_flya)
		ent_falya.current(0)
	if ent_village.get() == "Khilodi":
		ent_falya.config(value=khi_flya)
		ent_falya.current(0)
	if ent_village.get() == "Ranipura":
		ent_falya.config(value=ran_flya)
		ent_falya.current(0)
	if ent_village.get() == "Shaniyada":	
		ent_falya.config(value=sha_flya)
		ent_falya.current(0)
	if ent_village.get() == "Vangarava":		
		ent_falya.config(value=van_flya)
		ent_falya.current(0)	


#main heading
labl_1 = Label(win,text="NMEP REPORTING SYSTEM     PHC RINCHHVANI",bg= "red",bd=10,relief=RIDGE,fg=fg_color,font=font_family_heading)
labl_1.pack(side=TOP,fill=X)

frame_1 = Frame(win,bd=10,relief=RIDGE)
frame_1.place(x=0,y=50,width=340,height=550)
frame_ent = LabelFrame(frame_1,text="M-1 Form Data Entry",background="white")
frame_ent.place(x=5,y=5)

# dataentry start
#first row - id
labl_id = Label(frame_ent,text="ID NO.",bg=bg_color,fg=fg_color,font=font_family_regular)
labl_id.grid(row=2,column=1,padx=10,pady=5,sticky=W)
ent_id = Entry(frame_ent,width=15,textvariable=id_num,font="calibri,16,bold",state="readonly")
ent_id.grid(row=2,column=2)

id = 0

#second row - receave date
labl_rcv_date = Label(frame_ent,text="RECEAVE DATE",bg=bg_color,fg=fg_color,font="calibri,16,bold")
labl_rcv_date.grid(row=3,column=1,padx=10,pady=5,sticky=W)
ent_rcv_date = DateEntry(frame_ent,textvariable = rcv_date,date_pattern="yyyy-mm-dd",state="readonly",width=15)
ent_rcv_date.grid(row=3,column=2)


#combobox for agency selection
labl_agency = Label(frame_ent,text="AGENCY TYPE",bg=bg_color,fg=fg_color,font="calibri,16,bold")
labl_agency.grid(row=4,column=1,padx=10,pady=5,sticky=W)
ent_agency = ttk.Combobox(frame_ent,width= 15,textvariable=agency,state="readonly",values=("ACTIVE","FHW","ASHA","CLINIC","CHO","OTHER"),font="calibri,16,bold")
ent_agency.grid(row=4,column=2)
ent_agency.bind("<<ComboboxSelected>>", pick_code)

#combobox for agency code selection
labl_agency_code = Label(frame_ent,text="AGENCY CODE",bg=bg_color,fg=fg_color,font="calibri,16,bold")
labl_agency_code.grid(row=5,column=1,padx=10,pady=5,sticky=W)
ent_agency_code = ttk.Combobox(frame_ent,width=15,textvariable=agency_code,font="calibri,16,bold",state="readonly")
ent_agency_code.grid(row=5,column=2)

#combobox for village selection
labl_village = Label(frame_ent,text="VILLAGE",bg=bg_color,fg=fg_color,font="calibri,16,bold")
labl_village.grid(row=6,column=1,padx=10,pady=5,sticky=W)
ent_village = ttk.Combobox(frame_ent,width=15,textvariable=village,font="calibri,16,bold",values= villages,state="readonly")
ent_village.grid(row=6,column=2)
ent_village.bind("<<ComboboxSelected>>", pick_falya)

#falya selection
labl_falya = Label(frame_ent,text="FALYA",bg=bg_color,fg=fg_color,font="calibri,16,bold")
labl_falya.grid(row=7,column=1,padx=10,pady=5,sticky=W)
ent_falya = ttk.Combobox(frame_ent,width=15,textvariable=falya,font="calibri,16,bold",state="readonly")
ent_falya.grid(row=7,column=2)

#coll date setting
labl_coll_date = Label(frame_ent,text="COLL. DATE",bg=bg_color, fg=fg_color,font="calibri,16,bold")
labl_coll_date.grid(row=8,column=1,padx=10,pady=5,sticky=W)
ent_coll_date = DateEntry(frame_ent,textvariable=coll_date, date_pattern="yyyy-mm-dd",state="readonly",width=15)
ent_coll_date.grid(row=8,column=2)

#exam date setting
labl_exam_date = Label(frame_ent,text="EXAM DATE",bg=bg_color,fg=fg_color,font="calibri,16,bold")
labl_exam_date.grid(row=9,column=1,padx=10,pady=5,sticky=W)
ent_exam_date = DateEntry(frame_ent, date_pattern="yyyy-mm-dd",textvariable=exam_date,state="readonly",width=15)
ent_exam_date.grid(row=9,column=2)

#rdt test entry
labl_rdt = Label(frame_ent,text="RDT TEST",bg=bg_color,fg=fg_color,font="calibri,16,bold")
labl_rdt.grid(row=10,column=1,padx=10,pady=5,sticky=W)
ent_rdt = Spinbox(frame_ent,width=15,textvariable=rdt_test,font="calibri,16,bold",from_=0,to=100)
ent_rdt.grid(row=10,column=2)

#rdt pv  entry
labl_rdt_pv = Label(frame_ent,text="RDT PV",bg=bg_color,fg=fg_color,font="calibri,16,bold")
labl_rdt_pv.grid(row=11,column=1,padx=10,pady=5,sticky=W)
ent_rdt_pv = Spinbox(frame_ent,width=15,textvariable=rdt_pv,font="calibri,16,bold",from_=0,to=100)
ent_rdt_pv.grid(row=11,column=2)

#rdt pf  entry
labl_rdt_pf = Label(frame_ent,text="RDT PF",bg=bg_color,fg=fg_color,font="calibri,16,bold")
labl_rdt_pf.grid(row=12,column=1,padx=10,pady=5,sticky=W)
ent_rdt_pf = Spinbox(frame_ent,width=15,textvariable=rdt_pf,font="calibri,16,bold",from_=0,to=100)
ent_rdt_pf.grid(row=12,column=2)

#bs test  entry
labl_bs = Label(frame_ent,text="BS TEST",bg=bg_color,fg=fg_color,font="calibri,16,bold")
labl_bs.grid(row=13,column=1,padx=10,pady=5,sticky=W)
ent_bs = Spinbox(frame_ent,width=15,textvariable=bs_test,font="calibri,16,bold",from_=0,to=100)
ent_bs.grid(row=13,column=2)

#bs pv  entry
labl_bs_pv = Label(frame_ent,text="BS PV",bg=bg_color,fg=fg_color,font="calibri,16,bold")
labl_bs_pv.grid(row=14,column=1,padx=10,pady=5,sticky=W)
ent_bs_pv = Spinbox(frame_ent,width=15,textvariable=bs_pv,font="calibri,16,bold",from_=0,to=100)
ent_bs_pv.grid(row=14,column=2)

#bs pf  entry
labl_bs_pf = Label(frame_ent,text="BS PF",bg=bg_color,fg=fg_color,font="calibri,16,bold")
labl_bs_pf.grid(row=15,column=1,padx=10,pady=5,sticky=W)
ent_bs_pf = Spinbox(frame_ent,width=15,textvariable=bs_pf,font="calibri,16,bold",from_=0,to=100)
ent_bs_pf.grid(row=15,column=2)

#button for data submit
btn1_submit = Button(frame_ent,text="submit",height=1,width=15,font="calibri,16,bold" )#,command=submit
btn1_submit.grid(row=16,column=1,columnspan=2)




#frame 2 for list box
frame_2 = Frame(win,bd=10,relief=RIDGE)
frame_2.place(x=340,y=50,width=760,height=550)




#frame 3 for list buttons
frame_3 = Frame(win,bd=10,relief=RIDGE)
frame_3.place(x=0,y=590,width=1100,height=50)

#button for MF8
btn_mf8 = Button(frame_3,text="Generate MF8",height=1,width=19,font="calibri,16,bold")#,command=gen_mf8
btn_mf8.grid(row=0,column=0,padx=2,pady=2)

#button for generate report
btn_report = Button(frame_3,text="GENERATE REPORTS",height=1,width=19,font="calibri,16,bold")#,command=gen_mf8
btn_report.grid(row=0,column=1,padx=2,pady=2)

#search button======================================================
search_lbl = Label(frame_3,text = "ID",font="calibri,16,bold")
search_lbl.grid(row=0,column=2)

search_ent = Entry(frame_3,font="calibri,16,bold",width=10)
search_ent.grid(row=0,column=3)

#button for search
btn_search = Button(frame_3,text="SEARCH",height=1,width=15,font="calibri,16,bold")#,command=gen_mf8
btn_search.grid(row=0,column=4,padx=2,pady=2)

#button for update
btn_update = Button(frame_3,text="UPDATE",height=1,width=15,font="calibri,16,bold")#,command=gen_mf8
btn_update.grid(row=0,column=5,padx=2,pady=2)

#button for delete
btn_delete = Button(frame_3,text="DELETE",height=1,width=15,font="calibri,16,bold")#,command=gen_mf8
btn_delete.grid(row=0,column=6,padx=2,pady=2)

#button for close
btn_close = Button(frame_3,text="CLOSE",height=1,width=15,font="calibri,16,bold")#,command=gen_mf8
btn_close.grid(row=0,column=7,padx=2,pady=2)





win.mainloop()