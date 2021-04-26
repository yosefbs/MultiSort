# this class is used to wrap text file iterate in it
# and compere between files.
# the compression is done by comparing the current line in 2 files.


class FileHandler:
    def __init__(self, file):
        self.file = file
        self.file_iter = iter(open(file, 'r').readline, '')
        self.cur_line = next(self.file_iter)
        self.EOF = False

    def __lt__(self, other):
        return self.cur_line < other.cur_line

    def __gt__(self, other):
        return other.__lt__(self)

    def __eq__(self, other):
        return self.cur_line == other.cur_line

    def __ne__(self, other):
        return not self.__eq__(other)

# this method return the current line and move the iterator to next line
    def get_line_and_go_next(self):
        res = self.cur_line
        try:
            self.cur_line = next(self.file_iter)
        except StopIteration:
            self.EOF = True
        return res
