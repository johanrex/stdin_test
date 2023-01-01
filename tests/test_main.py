
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import main

def read_int_from_file(filename):
    #let's read the file content into a list of strings that we can feed the input() function somehow. 
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    
    #perhaps involve generator that yields the next line? idk...
    for line in lines:
        pass
        #TODO... 

def test_1():
    #monkey patch perhaps?
    main.read_int = read_int_from_file("tests/input_1.txt")
    main.main()
