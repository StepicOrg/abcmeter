# Generated from /home/meanmail/MyProjects/antlr/grammars/CPP14.g4 by ANTLR 4.7
import math

from antlr4 import ParserRuleContext

from java8.parsers.Java8Listener import Java8Listener

if __name__ is not None and "." in __name__:
    from java8.parsers.Java8Parser import Java8Parser
else:
    from java8.parsers.Java8Parser import Java8Parser

# ABC rules for C++

ASSIGNMENTS = (
    # Occurrence of an assignment operator (exclude constant declarations and default parameter assignments)
    #       (=, *=, /=, %=, +=, <<=, >>=, &=, !=, ^=).
    Java8Parser.RULE_assignmentOperator,
    # (prefix or postfix) (++, --)

    # Initialization of a variable or a nonconstant class member.
    Java8Parser.RULE_arrayInitializer,
    Java8Parser.RULE_variableInitializer)

BRANCHES = (
    # Occurrence of a function call or a class method call.

    # Occurrence of any goto statement which has a target at a deeper level of nesting than the level to the goto.

    # Occurrence of ‘new’ or ‘delete’ operators.

)

CONDITIONALS = (
    # Occurrence of a conditional operator (<, >, <=, >=, ==, !=).
    Java8Parser.RULE_equalityExpression,
    Java8Parser.RULE_relationalExpression,
    # Occurrence of the following keywords (‘else’, ‘case’, ‘default’, ‘?’, ‘try’, ‘catch’).
    Java8Parser.RULE_ifThenElseStatement,

    Java8Parser.RULE_tryStatement,
    Java8Parser.RULE_tryWithResourcesStatement,
    Java8Parser.RULE_catches,
    # Occurrence of a unary conditional operator.

)


# This class defines a complete listener for a parse tree produced by Java8Parser.
class Listener(Java8Listener):
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    @property
    def abc_score(self):
        return round(math.sqrt(self.a ** 2 + self.b ** 2 + self.c ** 2), 2)

    def enter(self, ctx: ParserRuleContext):
        rule = ctx.getRuleIndex()
        if rule in ASSIGNMENTS:
            self.a += 1
        elif rule in BRANCHES:
            self.b += 1
        elif rule in CONDITIONALS:
            self.c += 1

    # Enter a parse tree produced by Java8Parser#equalityExpression.
    def enterEqualityExpression(self, ctx: Java8Parser.EqualityExpressionContext):
        self.enter(ctx)

    # Enter a parse tree produced by Java8Parser#assignmentOperator.
    def enterAssignmentOperator(self, ctx: Java8Parser.AssignmentOperatorContext):
        self.enter(ctx)

    # Enter a parse tree produced by Java8Parser#ifThenElseStatement.
    def enterIfThenElseStatement(self, ctx: Java8Parser.IfThenElseStatementContext):
        self.enter(ctx)

    # Enter a parse tree produced by Java8Parser#variableInitializer.
    def enterVariableInitializer(self, ctx: Java8Parser.VariableInitializerContext):
        self.enter(ctx)

    # Enter a parse tree produced by Java8Parser#arrayInitializer.
    def enterArrayInitializer(self, ctx: Java8Parser.ArrayInitializerContext):
        self.enter(ctx)

    # Enter a parse tree produced by Java8Parser#tryStatement.
    def enterTryStatement(self, ctx: Java8Parser.TryStatementContext):
        self.enter(ctx)

    # Enter a parse tree produced by Java8Parser#tryWithResourcesStatement.
    def enterTryWithResourcesStatement(self, ctx: Java8Parser.TryWithResourcesStatementContext):
        self.enter(ctx)

    # Enter a parse tree produced by Java8Parser#catches.
    def enterCatches(self, ctx: Java8Parser.CatchesContext):
        self.enter(ctx)

    # Enter a parse tree produced by Java8Parser#relationalExpression.
    def enterRelationalExpression(self, ctx: Java8Parser.RelationalExpressionContext):
        self.enter(ctx)
