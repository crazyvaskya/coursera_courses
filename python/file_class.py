from tempfile import gettempdir as gettempdir
from os.path import join as join
import ntpath


class File:
    def __init__(self, filedir):
        self.filedir = filedir
        self.file_position = 0

    def write(self, string):
        with open(self.filedir, 'a') as f:
            f.write(string)

    def __str__(self):
        return self.filedir

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.filedir) as f:
            f.seek(self.file_position, 0)
            line = f.readline()
            self.file_position = f.tell()
        if line:
            return line
        else:
            raise StopIteration

    def __add__(self, rhs):
        temp_dir = gettempdir()
        new_file_name = join(temp_dir, '{}_{}'.format(
            ntpath.basename(self.filedir), ntpath.basename(rhs.filedir)))
        with open(new_file_name, 'w') as new_file:
            with open(self.filedir) as f:
                new_file.write(f.read())
            with open(rhs.filedir) as f:
                new_file.write(f.read())
        return File(new_file_name)

    def read(self):
        with open(self.filedir, 'r') as f:
            string = f.read()
        return string


def _main():
    a = File(join(gettempdir(), 'a.txt'))
    b = File(join(gettempdir(), 'b.txt'))

    print(a)
    print(b)

    a.write('ahah\n')

    b.write('wtf\n')
    b.write('what\n')

    c = a + b
    print(c.read())
    print(c)
    print('---------------')
    for line in c:
        print(line)


if __name__ == "__main__":
    _main()
