from contextlib import contextmanager

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker


CPP = 'c++'
JAVA = 'java8'
PYTHON = 'python3'


def get_lexer_parser_listener(language):
    if language == CPP:
        from cpp.listener import Listener
        from cpp.parsers.CPP14Lexer import CPP14Lexer
        from cpp.parsers.CPP14Parser import CPP14Parser
        return CPP14Lexer, CPP14Parser, Listener, CPP14Parser.translationunit

    if language == JAVA:
        from java8.listener import Listener
        from java8.parsers.Java8Lexer import Java8Lexer
        from java8.parsers.Java8Parser import Java8Parser
        return Java8Lexer, Java8Parser, Listener, Java8Parser.compilationUnit


@contextmanager
def nope_printer(*args, **kwargs):
    yield


def calculate_abc_score(start_time, file_name, language, printer=nope_printer):
    Lexer, Parser, Listener, start_token = get_lexer_parser_listener(language)

    with printer(start_time, f'input from {file_name}'):
        input = FileStream(file_name, encoding='utf8')

    with printer(start_time, 'analysis'):
        lexer = Lexer(input)
        stream = CommonTokenStream(lexer)

    with printer(start_time, 'parsing'):
        parser = Parser(stream)
        tree = start_token(parser)

    with printer(start_time, 'calculate score'):
        listener = Listener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    return listener
