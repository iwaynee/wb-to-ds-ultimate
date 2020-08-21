from requests.sessions import Session
from lxml import html
from io import StringIO

from tribalwars_data import DsData
from command import WB_Command

def main():
    SERVER = "178"


    # Step 0 - Init world
    data = DsData(server=SERVER)

    # Step 1 - Download Villages
    data.download_village_data()

    # Step 2 - Download Player
    data.download_player_data()

    # Read the downloaded Data
    data.read_ds_data()

    # Step 3 - Read Input Commands
    with open("input.txt", "r") as file:
        for line in file:
            # Step 4 - Split Commands to players
            data.append_command(WB_Command(line))

    # Step 5 - Generate ds ultimate links
    players = data.get_unique_player()

    urls = {}
    for player in players:

        # Get all commands of one player
        commands = data.get_commands_of_player(player)

        # compile commands to text
        text = ""
        for command in commands["command"]:
            text += command.raw

        # Create a new Attack plan on ds ultimate
        session = Session()
        session.headers.update({'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'})

        response = session.get(
            'https://ds-ultimate.de/de/' + data.server + '/tools/attackPlanner'
        )

        # Get Attack plan URL
        url_player_plan = response.url
        print("URL", url_player_plan)
        urls[player] = url_player_plan

        # Get Attack plan Number
        attack_list_id = url_player_plan.split("/")[-3]

        # Get Attack plan Key
        key = url_player_plan.split("/")[-1]

        # Get csrf token
        tree = html.parse(StringIO(response.text))
        metas = tree.xpath("//input")

        token = None
        for meta in metas:
            if meta.name == "_token":
                token = meta.value

        # Post import the WB Commands
        session.headers.update({"X-CSRF-TOKEN": token})
        pload = {'import': text,
                'key': key}
        response = session.post("https://ds-ultimate.de/tools/attackPlanner/"+ str(attack_list_id) +"/importWB/" + key, pload)
        session.close()


    # Step 6 - Generate readable forum table
    output_text =   "[table]\n" \
                    "[**]Player[||]URL[/**]\n"

    for url in urls:
        player = data.get_name_of_player(url)
        output_text += "[*][player]" + player + "[/player][|][url=" + urls[url] +"]" + "DS Ultimate Link" + "[/url]\n"
    output_text += "[/table]"

    # Write the Data to a file
    with open("output.txt", "w") as file:
        file.write(output_text)


























if __name__ == '__main__':
    main()