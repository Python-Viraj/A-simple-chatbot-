import webbrowser
import sys
import wikipedia
import datetime
import time

quit = ['quit', 'Quit', 'bye', 'Bye', 'Goodbye', 'goodbye']
hi = ['hi', 'Hi', 'Hello', 'hello', 'Hey', 'hey']
def T(hi, quit):    
    ask = input('HOW CAN I HELP YOU\n>')
    if ask == 'what is the time' or 'what is time' or 'Time' or 'time':
        print(time.asctime())
    if ask in hi:
        print('HI THERE\n \n \n')
        T(hi, quit)
    if ask in quit:
        print('See you later......\n \n \n')
        sys.exit()
    if ask == 'dance' or ask == 'Dance':
        webbrowser.open('https://www.youtube.com/watch?v=FzG4uDgje3M')
        T(hi, quit)
    if ask == 'open wikipedia':
        print('ASK ME ANYTHING')
        wiki = input('>')
        if True:
            print(wikipedia.summary(wiki, sentences=2))
            T(hi, quit)
        if False:
            print('HEY I DID NOT GET THAT!')
            t(hi, quit)
    lt = ['how do you work', 'How do you work', 'how does your system work']
    if ask in lt:
        print('Sssshhhhhh......\n It is a secret.....')
        T(hi, quit)
print('INITIALISING CHATBOT')
time.sleep(2)
for x in range(0, 50):
    print('')
print('HELLO THERE \n CAN YOU PLEASE NAME ME?')
name = input('>')
print(name,' IS SUCH A NICE NAME')
print('.....')
time.sleep(2)
print('WELL I AM A CHATBOT.\nI CAN TALK TO YOU,\nPLAY MUSIC,\nAND MANY OTHER THINGS')
print('.....')
time.sleep(2)
T(hi, quit)
