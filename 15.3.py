class StringVar():
    string = ''

    def __init__(self, string):
        self.string = string

    def getString(self):
        return self.string

    def setString(self, string):
        self.string = string

newstring = StringVar('Hello, world!')
print(newstring.getString())
newstring.setString('What\'s up?')
print(newstring.getString())
