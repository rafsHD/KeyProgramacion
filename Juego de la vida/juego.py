def load_file():
    filepath = input("Enter the path of the file to load: ")
    
    file = open(filepath, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    return lines 

my_file = load_file()


def set_environment(raw_file):
    env = []
    for line in raw_file:
        line = line.strip()
        env.append([int(c) for c in line])
    return env

my_file = load_file()
env = set_environment(my_file)
print(env)