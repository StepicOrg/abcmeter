from antlr4 import CommonTokenStream, ParseTreeWalker, PredictionMode

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


def calculate_abc_score(input, language):
    Lexer, Parser, Listener, start_token = get_lexer_parser_listener(language)

    lexer = Lexer(input)
    tokens = CommonTokenStream(lexer)

    parser = Parser(tokens)
    parser._interp.predictionMode = PredictionMode.SLL

    try:
        tree = start_token(parser)
    except:
        tokens.reset()  # rewind
        parser.reset()
        parser._interp.predictionMode = PredictionMode.LL
        tree = start_token(parser)

    listener = Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return listener
