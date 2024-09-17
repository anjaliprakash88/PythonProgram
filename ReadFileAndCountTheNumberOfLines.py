with open("count") as file:
    lines = file.readlines()
    lines = [line for line in lines if line.strip()]
    total_lines = len(lines)
    print("Total: ", total_lines)