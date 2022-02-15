def main():
    try:
        configuration = open('config.txt')
        print("Found it!")
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")

main()