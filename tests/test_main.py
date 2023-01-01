
#test_main.py:
import sys
from pathlib import Path

#silly stuff in order to import the main.py module
sys.path.insert(0, str(Path(__file__).parent.parent))
import main


class MockIO:
    def __init__(self, input_path, output_path):
        
        with open(input_path, "r") as f:
            self.input_lines = [line.strip() for line in f.readlines()]

        with open(output_path, "r") as f:
            self.output_lines = [line.strip() for line in f.readlines()]

        self.input_file_index = 0
        self.output_file_index = 0

    def mock_input(self, prompt=None):
        if self.input_file_index >= len(self.input_lines):
            raise EOFError

        line = self.input_lines[self.input_file_index]
        self.input_file_index += 1
        return line

    def mock_print(self, *args, **kwargs):
        if self.output_file_index >= len(self.output_lines):
            raise EOFError

        line = self.output_lines[self.output_file_index]
        self.output_file_index += 1
        assert line == " ".join([str(arg) for arg in args])



def test_1():
    mock_io = MockIO("tests/input_1.txt", "tests/output_1.txt")
    main.main(mock_io.mock_input, mock_io.mock_print)

if __name__ == "__main__":
    test_1()
