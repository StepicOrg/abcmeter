from contextlib import contextmanager
from datetime import datetime

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from cpp.CPP14Listener import CPP14Listener
from cpp.parsers.CPP14Lexer import CPP14Lexer
from cpp.parsers.CPP14Parser import CPP14Parser


def print_with_time_label(start_time, content, end='\n'):
    delta_time = datetime.now() - start_time
    print(f'{format(delta_time.total_seconds(), ".5f")}: {content}', end=end)


@contextmanager
def print_process(start_time, process_name):
    print_with_time_label(start_time, process_name + ' start')
    yield
    print_with_time_label(start_time, process_name + ' done')


def main():
    file_name = 'cpp/tests/positives_negatives.cpp'
    start_time = datetime.now()
    with print_process(start_time, f'input from {file_name}'):
        input = FileStream(file_name, encoding='utf8')

    with print_process(start_time, 'analysis'):
        lexer = CPP14Lexer(input)
        stream = CommonTokenStream(lexer)

    with print_process(start_time, 'parsing'):
        parser = CPP14Parser(stream)
        tree = parser.translationunit()

    with print_process(start_time, 'calculate score'):
        CPP14 = CPP14Listener()
        walker = ParseTreeWalker()
        walker.walk(CPP14, tree)
    print_with_time_label(start_time, 'a: ' + str(CPP14.a))
    print_with_time_label(start_time, 'b: ' + str(CPP14.b))
    print_with_time_label(start_time, 'c: ' + str(CPP14.c))
    print_with_time_label(start_time, 'ABC score: ' + str(CPP14.abc_score))


if __name__ == '__main__':
    main()
