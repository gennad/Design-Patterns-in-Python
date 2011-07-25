#coding: UTF8

class JapaneseGetter:
    """A simple localizer a la gettext"""

    def __init__(self):
        self.trans = dict(dog="犬", cat="猫")

    def get(self, msgid):
        """We'll punt if we don't have a translation"""

        try:
            return unicode(self.trans[msgid], "utf-8")
        except KeyError:
            return unicode(msgid)

class EnglishGetter:
    """Simply echoes the msg ids"""
    def get(self, msgid):
        return unicode(msgid)

def get_localizer(language="English"):
    """The factory method"""

    languages = dict(English=EnglishGetter,
                     Japanese=JapaneseGetter)

    return languages[language]()

# Create our localizers
e, j = get_localizer("English"), get_localizer("Japanese")

# Localize some text
for msgid in "dog parrot cat".split():
    print e.get(msgid), j.get(msgid)
