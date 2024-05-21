import pyttsx3

friend = pyttsx3.init()
names = ["StupidProgramm1","AayushGarg15", "Yuniek", "NiteshUpadhyay2",]
for name in names:
    friend.say(f'Shout out to the my friend {name}')

friend.runAndWait()

#write anything he copy your text
friend = pyttsx3.init()
speech = input ("say something:")
friend.say(speech)
friend.runAndWait()
