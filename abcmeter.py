import os
from contextlib import contextmanager
from datetime import datetime

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

CPP = 'c++'
JAVA = 'java8'
PYTHON = 'python3'

language_by_extension = {
    '.cpp': CPP,
    '.java': JAVA,
    '.py': PYTHON,
}


def print_with_time_label(start_time, content, end='\n'):
    delta_time = datetime.now() - start_time
    print(f'{format(delta_time.total_seconds(), ".5f")}: {content}', end=end)


@contextmanager
def print_process(start_time, process_name):
    print_with_time_label(start_time, process_name + ' start')
    yield
    print_with_time_label(start_time, process_name + ' done')


def get_lexer_parser_listener(language):
    if language == CPP:
        from cpp.CPP14Listener import Listener
        from cpp.parsers.CPP14Lexer import CPP14Lexer
        from cpp.parsers.CPP14Parser import CPP14Parser
        return CPP14Lexer, CPP14Parser, Listener, CPP14Parser.translationunit

    if language == JAVA:
        from java8.Java8Listener import Listener
        from java8.parsers.Java8Lexer import Java8Lexer
        from java8.parsers.Java8Parser import Java8Parser
        return Java8Lexer, Java8Parser, Listener, Java8Parser.compilationUnit


def get_language_by_file(file_name):
    _, extension = os.path.splitext(file_name)

    return language_by_extension[extension]


def calculate_abc_score(start_time, file_name, language):
    Lexer, Parser, Listener, start_token = get_lexer_parser_listener(language)

    with print_process(start_time, f'input from {file_name}'):
        input = FileStream(file_name, encoding='utf8')

    with print_process(start_time, 'analysis'):
        lexer = Lexer(input)
        stream = CommonTokenStream(lexer)

    with print_process(start_time, 'parsing'):
        parser = Parser(stream)
        tree = start_token(parser)

    with print_process(start_time, 'calculate score'):
        listener = Listener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    return listener


def main():
    file_name = 'cpp/tests/main.cpp'
    language = get_language_by_file(file_name)

    start_time = datetime.now()

    listener = calculate_abc_score(start_time, file_name, language)

    print_with_time_label(start_time, 'a: ' + str(listener.a))
    print_with_time_label(start_time, 'b: ' + str(listener.b))
    print_with_time_label(start_time, 'c: ' + str(listener.c))
    print_with_time_label(start_time, 'ABC score: ' + str(listener.abc_score))


if __name__ == '__main__':
    main()
