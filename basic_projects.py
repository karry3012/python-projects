# python dice project 
'''import random
while True:
    r=random.randint(1,6)
    print(r)
    
    a=input("do u want to continue--? plz press (y) yes or no(n)")
    if ( a=='y'):
        continue
    else:
        break
print("Thanks for playing!!:)")'''
# clock 
'''from time import strftime
import tkinter
def clock():
    time1= strftime('%H : %M : %S: %p')
    l.config(text=time1,font=('arial',150))
    l.after(1000,clock)
r=tkinter.Tk()
l=tkinter.Label(r)
l.pack()
clock()
    
r.mainloop()'''

# world clock
'''import pytz
from datetime import datetime
#time_zone = pytz.all_timezones
#print(time_zone,end='\n')
country_name = pytz.timezone('Asia/Jakarta')
country_time = datetime.now(country_name)
print(country_time.strftime("date is %d-%m-%y and time is %H:%M:%S:%p"))'''
# random password generator
'''import random
import string
print("\n welcome to random python generator:-")
def main():
    
    length=int(input("enter the length of password that u want:"))
    a=string.ascii_lowercase
    b=string.ascii_uppercase
    c=string.digits
    d=string.punctuation
    combine = a+b+c+d
    x=random.sample(combine,length)
    passw=''.join(x)
    print(passw)
    main()
main()

'''









