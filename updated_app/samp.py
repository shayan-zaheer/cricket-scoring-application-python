import sqlite3
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
import customtkinter
from tkinter import *
from tkinter import ttk
from CTkMessagebox import CTkMessagebox
from random import *
from customtkinter import *
from PIL import Image,ImageTk
from PIL import *

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

conn = sqlite3.connect('match.db')
c=conn.cursor()

m = Tk()
m.geometry("1400x700")
m.title("Cricket Scoring App")
photo=PhotoImage(file="icon.png")
m.iconphoto(True,photo)
m.resizable(False, False)

img=ImageTk.PhotoImage(file="cricket.jpg")

main_font=CTkFont(
    family="ALGERIAN",
    size=70,
    weight="normal",
    slant="roman",
    underline=0
)

label_font=CTkFont(
    family="Georgia",
    size=40,
    weight="normal",
    slant="italic",
    underline=0
)

l1=CTkLabel(m,text="CRICKET SCORING APPLICATION",fg_color="green",text_color="white",font=main_font,height=70)
l1.pack(side=TOP,fill="x")

label_img=ImageTk.PhotoImage(file="label.png")

img_label=CTkLabel(l1,text=" ",image=label_img)
img_label.place(x=100,y=5)

img_label2=CTkLabel(l1,text=" ",image=label_img)
img_label2.place(x=1225,y=5)

back_img=Image.open("back.jpg")
bck_img=CTkImage(light_image=back_img,size=(1400,800))

f1=CTkFrame(m,corner_radius=0,width=1367,height=637,fg_color="#FFFF99",border_width=5,border_color="green")
f1.place(x=0,y=70)
back_label=CTkLabel(f1,width=1367,height=637,image=bck_img)
back_label.pack()

main_frame=CTkFrame(f1,width=250,height=700,fg_color="black")
main_frame.place(x=0,y=0)
i=Label(main_frame,width=250,border=5,height=700,image=img)
i.pack()

f2=CTkFrame(m,width=1050,height=130,corner_radius=0,border_width=3,border_color="green",fg_color="#E5FFCC")
f2.place(x=260,y=80)

batsman_img=Image.open("batsman.png")
bat_img=CTkImage(light_image=batsman_img,size=(120,120))
bat_lab=CTkLabel(f2,width=60,height=9,text=" ",image=bat_img).place(x=100,y=7)

match_lab= CTkLabel(f2,corner_radius=10,text="Match Name",text_color="white",font=label_font,fg_color="green").place(x=400,y=10)
match=CTkEntry(f2,width=500,height=40,text_color="black",border_color="green",placeholder_text="Enter Match Name",placeholder_text_color="grey",font=("Arial",30))
match.place(x=240,y=70)

match_name_img1=Image.open("match_name.png")
match_name_img=CTkImage(light_image=match_name_img1)
match_name_label=CTkLabel(match_lab,text=" ",image=match_name_img)
match_name_label.place(x=630,y=95)


f3=CTkFrame(m,width=1050,height=448,border_width=3,corner_radius=0,border_color="green",fg_color="#E5FFCC")
f3.place(x=260,y=220)
match_lab= CTkLabel(f3,corner_radius=10,text="Match Information",text_color="white",font=label_font,fg_color="green").place(x=340,y=10)

trophy_img=Image.open("trophy.png")
trop_img=CTkImage(light_image=trophy_img,size=(150,150))
trop_lab=CTkLabel(f3,width=60,height=90,text=" ",image=trop_img).place(x=50,y=295)

wicket_img=Image.open("wicket.png")
wic_img=CTkImage(light_image=wicket_img,size=(140,200))
wic_lab=CTkLabel(f3,width=150,height=100,text=" ",image=wic_img).place(x=890,y=245)

samp_font=CTkFont(
    family="Times",
    size=22,
    weight="normal",
    slant="roman",
    underline=0
)

team_name1_label=CTkLabel(f3,text="Enter first team's Name",text_color="white",corner_radius=5,fg_color="green",font=samp_font).place(x=30,y=75)
team_name1=CTkEntry(f3,width=200,height=10,text_color="black",border_color="green",font=("Arial",20))
team_name1.place(x=250,y=75)

team_name2_label=CTkLabel(f3,text="Enter second team's Name",corner_radius=5,text_color="white",fg_color="green",font=samp_font).place(x=520,y=75)
team_name2=CTkEntry(f3,width=200,height=10,text_color="black",border_color="green",font=("Arial",20))
team_name2.place(x=770,y=75)

def toss(event):
    opt.configure(values=[team_name1.get(), team_name2.get()])

warning_font=CTkFont(
    family="Arial",
    size=20,
    weight="bold",
    slant="italic"
    )
opt = customtkinter.CTkComboBox(f3,dropdown_fg_color="white",values=['Select batting Team'],dropdown_text_color="green",dropdown_font=("Arial",15),dropdown_hover_color="darkGreen",width=270,height=30,border_width=2,button_color="green",border_color="green",button_hover_color="darkGreen",command=toss)
opt.place(x=350,y=160)

team_name1.bind('<KeyRelease>', toss)
team_name2.bind('<KeyRelease>', toss)
opt.bind('<KeyRelease>', toss)

def batter_name(bat_name_1,bat_name_2,batting):
    #this function just inserts batsmen names in tables
    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    c.execute(f"""INSERT INTO {batting} VALUES('{bat_name_1}',0,0,0)""")
    c.execute(f"""INSERT INTO {batting} VALUES('{bat_name_2}',0,0,0)""")
    conn.commit()
    
def bowler_name_func(bowler,bowling):
    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    c.execute(f"""INSERT INTO {bowling} VALUES('{bowler}',0,0,0)""")
    conn.commit()

def team_a_batting_f():
    global m
    global bat_1_name
    global bat_2_name
    global bowler_name
    global bat_1
    global bat_2
    global match_format

    bat_1_name=StringVar()
    bat_2_name=StringVar()
    

    #team A batting means team B is bowling so tbat1on will also include feaatures related to team b bowling
    bat1_label=CTkLabel(f3,text="Enter Batsman Name(Opener)",text_color="white",corner_radius=5,fg_color="green",font=(samp_font,15)).place(x=30,y=210)
    bat_1=CTkEntry(f3,width=200,height=10,textvariable=bat_1_name,text_color="black",border_color="green",font=("Arial",20))
    bat_1.place(x=250,y=210)
 
    bat2_label=CTkLabel(f3,text="Enter Batsman Name(Runner)",text_color="white",corner_radius=5,fg_color="green",font=(samp_font,17))
    bat2_label.place(x=520,y=210)
    bat_2=CTkEntry(f3,width=200,height=10,textvariable=bat_2_name,text_color="black",border_color="green",font=("Arial",20))
    bat_2.place(x=770,y=210)

    bowler_name=StringVar()
    bowler_Lab=CTkLabel(f3,text="Enter Bowler Name",text_color="white",corner_radius=5,fg_color="green",font=(samp_font)).place(x=30,y=250)
    bowler =CTkEntry(f3,width=200,height=10,textvariable=bowler_name,text_color="black",border_color="green",font=("Arial",20))
    bowler.place(x=250,y=250)

    global match_format_var
    match_format_var=StringVar()
    match_format_lab = CTkLabel(f3,text="How many Overs?",text_color="white",corner_radius=5,fg_color="green",font=samp_font).place(x=30,y=290)
    match_format =CTkEntry(f3,width=200,height=10,textvariable=match_format_var,text_color="black",border_color="green",font=("Arial",20))
    match_format.place(x=250,y=290)

    start_i=Image.open("start.png")
 
    start_img=CTkImage(dark_image=start_i,size=(30,30))
    start= CTkButton(f3,text="START MATCH",text_color="white",image=start_img,compound=LEFT,command=next_screen,fg_color="#FF0000",hover=True,hover_color="orange",height=45,font=("Arial",15),corner_radius=100,border_width=3,border_color="darkGreen")
    start.place(x=800,y=300)
  
def table_name(name):
    if " " in name:
        location =name.index(" ")
        name = name[0:location]
        # print(name)
    return name    
    
def begin_match():
    global main
    global bowler_present
    global _2_bat_name
    global _1_bat_name
    global team_a
    global team_b
    global match_id
    global match_name_cut

    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    match_name = match.get()    
    match_name_cut = table_name(match_name)
    team_a = team_name1.get()
    team_a_cut = table_name(team_a)
    team_b = team_name2.get()
    team_b_cut = table_name(team_b)

    c.execute(f"""CREATE TABLE IF NOT EXISTS match_id (ID INT)""")
    id=c.execute("SELECT ID FROM match_id").fetchall()
    rand=[]
    for i in id:
        for j in i:
            rand.append(j)
    match_id=str(randint(1,1000))
    while match_id in rand:
        match_id= str(randint(1,1000))
    c.execute(f"INSERT INTO match_id VALUES({match_id})")

    global team_a_batting
    global team_b_batting
    global team_a_bowling
    global team_b_bowling
    global main
    team_a_batting = str(team_a_cut) + "_batting"+match_id
    team_b_batting = str(team_b_cut) + "_batting"+match_id
    team_a_bowling = str(team_a_cut)+ "_bowling"+match_id
    team_b_bowling = str(team_b_cut) + "_bowling"+match_id
    main = str(match_name_cut)+"_main_scorecard"+match_id
    # print(main)

    c.execute(f""" CREATE TABLE  IF NOT EXISTS {main}
                    (SCORE INT, OVERS INT , WICKETS INT)""")
    c.execute(f"""INSERT INTO {main} VALUES(0,0,0)""")
    c.execute(f""" CREATE TABLE  IF NOT EXISTS  {team_a_batting}
                    (BATSMAN TEXT, RUNS INT, BALLS INT, STRIKE_RATE REAL)""")
    c.execute(f""" CREATE TABLE  IF NOT EXISTS  {team_b_batting}
                   (BATSMAN TEXT, RUNS INT, BALLS INT, STRIKE_RATE REAL)""")
    c.execute(f""" CREATE TABLE IF NOT EXISTS  {team_a_bowling}
                    (BOWLER TEXT, OVERS REAL, RUNS INT,WICKETS INT)""")
    c.execute(f""" CREATE TABLE IF NOT EXISTS  {team_b_bowling }
                    (BOWLER TEXT, OVERS REAL, RUNS INT,WICKETS INT)""")
    
    # print("Tables created successfully!!!")
    
    global batting_side
    global bowling_side
    ent = opt.get()
    global bs
    if ent==team_a:
        team_a_batting_f()
        batting_side = team_a_batting
        bs=team_name1.get()
        bowling_side = team_b_bowling
    elif ent==team_b:
        team_a_batting_f()
        batting_side = team_b_batting
        bs=team_name2.get()
        bowling_side = team_a_bowling
    else:
        CTkMessagebox(title="Error", message="Please select a team name!", icon="cancel", button_color="darkGreen")
    # print(match,team_a_batting,team_b_batting)
    conn.commit()
    conn.close()


start= CTkButton(f3,text="NEXT",text_color="white",command=begin_match,fg_color="#FF0000",hover=True,hover_color="orange",width=10,height=30,font=("Arial",15),corner_radius=100,border_width=3,border_color="darkGreen")
start.place(x=900,y=160)

exitFlag=True

def next_screen():
    global exitFlag
    if exitFlag == True:
        exitFlag = False
        m.destroy()
    global current_batsmen_score
    global current_batsmen_balls
    global current_bowler_score
    global current_bowler_balls
    global batsman_strike
    global extras
    global all_bowlers
    global bowler_present
    global current_bowler_wickets
    global _1_bat_name
    global _2_bat_name
    global overs_lim
    global match_format
    global match_format_var
    global bottom_news

    _1_bat_name = str(bat_1_name.get())
    _2_bat_name = str(bat_2_name.get())
    bowler_present = bowler_name.get()
    overs_lim = match_format_var.get()
    # print(overs_lim)

    
    # print(_1_bat_name)
    # print(_2_bat_name)

    extras = 0
    all_bowlers = set()
    current_batsmen_score = dict()
    current_batsmen_balls = dict()
    current_bowler_score = dict()
    current_bowler_balls = dict()
    current_bowler_wickets= dict()
    all_bowlers ={bowler_present}

    current_batsmen_score[str(bat_1_name.get())]=0
    current_batsmen_score[str(bat_2_name.get())]=0

    current_batsmen_balls[str(bat_1_name.get())]=0
    current_batsmen_balls[str(bat_2_name.get())]=0

    current_bowler_score[bowler_present]=0
    current_bowler_balls[bowler_present]=0
    current_bowler_wickets[bowler_present]=0
    

    batsman_strike = str(bat_1_name.get())
    # print(batsman_strike)
    
    batter_name(str(bat_1_name.get()),str(bat_2_name.get()),batting_side)
    bowler_name_func(str(bowler_name.get()),bowling_side)
    global h
    h = Tk()
    h.geometry("1400x800")
    h.title("Cricket Scoring App")
    h.resizable(False, False)
    CTkMessagebox(master=h, title="Cricket Scoring App", message="Match has started!", icon="info", button_color="darkGreen")

    back_img=Image.open("back.jpg")
    bck_img=CTkImage(light_image=back_img,size=(1400,800))
    l1=CTkLabel(h,text="CRICKET SCORING APPLICATION",fg_color="green",text_color="white",font=main_font,height=70)
    l1.pack(side=TOP,fill="x")

    label_img=ImageTk.PhotoImage(file="label.png")

    img_label=CTkLabel(l1,text=" ",image=label_img)
    img_label.place(x=100,y=5)

    img_label2=CTkLabel(l1,text=" ",image=label_img)
    img_label2.place(x=1225,y=5)

    global new_f1,back_new_label

    new_f1=CTkFrame(h,corner_radius=0,width=1367,height=637,fg_color="#FFFF99",border_width=5,border_color="green")
    new_f1.place(x=0,y=70)
    back_new_label=CTkLabel(new_f1,width=1367,text=" ",height=637,image=bck_img)
    back_new_label.pack()

    global new
    new=CTkFrame(new_f1,corner_radius=0,border_width=5,border_color="darkGreen",width=345,height=637)
    new.place(x=0,y=0)
    
    runlab=CTkLabel(new,text="RUNS BUTTONS",width=345,font=("Arial Black",26),text_color="white",height=35,fg_color="darkBlue")
    runlab.place(x=0,y=0)
    
    global dot_b
    dot_b=CTkButton(new,text="DOT",command=dot,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=30,height=20)
    dot_b.place(x=30,y=40)
    
    global one_b
    global two_b
    global three_b
    global four_b
    global six_b

    one_b=CTkButton(new,text="1",command =one,width=50,height=20,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen")
    one_b.place(x=115,y=40)

    two_b=CTkButton(new,text="2",command =two,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    two_b.place(x=185,y=40)
    
    three_b=CTkButton(new,text="3",command =three,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    three_b.place(x=255,y=40)
    
    four_b=CTkButton(new,text="4",command =four,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    four_b.place(x=115,y=80)
    
    six_b=CTkButton(new,text="6",command =six,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    six_b.place(x=185,y=80)
    
    global wd_b
    global out_b
    global byes_1
    global byes_2
    global byes_3
    global byes_4

    wd_b=CTkButton(new,text="WD",command=wd,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    wd_b.place(x=30,y=80)

    out_b=CTkButton(new,text="OUT",command=out,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    out_b.place(x=255,y=80)   

    byes_1=CTkButton(new,text="B1",command=byes_1_f,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    byes_1.place(x=30,y=120)

    byes_2=CTkButton(new,text="B2",command=byes_2_f,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    byes_2.place(x=115,y=120)

    byes_3=CTkButton(new,text="B3",command=byes_3_f,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    byes_3.place(x=185,y=120)

    byes_4=CTkButton(new,text="B4",command=byes_4_f,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    byes_4.place(x=255,y=120)

    global byes_wide_1
    global byes_wide_2
    global byes_wide_3
    global byes_wide_4
    global runout_b

    byes_wide_1=CTkButton(new,text="WD-BYE1",command=wide_1,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=30,height=20)
    byes_wide_1.place(x=50,y=160)

    byes_wide_2=CTkButton(new,text="WD-BYE2",command=wide_2,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=30,height=20)
    byes_wide_2.place(x=180,y=160)

    byes_wide_3=CTkButton(new,text="WD-BYE3",command=wide_3,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=30,height=20)
    byes_wide_3.place(x=50,y=200)

    byes_wide_4=CTkButton(new,text="WD-BYE4",command=wide_4,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=30,height=20)
    byes_wide_4.place(x=180,y=200)

    runout_b=CTkButton(new,text="RUN-OUT",command=run_out,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=30,height=20)
    runout_b.place(x=50,y=240)

    nb_b=CTkButton(new,text="NO BALL",command=nb,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=30,height=20)
    nb_b.place(x=180,y=240)

    undo_b=CTkButton(new,text="UNDO",command=undo,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=30,height=20)
    undo_b.place(x=260,y=270)

    global next_over_b
    next_over_b=CTkButton(new,text="NEXT OVER",command=over_change,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=30,height=20)
    next_over_b.place(x=20, y=275)
    next_over_b.place_forget()

    global score_f
    score_f=CTkFrame(h,corner_radius=0,width=800,height=450,fg_color="#E5FFCC",border_width=5,border_color="darkGreen")
    score_f.place(x=470,y=150)

    lab_score=CTkLabel(score_f,fg_color="darkGreen",text="SCORE BOARD",width=70,font=("Georgia",35),text_color="white",corner_radius=30)
    lab_score.place(x=300,y=20)

    conn = sqlite3.connect('score.db')
    conn.row_factory= lambda cursor, row:row[0]
    c=conn.cursor()

    c.execute(f"""SELECT SCORE FROM {main}""")
    s=c.fetchall()

    c.execute(f"""SELECT WICKETS FROM {main}""")
    w=c.fetchall()

    c.execute(f"""SELECT OVERS FROM {main}""")
    o=c.fetchall()

    global s_lab,s1_lab,score_lab,bats1score,bats2score,score1_lab,w_lab,w1_lab,o_lab,o1_lab,bats1_lab,bats_lab,batsrunner_lab,batsrunner1_lab


    s_lab=CTkLabel(score_f,text="BATTING",fg_color="darkGreen",font=("Times",25),text_color="white",corner_radius=40)
    s_lab.place(x=30,y=85)

    s1_lab=CTkLabel(score_f,text=bs,width=70,fg_color="white",font=("Times",23),text_color="darkGreen",corner_radius=5)
    s1_lab.place(x=200,y=85)

    score_lab=CTkLabel(score_f,text="SCORE",fg_color="darkGreen",font=("Times",25),text_color="white",corner_radius=40)
    score_lab.place(x=30,y=135)

    score1_lab=CTkLabel(score_f,text=s,width=70,fg_color="white",font=("Times",23),text_color="darkGreen",corner_radius=5)
    score1_lab.place(x=200,y=135)

    w_lab=CTkLabel(score_f,text="WICKETS",fg_color="darkGreen",font=("Times",25),text_color="white",corner_radius=40)
    w_lab.place(x=30,y=185)

    w1_lab=CTkLabel(score_f,text=w,width=70,fg_color="white",font=("Times",23),text_color="darkGreen",corner_radius=5)
    w1_lab.place(x=200,y=185)

    o_lab=CTkLabel(score_f,text="OVERS",fg_color="darkGreen",font=("Times",25),text_color="white",corner_radius=40)
    o_lab.place(x=30,y=235)

    o1_lab=CTkLabel(score_f,text=o,width=70,fg_color="white",font=("Times",23),text_color="darkGreen",corner_radius=5)
    o1_lab.place(x=200,y=235)

    global crr1_lab

    crr_lab=CTkLabel(score_f,text="CRR",fg_color="darkGreen",font=("Times",25),text_color="white",corner_radius=40)
    crr_lab.place(x=30,y=285)

    crr1_lab=CTkLabel(score_f,text=0,width=70,fg_color="white",font=("Times",23),text_color="darkGreen",corner_radius=5)
    crr1_lab.place(x=200,y=285)

    bats_lab=CTkLabel(score_f,text="BATSMAN 1",fg_color="darkGreen",font=("Times",25),text_color="white",corner_radius=40)
    bats_lab.place(x=350,y=85)

    bats1_lab=CTkLabel(score_f,text=f"{_1_bat_name}",width=70,fg_color="white",font=("Times",23),text_color="darkGreen",corner_radius=5)
    bats1_lab.place(x=550,y=85)
    
    batsrunner_lab=CTkLabel(score_f,text="BATSMAN 2",fg_color="darkGreen",font=("Times",25),text_color="white",corner_radius=40)
    batsrunner_lab.place(x=350,y=135)

    batsrunner1_lab=CTkLabel(score_f,text=f"{_2_bat_name}",width=70,fg_color="white",font=("Times",23),text_color="darkGreen",corner_radius=5)
    batsrunner1_lab.place(x=550,y=135)

    c.execute(f"""SELECT RUNS FROM {batting_side} WHERE BATSMAN='{_1_bat_name}'""")
    b1s=c.fetchall()
    b2s=c.execute(f"SELECT RUNS FROM {batting_side} WHERE BATSMAN='{_2_bat_name}'").fetchall()

    b1b=c.execute(f"SELECT BALLS FROM {batting_side} WHERE BATSMAN='{_1_bat_name}'").fetchall()
    b2b=c.execute(f"SELECT BALLS FROM {batting_side} WHERE BATSMAN='{_2_bat_name}'").fetchall()


    bats1score=CTkLabel(score_f,text=(b1s,"(",b1b,")"),fg_color="white",font=("Times",23),text_color="darkGreen")
    bats1score.place(x=650,y=85)

    bats2score=CTkLabel(score_f,text=(b2s,"(",b2b,")"),fg_color="white",font=("Times",23),text_color="darkGreen")
    bats2score.place(x=650,y=135)

    bo=c.execute(f"""SELECT OVERS FROM {bowling_side} WHERE BOWLER='{bowler_present}'""").fetchall()
    br=c.execute(f"""SELECT RUNS FROM {bowling_side} WHERE BOWLER='{bowler_present}'""").fetchall()
    bw=c.execute(f"""SELECT WICKETS FROM {bowling_side} WHERE BOWLER='{bowler_present}'""").fetchall()

    global bo_lab,bo1_lab,bowler_info,record_lab,record1_lab

    bo_lab=CTkLabel(score_f,text="BOWLER",fg_color="darkGreen",font=("Times",25),text_color="white",corner_radius=40)
    bo_lab.place(x=350,y=185)

    bo1_lab=CTkLabel(score_f,text=bowler_present,width=70,fg_color="white",font=("Times",23),text_color="darkGreen")
    bo1_lab.place(x=550,y=185)

    bowler_info=CTkLabel(score_f,text=(bo,"(",br,"/",bw,")"),width=70,fg_color="white",font=("Times",23),text_color="darkGreen")
    bowler_info.place(x=650,y=185)

    record_lab=CTkLabel(score_f,text="RECENT BALLS RECORD",fg_color="darkGreen",font=("Times",25),text_color="white",corner_radius=40)
    record_lab.place(x=350,y=235)

    record1_lab=CTkLabel(score_f,text=" ",fg_color=None,font=("Times",18),text_color="darkGreen",corner_radius=40)
    record1_lab.place(x=350,y=285)

    if batsman_strike==_1_bat_name:
        bats1_lab.configure(text=f"{_1_bat_name}*")
        batsrunner1_lab.configure(text=f"{_2_bat_name}")
    elif batsman_strike==_2_bat_name:
        bats1_lab.configure(text=f"{_1_bat_name}")
        batsrunner1_lab.configure(text=f"{_2_bat_name}*")

    to_lab=CTkLabel(score_f,text="Total Overs",fg_color="darkGreen",font=("Times",20),text_color="white",corner_radius=40)
    to_lab.place(x=30,y=400)

    to11_lab=CTkLabel(score_f,text=overs_lim,fg_color="white",font=("Times",18),text_color="darkGreen",corner_radius=40)
    to11_lab.place(x=170,y=400)

    sum_but=CTkButton(score_f,text="MATCH SUMMARY",command=summary,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    sum_but.place(x=380,y=400)
    
def extract_data_from_db(table_name):
    conn = sqlite3.connect("score.db")
    c = conn.cursor()
    c.execute(f"""SELECT * FROM {table_name}""")
    data = c.fetchall()
    conn.close()
    return data

def create_pdf(team_a_bat_table, team_b_bowl_table, team_b_bat_table, team_a_bowl_table, filename):
    team_a_bat_data = extract_data_from_db(team_a_bat_table)
    team_b_bowl_data = extract_data_from_db(team_b_bowl_table)
    team_b_bat_data = extract_data_from_db(team_b_bat_table)
    team_a_bowl_data = extract_data_from_db(team_a_bowl_table)

    # pdf = canvas.Canvas(filename, pagesize=letter)
    # pdf.setFont("Helvetica-Bold", 12)
    # pdf.setFillColorRGB(1, 1, 0) # making font color white

    # pdf.drawImage("pdf_back.png", 0, 0, width=letter[0], height=letter[1], preserveAspectRatio=True)

    # pdf.drawString(100, 750, f"{team_a} Batting (1st Innings)")
    # pdf.setFont("Helvetica", 12)
    # pdf.setFillColorRGB(1, 1, 1)
    # y_position = 730
    # for i in team_a_bat_data:
    #     pdf.drawString(100, y_position, f"Batsman: {i[0]}, Runs: {i[1]}, Balls: {i[2]}, Strike Rate: {i[3]:.2f}")
    #     y_position -= 20

    # pdf.setFillColorRGB(0, 0, 1)
    # pdf.setFont("Helvetica-Bold", 12)
    # pdf.drawString(100, y_position - 40, f"{team_b} Bowling (1st Innings)")
    # pdf.setFont("Helvetica", 12)
    # pdf.setFillColorRGB(1, 1, 1)
    # y_position -= 60
    # for i in team_b_bowl_data:
    #     pdf.drawString(100, y_position, f"Bowler: {i[0]}, Overs: {i[1]}, Runs: {i[2]}, Wickets: {i[3]}")
    #     y_position -= 20
    # pdf.setFont("Helvetica-Bold", 12)
    # pdf.drawString(100, y_position, f"Total Score: {first_inning_score}, Total Overs: {first_inning_over}, Total Wickets: {first_inning_wicket}")
    

    # pdf.setFillColorRGB(0, 1, 0)
    # pdf.drawString(100, y_position - 100, f"{team_b} Batting (2nd Innings)")
    # pdf.setFont("Helvetica", 12)
    # pdf.setFillColorRGB(1, 1, 1)
    # y_position -= 120
    # for i in team_b_bat_data:
    #     pdf.drawString(100, y_position, f"Batsman: {i[0]}, Runs: {i[1]}, Balls: {i[2]}, Strike Rate: {i[3]:.2f}")
    #     y_position -= 20

    # pdf.setFillColorRGB(0.5, 0, 0.5)
    # pdf.setFont("Helvetica-Bold", 12)
    # pdf.drawString(100, y_position - 40, f"{team_a} Bowling (2nd Innings)")
    # pdf.setFont("Helvetica", 12)
    # pdf.setFillColorRGB(1, 1, 1)
    # y_position -= 60
    # for i in team_a_bowl_data:
    #     pdf.drawString(100, y_position, f"Bowler: {i[0]}, Overs: {i[1]}, Runs: {i[2]}, Wickets: {i[3]}")
    #     y_position -= 20
    # pdf.setFont("Helvetica-Bold", 12)
    # pdf.drawString(100, y_position, f"Total Score: {score}, Total Overs: {OVERS}, Total Wickets: {wickets}")

    # if winner != "DRAWN":
    #     pdf.drawString(100, y_position - 20, f"{winner} win the match!")
    # else:
    #     pdf.drawString(100, y_position - 20, f"Match ended in a DRAW!")

    # pdf.save()
    pdf = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()

    stats = []
    stats.append(Paragraph("Cricket Match Report", styles['Heading1']))

    stats.append(Paragraph(f"{team_a} Batting (1st Innings)", styles['Heading2']))
    team_a_bat_table = Table(data=[["Batsman", "Runs", "Balls", "Strike Rate"]] + team_a_bat_data, style=[('BACKGROUND', (0, 0), (-1, 0), colors.grey), ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')])
    stats.append(team_a_bat_table)
    stats.append(Paragraph("", styles['Normal'])) # space is added to add to the aesthetic, no specific reason

    stats.append(Paragraph(f"{team_b} Bowling (1st Innings)", styles['Heading2']))
    team_b_bowl_table = Table(data=[["Bowler", "Overs", "Runs", "Wickets"]] + team_b_bowl_data, style=[('BACKGROUND', (0, 0), (-1, 0), colors.grey), ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')])
    stats.append(team_b_bowl_table)
    stats.append(Paragraph("", styles['Normal']))

    stats.append(Paragraph("1st Innings Summary", styles['Heading2']))
    summary_table = Table(data=[["Total Score", "Total Overs", "Total Wickets"], [first_inning_score, first_inning_over, first_inning_wicket]], style=[('ALIGN', (0, 0), (-1, -1), 'CENTER')])
    stats.append(summary_table)
    stats.append(Paragraph("", styles['Normal']))

    stats.append(Paragraph(f"{team_b} Batting (2nd Innings)", styles['Heading2']))
    team_b_bat_table = Table(data=[["Batsman", "Runs", "Balls", "Strike Rate"]] + team_b_bat_data, style=[('BACKGROUND', (0, 0), (-1, 0), colors.grey), ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')])
    stats.append(team_b_bat_table)
    stats.append(Paragraph("", styles['Normal']))

    stats.append(Paragraph(f"{team_a} Bowling (2nd Innings)", styles['Heading2']))
    team_a_bowl_table = Table(data=[["Bowler", "Overs", "Runs", "Wickets"]] + team_a_bowl_data, style=[('BACKGROUND', (0, 0), (-1, 0), colors.grey), ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')])
    stats.append(team_a_bowl_table)
    stats.append(Paragraph("", styles['Normal']))

    stats.append(Paragraph("2nd Innings Summary", styles['Heading2']))
    summary_table = Table(data=[["Total Score", "Total Overs", "Total Wickets"], [score, OVERS, wickets]], style=[('ALIGN', (0, 0), (-1, -1), 'CENTER')])
    stats.append(summary_table)
    stats.append(Paragraph("", styles['Normal']))

    stats.append(Paragraph("Match Result", styles['Heading2']))
    if winner != "DRAWN":
        stats.append(Paragraph(f"{winner} win the match!", styles['Normal']))
    else:
        stats.append(Paragraph("Match ended in a DRAW!", styles['Normal']))
    pdf.build(stats)

def summary():
    s=Tk()
    s.geometry("1100x900+300+50")
    s.title("Match Summary")
    s.resizable(False, False)

    c_lab=CTkLabel(s,fg_color="darkGreen",font=("Times",30),text_color="white",corner_radius=40)
    c_lab.place(x=450,y=10)

    if batting_side==team_a_batting:
        c_lab.configure(text=f"{team_a} BATTING")
    else:
        c_lab.configure(text=f"{team_b} BATTING")

    s_frame1=CTkFrame(s,width=680,height=300,fg_color="lightGreen",border_color="darkGreen",border_width=5)
    s_frame1.place(x=10,y=70)
    tree=ttk.Treeview(s_frame1,columns=("BATSMAN","RUNS","BALLS","STRIKE_RATE"))
    tree.pack()

    conn=sqlite3.connect("score.db")
    tree.column("#1",anchor=CENTER)
    tree.heading("#1",text="BATSMAN NAME")

    tree.column("#2",anchor=CENTER)
    tree.heading("#2",text="RUN")

    tree.column("#3",anchor=CENTER)
    tree.heading("#3",text="BALLS")

    tree.column("#4",anchor=CENTER)
    tree.heading("#4",text="STRIKE RATE")

    c=conn.cursor()
    c.execute(f"SELECT * FROM {batting_side}")
    a=c.fetchall()
    # print(a)
    for i in a:
        tree.insert(parent="",index=END,values=i)
    conn.commit()
    conn.close()

    c2_lab=CTkLabel(s,fg_color="darkGreen",font=("Times",30),text_color="white",corner_radius=40)
    c2_lab.place(x=450,y=350)

    if bowling_side==team_a_bowling:
        c2_lab.configure(text=f"{team_a} BOWLING")
    else:
        c2_lab.configure(text=f"{team_b} BOWLING")

    s2_frame1=CTkFrame(s,width=680,height=300,fg_color="lightGreen",border_color="darkGreen",border_width=5)
    s2_frame1.place(x=10,y=400)
    tree2=ttk.Treeview(s2_frame1,columns=("BOWLER","OVERS","RUNS","WICKETS"))
    tree2.pack()

    conn=sqlite3.connect("score.db")
    tree2.column("#1",anchor=CENTER)
    tree2.heading("#1",text="BOWLER NAME")

    tree2.column("#2",anchor=CENTER)
    tree2.heading("#2",text="OVERS")

    tree2.column("#3",anchor=CENTER)
    tree2.heading("#3",text="RUNS")

    tree2.column("#4",anchor=CENTER)
    tree2.heading("#4",text="WICKETS")

    c=conn.cursor()
    c.execute(f"SELECT * FROM {bowling_side}")
    a=c.fetchall()
    # print(a)
    for i in a:
        tree2.insert(parent="",index=END,values=i)
    conn.commit()
    conn.close()

    data_file = f"{match_id}_data.pdf"
    # print("OVERS:", OVERS, '\nSCORE:', score, '\nWICKETS:', wickets)
    if(innings_no == 2 and OVERS == int(overs_lim)) or (innings_no == 2 and wickets==10) or (innings_no == 2 and score>=target):
        create_pdf(team_a_batting, team_b_bowling, team_b_batting, team_a_bowling, data_file)
        CTkMessagebox(title="Match Summary", message=f"Your match summary {data_file} has been saved.", icon="info", button_color="darkGreen")

def display():
    global main
    global s_lab,s1_lab,score_lab,score1_lab,w_lab,w1_lab,o_lab,o1_lab,bats1_lab,bats_lab,batsrunner_lab,batsrunner1_lab

    conn = sqlite3.connect('score.db')
    conn.row_factory= lambda cursor, row:row[0]
    c=conn.cursor()

    c.execute(f"""SELECT SCORE FROM {main}""")
    s=c.fetchall()

    if BALLS==0:
        crr=score
    else:
        crr1=score/BALLS
        crr=round(crr1,3)

    crr1_lab.configure(text=crr)

    c.execute(f"""SELECT WICKETS FROM {main}""")
    w=c.fetchall()

    c.execute(f"""SELECT OVERS FROM {main}""")
    o=c.fetchall()
    
    score1_lab.configure(text=s)
    w1_lab.configure(text=w)
    o1_lab.configure(text=o)

    conn.row_factory= lambda cursor, row:row[0]

    b1s=c.execute(f"SELECT RUNS FROM {batting_side} WHERE BATSMAN='{_1_bat_name}'").fetchall()
    b2s=c.execute(f"SELECT RUNS FROM {batting_side} WHERE BATSMAN='{_2_bat_name}'").fetchall()

    b1b=c.execute(f"SELECT BALLS FROM {batting_side} WHERE BATSMAN='{_1_bat_name}'").fetchall()
    b2b=c.execute(f"SELECT BALLS FROM {batting_side} WHERE BATSMAN='{_2_bat_name}'").fetchall()

    
    bats1score.configure(text=(b1s,"(",b1b,")"))
    bats2score.configure(text=(b2s,"(",b2b,")"))

    bo=c.execute(f"""SELECT OVERS FROM {bowling_side} WHERE BOWLER='{bowler_present}'""").fetchall()
    br=c.execute(f"""SELECT RUNS FROM {bowling_side} WHERE BOWLER='{bowler_present}'""").fetchall()
    bw=c.execute(f"""SELECT WICKETS FROM {bowling_side} WHERE BOWLER='{bowler_present}'""").fetchall()

    bowler_info.configure(text=(bo,"(",br,"/",bw,")"))

    bo1_lab.configure(text=bowler_present)

    if batsman_strike==_1_bat_name:
        bats1_lab.configure(text=f"{_1_bat_name}*")
        batsrunner1_lab.configure(text=f"{_2_bat_name}")
    elif batsman_strike==_2_bat_name:
        bats1_lab.configure(text=f"{_1_bat_name}")
        batsrunner1_lab.configure(text=f"{_2_bat_name}*")
    global recent
    global record_str
    record_str=" "
    for i in recent[::-1]:
        record_str+=f"{i}  "
    record1_lab.configure(text=record_str)
    # if OVERS%1==0 and OVERS!=0:
    #     recent=["","","","","","","","","",""]
    #     record_str=""

    if innings_no == 2 and BALLS>0:
        max_overs = int(overs_lim)
        current_overs = int(OVERS)
        current_balls = int((OVERS - current_overs) * 10)

        remaining_balls = (max_overs - current_overs) * 6 - current_balls
        bottom_news.configure(text=f"Need {target-score} on {remaining_balls} balls")

    conn.commit()
    conn.close()

def new_bowler():
    global ov
    global o
    global bowler_present
    bowler_present= ov.get()
    if bowler_present not in all_bowlers:
        current_bowler_balls[bowler_present]=0
        current_bowler_score[bowler_present]=0
        current_bowler_wickets[bowler_present]=0
        all_bowlers.add(bowler_present)
        bowler_name_func(bowler_present,bowling_side)
    # print(bowler_present,"is bowling now")
    o.destroy()
    display()

global innings_no
innings_no=1
def innings_change():
    global first_inning_score
    global first_inning_wicket
    global first_inning_over
    global batting_side
    global team_a_batting
    global team_a_bowling 
    global team_b_batting
    global team_b_bowling
    global bowling_side
    global b1e
    global b2e
    global bwe
    global ic
    global innings_no
    global BALLS
    global score
    global extras
    global wickets
    global target
    global bs
    global team_name1
    global team_name2
    global bottom_news
    global OVERS
    first_inning_score = score
    first_inning_wicket = wickets
    first_inning_over = OVERS

    target = score+1
    innings_no = 2
    BALLS = 0
    OVERS=0
    score = 0
    extras= 0
    wickets = 0
    recent = ["", "", "", "", "", "", "", "", "", ""]
    for i in l1:
        i.configure(state = "normal")
    next_over_b.place_forget()
    if batting_side==team_a_batting:
        bs=team_b
        batting_side = team_b_batting
        bowling_side = team_a_bowling
    elif batting_side==team_b_batting:
        bs=team_a
        batting_side = team_a_batting
        bowling_side = team_b_bowling
    # h.destroy()
    # summary()

    ic = Tk()
    ic.geometry("600x400")
    ic.title("NEW INNINGS RECORD")
    ic.resizable(False, False)

    ic_frame=CTkFrame(ic,width=600,height=400,fg_color="lightGreen")
    ic_frame.place(x=0,y=0)

    nin_lab=CTkLabel(ic_frame,text=f"TEAM {bs} INFO",fg_color="darkGreen",font=("Times",30),text_color="white",corner_radius=40)
    nin_lab.place(x=190,y=20)

    b1l =CTkLabel(ic_frame,text="Enter Batsman Name(Striker)",fg_color="darkGreen",font=("Times",25),text_color="white",corner_radius=40)
    b1l.place(x=10,y=100)
    
    b1e =CTkEntry(ic_frame,fg_color="white",width=220,text_color="darkGreen",font=("Times",20))
    b1e.place(x=350,y=100)

    b2l =CTkLabel(ic_frame,text="Enter Batsman Name(Runner)",fg_color="darkGreen",font=("Times",25),text_color="white",corner_radius=40)
    b2l.place(x=10,y=150)
    
    b2e =CTkEntry(ic_frame,fg_color="white",width=220,text_color="darkGreen",font=("Times",20))
    b2e.place(x=350,y=150)
    
    bwl =CTkLabel(ic_frame,text="Enter Bowler Name",fg_color="darkGreen",font=("Times",25),text_color="white",corner_radius=40)
    bwl.place(x=10,y=200)
    
    bwe =CTkEntry(ic_frame,fg_color="white",width=220,text_color="darkGreen",font=("Times",20))
    bwe.place(x=350,y=200)

    ic_but=CTkButton(ic_frame,text="DONE",command=innings_change2,bg_color="lightGreen",fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",25,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    ic_but.place(x=150,y=250)

    bottom_news = CTkLabel(score_f, text=f"Need {target-score} on {int(overs_lim) * 6} balls", fg_color="gray",font=("Times",18),text_color="white",corner_radius=40, width=50,height=20)
    bottom_news.place(x=380, y=360)

    ic.mainloop()

def innings_change2():
    global bowling_side
    global b1e
    global b2e
    global bwe
    global ic
    global _1_bat_name
    global _2_bat_name
    global bowler_present
    global batsman_strike
    global recent, record_str
    global current_batsmen_balls,current_batsmen_score,current_bowler_balls,current_bowler_score,current_bowler_wickets
    global all_bowlers
    # print(b1e.get(),"HELLOOOO")
    _1_bat_name = str(b1e.get())
    batsman_strike = _1_bat_name
    _2_bat_name = str(b2e.get())
    bowler_present = bwe.get()
    # print(_1_bat_name, " is the new batter for second innings")
    conn=sqlite3.connect("score.db")
    c=conn.cursor()
    c.execute(f"""UPDATE {main} SET SCORE=0,WICKETS=0,OVERS=0""")
    conn.commit()
    conn.close()

    batter_name(str(_1_bat_name),str(_2_bat_name),batting_side)
    bowler_name_func(str(bowler_present),bowling_side)

    s1_lab.configure(text=bs)

    t_lab=CTkLabel(score_f,text="Target",fg_color="darkGreen",font=("Times",20),text_color="white",corner_radius=40)
    t_lab.place(x=660,y=400)

    t1_lab=CTkLabel(score_f,text=target,fg_color="white",font=("Times",18),text_color="darkGreen",corner_radius=40)
    t1_lab.place(x=740,y=400)

    current_batsmen_score = dict()
    current_batsmen_balls = dict()
    current_bowler_score = dict()
    current_bowler_balls = dict()
    current_bowler_wickets= dict()
    all_bowlers ={bowler_present}

    current_batsmen_score[_1_bat_name]=0
    current_batsmen_score[_2_bat_name]=0

    current_batsmen_balls[_1_bat_name]=0
    current_batsmen_balls[_2_bat_name]=0

    current_bowler_score[bowler_present]=0
    current_bowler_balls[bowler_present]=0
    current_bowler_wickets[bowler_present]=0
    # print(current_batsmen_score)
    # print(str(_1_bat_name))
    recent=["", "", "", "", "", "", "", "", "", ""]
    record_str = ""
    display()
    ic.destroy()

def over_change():
    global batsman_strike
    global _1_bat_name
    global _2_bat_name
    # global ov_g
    global ov
    global o
    global new_bowler
    # ov_g = StringVar()
    global bowler_present
    global recent
    global all_bowlers
    global OVERS
    global BALLS
    global overs_lim
    global innings_no
    # print(recent)
    if innings_no == 1:
        if OVERS == int(overs_lim):
            innings_change()
            return 1
    elif innings_no ==2 and OVERS==int(overs_lim):
         return match_finish()
    if batsman_strike==_1_bat_name:
        batsman_strike=_2_bat_name
    else:
        batsman_strike=_1_bat_name

    if batsman_strike==_1_bat_name:
        bats1_lab.configure(text=f"{_1_bat_name}*")
        batsrunner1_lab.configure(text=f"{_2_bat_name}")
    elif batsman_strike==_2_bat_name:
        bats1_lab.configure(text=f"{_1_bat_name}")
        batsrunner1_lab.configure(text=f"{_2_bat_name}*")

    
    o=Tk()
    o.geometry("500x300+150+100")
    o.title("New Bowler")
    o.resizable(False, False)
    o_frame=CTkFrame(o,width=500,height=300,fg_color="lightGreen")
    o_frame.place(x=0,y=0)
    d_lab=CTkLabel(o_frame,text=f"{bowler_present}'s Over has been ended",text_color="darkGreen",font=("Georgia",35,"italic"),width=70)
    d_lab.place(x=30,y=20)

    n_lab=CTkLabel(o_frame,text="Enter new bowler name",fg_color="darkGreen",corner_radius=3,text_color="white",font=("Times",30))
    n_lab.place(x=80,y=100)

    ov=customtkinter.CTkComboBox(o_frame, values=["Bowler name"], dropdown_fg_color="white", dropdown_text_color="green", dropdown_font=("Arial",15),dropdown_hover_color="darkGreen", width=270, height=30, border_width=2, button_color="green", border_color="green", button_hover_color="darkGreen")
    ov.place(x=80,y=150)
    options = tuple(all_bowlers)
    ov.configure(values=(options))

    ov_but=CTkButton(o_frame, text="OK", command=new_bowler, bg_color="lightGreen", fg_color="#FF0000", hover=True, hover_color="orange", font=("Arial",25,"bold"), corner_radius=15, border_width=3, border_color="darkGreen", width=50, height=20)
    ov_but.place(x=230,y=200)

    for i in l1:
        i.configure(state = "normal")
    next_over_b.place_forget()
    
    o.mainloop()


def new_batsman():
    global batting_side
    global batsman_strike
    global current_batsmen_score
    global current_batsmen_balls
    global _1_bat_name
    global _2_bat_name
    global OVERS
    global ov
    global w
    global ovget
    global dismissed
    global new_batter
    w = Tk()
    ovget = StringVar(w)
    
    # print(batsman_strike)
    w.geometry("500x300+150+100")
    w.title("New Batsman")
    w.resizable(False, False)
    w_frame=CTkFrame(w,width=500,height=300,fg_color="lightGreen")
    w_frame.place(x=0,y=0)
    d_lab=CTkLabel(w_frame,text=f"{dismissed} has been dismissed",text_color="darkGreen",font=("Georgia",35,"italic"),width=70)
    d_lab.place(x=30,y=20)

    n_lab=CTkLabel(w_frame,text="Enter new batsman name",fg_color="darkGreen",corner_radius=3,text_color="white",font=("Times",30))
    n_lab.place(x=80,y=100)
    ov=CTkEntry(w_frame,textvariable=ovget,fg_color="white",width=300,text_color="darkGreen",font=("Times",25))
    ov.place(x=80,y=150)
    
    ov_but=CTkButton(w_frame,text="OK",command=new_batter,bg_color="lightGreen",fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",25,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    ov_but.place(x=230,y=200)
    w.mainloop()

def new_batter(): 
    global batsman_strike
    global ovget
    global w
    global _1_bat_name
    global _2_bat_name
    global dismissed
    global OVERS
    w.destroy()
    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    if dismissed==_1_bat_name:
        _1_bat_name = ovget.get()
        # print(_1_bat_name,"has arrived to the crease")
        batsman_strike = ovget.get()
        current_batsmen_score[_1_bat_name]=0
        current_batsmen_balls[_1_bat_name]=0
        
        c.execute(f"""INSERT INTO {batting_side} VALUES('{_1_bat_name}',0,0,0)""")
    elif dismissed==_2_bat_name:
        _2_bat_name = str(ovget.get())
        # print(_2_bat_name,"has arrived to the crease")
        batsman_strike = ovget.get()
        current_batsmen_score[_2_bat_name]=0
        current_batsmen_balls[_2_bat_name]=0
        
        c.execute(f"""INSERT INTO {batting_side} VALUES('{_2_bat_name}',0,0,0)""")
    conn.commit()
    conn.close()
    display()
    if OVERS%1==0 and OVERS!=0.0:
        over_change()

target=0
score=0
wickets=0
BALLS=0
global recent
recent =['','','','','','','','','','']

def match_finish():
    global target
    global score
    global batting_side
    global bowling_side
    global winner
    global BALLS

    if score >= target:
        if batting_side == team_a_batting:
            winner = team_a
        elif batting_side == team_b_batting:
            winner = team_b
    elif score == target-1 and OVERS==int(overs_lim):
        winner = "DRAWN"
    elif score < target:
        if bowling_side == team_a_bowling:
            winner = team_a
        elif bowling_side == team_b_bowling:
            winner = team_b
    if winner == "DRAWN":
        win_msg = CTkMessagebox(master=h, message="Match ended in a DRAW.", icon="info", option_1="Exit")
    else:
        win_msg = CTkMessagebox(master=h, message=f"Match ended, Match won by {winner}", icon="info", option_1="Exit")
    if win_msg.get() == "Exit":
        h.destroy()
        summary()

def dot():
    global score
    global BALLS
    global batsman_strike
    global current_batsmen_balls
    global current_bowler_balls
    global current_bowler_wickets
    global current_batsmen_score
    global current_bowler_score
    global bowler_present
    global recent
    global batting_side
    global bowling_side
    global a
    global b

    recent.pop()
    recent.insert(0,'DOT')
    # print(recent)
    BALLS+=1
    X= BALLS//6
    Y=(BALLS%6)/10
    global OVERS
    OVERS = X+Y
    current_batsmen_balls[batsman_strike]+=1
    current_bowler_balls[bowler_present]+=1
    a = current_bowler_balls[bowler_present]//6
    b= (current_bowler_balls[bowler_present]%6)/10
    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    
    c.execute(f"""UPDATE {main} SET SCORE={score},OVERS={OVERS}""")
    c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE ={(current_batsmen_score[batsman_strike]/current_batsmen_balls[batsman_strike])*100} WHERE BATSMAN = '{batsman_strike}'""")
    c.execute(f"""UPDATE {bowling_side} SET OVERS={a+b},RUNS ={current_bowler_score[bowler_present]},WICKETS ={current_bowler_wickets[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
    
    
    # print(OVERS,score)
    conn.commit()
    conn.close()
    display()
    
    if OVERS%1==0 and OVERS!=0.0:
        global l1
        next_over_b.place(x=20, y=275)
        l1 = [dot_b,one_b,two_b,three_b,four_b,six_b,wd_b,out_b,byes_1,byes_2,byes_3,byes_4, byes_wide_1,byes_wide_2,byes_wide_3,byes_wide_4, runout_b]
        for i in l1:
            i.configure(state = "disabled")

def one():
    global score
    global BALLS
    global batsman_strike
    global current_batsmen_balls
    global current_batsmen_score
    global current_bowler_score
    global current_bowler_balls
    global current_bowler_wickets
    global a 
    global b
    global _1_bat_name
    global _2_bat_name
    global bowler_present
    global OVERS
    global recent
    global target
    global wickets
    global innings_no

    recent.pop()
    recent.insert(0,'1')
    score=score+1
    BALLS+=1
    X= BALLS//6
    Y=(BALLS%6)/10
    OVERS = X+Y
    current_batsmen_score[batsman_strike]+=1
    current_batsmen_balls[batsman_strike]+=1
    current_bowler_score[bowler_present]+=1
    current_bowler_balls[bowler_present]+=1
    a = current_bowler_balls[bowler_present]//6
    b= (current_bowler_balls[bowler_present]%6)/10
    # print(batsman_strike," score is ",current_batsmen_score[batsman_strike],"on",current_batsmen_balls[batsman_strike])

    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    c.execute(f"""UPDATE {main} SET SCORE={score}""")
    
    c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
    c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE ={(current_batsmen_score[batsman_strike]/current_batsmen_balls[batsman_strike])*100} WHERE BATSMAN = '{batsman_strike}'""")
    c.execute(f"""UPDATE {bowling_side} SET OVERS={a+b},RUNS ={current_bowler_score[bowler_present]},WICKETS ={current_bowler_wickets[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
    
    conn.commit()
    conn.close()
    display()
    if batsman_strike == _1_bat_name:
        batsman_strike=_2_bat_name
    else:
        batsman_strike =_1_bat_name

    if batsman_strike==_1_bat_name:
        bats1_lab.configure(text=f"{_1_bat_name}*")
        batsrunner1_lab.configure(text=f"{_2_bat_name}")
    elif batsman_strike==_2_bat_name:
        bats1_lab.configure(text=f"{_1_bat_name}")
        batsrunner1_lab.configure(text=f"{_2_bat_name}*")

    if innings_no==2 and (score>=target or wickets==10):
        return match_finish()
    # print(OVERS,score)
    if OVERS%1==0 and OVERS!=0.0:
        global l1
        next_over_b.place(x=20, y=275)
        l1 = [dot_b,one_b,two_b,three_b,four_b,six_b,wd_b,out_b,byes_1,byes_2,byes_3,byes_4, byes_wide_1,byes_wide_2,byes_wide_3,byes_wide_4, runout_b]
        for i in l1:
            i.configure(state = "disabled")


def two():
    global score
    global BALLS
    global batsman_strike
    global _1_bat_name
    global _2_bat_name
    global OVERS
    global current_batsmen_score
    global current_batsmen_balls
    global current_bowler_score
    global current_bowler_balls
    global current_bowler_wickets
    global a
    global b
    global bowler_present
    global recent
    global wickets 
    global target
    global innings_no
    recent.pop()
    recent.insert(0,'2')
    score=score+2
    BALLS+=1
    X= BALLS//6
    Y=(BALLS%6)/10
    OVERS = X+Y
    current_batsmen_score[batsman_strike]+=2
    current_batsmen_balls[batsman_strike]+=1
    current_bowler_score[bowler_present]+=2
    current_bowler_balls[bowler_present]+=1
    a = current_bowler_balls[bowler_present]//6
    b= (current_bowler_balls[bowler_present]%6)/10
    # print(batsman_strike,"batsman score is ",current_batsmen_score[batsman_strike])

    conn = sqlite3.connect('score.db')
    c=conn.cursor()    
    c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
    c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE ={(current_batsmen_score[batsman_strike]/current_batsmen_balls[batsman_strike])*100} WHERE BATSMAN = '{batsman_strike}'""")
    c.execute(f"""UPDATE {bowling_side} SET OVERS={a+b},RUNS ={current_bowler_score[bowler_present]},WICKETS ={current_bowler_wickets[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
    conn.commit()
    conn.close()
    
    
    # print(OVERS,score)

    if batsman_strike==_1_bat_name:
        bats1_lab.configure(text=f"{_1_bat_name}*")
        batsrunner1_lab.configure(text=f"{_2_bat_name}")
    elif batsman_strike==_2_bat_name:
        bats1_lab.configure(text=f"{_1_bat_name}")
        batsrunner1_lab.configure(text=f"{_2_bat_name}*")

    display()

    if innings_no==2 and (score>=target or wickets==10):
        return match_finish()
    if OVERS%1==0 and OVERS!=0.0:
        global l1
        next_over_b.place(x=20, y=275)
        l1 = [dot_b,one_b,two_b,three_b,four_b,six_b,wd_b,out_b,byes_1,byes_2,byes_3,byes_4, byes_wide_1,byes_wide_2,byes_wide_3,byes_wide_4, runout_b]
        for i in l1:
            i.configure(state = "disabled")

def three():
    global score
    global BALLS
    global batsman_strike
    global OVERS
    global _1_bat_name
    global _2_bat_name
    global current_bowler_score
    global current_bowler_balls
    global bowler_present
    global current_batsmen_balls
    global current_batsmen_score
    global current_bowler_wickets
    global a
    global b
    global recent
    global wickets
    global target
    global innings_no

    recent.pop()
    recent.insert(0,'3')
    score=score+3
    BALLS+=1
    X= BALLS//6
    Y=(BALLS%6)/10
    OVERS = X+Y
    current_batsmen_score[batsman_strike]+=3
    current_batsmen_balls[batsman_strike]+=1
    current_bowler_score[bowler_present]+=3
    current_bowler_balls[bowler_present]+=1
    a = current_bowler_balls[bowler_present]//6
    b= (current_bowler_balls[bowler_present]%6)/10
    r=current_batsmen_score[batsman_strike]
    d =current_batsmen_balls[batsman_strike]
    sr = (r/d)*100
    # print(batsman_strike,"batsman score is ",current_batsmen_score[batsman_strike])
    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    c.execute(f"""UPDATE {batting_side} SET RUNS={r},BALLS={d},STRIKE_RATE ={sr} WHERE BATSMAN = '{batsman_strike}' """)
    c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets},SCORE ={score}""")
    c.execute(f"""UPDATE {bowling_side} SET OVERS={a+b},RUNS ={current_bowler_score[bowler_present]},WICKETS ={current_bowler_wickets[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
    conn.commit()
    conn.close()
   
    if batsman_strike == _1_bat_name:
        batsman_strike=_2_bat_name
    else:
        batsman_strike =_1_bat_name

    if batsman_strike==_1_bat_name:
        bats1_lab.configure(text=f"{_1_bat_name}*")
        batsrunner1_lab.configure(text=f"{_2_bat_name}")
    elif batsman_strike==_2_bat_name:
        bats1_lab.configure(text=f"{_1_bat_name}")
        batsrunner1_lab.configure(text=f"{_2_bat_name}*")

    display()

    if innings_no==2 and (score>=target or wickets==10):
        return match_finish()
    if OVERS%1==0 and OVERS!=0.0:
        global l1
        next_over_b.place(x=20, y=275)
        l1 = [dot_b,one_b,two_b,three_b,four_b,six_b,wd_b,out_b,byes_1,byes_2,byes_3,byes_4, byes_wide_1,byes_wide_2,byes_wide_3,byes_wide_4, runout_b]
        for i in l1:
            i.configure(state = "disabled")
    # print(OVERS,score)


def four():
    global score
    global BALLS
    global OVERS
    global current_bowler_score
    global current_bowler_balls
    global bowler_present
    global current_batsmen_balls
    global current_batsmen_score
    global current_bowler_wickets
    global a
    global b
    global recent
    global wickets 
    global target
    global innings_no

    recent.pop()
    recent.insert(0,'4')
    score=score+4
    BALLS+=1
    X= BALLS//6
    Y=(BALLS%6)/10
    OVERS = X+Y
    current_bowler_score[bowler_present]+=4
    current_bowler_balls[bowler_present]+=1
    current_batsmen_score[batsman_strike]+=4
    current_batsmen_balls[batsman_strike]+=1
    a = current_bowler_balls[bowler_present]//6
    b= (current_bowler_balls[bowler_present]%6)/10
    # print(batsman_strike,"batsman score is ",current_batsmen_score[batsman_strike])
    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
    c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE ={(current_batsmen_score[batsman_strike]/current_batsmen_balls[batsman_strike])*100} WHERE BATSMAN = '{batsman_strike}'""")
    c.execute(f"""UPDATE {bowling_side} SET OVERS={a+b},RUNS ={current_bowler_score[bowler_present]},WICKETS ={current_bowler_wickets[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
    conn.commit()
    conn.close()
    

    if batsman_strike==_1_bat_name:
        bats1_lab.configure(text=f"{_1_bat_name}*")
        batsrunner1_lab.configure(text=f"{_2_bat_name}")
    elif batsman_strike==_2_bat_name:
        bats1_lab.configure(text=f"{_1_bat_name}")
        batsrunner1_lab.configure(text=f"{_2_bat_name}*")

    display()

    if innings_no==2 and (score>=target or wickets==10):
        return match_finish()

    

    if OVERS%1==0 and OVERS!=0.0:
        global l1
        next_over_b.place(x=20, y=275)
        l1 = [dot_b,one_b,two_b,three_b,four_b,six_b,wd_b,out_b,byes_1,byes_2,byes_3,byes_4, byes_wide_1,byes_wide_2,byes_wide_3,byes_wide_4, runout_b]
        for i in l1:
            i.configure(state = "disabled")
    # print(OVERS,score)


def six():
    global score
    global BALLS
    global OVERS
    global current_bowler_score
    global current_bowler_balls
    global current_batsmen_balls
    global current_batsmen_score
    global current_bowler_wickets
    global a
    global b
    global bowler_present
    global recent
    global target
    global wickets
    global innings_no

    recent.pop()

    recent.insert(0,'6')
    current_bowler_score[bowler_present]+=6
    current_bowler_balls[bowler_present]+=1
    score=score+6
    BALLS+=1
    X= BALLS//6
    Y=(BALLS%6)/10
    OVERS = X+Y
    current_batsmen_score[batsman_strike]+=6
    global current_batsmen_balls
    current_batsmen_balls[batsman_strike]+=1
    a = current_bowler_balls[bowler_present]//6
    b= (current_bowler_balls[bowler_present]%6)/10
    # print(batsman_strike,"batsman score is ",current_batsmen_score[batsman_strike])
    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
    c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE ={(current_batsmen_score[batsman_strike]/current_batsmen_balls[batsman_strike])*100} WHERE BATSMAN = '{batsman_strike}' """)
    c.execute(f"""UPDATE {bowling_side} SET OVERS={a+b},RUNS ={current_bowler_score[bowler_present]},WICKETS ={current_bowler_wickets[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
    conn.commit()
    conn.close()

    display()

    if innings_no==2 and (score>=target or wickets==10):
        return match_finish()
    if OVERS%1==0 and OVERS!=0.0:
        global l1
        next_over_b.place(x=20, y=275)
        l1 = [dot_b,one_b,two_b,three_b,four_b,six_b,wd_b,out_b,byes_1,byes_2,byes_3,byes_4, byes_wide_1,byes_wide_2,byes_wide_3,byes_wide_4, runout_b]
        for i in l1:
            i.configure(state = "disabled")
    # print(OVERS,score)

def wd():
    global score
    global current_bowler_score
    global bowler_present
    global extras
    global recent
    global target 
    global wickets
    global innings_no

    recent.pop()
    recent.insert(0,'WD')
    current_bowler_score[bowler_present]+=1
    score+=1
    extras +=1
    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    c.execute(f"""UPDATE {main} SET SCORE={score}""")
    c.execute(f"""UPDATE {bowling_side} SET RUNS ={current_bowler_score[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
    conn.commit()
    conn.close()

    display()
    
    if innings_no==2 and (score>=target or wickets==10):
        return match_finish()

def nb():
    global score
    global BALLS
    global current_bowler_score
    global bowler_present
    global extras
    global recent
    global target
    global wickets
    global innings_no

    recent.pop()
    recent.insert(0,'NB')
    if BALLS==0:
        CTkMessagebox(title="Error", message="Please enter the score of this ball first.", icon="info", button_color="darkGreen")
        # messagebox.showerror("ERROR","Please enter the score of this ball first.")
        return     
    BALLS-=1
    X= BALLS//6
    Y=(BALLS%6)/10
    OVERS = X+Y
    current_bowler_score[bowler_present]+=1
    current_bowler_balls[bowler_present]-=1
    score+=1
    extras +=1
    a = current_bowler_balls[bowler_present]//6
    b= (current_bowler_balls[bowler_present]%6)/10
    
    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
    c.execute(f"""UPDATE {bowling_side} SET OVERS={a+b},RUNS ={current_bowler_score[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
    conn.commit()
    conn.close()

    display()
    
    if innings_no==2 and (score>=target or wickets==10):
        return match_finish()
    freehit()
    # print(OVERS,score)

def bind():
    f1.destroy()

def freehit():
    global f1
    global new
    f1=CTkFrame(new,width=345,border_color="darkGreen",border_width=5,corner_radius=0,height=340,bg_color="lightBlue")
    f1.place(x=0,y=300)

    freelab=CTkLabel(f1,text="FREE HIT",width=345,font=("Arial Black",26),text_color="orange",height=35,fg_color="darkBlue")
    freelab.place(x=0,y=0)

    dot_bb=CTkButton(f1,text="DOT",command=lambda:[bind(),dot()],fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=30,height=20)
    dot_bb.place(x=30,y=40)
    
    one_bb=CTkButton(f1,text="1",command =lambda:[bind(),one()],width=50,height=20,fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen")
    one_bb.place(x=115,y=40)

    two_bb=CTkButton(f1,text="2",command =lambda:[bind(),two()],fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    two_bb.place(x=185,y=40)
    
    three_bb=CTkButton(f1,text="3",command =lambda:[bind(),three()],fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    three_bb.place(x=255,y=40)
    
    four_bb=CTkButton(f1,text="4",command =lambda:[bind(),four()],fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    four_bb.place(x=115,y=80)
    
    six_bb=CTkButton(f1,text="6",command =lambda:[bind(),six()],fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    six_bb.place(x=185,y=80)
    
    wd_bb=CTkButton(f1,text="WD",command=lambda:[bind(),wd()],fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    wd_bb.place(x=30,y=80)

    byes_1b=CTkButton(f1,text="B1",command=lambda:[bind(),byes_1_f()],fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    byes_1b.place(x=30,y=120)

    byes_2b=CTkButton(f1,text="B2",command=lambda:[bind(),byes_2_f()],fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    byes_2b.place(x=115,y=120)

    byes_3b=CTkButton(f1,text="B3",command=lambda:[bind(),byes_3_f()],fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    byes_3b.place(x=185,y=120)

    byes_4b=CTkButton(f1,text="B4",command=lambda:[bind(),byes_4_f()],fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    byes_4b.place(x=255,y=120)

    byes_wide_1b=CTkButton(f1,text="WD-BYE1",command=lambda:[bind(),wide_1()],fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=30,height=20)
    byes_wide_1b.place(x=50,y=160)

    byes_wide_2b=CTkButton(f1,text="WD-BYE2",command=lambda:[bind(),wide_2()],fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=30,height=20)
    byes_wide_2b.place(x=180,y=160)

    byes_wide_3b=CTkButton(f1,text="WD-BYE3",command=lambda:[bind(),wide_3()],fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=30,height=20)
    byes_wide_3b.place(x=50,y=200)

    byes_wide_4b=CTkButton(f1,text="WD-BYE4",command=lambda:[bind(),wide_4()],fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=30,height=20)
    byes_wide_4b.place(x=180,y=200)

    runout_bb=CTkButton(f1,text="RUN-OUT",command=lambda:[bind(),run_out()],fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",15,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=30,height=20)
    runout_bb.place(x=50,y=240)
    
def out():
    global wickets
    global BALLS
    global batsman_strike
    global OVERS
    global new_batsman
    global current_bowler_balls
    global bowler_present
    global dismissed
    global current_bowler_wickets
    global recent
    global wickets
    global target
    global innings_no

    recent.pop()
    recent.insert(0,'OUT')
    dismissed = batsman_strike
    current_bowler_balls[bowler_present]+=1
    current_bowler_wickets[bowler_present]+=1
    a = current_bowler_balls[bowler_present]//6
    b= (current_bowler_balls[bowler_present]%6)/10
    # current_batsmen_score.pop(dismissed)
    # current_batsmen_balls.pop(dismissed)
    BALLS+=1
    wickets+=1
    if innings_no == 1 and wickets == 10:
        innings_change()
    X= BALLS//6
    Y=(BALLS%6)/10
    OVERS = X+Y
    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    
    c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets},WICKETS ={wickets}""")
    c.execute(f"""UPDATE {bowling_side} SET OVERS={a+b},WICKETS ={current_bowler_wickets[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
    conn.commit()
    conn.close()
    
    display()
    
    
    if innings_no==2 and (score>=target or wickets==10):
        return match_finish()
    # print(batsman_strike,"has been dismissed!!")
    new_batsman()
    


def run_out():
    global ro
    global ask1
    global ask2
    global recent
    

    ro=Tk()
    ro.geometry("500x300+150+100")
    ro.title("RUN-OUT")
    ro_frame=CTkFrame(ro,width=500,height=300,fg_color="lightGreen")
    ro_frame.place(x=0,y=0)
    d_lab=CTkLabel(ro_frame,text="Which Batsman got out?",text_color="darkGreen",font=("Georgia",20,"italic"),width=70)
    d_lab.place(x=80,y=20)

    ask1=customtkinter.CTkComboBox(ro_frame,dropdown_fg_color="white",values=" ",dropdown_text_color="green",dropdown_font=("Arial",20),dropdown_hover_color="darkGreen",width=270,height=30,border_width=2,button_color="green",border_color="green",button_hover_color="darkGreen")
    ask1.place(x=80,y=70)
    ask1.configure(values=[_1_bat_name,_2_bat_name])

    f_lab=CTkLabel(ro_frame,text="How many runs were scored in this ball?",text_color="darkGreen",font=("Georgia",20,"italic"),width=70)
    f_lab.place(x=80,y=120)

    ask2=customtkinter.CTkComboBox(ro_frame,dropdown_fg_color="white",values=" ",dropdown_text_color="green",dropdown_font=("Arial",20),dropdown_hover_color="darkGreen",width=270,height=30,border_width=2,button_color="green",border_color="green",button_hover_color="darkGreen")
    ask2.place(x=80,y=170)
    ask2.configure(values=("DOT","1","2","3","W1","W2","W3","B1","B2","B3"))


    ro_but=CTkButton(ro_frame,text="OK",command=run_out2,bg_color="lightGreen",fg_color="#FF0000",hover=True,hover_color="orange",font=("Arial",25,"bold"),corner_radius=15,border_width=3,border_color="darkGreen",width=50,height=20)
    ro_but.place(x=230,y=220)
    ro.mainloop()

def run_out2():
    global current_bowler_wickets
    global bowler_present
    global dismissed
    global wickets  
    dismissed =ask1.get()
    runs_run_out =ask2.get()
    recent.pop()
    recent.insert(0,f'RO({runs_run_out})')
    # print("but runs scored on this ball were",runs_run_out)
    if runs_run_out =="1":
        wickets+=1
        one()
        recent.pop(0)
        current_bowler_wickets[bowler_present]+=1
        display()
        ro.destroy()
        
        
    elif runs_run_out =="2":
        wickets+=1
        two()
        recent.pop(0)
        display()
        ro.destroy()
        current_bowler_wickets[bowler_present]+=1
    elif runs_run_out =="3":
        wickets+=1
        three()
        recent.pop(0)
        display()
        ro.destroy()
    elif runs_run_out =="wide1":
        wickets+=1
        wide_1()
        recent.pop(0)
        display()
        ro.destroy()
        current_bowler_wickets[bowler_present]+=1
    elif runs_run_out =="wide2":
        wickets+=1
        wide_2()
        current_bowler_wickets[bowler_present]+=1
        display()
        ro.destroy()
        
    elif runs_run_out =="wide3":
        wickets+=1
        wide_3()
        recent.pop(0)
        current_bowler_wickets[bowler_present]+=1
        display()
        ro.destroy()
        
    elif runs_run_out =="bye1":
        wickets+=1
        byes_1_f()
        recent.pop(0)
        current_bowler_wickets[bowler_present]+=1
        ro.destroy()
        display()
        
    elif runs_run_out =="bye2":
        wickets+=1
        byes_2_f()
        recent.pop(0)
        current_bowler_wickets[bowler_present]+=1
        display()
        ro.destroy()
        
    elif runs_run_out =="bye3":
        wickets+=1
        byes_3_f()
        recent.pop(0)
        current_bowler_wickets[bowler_present]+=1
        display()
        ro.destroy()
    elif runs_run_out == "DOT":
        wickets+=1
        dot()
        recent.pop(0)
        current_bowler_wickets[bowler_present]+=1
        display()
        ro.destroy()

    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets},WICKETS ={wickets}""")
    c.execute(f"""UPDATE {bowling_side} SET WICKETS ={current_bowler_wickets[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
    conn.commit()
    conn.close()
    # print(dismissed,"has been dismissed!")
    new_batsman()
def byes_1_f():
    global score
    global BALLS
    global OVERS
    global current_bowler_balls
    global bowler_present
    global batsman_strike
    global extras
    global recent
    global target
    global wickets
    global innings_no

    recent.pop()
    recent.insert(0,'B1')
    score=score+1
    extras+=1
    BALLS+=1
    X= BALLS//6
    Y=(BALLS%6)/10
    OVERS = X+Y
    global current_batsmen_balls
    current_batsmen_balls[batsman_strike]+=1
    current_bowler_balls[bowler_present]+=1
    a = current_bowler_balls[bowler_present]//6
    b= (current_bowler_balls[bowler_present]%6)/10
    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    c.execute(f"""UPDATE {bowling_side} SET OVERS ={a+b} WHERE bowler='{bowler_present}'""")
    c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
    conn.commit()
    conn.close()
    
    if batsman_strike == _1_bat_name:
        batsman_strike=_2_bat_name
    else:
        batsman_strike =_1_bat_name

    display()

    if innings_no==2 and (score>=target or wickets==10):
        return match_finish()
    if OVERS%1==0 and OVERS!=0.0:
           over_change()
    # print(OVERS,score)

def byes_2_f():
    global score
    global BALLS
    global OVERS
    global current_bowler_balls
    global bowler_present
    global batsman_strike
    global extras
    global recent
    global target
    global wickets
    global innings_no

    recent.pop()
    recent.insert(0,'B2')
    extras+=2
    current_bowler_balls[bowler_present]+=1

    score=score+2
    BALLS+=1
    X= BALLS//6
    Y=(BALLS%6)/10
    OVERS = X+Y
    global current_batsmen_balls
    current_batsmen_balls[batsman_strike]+=1
    a = current_bowler_balls[bowler_present]//6
    b= (current_bowler_balls[bowler_present]%6)/10
    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    c.execute(f"""UPDATE {bowling_side} SET OVERS ={a+b} WHERE bowler='{bowler_present}'""")
    c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
    conn.commit()
    conn.close()
    
    display()

    if innings_no==2 and (score>=target or wickets==10):
        return match_finish()
    if OVERS%1==0 and OVERS!=0.0:
           over_change()
    # print(OVERS,score)
    
def byes_3_f():
    global score
    global BALLS
    global OVERS
    global current_bowler_balls
    global bowler_present
    global batsman_strike
    global extras
    global recent
    global target
    global wickets
    global innings_no

    recent.pop()
    recent.insert(0,'B3')
    extras+=3
    current_bowler_balls[bowler_present]+=1

    score=score+3
    BALLS+=1
    X= BALLS//6
    Y=(BALLS%6)/10
    OVERS = X+Y
    global current_batsmen_balls
    current_batsmen_balls[batsman_strike]+=1
    a = current_bowler_balls[bowler_present]//6
    b= (current_bowler_balls[bowler_present]%6)/10
    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    c.execute(f"""UPDATE {bowling_side} SET OVERS ={a+b} WHERE bowler='{bowler_present}'""")
    c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
    conn.commit()
    conn.close()
    
    if batsman_strike == _1_bat_name:
        batsman_strike=_2_bat_name
    else:
        batsman_strike =_1_bat_name


    display()

    if innings_no==2 and (score>=target or wickets==10):
        return match_finish()
    if OVERS%1==0 and OVERS!=0.0:
           over_change()
    # print(OVERS,score)

def byes_4_f():
    global score
    global BALLS
    global OVERS
    global current_bowler_balls
    global bowler_present
    global batsman_strike
    global extras
    global recent
    global target
    global wickets
    global innings_no

    recent.pop()
    recent.insert(0,'B4')
    extras+=4
    current_bowler_balls[bowler_present]+=1
    score=score+4
    BALLS+=1
    X= BALLS//6
    Y=(BALLS%6)/10
    OVERS = X+Y
    global current_batsmen_balls
    current_batsmen_balls[batsman_strike]+=1
    a = current_bowler_balls[bowler_present]//6
    b= (current_bowler_balls[bowler_present]%6)/10
    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    c.execute(f"""UPDATE {bowling_side} SET OVERS ={a+b} WHERE bowler='{bowler_present}'""")
    c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
    conn.commit()
    conn.close()




    display()
    
    if innings_no==2 and (score>=target or wickets==10):
        return match_finish()
    if OVERS%1==0 and OVERS!=0.0:
           over_change()
    # print(OVERS,score)
    
def wide_1():
    global score
    global BALLS
    global recent
    global target
    global wickets
    global innings_no
    global batsman_strike

    recent.pop()
    recent.insert(0,'W1')
    global extras
    extras+=2
    score=score+2
    current_bowler_score[bowler_present]+=2
    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    c.execute(f"""UPDATE {main} SET SCORE={score} """)
    c.execute(f"""UPDATE {bowling_side} SET RUNS={current_bowler_score[bowler_present]} WHERE bowler ='{bowler_present}' """)

    conn.commit()
    conn.close()
    
    if batsman_strike == _1_bat_name:
        batsman_strike=_2_bat_name
    else:
        batsman_strike =_1_bat_name


    display()
    
    if innings_no==2 and (score>=target or wickets==10):
        return match_finish()

def wide_2():
    global score
    global BALLS
    global extras
    global recent
    global target
    global wickets
    global innings_no
    global batsman_strike

    recent.pop()
    recent.insert(0,'W2')
    extras+=3
    score=score+3
    current_bowler_score[bowler_present]+=3
    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    c.execute(f"""UPDATE {main} SET SCORE={score} """)
    c.execute(f"""UPDATE {bowling_side} SET RUNS={current_bowler_score[bowler_present]} WHERE bowler ='{bowler_present}' """)

    conn.commit()
    conn.close()


    display()
    
    if innings_no==2 and (score>=target  or wickets==10):
        return match_finish()

def wide_3():
    global score
    global BALLS
    global extras
    global recent
    global target
    global wickets
    global innings_no
    global batsman_strike

    recent.pop()
    recent.insert(0,'W3')
    extras+=4
    score=score+4
    current_bowler_score[bowler_present]+=4
    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    c.execute(f"""UPDATE {main} SET SCORE={score} """)
    c.execute(f"""UPDATE {bowling_side} SET RUNS={current_bowler_score[bowler_present]} WHERE bowler ='{bowler_present}' """)
    conn.commit()
    conn.close()
    
    if batsman_strike == _1_bat_name:
        batsman_strike=_2_bat_name
    else:
        batsman_strike =_1_bat_name

    display()

    if innings_no==2 and (score>=target or wickets==10):
        return match_finish()

def wide_4():
    global score
    global BALLS
    global extras
    global recent
    global target
    global wickets
    global innings_no
    global batsman_strike

    recent.pop()
    recent.insert(0,'W4')
    extras+=5
    score=score+5
    current_bowler_score[bowler_present]+=5
    conn = sqlite3.connect('score.db')
    c=conn.cursor()
    c.execute(f"""UPDATE {main} SET SCORE={score} """)
    c.execute(f"""UPDATE {bowling_side} SET RUNS={current_bowler_score[bowler_present]} WHERE bowler ='{bowler_present}' """)
    conn.commit()
    conn.close()


    display()
    
    if innings_no==2 and (score>=target or wickets==10):
        return match_finish()
    
def undo():
    global recent
    global BALLS
    global OVERS
    global batsman_strike
    global current_batsmen_score
    global current_batsmen_balls
    global current_bowler_score
    global current_bowler_balls
    global current_bowler_wickets
    global wickets
    global score
    global extras
    global _1_bat_name
    global _2_bat_name
    global bowler_present
    global bottom_news

    # if OVERS%1==0 and OVERS!=0.0:
    #     BALLS-=1
    #     X= BALLS//6
    #     Y=(BALLS%6)/10
        
    #     OVERS = X+Y
    print(recent)
    next_over_b.place_forget()
    for i in l1:
        i.configure(state = "normal")

    if recent[0]=="DOT":
        BALLS-=1
        X= BALLS//6
        Y=(BALLS%6)/10
        
        OVERS = X+Y
        current_batsmen_balls[batsman_strike]-=1
        current_bowler_balls[bowler_present]-=1
        a=current_bowler_balls[bowler_present]//6
        b=(current_bowler_balls[bowler_present]%6)/10
        conn = sqlite3.connect('score.db')
        c=conn.cursor()    
        c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
        c.execute(f"""UPDATE {bowling_side} SET OVERS={a+b},RUNS ={current_bowler_score[bowler_present]},WICKETS ={current_bowler_wickets[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
        if current_batsmen_balls[batsman_strike]==0:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE =0 WHERE BATSMAN = '{batsman_strike}'""")
        else:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE ={(current_batsmen_score[batsman_strike]/current_batsmen_balls[batsman_strike])*100} WHERE BATSMAN = '{batsman_strike}'""")
        conn.commit()
        conn.close()
        recent.pop(0)
        if innings_no == 2 and BALLS>0:
            max_overs = int(overs_lim)
            current_overs = int(OVERS)
            current_balls = int((OVERS - current_overs) * 10)

            remaining_balls = (max_overs - current_overs) * 6 - current_balls
            bottom_news.configure(text=f"Need {target-score} on {remaining_balls} balls")
        elif BALLS==0 and innings_no == 2:
            bottom_news.configure(text=f"Need {target-score} on {int(overs_lim) * 6} balls")
        display()

    elif recent[0]=="1":
        score=score-1
        BALLS-=1
        X= BALLS//6
        Y=(BALLS%6)/10
        OVERS = X+Y
        if batsman_strike == _1_bat_name:
            batsman_strike=_2_bat_name
        else:
            batsman_strike =_1_bat_name
        current_batsmen_score[batsman_strike]-=1
        current_batsmen_balls[batsman_strike]-=1
        current_bowler_score[bowler_present]-=1
        current_bowler_balls[bowler_present]-=1
        
        a=current_bowler_balls[bowler_present]//6
        b=(current_bowler_balls[bowler_present]%6)/10

        # print(batsman_strike," score is ",current_batsmen_score[batsman_strike],"on",current_batsmen_balls[batsman_strike])
        conn = sqlite3.connect('score.db')
        c=conn.cursor()    
        c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
        c.execute(f"""UPDATE {bowling_side} SET OVERS={a+b},RUNS ={current_bowler_score[bowler_present]},WICKETS ={current_bowler_wickets[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
        if current_batsmen_balls[batsman_strike]==0:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE =0 WHERE BATSMAN = '{batsman_strike}'""")
        else:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE ={(current_batsmen_score[batsman_strike]/current_batsmen_balls[batsman_strike])*100} WHERE BATSMAN = '{batsman_strike}'""")
        
        
        conn.commit()
        conn.close()
        recent.pop(0)
         
        # print(OVERS,score)
        if innings_no == 2 and BALLS>0:
            max_overs = int(overs_lim)
            current_overs = int(OVERS)
            current_balls = int((OVERS - current_overs) * 10)

            remaining_balls = (max_overs - current_overs) * 6 - current_balls
            bottom_news.configure(text=f"Need {target-score} on {remaining_balls} balls")
        elif BALLS==0 and innings_no == 2:
            bottom_news.configure(text=f"Need {target-score} on {int(overs_lim) * 6} balls")
        display()

    elif recent[0]=="2":
        score=score-2
        BALLS-=1
        X= BALLS//6
        Y=(BALLS%6)/10
        OVERS = X+Y
        current_batsmen_score[batsman_strike]-=2
        current_batsmen_balls[batsman_strike]-=1
        current_bowler_score[bowler_present]-=2
        current_bowler_balls[bowler_present]-=1
        a=current_bowler_balls[bowler_present]//6
        b=(current_bowler_balls[bowler_present]%6)/10
        # print(batsman_strike," score is ",current_batsmen_score[batsman_strike],"on",current_batsmen_balls[batsman_strike])
        
        conn = sqlite3.connect('score.db')
        c=conn.cursor()    
        c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
        c.execute(f"""UPDATE {bowling_side} SET OVERS={a+b},RUNS ={current_bowler_score[bowler_present]},WICKETS ={current_bowler_wickets[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
        if current_batsmen_balls[batsman_strike]==0:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE =0 WHERE BATSMAN = '{batsman_strike}'""")
        else:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE ={(current_batsmen_score[batsman_strike]/current_batsmen_balls[batsman_strike])*100} WHERE BATSMAN = '{batsman_strike}'""")
        conn.commit()
        conn.close()
        recent.pop(0)


        if innings_no == 2 and BALLS>0:
            max_overs = int(overs_lim)
            current_overs = int(OVERS)
            current_balls = int((OVERS - current_overs) * 10)

            remaining_balls = (max_overs - current_overs) * 6 - current_balls
            bottom_news.configure(text=f"Need {target-score} on {remaining_balls} balls")
        elif BALLS==0 and innings_no == 2:
            bottom_news.configure(text=f"Need {target-score} on {int(overs_lim) * 6} balls")
        display()
        # print(OVERS,score)
    elif recent[0]=="3":
        score=score-3
        BALLS-=1
        X= BALLS//6
        Y=(BALLS%6)/10
        OVERS = X+Y

        if batsman_strike == _1_bat_name:
            batsman_strike=_2_bat_name
        else:
            batsman_strike =_1_bat_name
        current_batsmen_score[batsman_strike]-=3
        current_batsmen_balls[batsman_strike]-=1
        current_bowler_score[bowler_present]-=3
        current_bowler_balls[bowler_present]-=1
        a=current_bowler_balls[bowler_present]//6
        b=(current_bowler_balls[bowler_present]%6)/10
        # print(batsman_strike," score is ",current_batsmen_score[batsman_strike],"on",current_batsmen_balls[batsman_strike])
        conn = sqlite3.connect('score.db')
        c=conn.cursor()    
        c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
        c.execute(f"""UPDATE {bowling_side} SET OVERS={a+b},RUNS ={current_bowler_score[bowler_present]},WICKETS ={current_bowler_wickets[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
        if current_batsmen_balls[batsman_strike]==0:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE =0 WHERE BATSMAN = '{batsman_strike}'""")
        else:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE ={(current_batsmen_score[batsman_strike]/current_batsmen_balls[batsman_strike])*100} WHERE BATSMAN = '{batsman_strike}'""")
        conn.commit()
        conn.close()
        recent.pop(0)
        
        
        if innings_no == 2 and BALLS>0:
            max_overs = int(overs_lim)
            current_overs = int(OVERS)
            current_balls = int((OVERS - current_overs) * 10)

            remaining_balls = (max_overs - current_overs) * 6 - current_balls
            bottom_news.configure(text=f"Need {target-score} on {remaining_balls} balls")
        elif BALLS==0 and innings_no == 2:
            bottom_news.configure(text=f"Need {target-score} on {int(overs_lim) * 6} balls")
        display()

        # print(OVERS,score)

    elif recent[0]=="4":
        score=score-4
        BALLS-=1
        X= BALLS//6
        Y=(BALLS%6)/10
        OVERS = X+Y
        current_batsmen_score[batsman_strike]-=4
        current_batsmen_balls[batsman_strike]-=1
        current_bowler_score[bowler_present]-=4
        current_bowler_balls[bowler_present]-=1
        a=current_bowler_balls[bowler_present]//6
        b=(current_bowler_balls[bowler_present]%6)/10
        # print(batsman_strike," score is ",current_batsmen_score[batsman_strike],"on",current_batsmen_balls[batsman_strike])
        
        conn = sqlite3.connect('score.db')
        c=conn.cursor()    
        c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
        c.execute(f"""UPDATE {bowling_side} SET OVERS={a+b},RUNS ={current_bowler_score[bowler_present]},WICKETS ={current_bowler_wickets[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
        if current_batsmen_balls[batsman_strike]==0:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE =0 WHERE BATSMAN = '{batsman_strike}'""")
        else:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE ={(current_batsmen_score[batsman_strike]/current_batsmen_balls[batsman_strike])*100} WHERE BATSMAN = '{batsman_strike}'""")
        conn.commit()
        conn.close()
        recent.pop(0)

        if innings_no == 2 and BALLS>0:
            max_overs = int(overs_lim)
            current_overs = int(OVERS)
            current_balls = int((OVERS - current_overs) * 10)

            remaining_balls = (max_overs - current_overs) * 6 - current_balls
            bottom_news.configure(text=f"Need {target-score} on {remaining_balls} balls")
        elif BALLS==0 and innings_no == 2:
            bottom_news.configure(text=f"Need {target-score} on {int(overs_lim) * 6} balls")
        display()

        # print(OVERS,score)
    elif recent[0]=="6":
        score=score-6
        BALLS-=1
        X= BALLS//6
        Y=(BALLS%6)/10
        OVERS = X+Y
        current_batsmen_score[batsman_strike]-=6
        current_batsmen_balls[batsman_strike]-=1
        current_bowler_score[bowler_present]-=6
        current_bowler_balls[bowler_present]-=1
        a=current_bowler_balls[bowler_present]//6
        b=(current_bowler_balls[bowler_present]%6)/10
        # print(batsman_strike," score is ",current_batsmen_score[batsman_strike],"on",current_batsmen_balls[batsman_strike])
        
        conn = sqlite3.connect('score.db')
        c=conn.cursor()    
        c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
        c.execute(f"""UPDATE {bowling_side} SET OVERS={a+b},RUNS ={current_bowler_score[bowler_present]},WICKETS ={current_bowler_wickets[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
        if current_batsmen_balls[batsman_strike]==0:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE =0 WHERE BATSMAN = '{batsman_strike}'""")
        else:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE ={(current_batsmen_score[batsman_strike]/current_batsmen_balls[batsman_strike])*100} WHERE BATSMAN = '{batsman_strike}'""")
        conn.commit()
        conn.close()
        recent.pop(0)

        if innings_no == 2 and BALLS>0:
            max_overs = int(overs_lim)
            current_overs = int(OVERS)
            current_balls = int((OVERS - current_overs) * 10)

            remaining_balls = (max_overs - current_overs) * 6 - current_balls
            bottom_news.configure(text=f"Need {target-score} on {remaining_balls} balls")
        elif BALLS==0 and innings_no == 2:
            bottom_news.configure(text=f"Need {target-score} on {int(overs_lim) * 6} balls")
        display()
        # print(OVERS,score)

    elif recent[0]=="WD":
        current_bowler_score[bowler_present]-=1
        score-=1
        extras -=1
        X= BALLS//6
        Y=(BALLS%6)/10
        OVERS = X+Y
        a=current_bowler_balls[bowler_present]//6
        b=(current_bowler_balls[bowler_present]%6)/10
        conn = sqlite3.connect('score.db')
        c=conn.cursor()    
        c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
        c.execute(f"""UPDATE {bowling_side} SET OVERS={a+b},RUNS ={current_bowler_score[bowler_present]},WICKETS ={current_bowler_wickets[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
        if current_batsmen_balls[batsman_strike]==0:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE =0 WHERE BATSMAN = '{batsman_strike}'""")
        else:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE ={(current_batsmen_score[batsman_strike]/current_batsmen_balls[batsman_strike])*100} WHERE BATSMAN = '{batsman_strike}'""")
        conn.commit()
        conn.close()
        recent.pop(0)
        if innings_no == 2 and BALLS>0:
            max_overs = int(overs_lim)
            current_overs = int(OVERS)
            current_balls = int((OVERS - current_overs) * 10)

            remaining_balls = (max_overs - current_overs) * 6 - current_balls
            bottom_news.configure(text=f"Need {target-score} on {remaining_balls} balls")
        elif BALLS==0 and innings_no == 2:
            bottom_news.configure(text=f"Need {target-score} on {int(overs_lim) * 6} balls")
        display()

    elif recent[0]=="OUT":
        CTkMessagebox(title="Error", message="UNDO function can not work on 'OUT'", icon="cancel", button_color="darkGreen")
    elif recent[0]=="NB":
        global f1
        BALLS+=1
        X= BALLS//6
        Y=(BALLS%6)/10
        OVERS = X+Y
        current_bowler_score[bowler_present]-=1
        current_bowler_balls[bowler_present]+=1
        score-=1
        extras -=1
        a=current_bowler_balls[bowler_present]//6
        b=(current_bowler_balls[bowler_present]%6)/10
        
        conn = sqlite3.connect('score.db')
        c=conn.cursor()    
        c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
        c.execute(f"""UPDATE {bowling_side} SET OVERS={a+b},RUNS ={current_bowler_score[bowler_present]},WICKETS ={current_bowler_wickets[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
        if current_batsmen_balls[batsman_strike]==0:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE =0 WHERE BATSMAN = '{batsman_strike}'""")
        else:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE ={(current_batsmen_score[batsman_strike]/current_batsmen_balls[batsman_strike])*100} WHERE BATSMAN = '{batsman_strike}'""")
        conn.commit()
        conn.close()
        f1.destroy()
        recent.pop(0)
        if innings_no == 2 and BALLS>0:
            max_overs = int(overs_lim)
            current_overs = int(OVERS)
            current_balls = int((OVERS - current_overs) * 10)

            remaining_balls = (max_overs - current_overs) * 6 - current_balls
            bottom_news.configure(text=f"Need {target-score} on {remaining_balls} balls")
        elif BALLS==0 and innings_no == 2:
            bottom_news.configure(text=f"Need {target-score} on {int(overs_lim) * 6} balls")
        display()

    elif recent[0]=="B1":
        score=score-1
        extras-=1
        BALLS-=1
        X= BALLS//6
        Y=(BALLS%6)/10
        OVERS = X+Y
        
        if batsman_strike == _1_bat_name:
            batsman_strike=_2_bat_name
        else:
            batsman_strike =_1_bat_name
        current_batsmen_balls[batsman_strike]-=1
        current_bowler_balls[bowler_present]-=1

        a=current_bowler_balls[bowler_present]//6
        b=(current_bowler_balls[bowler_present]%6)/10
        conn = sqlite3.connect('score.db')
        c=conn.cursor()    
        c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
        c.execute(f"""UPDATE {bowling_side} SET OVERS={a+b},RUNS ={current_bowler_score[bowler_present]},WICKETS ={current_bowler_wickets[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
        if current_batsmen_balls[batsman_strike]==0:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE =0 WHERE BATSMAN = '{batsman_strike}'""")
        else:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE ={(current_batsmen_score[batsman_strike]/current_batsmen_balls[batsman_strike])*100} WHERE BATSMAN = '{batsman_strike}'""")
        conn.commit()
        conn.close()

        recent.pop(0)

        if innings_no == 2 and BALLS>0:
            max_overs = int(overs_lim)
            current_overs = int(OVERS)
            current_balls = int((OVERS - current_overs) * 10)

            remaining_balls = (max_overs - current_overs) * 6 - current_balls
            bottom_news.configure(text=f"Need {target-score} on {remaining_balls} balls")
        elif BALLS==0 and innings_no == 2:
            bottom_news.configure(text=f"Need {target-score} on {int(overs_lim) * 6} balls")

        display()
        

    elif recent[0]=="B2":
        score=score-2
        extras-=2
        BALLS-=1
        X= BALLS//6
        Y=(BALLS%6)/10
        OVERS = X+Y
        
        current_batsmen_balls[batsman_strike]-=1
        current_bowler_balls[bowler_present]-=1
        a=current_bowler_balls[bowler_present]//6
        b=(current_bowler_balls[bowler_present]%6)/10
        conn = sqlite3.connect('score.db')
        c=conn.cursor()    
        c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
        c.execute(f"""UPDATE {bowling_side} SET OVERS={a+b},RUNS ={current_bowler_score[bowler_present]},WICKETS ={current_bowler_wickets[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
        if current_batsmen_balls[batsman_strike]==0:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE =0 WHERE BATSMAN = '{batsman_strike}'""")
        else:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE ={(current_batsmen_score[batsman_strike]/current_batsmen_balls[batsman_strike])*100} WHERE BATSMAN = '{batsman_strike}'""")
        conn.commit()
        conn.close()
        recent.pop(0)
        if innings_no == 2 and BALLS>0:
            max_overs = int(overs_lim)
            current_overs = int(OVERS)
            current_balls = int((OVERS - current_overs) * 10)

            remaining_balls = (max_overs - current_overs) * 6 - current_balls
            bottom_news.configure(text=f"Need {target-score} on {remaining_balls} balls")
        elif BALLS==0 and innings_no == 2:
            bottom_news.configure(text=f"Need {target-score} on {int(overs_lim) * 6} balls")
        display()

    elif recent[0]=="B3":
        score=score-3
        extras-=3
        BALLS-=1
        X= BALLS//6
        Y=(BALLS%6)/10
        OVERS = X+Y
        if batsman_strike == _1_bat_name:
            batsman_strike=_2_bat_name
        else:
            batsman_strike =_1_bat_name
        
        current_batsmen_balls[batsman_strike]-=1
        current_bowler_balls[bowler_present]-=1
        a=current_bowler_balls[bowler_present]//6
        b=(current_bowler_balls[bowler_present]%6)/10
        conn = sqlite3.connect('score.db')
        c=conn.cursor()    
        c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
        c.execute(f"""UPDATE {bowling_side} SET OVERS={a+b},RUNS ={current_bowler_score[bowler_present]},WICKETS ={current_bowler_wickets[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
        if current_batsmen_balls[batsman_strike]==0:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE =0 WHERE BATSMAN = '{batsman_strike}'""")
        else:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE ={(current_batsmen_score[batsman_strike]/current_batsmen_balls[batsman_strike])*100} WHERE BATSMAN = '{batsman_strike}'""")
        conn.commit()
        conn.close()
        recent.pop(0)
        if innings_no == 2 and BALLS>0:
            max_overs = int(overs_lim)
            current_overs = int(OVERS)
            current_balls = int((OVERS - current_overs) * 10)

            remaining_balls = (max_overs - current_overs) * 6 - current_balls
            bottom_news.configure(text=f"Need {target-score} on {remaining_balls} balls")
        elif BALLS==0 and innings_no == 2:
            bottom_news.configure(text=f"Need {target-score} on {int(overs_lim) * 6} balls")
        display()

    elif recent[0]=="B4":
        score=score-4
        extras-=4
        BALLS-=1
        X= BALLS//6
        Y=(BALLS%6)/10
        OVERS = X+Y
        
        current_batsmen_balls[batsman_strike]-=1
        current_bowler_balls[bowler_present]-=1
        a=current_bowler_balls[bowler_present]//6
        b=(current_bowler_balls[bowler_present]%6)/10
        conn = sqlite3.connect('score.db')
        c=conn.cursor()    
        c.execute(f"""UPDATE {main} SET OVERS={OVERS},SCORE={score},WICKETS={wickets}""")
        c.execute(f"""UPDATE {bowling_side} SET OVERS={a+b},RUNS ={current_bowler_score[bowler_present]},WICKETS ={current_bowler_wickets[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
        if current_batsmen_balls[batsman_strike]==0:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE =0 WHERE BATSMAN = '{batsman_strike}'""")
        else:
            c.execute(f"""UPDATE {batting_side} SET RUNS={current_batsmen_score[batsman_strike]},BALLS={current_batsmen_balls[batsman_strike]},STRIKE_RATE ={(current_batsmen_score[batsman_strike]/current_batsmen_balls[batsman_strike])*100} WHERE BATSMAN = '{batsman_strike}'""")
        conn.commit()
        conn.close()
        recent.pop(0)
        if innings_no == 2 and BALLS>0:
            max_overs = int(overs_lim)
            current_overs = int(OVERS)
            current_balls = int((OVERS - current_overs) * 10)

            remaining_balls = (max_overs - current_overs) * 6 - current_balls
            bottom_news.configure(text=f"Need {target-score} on {remaining_balls} balls")
        elif BALLS==0 and innings_no == 2:
            bottom_news.configure(text=f"Need {target-score} on {int(overs_lim) * 6} balls")
        display()

    elif recent[0]=="W1":
        extras-=2
        score=score-2
        if batsman_strike == _1_bat_name:
            batsman_strike=_2_bat_name
        else:
            batsman_strike =_1_bat_name
        current_bowler_score[bowler_present]-=2
        conn = sqlite3.connect('score.db')
        c=conn.cursor()
        c.execute(f"""UPDATE {main} SET SCORE={score}""")
        c.execute(f"""UPDATE {bowling_side} SET RUNS ={current_bowler_score[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
        conn.commit()
        conn.close()

        recent.pop(0)
        if innings_no == 2 and BALLS>0:
            max_overs = int(overs_lim)
            current_overs = int(OVERS)
            current_balls = int((OVERS - current_overs) * 10)

            remaining_balls = (max_overs - current_overs) * 6 - current_balls
            bottom_news.configure(text=f"Need {target-score} on {remaining_balls} balls")
        elif BALLS==0 and innings_no == 2:
            bottom_news.configure(text=f"Need {target-score} on {int(overs_lim) * 6} balls")
        display()
        
    elif recent[0]=="W2":
        extras-=3
        score=score-3
        current_bowler_score[bowler_present]-=3
        conn = sqlite3.connect('score.db')
        c=conn.cursor()
        c.execute(f"""UPDATE {main} SET SCORE={score}""")
        c.execute(f"""UPDATE {bowling_side} SET RUNS ={current_bowler_score[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
        conn.commit()
        conn.close()

        recent.pop(0)
        if innings_no == 2 and BALLS>0:
            max_overs = int(overs_lim)
            current_overs = int(OVERS)
            current_balls = int((OVERS - current_overs) * 10)

            remaining_balls = (max_overs - current_overs) * 6 - current_balls
            bottom_news.configure(text=f"Need {target-score} on {remaining_balls} balls")
        elif BALLS==0 and innings_no == 2:
            bottom_news.configure(text=f"Need {target-score} on {int(overs_lim) * 6} balls")
        display()

    elif recent[0]=="W3":
        extras-=4
        score=score-4
        current_bowler_score[bowler_present]-=4
        conn = sqlite3.connect('score.db')
        c=conn.cursor()
        c.execute(f"""UPDATE {main} SET SCORE={score}""")
        c.execute(f"""UPDATE {bowling_side} SET RUNS ={current_bowler_score[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
        conn.commit()
        conn.close()
        if batsman_strike == _1_bat_name:
            batsman_strike=_2_bat_name
        else:
            batsman_strike =_1_bat_name
        recent.pop(0)
        if innings_no == 2 and BALLS>0:
            max_overs = int(overs_lim)
            current_overs = int(OVERS)
            current_balls = int((OVERS - current_overs) * 10)

            remaining_balls = (max_overs - current_overs) * 6 - current_balls
            bottom_news.configure(text=f"Need {target-score} on {remaining_balls} balls")
        elif BALLS==0 and innings_no == 2:
            bottom_news.configure(text=f"Need {target-score} on {int(overs_lim) * 6} balls")
        display()

    elif recent[0]=="W4":
        extras-=5
        score=score-5
        current_bowler_score[bowler_present]-=5
        conn = sqlite3.connect('score.db')
        c=conn.cursor()
        c.execute(f"""UPDATE {main} SET SCORE={score}""")
        c.execute(f"""UPDATE {bowling_side} SET RUNS ={current_bowler_score[bowler_present]} WHERE BOWLER = '{bowler_present}'""")
        conn.commit()
        conn.close()

        recent.pop(0)
        if innings_no == 2 and BALLS>0:
            max_overs = int(overs_lim)
            current_overs = int(OVERS)
            current_balls = int((OVERS - current_overs) * 10)

            remaining_balls = (max_overs - current_overs) * 6 - current_balls
            bottom_news.configure(text=f"Need {target-score} on {remaining_balls} balls")
        elif BALLS==0 and innings_no == 2:
            bottom_news.configure(text=f"Need {target-score} on {int(overs_lim) * 6} balls")
        display()
      
conn.commit()
conn.close()

exitFlag = True
m.mainloop()
