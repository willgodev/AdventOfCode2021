if __name__ == "__main__":
    with open("input", "r") as input_file:
        commands = [command.strip() for command in input_file]
        vertical_pos = 0
        horizontal_pos = 0
        aim = 0
        for command in commands:
            parsed_commands = command.split()
            movement = parsed_commands[0]
            units = int(parsed_commands[1])
            if movement == "forward":
                horizontal_pos += units
                vertical_pos += (aim * units)
            elif movement == "up":
                aim -= units
            elif movement == "down":
                aim += units
        print(vertical_pos * horizontal_pos)