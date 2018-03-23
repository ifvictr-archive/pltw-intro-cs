class Boat():
    def __init__(self):
        self.tonnage = 0
        self.name = ""
        self.is_docked = True

    def dock(self):
        if self.is_docked:
            print("You are already docked")
        else:
            self.is_docked = True
            print("Docking")

    def undock(self):
        if not self.is_docked:
            print("You aren't docked")
        else:
            self.is_docked = False
            print("Undocking")

class Submarine(Boat):
    def __init__(self):
        super().__init__()
        self.windows = 0

    def submerge(self):
        print("Submerge")

s = Submarine()
print(s.name, s.tonnage, s.is_docked, s.windows)