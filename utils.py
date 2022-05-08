from config import EXCLUDE_CHANNELS_PATH


def get_exclude_channels():
    with open(EXCLUDE_CHANNELS_PATH, "r+") as file:
        lines = file.readlines()
        channels = list()
        for line in lines:
            if not line: continue
            if line[0] == "#": continue
            if line == "\n": continue
            line = line.replace("\n", "")
            channels.append(line)
        return channels






def format_text(text: str) -> str:
    regular = "[]"


def bold(text):
    return f"<b>{text}</b>"


def code(text):
    return f"<code>{text}</code>"


def text_wrap(text):
    # TODO: Experiment with this
    wrapped = ""
    i = 0
    if len(text) > 34:
        while True:
            text_part = " ".join(text[i: i + 34].split(" ")[:-1])
            print(f"{text[i: i + 35]}   |   {text_part}")
            i += len(text_part)
            if text_part[0] == " ": text_part = text_part[1:]
            wrapped += text_part + "\n"
            if i + 34 > len(text): break
        wrapped += text.split(" ")[-1]
    else:
        return text

    return wrapped


if __name__ == '__main__':
    print(get_exclude_channels())