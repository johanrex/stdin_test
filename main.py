#main.py:
def generate_output(the_input):
    #pretend this is something complicated
    return -1*the_input

def read_int(input_):
    return int(input_()) 

def main(input_=input, print_=print):
    while True:
        try:
            the_input = read_int(input_)
        except EOFError:
            break

        print_(generate_output(the_input))

if __name__ == "__main__":
    main()

    
