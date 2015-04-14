class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print self.sounds[i % len(self.sounds)],
        print ""

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print "Be with you in a moment"
        print "Twoning, sproing, splang"

class Drummer(Musician):
    def __init__(self):
        super(Drummer, self).__init__(["Tsh", "Uhg", "Pock"])

    def four_count(self):
        for i in range(0,5):
            print i

    def combust(self):
        print "Spontaneously combusting!"

class Band(object):
    def __init__(self):
        self.members = []

    def hire(self, musician):
        self.members.append(musician)

    def fire(self, musician):
        self.members.remove(musician)

    def start_playing(self):
        for member in self.members:
            if isinstance(member, Drummer):
                member.four_count()
        for member in self.members:
            if not isinstance(member, Drummer):
                member.solo(10)

blaze = Guitarist()
lazer = Drummer()
blazer = Bassist()

pythons = Band()
pythons.hire(blaze)
pythons.hire(lazer)
pythons.hire(blazer)

pythons.start_playing()
