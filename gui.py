#import mysql.connector
#import sqlite3
from tkinter import*
from tkinter import ttk

import random
import tkinter.messagebox
import datetime
import time
import tempfile, os

# gui class 만들기
from pip._vendor import requests


class gui:
    def __init__(self, root):
        self.root = root
        self.root.title("ACUOUS")  #제목 생성
        self.root.geometry("947x580")  #창 크기 설정
        self.root.configure(bg="light blue", bd=5, relief=GROOVE)  #창 배경색, 테두리
        self.root.resizable(0,0)  #창 크기 고정
#FRAME----------------------------------------------------------------------------------------------------------------------
        mainframe = Frame(self.root, height=+1000)  #창 메인프레임 생성
        mainframe.pack(fill=BOTH)  #창 메인프레임 상하좌우로 꽉 채우도록 설정

        leftframe=Frame(mainframe, bg="white")  #메인프레임 안의 좌측 프레임 형성
        leftframe.pack(side=LEFT,fill=BOTH)  #좌측 프레임 좌측으로 붙도록, 상하좌우 채우도록 설정

        rightframe=Frame(mainframe, bd=3, width=1000, height=1000, bg="gainsboro", relief=GROOVE)  #메인프레임 안의 우측 프레임 형성
        rightframe.place(x=325, y=0)

# 우측 FRAME의 환자정보 LABLE-----------------------------------------------------------------------------------------------------------------
        def rfinfo():   #rightframe information 함수 (우측 프레임 안에 name/num/age/sex/diagnosis 레이블 넣을 것임)
            rightframe2 = Frame(rightframe, bd=3, width=500, height=100, padx=4, pady=4, bg="gainsboro", relief=RIDGE)  #우측프레임 안의 프레임 설정
            rightframe2.pack(side=TOP, fill='y')

            # 라벨
            fakelb2 = Label(rightframe2, width=20, bg='gainsboro')  #어떻게 왼쪽으로 붙일지 몰라서^^ 하다하다 fake 레이블 넣어서 왼쪽으로 붙여버림
            fakelb2.grid(row=0, column=4)
            fakelb4 = Label(rightframe2, width=20, bg='gainsboro')
            fakelb4.grid(row=0, column=4)

            # 이름 레이블
            lbname = Label(rightframe2, text="name", width=10, bd=1, relief=GROOVE)
            lbname.grid(row=0, column=0, sticky=E)
            lbname_ = Label(rightframe2, text="전00", width=20, bd=1, relief=GROOVE)
            lbname_.grid(row=0, column=1, sticky=E)

            #등록번호 레이블
            lbpatientnum = Label(rightframe2, text="patientnum", width=10, bd=1, relief=GROOVE)
            lbpatientnum.grid(row=0, column=2, sticky=E)
            lbpatientnum_ = Label(rightframe2, text="000002", width=20, bd=1, relief=GROOVE)
            lbpatientnum_.grid(row=0, column=3, sticky=E)

            #나이 레이블
            lbage = Label(rightframe2, text="age", width=10, bd=1, relief=GROOVE)
            lbage.grid(row=1, column=0, sticky=E)
            lbage_ = Label(rightframe2, text="49", width=20, bd=1, relief=GROOVE)
            lbage_.grid(row=1, column=1, sticky=E)

            #성별 레이블
            lbsex = Label(rightframe2, text="sex", width=10, bd=1, relief=GROOVE)
            lbsex.grid(row=1, column=2, sticky=E)
            lbsex_ = Label(rightframe2, text="M", width=20, bd=1, relief=GROOVE)
            lbsex_.grid(row=1, column=3, sticky=E)

            #진단명 레이블
            lbdiagnosis = Label(rightframe2, text="diagnosis", width=10, bd=1, relief=GROOVE)
            lbdiagnosis.grid(row=2, column=0, sticky=E)
            lbdiagnosis_ = Label(rightframe2, text="Polyuria", width=20, bd=1, relief=GROOVE)
            lbdiagnosis_.grid(row=2, column=1, sticky=E)
# PATINET INFORMATION TABLE(TREEVIEW 사용)----------------------------------------------------------------------------------------------
        # 환자정보 표 데이터(MySQL이랑 연동시켜야 함)
        ###아래 은희가 준 것
        #data = [list(requests.get('http://localhost:3000/patientinfo/').json()[0].values())]
        #print(data)
        
        ### 인터넷으로 찾아본 것
        #https://www.plus2net.com/python/tkinter-mysql.php 데이터 연결
        #my_connect = mysql.connector.connect(host="localhost", user="userid", passwd="password", database="database_name")
        
        ### end of connection ###
        #my_cursor = my_connect.cursor()
        #my_cursor.execute("SELECT * FROM ~~~ limit 0,10")
        #i=0
        #for ~~~ in my_cursor:
            #for j in range(len(~~~)):
                #print(~~~[j],end='')
            #i=i+1
            #print()# line break at the end of one row
        
        data = [["김00","000001","24",'F','Diabetes Mellitus'], ["전00","000002","49",'M','Polyuria'], ["서00","000003","70",'F','Hematuria'], ["조00","000004","9",'F','Acute renal failure']]
        #환자정보 표 설정
        tree = ttk.Treeview(leftframe, height=100, columns=("column1", "column2", "column3", "column4", "column5"), show="headings")

        # URINE INFORMATION FUCITON-----------------------------------------------------------------------------------------
        # 소변정보 확인 버튼 함수
        def urinecheck():
            rfinfo()  #선택된 환자 정보 레이블 여기 넣어야 함

            # 오른쪽 정보 창 만들기 <= rfinfo 아래에 위치해서, rfinfo는 계속 떠있고 선택된 환자 소변정보 보여주게 함
            c = Canvas(rightframe, bg="white", width=600, height=486)
            c.pack(fill=BOTH, expand=TRUE)

            def swap(button):
                button.tkraise()

        # URINE VOLUME FUCITON-IN-URINECHECK FUNTION--------------------------------------------------------------------
            # 소변량 확인 버튼 누르면 나오는 창 만들기
            def uvolume():
                data1 = [["2020-09-11 (16:49)", "200ml"]]  # 소변량 정보 들어가는 곳

                tree1 = ttk.Treeview(c, columns=(1, 2),show="headings")
                tree1.place(x=85, y=5)

                tree1.heading(1, text="date/time")
                tree1.heading(2, text="urine-volume")

                tree1.column(1, width=150, anchor="center")
                tree1.column(2, width=150, anchor="center")

                # URINE VOLUME 표 DATA
                for val in data1:
                    tree1.insert('', 'end', values=(val[0], val[1]))

        # URINALYSIS FUCITON-IN-URINECHECK FUNTION------------------------------------------------------------------------------------
            # 뇨성분 분석 버튼 누르면 나오는 창
            def nalysis():

                data2 = [["참고치", "(-)", "(-)", "(-)", "(+-)", "(-)", "(-)", "4.5-8.0"], ["2020-09-11 (16:49)", "+", "+", "+-", "+", "-", "+", "6.5"]]

                tree2 = ttk.Treeview(c, columns=(1, 2, 3, 4, 5, 6, 7, 8), height=10, show="headings")
                tree2.place(x=85, y=250)

                tree2.heading(1, text="date/time")
                tree2.heading(2, text="blood")
                tree2.heading(3, text="bilirubin")
                tree2.heading(4, text="urobilinogen")
                tree2.heading(5, text="ketones")
                tree2.heading(6, text="protein")
                tree2.heading(7, text="glucose")
                tree2.heading(8, text="pH")

                tree2.column(1, width=120, anchor="center")
                tree2.column(2, width=45, anchor="center")
                tree2.column(3, width=60, anchor="center")
                tree2.column(4, width=80, anchor="center")
                tree2.column(5, width=50, anchor="center")
                tree2.column(6, width=50, anchor="center")
                tree2.column(7, width=50, anchor="center")
                tree2.column(8, width=55, anchor="center")

                # URINALYSIS 표 DATA
                for val in data2:
                    tree2.insert('', 'end', values=(val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7]))

        # URINE VOLUME, URINALYSIS BUTTON
            btn1 = Button(c, text="소변량 확인", command=lambda :[uvolume(), swap(btn2)])
            btn1.place(x=5, y=5)

            btn2 = Button(c, text="뇨성분 분석", command=lambda :[nalysis(), swap(btn1)])
            btn2.place(x=5, y=250)

            btn1.tkraise()

    #!!!여기부터 LEFTFRAME 환자정보 표 DATA
        for val in data:
            tree.insert('', 'end', values=(val[0], val[1], val[2], val[3], val[4]))
        tree.pack(fill=BOTH)
        
        #이거 row 누르면 urinecheck fuction 뜨도록 설정하는 함수
        def select(event):
            curItem = tree.item(tree.focus())
            row = tree.identify_row(event.y)
            urinecheck()

        # Left frame환자정보
        tree.heading('#1', text="name")
        tree.heading('#2', text="patientnum")
        tree.heading('#3', text="age")
        tree.heading('#4', text="sex")
        tree.heading('#5', text="diagnosis")
        tree.bind('<ButtonRelease-1>', select)

        tree.column('#1', width=50, anchor="center")
        tree.column('#2', width=70, anchor="center")
        tree.column('#3', width=47, anchor="center")
        tree.column('#4', width=38, anchor="center")
        tree.column('#5', width=115, anchor="w")
    # !!!!!!여기까지 LEFTFRAME 환자정보 표 DATA

        # 위에 메뉴챵 만들기
        mb = Menu(root)
        f = Menu(mb, tearoff=0)
        f.add_command(label="Urine volume", command=urinecheck)
        f.add_command(label="Urinalysis", command=urinecheck)
        f.add_command(label="Save")
        f.add_command(label="Close")
        f.add_separator()
        f.add_command(label="Quit", command=root.quit)
        mb.add_cascade(label="File", menu=f)

        e = Menu(mb, tearoff=0)
        e.add_command(label="Undo")
        e.add_command(label="Cut")
        e.add_command(label="Copy")
        e.add_command(label="Paste")
        e.add_command(label="Cancel")
        e.add_command(label="Select all")
        mb.add_cascade(label="Edit", menu=e)

        h = Menu(mb, tearoff=0)
        h.add_command(label="What is ACUOUS?")
        h.add_command(label="How to use ACUOUS")
        mb.add_cascade(label="For help", menu=h)

        root.config(menu=mb)



if __name__ == '__main__':
    root = Tk()
    application = gui(root)
    root.mainloop()

        # (중요)우측프레임 환자 레이블에 선택하는 행 정보 넣는 방법
        # 소변량 / 뇨성분 분석 표 세로로 만들기 -->>> 불가할 듯 treeview 하나만 바꾸는 것 불가하다고 함(?) 그리고 잘 안나옴.. 더 찾아볼 것
        # tree table에 scrollbar가 안만들어짐... +전체 창 scroll bar 만들기 => 코드 오류는 안나는데 화면에 안쯤
        # 상위메뉴에 뭐 넣을까 + 메뉴 연동시키기 command
        # URINALYSIS TABLE CELL HEIGHT 길게 하기 -->>> 불가할 듯 treeview 하나만 바꾸는 것 불가하다고 함(?) 그리고 잘 안나옴.. 더 찾아볼 것