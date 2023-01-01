
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import main

def read_int_from_file(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    
    #perhaps involve generator that yields the next line?
    for line in lines:
        pass
        #TODO... 

def test_1():
    main.read_int = read_int_from_file("test1.txt")
    main.main()
