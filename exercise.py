# # Exercise 1
# # Create an emotions dict, where the keys are the names of different human emotions and
# # the values are the degree to which the emotion is being felt on a scale from 1 to 3.
emotions = {
'happiness': 3,
'sad': 1,
'stress': 2
}

# Write a Person class with the following characteristics:
#
# name (string)
# emotions (dict)
# Initialize an instance of Person using your emotions dict from exercise 1.

class Person:

    def __init__(self, name, emotions):
        self.name = name
        self.emotions = emotions

    def __str__(self):
        return "{} is feeling {}.".format(self.name, self.emotions)

# Exercise 3
# Add an instance method to your class that displays a message describing how the person is feeling.

# Substitute the words "high", "medium", and "low" for the emotion levels 1, 2, and 3.
#
# For example:
#
# I am feeling a high amount of happiness.
# I am feeling a medium amount of stress.
# I am feeling a low amount of fear.
# would be the output for the dict
#
# { 'happiness': 3, 'stress': 2, 'fear': 1 }
# Try it out to make sure the method works.

    def emotion_level(self):
        for emotion, level in emotions.items():
            description = ""
            if level == 1:
                description = "low"
            elif level == 2:
                description = "medium"
            elif level == 3:
                description = "high"

            print("{} is feeling a {} amount of {}.".format(self.name, description, emotion))

person1 = Person("Sarah", emotions)
print(person1)
print(person1.emotion_level())
