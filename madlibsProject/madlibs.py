color = input("Enter a color: ") # adjective
costume = input("Enter a noun: ") #noun
verb = input("Enter a verb ending in -ing: ") #verb

partsOfSpeech = [color,costume,verb]

def fullMadlib():
    print("Halloween is my favorite holiday because I get to dress up like a " + partsOfSpeech[1]+
     ". Also, Fall is the best season because the leaves are changing from green to " + partsOfSpeech[0] +
    ". My favorite part of Halloween is " + partsOfSpeech[2] + " lots of kitkats.")

fullMadlib() #call function
