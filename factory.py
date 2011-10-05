class Pizza(object):
    def __init__(self):
        self._price = None

    def get_price(self):
        return self._price

class HamAndMushroomPizza(Pizza):
    def __init__(self):
        self._price = 8.5

class DeluxePizza(Pizza):
    def __init__(self):
        self._price = 10.5

class HawaiianPizza(Pizza):
    def __init__(self):
        self._price = 11.5

class PizzaFactory(object):
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == 'HamMushroom':
            return HamAndMushroomPizza()
        elif pizza_type == 'Deluxe':
            return DeluxePizza()
        elif pizza_type == 'Hawaiian':
            return HawaiianPizza()

if __name__ == '__main__':
    for pizza_type in ('HamMushroom', 'Deluxe', 'Hawaiian'):
        print 'Price of {0} is {1}'.format(pizza_type, PizzaFactory.create_pizza(pizza_type).get_price())


# ------------------- Second example -----------------


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
