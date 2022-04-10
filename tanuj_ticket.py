# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 11:39:33 2022

@author: Ujwal
"""
import random 

print("Note: Be aware of upper and lower case in spellings when booking")
print("      An adult may only bring up to 2 children")
print("      An evening barbecue is only for 2 day tickets")
print("      A Family ticket consists of 3 children and 2 adults or seniors")
print("      A Group ticket consists of 6 people or more\n")
print("Ticket Type     Cost for One Day    Cost for Two Days")
print("-----------------------------------------------------")
print("One Adult            $20.00             $30.00")
print("One Child            $12.00             $18.00")
print("One Senior           $16.00             $24.00")
print("Family               $60.00             $90.00")
print("Group(per person)    $15.00             $22.50")
print("")
print("Extra Attractions                     Cost Per Person")
print("-----------------------------------------------------")
print("Lion Feeding                               $2.50")
print("Penguin Feeding                            $2.00")
print("Evening Barbecue(two day tickets only)     $5.00")
print("")

# Task 2
tta = str('Adult') # string  for calling Adults
tts = str('Senior') # string  for calling Adults
ttc = str('Child')
ttf = str('Family')
ttg = str('Group')

eal = str('Lion Feeding')
eap = str('Penguine Feeding')
eab = str('Evening Barbeque')

c1a = 20 #cost
c1s = 15 
c1c = 12
c1f = 60
c1g = 15

c2a = 30
c2s = 24
c2c = 18
c2f = 90
c2g = 22.50

lf = 2.5
pf = 2
eb = 5

t1lea = 0
t1pea = 0
cost1totalea = 0
tl2ea = 0
tp2ea = 0
tebea = 0
cost2totalea = 0
cost1total = 0
cost2total = 0

booknum = random.randint(10000, 99999)
print('When do you want the ticket for? (Mon, Tue, Wed,Thu, Fri, Sat, Sun')
week = input()
print('How many days would you want the ticket for(1 or 2)?')
day = int(input())
while day != 1 and day != 2:
    day = int(input("Please enter only 1 or 2 for number of days of ticket"))
print('How many tickets for Adults?')
tnumadult = int(input())
print('How many tickets for Seniors?')
tnumsenior = int(input())
print('How many tickets for Children?')
tnumchild = int(input())

ttotal = tnumadult + tnumsenior + tnumchild  #total number of tickets


if ttotal == 0 : print('You have not booked any tickets. Please restart the booking manually') 

elif tnumchild >=1 and (tnumadult or tnumsenior) == 0 :
    print('You must be accompanied by a Senior or an Adult')
    

    
else :
   print('Lets proceed')
   print('Would you like to avail any Extra Attractions?(yes or no)')
   tboolea= input()
   if tboolea == 'yes' : 
       print('')
       if day == 1:
         print('How many tickets do you want for Lion Feeding?')
         t1lea = int(input())
         while t1lea > ttotal :
          t1lea = int(input("Total number of tickets exceed total number of people"))
         print('How many tickets do you want for Penguin Feeding?')
         t1pea = int(input())
         while t1pea > ttotal :
          t1pea = int(input("Total number of tickets exceed total number of people"))
         print ('Your booking number for ' + str(week) + ' for ' +str(day)+' day(s) for '+ str(tnumadult) + ' Adults ' + str(tnumsenior) + ' Seniors ' + str(tnumchild) + ' Children is ' + str(booknum)) 
         cost1totalea = c1a*tnumadult + c1s*tnumsenior + c1c*tnumchild + t1lea*lf + t1pea*pf 
         print ('Your booking amount is $'  + str(cost1totalea)) 
       elif day == 2:
         print('How many tickets do you want for Lion Feeding?')
         tl2ea = int(input())
         while tl2ea > ttotal :
          tl2ea = int(input("Total number of tickets exceed total number of people"))
         print('How many tickets do you want for Penguine Feeding?')
         tp2ea = int(input())
         while tp2ea > ttotal :
          tp2ea = int(input("Total number of tickets exceed total number of people"))
         print('How many tickets do you want for Evening Barbeque?')
         tebea = int(input())
         while tebea > ttotal :
          tebea = int(input("Total number of tickets exceed total number of people"))
         print ('Your booking number for ' + str(week) + ' for ' +str(day)+' day(s) for '+ str(tnumadult) + ' Adults ' + str(tnumsenior) + ' Seniors ' + str(tnumchild) + ' Children is ' + str(booknum)) 
         cost2totalea = c2a*tnumadult + c2s*tnumsenior + c2c*tnumchild + + tl2ea*lf + tp2ea*pf + tebea*eb
         print ('Your booking amount is $'+ str(cost2totalea))
            
   elif tboolea == 'no' :  
      print ('Your booking number for ' + str(week) + ' for ' +str(day)+' day(s) for '+ str(tnumadult) + ' Adults ' + str(tnumsenior) + ' Seniors ' + str(tnumchild) + ' Children is ' + str(booknum)) 
      if day == 1:
         
         cost1total = c1a*tnumadult + c1s*tnumsenior + c1c*tnumchild 
         print ('Your booking amount is $'  + str(cost1total))
      elif day == 2:
         print ('Your booking number for ' + str(week) + ' for ' +str(day)+' day(s) for '+ str(tnumadult) + ' Adults ' + str(tnumsenior) + ' Seniors ' + str(tnumchild) + ' Children is ' + str(booknum))
         cost2total = c2a*tnumadult + c2s*tnumsenior + c2c*tnumchild 
         print ('Your booking amount is $'+ str(cost2total))
# task 3
if ( cost1total or cost1totalea or cost2total or cost2totalea ) >=1 :
    print('Would you like to proceed with the best value for your booking?')
    tboolbv = input()
    if tboolbv == 'yes' : 
        newbooknum = random.randint(10000, 99999)
        
        
        if day == 1 :
      
            costbvg1 = (ttotal)*(c1g) + tl2ea*lf + tp2ea*pf + tebea*eb + t1lea*lf + t1pea*pf 
            if ttotal >= 6 :
                if cost1total <= costbvg1 :
                 print('You already have the best value')
                elif cost2total > costbvg2 :
                 print('Your booking for ' + str(ttotal) + 'people is $' + str(costbvg1))
             
            
                 print ('Your new Booking Number is ' + str(newbooknum)) 
        
            elif tnumadult == 0 and tnumsenior == 2 and tnumchild == 3 :
                print ('You are eligible for Family ticket')
                print('Your booking value is ' +str(60 + tl2ea*lf + tp2ea*pf + tebea*eb + t1lea*lf + t1pea*pf))
                print ('Your new Booking Numbr is ' + str(newbooknum))
            elif tnumadult == 1 and tnumsenior == 1 and tnumchild == 3 :
                print ('You are eligible for Family ticket')
                print('Your booking value is ' +str(60 + tl2ea*lf + tp2ea*pf + tebea*eb + t1lea*lf + t1pea*pf))    
                print ('Your new Booking Numbr is ' + str(newbooknum))
            elif tnumadult == 2 and tnumsenior == 0 and tnumchild == 2 :
                print ('You are eligible for Family ticket')
                print('Your booking value is ' +str(60 + tl2ea*lf + tp2ea*pf + tebea*eb + t1lea*lf + t1pea*pf))   
                print ('Your new Booking Numbr is ' + str(newbooknum))
            elif tnumadult == 2 and tnumsenior == 0 and tnumchild == 3 :
                print ('You are eligible for Family ticket')
                print('Your booking value is ' +str(60 + tl2ea*lf + tp2ea*pf + tebea*eb + t1lea*lf + t1pea*pf))  
                print ('Your new Booking Numbr is ' + str(newbooknum))
                
        elif day ==2 :
            
            costbvg2 = (ttotal)*(c2g) + tl2ea*lf + tp2ea*pf + tebea*eb + t1lea*lf + t1pea*pf 
            
            if ttotal >= 6 :
                if cost2total <= costbvg2 :
                 print('You already have the best value')
                elif cost2total > costbvg2 :
                 print('Your booking for ' + str(ttotal) + 'people is $' + str(costbvg2))
             
             
             
            elif tnumadult == 0 and tnumsenior == 2 and tnumchild == 3 :
                print ('You are eligible for Family ticket')
                print('Your booking value is ' +str(90 + tl2ea*lf + tp2ea*pf + tebea*eb + t1lea*lf + t1pea*pf))
                print ('Your new Booking Numbr is ' + str(newbooknum))
            elif tnumadult == 1 and tnumsenior == 1 and tnumchild == 3 :
                print ('You are eligible for Family ticket')
                print('Your booking value is ' +str(90 + tl2ea*lf + tp2ea*pf + tebea*eb + t1lea*lf + t1pea*pf))    
                print ('Your new Booking Numbr is ' + str(newbooknum))
            elif tnumadult == 2 and tnumsenior == 0 and tnumchild == 2 :
                print ('You are eligible for Family ticket')
                print('Your booking value is ' +str(90 + tl2ea*lf + tp2ea*pf + tebea*eb + t1lea*lf + t1pea*pf))   
                print ('Your new Booking Numbr is ' + str(newbooknum))
            elif tnumadult == 2 and tnumsenior == 0 and tnumchild == 3 :
                print ('You are eligible for Family ticket')
                print('Your booking value is ' +str(90 + tl2ea*lf + tp2ea*pf + tebea*eb + t1lea*lf + t1pea*pf))  
                print ('Your new Booking Numbr is ' + str(newbooknum))
    
    elif tboolbv == 'no':
        print('Thankyou! Your total payable cost is $' + str(cost1total + cost1totalea + cost2total + cost2totalea))
    

 




