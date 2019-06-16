nh= input('Enter Hours:') #Numberof hours worked
np= input('Enter Rate:') #Normal pay per hour
ne= input('OT Rate post hours :') # After how many hours should OT rate apply
ot= input('Enter times Rate:') #what should be the Overtime rate
fe= float(ne) #If hours are in form of decimal, we need to convert to float
fh= float(nh) #If hours are in form of decimal, we need to convert to float
fp= float(np) #If pay is in form of decimal, we need to convert to float
OTR= float(ot)
if fh > OTR:
    #print('overtime')
    reg=fh*fp    #formula for regular pay
    OT= (OTR*fp)*(fh-fe) #formula for overtime
    #print('reg,OT')
    pay=reg+ OT
    print(pay)  #Do not put XPAY in quotes, otherwise python will take it as a string

else:
    #print('Regular pay')
     pay =fh*fp
     print(pay) #Do not put XPAY in quotes, otherwise python will take it as a string
