import datetime, discord
import constants

async def process_message(message):

    message_content = message.content.split()
    message_command = message_content[0].upper()

    if message_command == "!420" and len(message_content) > 1:
        print("Command received:", message_content[1].upper())
        match message_content[1].upper():
            case "?":
                last_line = get_last_timestamp()
                if last_line:
                    await message.channel.send(f"Last smoke: {last_line}\nYes! It's time to smoke!")
                else:
                    await message.channel.send("No smoke recorded yet.")
            case "SMOKE":
                append_timestamp()


def append_timestamp():
    try:
       print("opening file")
       with open(constants.LOG_FILE, "a") as f:
           time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           f.write(time_stamp + "\n")
    except Exception as e:
        print("Error writing to log file:", e)
        return False
    

def get_last_timestamp():
    try:
        with open(constants.LOG_FILE, "r") as f:
            lines = f.readlines()
            last_line = lines[-1]
            return last_line
    except Exception as e:
        print("Error reading from log file:", e)
        return False