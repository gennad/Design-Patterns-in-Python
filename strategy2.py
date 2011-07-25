class Button:
    """A very basic button widget."""
    def __init__(self, submit_func, label):
        self.on_submit = submit_func   # Set the strategy function directly
        self.label = label

# Create two instances with different strategies
button1 = Button(sum, "Add 'em")
button2 = Button(lambda nums: " ".join(map(str, nums)), "Join 'em")

# Test each button
numbers = range(1, 10)   # A list of numbers 1 through 9
print button1.on_submit(numbers)   # displays "45"
print button2.on_submit(numbers)   # displays "1 2 3 4 5 6 7 8 9"

