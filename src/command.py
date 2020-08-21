

class WB_Command():
    """
    This is used as a structure to safe the command data
    """

    def __init__(self, string):
        pieces = string.split("&")

        self.origin = pieces[0]
        self.target = pieces[1]
        self.unit  = pieces[2]
        self.start_time  = pieces[3]
        self.type = pieces[4]
        self.raw = string

    @staticmethod
    def create_new_command(string):
        pieces = string.split("&")

        if len(pieces) < 4:
            return None
        else:
            return WB_Command(
                string
            )