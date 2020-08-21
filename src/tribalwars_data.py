import requests
import pandas as pd



class DsData():

    def __init__(self, server):
        self.server = server

        self.villages = None
        self.player = None

        self.df = pd.DataFrame(columns=("player", "command"))

    def download_village_data(self):
        # create URL
        url = "https://de" + self.server + ".die-staemme.de/map/village.txt"

        r = requests.get(url, allow_redirects=True)
        open('data/village.txt', 'wb').write(r.content)



    def download_player_data(self):
        pass
        url = "https://de" + self.server + ".die-staemme.de/map/player.txt"

        r = requests.get(url, allow_redirects=True)
        open('data/player.txt', 'wb').write(r.content)

    def read_ds_data(self):

        # Read Village Data
        self.villages = pd.read_csv("data/village.txt", header=None)
        # id, name, x, y, player id, pkt,

        # sort out bb villages
        self.villages = self.villages.loc[self.villages[4] != 0]

        # Read Player Data
        self.player = pd.read_csv("data/player.txt", header=None)


    def append_command(self, cmd):
        """
        Appends a new command to the df an links it to a certain player
        The data from WB will just give you village id so you have to look for the village to get the owner of the village
        """

        # Get origin id
        origin = cmd.origin

        # Get plyer id
        playerId = self.villages.loc[self.villages[0] == int(origin)][4].values[0]
        self.df = self.df.append({"player": playerId, "command": cmd}, ignore_index=True)


    def get_unique_player(self):
        """
        Returns all unique players in the df.
        """
        var = self.df.player.unique()

        return var

    def get_commands_of_player(self, playerId):
        """
        Returns all commands of a certain player.
        """
        var = self.df.loc[self.df.player == playerId]

        return var

    def get_name_of_player(self, playerId):
        """
        Returns the name of a player.
        """
        var = self.player.loc[self.player[0] == int(playerId)]

        return var.values[0][1]