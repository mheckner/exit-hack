def main():
    my_file = open("myfile.txt", "w+")
    my_file.write("hello")
    my_file.close()

if __name__ == "__main__":
    main()
