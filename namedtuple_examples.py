from collections import namedtuple
#
# student = namedtuple('student', 'full_name age gender')
#
# john = student(full_name='John', age=25, gender='male')
# ann = student(full_name='Ann', age=22, gender='female')
# print(john.full_name)
# print(john.age)
# print(ann.gender)

import pyttsx3

engine = pyttsx3.init()

# print(engine.getProperty('rate'))

# engine.setProperty('rate', 100)
# print(engine.getProperty('rate'))

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# engine.setProperty('voice', voices[1].id)

engine.say('hi man, how are you?')
engine.runAndWait()
engine.stop()

engine.save_to_file('hi man, how are you?', 'hi.mp3')
engine.runAndWait()