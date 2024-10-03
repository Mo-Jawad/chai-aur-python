class players:
    def __init__(self, club, name):
        self.club = club
        self.name = name
    def together(self):
        return f"{self.club}: {self.name}"
    
class contact_year(players):
    def __init__(self, club, name, contact):
        super().__init__(club, name)
        self.contact = contact

bundesliga = contact_year("bayern", "kane", "3 years")
print(bundesliga.contact)
print(bundesliga.together())

my_Player = players("Barca", "Pedri")

print(my_Player.club)
print(my_Player.together())

players_arg = players("Inter Milan", "Lautaro")

print(players_arg.name)
print(players_arg.together())
