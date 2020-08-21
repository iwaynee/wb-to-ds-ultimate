# wb-to-ds-ultimate

This tool enables you to convert the raw commands from DS Workbench to multiple Attack plans in DS Ultimate.

- Splits all commands into different Attack plans for each player.
- Automatically generates an Attack plan on https://ds-ultimate.de/
- Currently only works on DE-Server
- At the end, this tool generates a BB-Code Table which you can post in the Forum

### How to use it
1. Install python
2. Install all dependencies (requests, lxml, pandas)
3. Mark all your commands in WB with CTRL + A and copy them with CTRL + C
4. Paste and save all commands in a text file named "input.txt" which should be placed in the same folder as "main.py"
5. Enter your server in "main.py" (see "SERVER")
6. Run the script
7. There should now be a file named "output.txt"
8. Copy the content of this file to your forum and share all the Attack plans!