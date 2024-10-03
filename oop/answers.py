class players:
    def __init__(self, club, name):
        self.club = club
        self.name = name
    def together(self):
        return f"{self.club}: {self.name}"

my_Player = players("Barca", "Pedri")

print(my_Player.club)
print(my_Player.together())

players_arg = players("Inter Milan", "Lautaro")

print(players_arg.name)
print(players_arg.together())
