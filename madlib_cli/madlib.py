import re


def main():
    name = input("Welcome to Madlib! What's your name? ")
    print(f"""
    Hello {name}, let's play a game! Fill in the blank spaces with the described word type.
    """)


def read_template(file_path):
    with open(file_path, "r")as file:
        content = file.read()
        return content


def parse_template(content):



def merge(new_string, find_all_list):


if __name__ == "__main__":
    main()
    read_template("../assets/dark_and_stormy_night_template.txt")
    read_template("../assets/make_me_a_video_game_template.txt")
    parse_template()
    merge()
