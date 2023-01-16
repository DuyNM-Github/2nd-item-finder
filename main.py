from selenium_automaton import selenium_automaton as SA

from sources import sources


def do_things():
    links = SA.get_items_based_on_prompt('voz', "", tag="HN")
    print(links)

if __name__ == "__main__":
    do_things()