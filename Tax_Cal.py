from tkinter import *
from tkinter import ttk

class Income_Tax:

    def __init__(self,root):
        self.root=root
        self.root.title("Income tax Calculator")
        self.root.geometry("800x500")
        #=========================================================
        income = 0
        allowance = 132000
        M=0
        M1=0
        M2=0
        total_income = 0
        total_M = 0
        income1=0
        income2=0
        #=========================================================
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=10, width = 31, padx = 5,relief=RIDGE)
        TitleFrame.pack(side=TOP)
        TitleFrame.pack_propagate(False)

        self.lblTitle = Label(TitleFrame, width = 31, font=('arial',30,'bold'),text="Income Tax Calculator",padx=11)
        self.lblTitle.grid()

        BodyFrame = Frame(MainFrame, bd = 5, width=800, height = 430, relief=RIDGE)
        BodyFrame.pack(side=TOP)
        BodyFrame.pack_propagate(False)

        TopBodyFrame = Frame(BodyFrame,bd=1,width=800, height = 30, relief=RIDGE)
        TopBodyFrame.pack(side=TOP)
        TopBodyFrame.pack_propagate(False)
        
        Page1 = Frame(BodyFrame,bd=1, width=800, height = 430, relief=RIDGE)
        Page1.pack(side=TOP)
        Page1.pack_propagate(False)

        Page2 = Frame(BodyFrame,bd=1, width=800, height = 430, relief=RIDGE)
        #=========================================================
        def single():
            tax = 0
            dis = 0
            sp = 0
            income = int(Page1.txtAnnualIncome1.get())
            disability = str(Page1.cbxdisability.get())
            kid1 =  int(Page1.cbxkids1.get())
            kid2 =  int(Page1.cbxkids2.get())
            singleparent =  str(Page1.cbxsingleparent.get())
            standard_rate = 0
            
            if income < 7100:
                M = 0
            else:
                M = income*0.05
    
            if M >= 18000:
                M = 18000

            if disability == 'No':
                dis = 0
            else:
                dis = 75000

            if singleparent == 'No':
                sp = 0
            else:
                sp = 132000
    
            net_income = income - M - allowance - dis - kid1*240000 - kid2*120000 - sp
            standard_rate = (net_income + allowance )* 0.15
            
            if net_income <= 0:
                tax = 0

            if net_income > 0:    
                if net_income > 50000:
                    A = 1000
                    tax = tax+A
                    net_income = net_income - 50000
                else:
                    A = net_income*0.02
                    tax = tax+A
                    net_income = net_income - 50000

            if net_income > 0:
                if net_income > 50000:
                    B = 3000
                    tax = tax+B
                    net_income = net_income - 50000
                else:   
                    B = net_income * 0.06
                    tax = tax + B
                    net_income = net_income - 50000
        
            if net_income > 0:
                if net_income > 50000:
                    C = 5000
                    tax=tax+C
                    net_income = net_income - 50000
                else:
                    C = net_income * 0.1
                    tax=tax+C
                    net_income = net_income - 50000
        
            if net_income > 0:
                if net_income > 50000:
                    D = 7000
                    tax=tax+D
                    net_income = net_income - 50000
                else:
                    D = net_income * 0.14
                    tax=tax+D
                    net_income = net_income - 50000
        
            if net_income > 0:
                E = net_income*0.17
                tax= tax+E

            print('Your tax:', tax)
            print('Using Standard rate', standard_rate)

            if tax > standard_rate:
                print('Standard rate is recommended')
            else:
                print('Standard rate is not recommended')

            
        #=========================================================
        def married():
            tax = 0
            income = int(Page2.txtAnnualIncome1.get())
            tax1 = 0
            income1 = int(Page2.txtAnnualIncome2.get())
            tax2 = 0
            net_income2 = 0
            disability = str(Page2.cbxdisability.get())
            disability1 = str(Page2.cbxdisability1.get())
            standard_rate = 0
            kid1 =  int(Page2.cbxkids1.get())
            kid2 =  int(Page2.cbxkids2.get())
            dis = 0
            dis1 = 0
        #=========================================================
            
            if income < 7100:
                M = 0
            else:
                M = income*0.05
    
            if M >= 18000:
                M = 18000
                
            if income1 < 7100:
                M1 = 0
            else:
                M1 = income1*0.05
    
            if M1 >= 18000:
                M1 = 18000

            if disability == 'No':
                dis = 0
            else:
                dis = 75000

            if disability1 == 'No':
                dis1 = 0
            else:
                dis1 = 75000

            net_income = income - M - allowance - dis - kid1*240000 - kid2*120000

            net_income1 = income1 - M1 - allowance - dis1
            
            net_income2 = (income + income1) - M - M1 - 2*allowance - dis - dis1 - kid1*240000 - kid2*120000

            standard_rate = (net_income2 + 2*allowance)*0.15

            print('Standard rate:', standard_rate)

            if net_income <= 0:
                tax = 0

            if net_income > 0:    
                if net_income > 50000:
                    A = 1000
                    tax = tax+A
                    net_income = net_income - 50000
                else:
                    A = net_income*0.02
                    tax = tax+A
                    net_income = net_income - 50000

            if net_income > 0:
                if net_income > 50000:
                    B = 3000
                    tax = tax+B
                    net_income = net_income - 50000
                else:   
                    B = net_income * 0.06
                    tax = tax + B
                    net_income = net_income - 50000
        
            if net_income > 0:
                if net_income > 50000:
                    C = 5000
                    tax=tax+C
                    net_income = net_income - 50000
                else:
                    C = net_income * 0.1
                    tax=tax+C
                    net_income = net_income - 50000
        
            if net_income > 0:
                if net_income > 50000:
                    D = 7000
                    tax=tax+D
                    net_income = net_income - 50000
                else:
                    D = net_income * 0.14
                    tax=tax+D
                    net_income = net_income - 50000
        
            if net_income > 0:
                E = net_income*0.17
                tax= tax+E

            print('Separate assessment of your:' ,tax)
#=========================================================

            if net_income1 <= 0:
                tax1 = 0

            if net_income1 > 0:    
                if net_income1 > 50000:
                    A = 1000
                    tax1 = tax1+A
                    net_income1 = net_income1 - 50000
                else:
                    A = net_income1*0.02
                    tax1 = tax1+A
                    net_income1 = net_income1 - 50000

            if net_income1 > 0:
                if net_income1 > 50000:
                    B = 3000
                    tax1 = tax1+B
                    net_income1 = net_income1 - 50000
                else:   
                    B = net_income1 * 0.06
                    tax1 = tax1 + B
                    net_income1 = net_income1 - 50000
        
            if net_income1 > 0:
                if net_income1 > 50000:
                    C = 5000
                    tax1=tax1+C
                    net_income1 = net_income1 - 50000
                else:
                    C = net_income1 * 0.15
                    tax1=tax1+C
                    net_income1 = net_income1 - 50000
        
            if net_income1 > 0:
                if net_income1 > 50000:
                    D = 7000
                    tax1=tax1+D
                    net_income1 = net_income1 - 50000
                else:
                    D = net_income1 * 0.14
                    tax1=tax1+D
                    net_income1 = net_income1 - 50000
        
            if net_income1 > 0:
                E = net_income1*0.17
                tax1= tax1+E
        
            print('Separate assessment of your partner:', tax1)
        #=========================================================
            if net_income2 <= 0:
                tax2 = 0

            if net_income2 > 0:
                if net_income2 > 50000:
                    A = 1000
                    tax2 = tax2+A
                    net_income2 = net_income2 - 50000
                else:
                    A = net_income2*0.02
                    tax2 = tax2+A
                    net_income2 = net_income2 - 50000

            if net_income2 > 0:
                if net_income2 > 50000:
                    B = 3000
                    tax2 = tax2+B
                    net_income2 = net_income2 - 50000
                else:
                    B = net_income2 * 0.06
                    tax2 = tax2 + B
                    net_income2 = net_income2 - 50000
                    
            if net_income2 > 0:
                if net_income2 > 50000:
                    C = 5000
                    tax2=tax2+C
                    net_income2 = net_income2 - 50000
                else:
                    C = net_income2 * 0.1
                    tax2=tax2+C
                    net_income2 = net_income2 - 50000

            if net_income2 > 0:
                if net_income2 > 50000:
                    D = 7000
                    tax2=tax2+D
                    net_income2 = net_income2 - 50000
                else:
                    D = net_income2 * 0.14
                    tax2=tax2+D
                    net_income2 = net_income2 - 50000

            if net_income2 > 0:
                E = net_income2*0.17
                tax2= tax2+E
                
            print('Total of Separate assessment:' ,tax+tax1)
            print('Joint assessment:', tax2)

            
            if  standard_rate < (tax1+ tax) and tax2:
                print('Standard_rate is recommended')
            else:
                    if tax + tax1 > tax2:
                        print('Joint assessment is recommended')
                    else:
                        print('Separate assessment is recommended')

        #=========================================================
        def Reset():
            Page1.txtAnnualIncome1.delete(0, 'end')
            Page1.cbxdisability.set("No")
            Page1.cbxkids1.set('0')
            Page1.cbxkids2.set('0')
            Page1.cbxsingleparent.set("No")
            Page2.txtAnnualIncome1.delete(0, 'end')
            Page2.txtAnnualIncome2.delete(0, 'end')
            Page2.cbxdisability.set("No")
            Page2.cbxdisability1.set("No")
            Page2.cbxkids1.set('0')
            Page2.cbxkids2.set('0')
            
        #=========================================================
        def change_to_Page1():
            Page1.pack(side=TOP)
            Page1.pack_propagate(False)
            Page2.pack_forget()
            
        def change_to_Page2():
            Page2.pack(side=TOP)
            Page2.pack_propagate(False)
            Page1.pack_forget()
            
        #=========================================================
        R1 = Radiobutton(TopBodyFrame, font=('arial',10,'bold'),text="Single/Separated/Divorced/Widowed",value=1,command=change_to_Page1)
        R1.place(x=0,y=0)
        R1.select()
        
        R2 = Radiobutton(TopBodyFrame, font=('arial',10,'bold'),text="Married",value=2,command=change_to_Page2)
        R2.place(x= 400,y=0)
    
        Page1.lblAnnualIncome1 = Label(Page1, font=('arial',15,'bold'),text="Please input your Annual Income:", pady = 2)
        Page1.lblAnnualIncome1.place(x = 0, y = 10)
        Page1.txtAnnualIncome1 = Entry(Page1,font=('arial',15,'bold'))
        Page1.txtAnnualIncome1.place(x = 350, y = 15, width=390, height= 25)

        Page1.lbldisability = Label(Page1, font=('arial',10,'bold'), text="Eligible to claim Personal Disability Allowance")
        Page1.lbldisability.place(x = 10, y = 55)
        Page1.cbxdisability = ttk.Combobox(Page1, font=('arial',10,'bold'), state='readonly')
        Page1.cbxdisability['value']=('No','Yes')
        Page1.cbxdisability.current(0)
        Page1.cbxdisability.place(x= 350, y = 55, width = 50, height = 20)

        Page1.lblallowances = Label(Page1, font=('arial',10,'bold'), text="Other Allowances Claimed")
        Page1.lblallowances.place(x=10,y=85)
        Page1.lblkids = Label(Page1, font=('arial',10,'bold'), text="Number of dependent children")
        Page1.lblkids.place(x=100,y= 105)
        Page1.lblkids1 = Label(Page1, font=('arial',10,'bold'), text="Born in the year")
        Page1.lblkids1.place(x=150,y=125)
        Page1.cbxkids1 = ttk.Combobox(Page1, font=('arial',10,'bold'), state='readonly')
        Page1.cbxkids1['value']=('0','1','2','3','4')
        Page1.cbxkids1.current(0)
        Page1.cbxkids1.place(x= 350, y = 125, width = 50, height = 20)
        Page1.lblkids2 = Label(Page1, font=('arial',10,'bold'), text="Born in other year(s)")
        Page1.lblkids2.place(x=150,y=145)
        Page1.cbxkids2 = ttk.Combobox(Page1, font=('arial',10,'bold'), state='readonly')
        Page1.cbxkids2['value']=('0','1','2','3','4')
        Page1.cbxkids2.current(0)
        Page1.cbxkids2.place(x= 350, y = 145, width = 50, height = 20)
        Page1.lblsingleparent = Label(Page1, font=('arial',10,'bold'), text="Single Parent Allowance")
        Page1.lblsingleparent.place(x=100, y = 165)
        Page1.cbxsingleparent = ttk.Combobox(Page1, font=('arial',10,'bold'), state='readonly')
        Page1.cbxsingleparent['value']=('No','Yes')
        Page1.cbxsingleparent.current(0)
        Page1.cbxsingleparent.place(x= 350, y = 165, width = 50, height = 20)
        

        Page1.btnCompute = Button(Page1, font =('arial',15), width = 10, text="Calculate", command = single).place(x = 10, y = 250)
        Page1.btnReset = Button(Page1, font=('arial',15), width = 10, text="Reset", command = Reset).place(x=150, y = 250)

        #=========================================================

        Page2.lblAnnualIncome1 = Label(Page2, font=('arial',12,'bold'),text="Please input your Annual Income(Highest one):", pady = 2)
        Page2.lblAnnualIncome1.place(x = 0, y = 10)
        Page2.txtAnnualIncome1 = Entry(Page2,font=('arial',15,'bold'))
        Page2.txtAnnualIncome1.place(x = 0, y = 40, width= 350, height= 30)
        
        Page2.lblAnnualIncome2 = Label(Page2, font=('arial',12,'bold'),text="Please input your partner Annual Income:", pady = 2)
        Page2.lblAnnualIncome2.place(x = 400, y = 10)
        Page2.txtAnnualIncome2 = Entry(Page2,width= 340, font=('arial',15,'bold'))
        Page2.txtAnnualIncome2.place(x = 400, y = 40, width = 350, height = 30)

        Page2.lbldisability = Label(Page2, font=('arial',10,'bold'), text="Eligible to claim Personal Disability Allowance")
        Page2.lbldisability.place(x = 10, y = 85)

        Page2.lbldisabilityu = Label(Page2, font=('arial',10,'bold'), text="You:")
        Page2.lbldisabilityu.place(x = 350, y = 85)
        Page2.cbxdisability = ttk.Combobox(Page2, font=('arial',10,'bold'), state='readonly')
        Page2.cbxdisability['value']=('No','Yes')
        Page2.cbxdisability.current(0)
        Page2.cbxdisability.place(x= 400, y = 85, width = 50, height = 20)

        Page2.lbldisabilityp = Label(Page2, font=('arial',10,'bold'), text="Your partner:")
        Page2.lbldisabilityp.place(x = 500, y = 85)        
        Page2.cbxdisability1 = ttk.Combobox(Page2, font=('arial',10,'bold'), state='readonly')
        Page2.cbxdisability1['value']=('No','Yes')
        Page2.cbxdisability1.current(0)
        Page2.cbxdisability1.place(x= 600, y = 85, width = 50, height = 20)

        Page2.lblallowances = Label(Page2, font=('arial',10,'bold'), text="Other Allowances Claimed")
        Page2.lblallowances.place(x=10,y=105)
        Page2.lblkids = Label(Page2, font=('arial',10,'bold'), text="Number of dependent children")
        Page2.lblkids.place(x=100,y= 125)
        Page2.lblkids1 = Label(Page2, font=('arial',10,'bold'), text="Born in the year")
        Page2.lblkids1.place(x=150,y=145)
        Page2.cbxkids1 = ttk.Combobox(Page2, font=('arial',10,'bold'), state='readonly')
        Page2.cbxkids1['value']=('0','1','2','3','4')
        Page2.cbxkids1.current(0)
        Page2.cbxkids1.place(x= 350, y = 145, width = 50, height = 20)
        Page2.lblkids2 = Label(Page2, font=('arial',10,'bold'), text="Born in other year(s)")
        Page2.lblkids2.place(x=150,y=165)
        Page2.cbxkids2 = ttk.Combobox(Page2, font=('arial',10,'bold'), state='readonly')
        Page2.cbxkids2['value']=('0','1','2','3','4')
        Page2.cbxkids2.current(0)
        Page2.cbxkids2.place(x= 350, y = 165, width = 50, height = 20)

        Page2.btnCompute = Button(Page2, font =('arial',15), width = 10, text="Calculate", command = married).place(x = 10, y = 250)
        Page2.btnReset = Button(Page2, font=('arial',15), width = 10, text="Reset", command = Reset).place(x=150, y = 250)
        #=========================================================


        
if __name__ == '__main__':
    root = Tk()
    application = Income_Tax(root)
    root.resizable(width=False, height=False)
    root.mainloop()
