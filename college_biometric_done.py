import DS1302
from machine import Pin
from time import sleep

led1 = machine.Pin(15, machine.Pin.OUT)
led2 = machine.Pin(16, machine.Pin.OUT)
ds = DS1302.DS1302(clk=Pin(0), dio=Pin(1), cs=Pin(2))
ds.start()

# ds.year(2021)
# ds.month(12)
# ds.day(15)
# ds.weekday(3)
# hour(15)
# ds.second(7)
# ds.minute(3)


# hour([2022, 3, 20, 0, 21, 56, 25])

# hour([2022, 3, 20, 0, 21, 20, 30])

morng_start = 8
morng_end = 9#:15
aftrn_start = 13
aftrn_end = 14#:15
evng_start = 16#:15
evng_end = 18
print(ds.hour())

#replace wvery ds.datetime with hour
hour = int(input())
print(type(hour))
#hour = ds.hour() uncommnet it and remove above statement to make it work properly

# Make the below code to run in a while True loop:

if hour < morng_start:
    while hour != morng_start:
        led1(0)
        led2(0)
else:
    pass

if hour < morng_end:
    while hour != morng_end:
        led1(1)
        led2(1)
else:
    pass

if hour < aftrn_start:
    while hour != aftrn_start:
        led1(0)
        led2(0)
else:
    pass

if hour < aftrn_end:
    while hour != aftrn_end:
        led1(1)
        led2(1)
else:
    pass
if hour < evng_start:
    while hour != evng_start:
        led1(0)
        led2(0)
else:
    pass

if hour < evng_end:
    while hour != evng_end:
        led1(1)
        led2(1)
else:
    pass

if hour > evng_end:
    while hour != morng_start:
	led1(0)
	led2(0)


# sleep(4500)
#     
#     
#     while True:
#     print(hour())
#     sleep(1)
# 
#     

