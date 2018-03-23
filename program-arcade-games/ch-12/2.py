class Address():
    def __init__(self):
        self.name = ""
        self.street = ""
        self.city = ""
        self.state = ""
        self.zip = ""

    def print(self):
        template = """
%s

%s
%s, %s %s
        """
        attrs = (self.name, self.street, self.city, self.state, self.zip)
        print(template % attrs)

home_addr = Address()
home_addr.name = "Mark Zuckerberg"
home_addr.street = "1 Hacker Way"
home_addr.city = "Menlo Park"
home_addr.state = "CA"
home_addr.zip = 94025
home_addr.print()