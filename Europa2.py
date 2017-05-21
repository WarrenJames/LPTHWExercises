# Callisto
# Mood Stablizer

from sys import argv

script = argv

sad = ['sad', 'tired', 'bored', 'lonely', 'depressed', 'ashamed',
'guilty', 'sleepy', 'apathetic', 'isolated', 'inferior', 'stupid',
'remorseful']
mad = ['mad', 'hurt', 'hostile', 'angry', 'selfish', 'hateful', 'critical',
'distant', 'sarcastic', 'frustrated', 'jealous', 'irritated', 'skeptical']
scared = ['scared', 'confused', 'rejected', 'helpless', 'submissive', 'insecure',
'anxious', 'bewildered', 'discouraged', 'insignificant', 'inadequate',
'embarrassed', 'overwhelmed']
joyful = ['joyful', 'excited', 'sensuous', 'energetic', 'cheerful', 'creative',
'hopeful', 'daring', 'fascinating', 'stimulating', 'amused', 'playful',
'optimistic', 'happy']
powerful = ['powerful', 'aware', 'proud', 'respected', 'appreciated', 'important',
'faithful', 'confident', 'discerning', 'valueable', 'worthwhile', 'successful',
'surprised']
peaceful = ['peaceful', 'content', 'thoughful', 'intimate', 'loving', 'trusting',
'nurturing', 'relaxed', 'pensive', 'responsive', 'serene', 'secure', 'thankful']

def start():
    print "Hi there my name is %s, What is yours?" % (script)
    user_name = raw_input("> ")
    print "Pleased to meet you %s" % (user_name)
    fq()

def fq():
    print "How are you feeling today?"
    mood = raw_input("> ")

    if mood.lower() in sad:
        print "Sad!"
    elif mood.lower() in mad:
        print "Mad!"
    elif mood.lower() in scared:
        print "Scared!"
    elif mood.lower() in joyful:
        print "Joyful!"
    elif mood.lower() in powerful:
        print "Powerful!"
    elif mood.lower() in peaceful:
        print "Peaceful!"
    else:
        print "Invalid input. Try typing your current emotion."
        fq()

start()
