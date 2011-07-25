"""An example of the Template pattern in Python"""

# Skeletons
def iter_elements(getter, action):
    """Template skeleton that iterates items"""

    for element in getter():
        action(element)
    print "-" * 10

def rev_elements(getter, action):
    """Template skeleton that iterates items in reverse order"""

    for element in getter()[::-1]:
        action(element)
    print "-" * 10

# Getters
def get_list():
    return "spam eggs".split()

def get_lists():
    return [list(x) for x in "spam eggs".split()]

# Actions
def print_item(item):
    print item

def reverse_item(item):
    print item[::-1]

# Makes templates
def make_template(skeleton, getter, action):
    """Instantiate a template method with getter and action"""
    def template():
        skeleton(getter, action)
    return template

# Create our template functions
templates = [make_template(s, g, a)
             for g in (get_list, get_lists)
             for a in (print_item, reverse_item)
             for s in (iter_elements, rev_elements)]

# Execute them
for template in templates:
    template()
