
def generate_output(the_input):
    #pretend this is something complicated
    return -1*the_input

def read_int():
    return int(input()) 

def main():
    while True:
        try:
            the_input = read_int()
        except EOFError:
            break

        print(generate_output(the_input))

if __name__ == "__main__":
    main()

    
