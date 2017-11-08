# Generated from /home/meanmail/MyProjects/antlr/grammars/CPP14.g4 by ANTLR 4.7
import math

from antlr4 import *

from parsers.CPP14Listener import CPP14Listener

if __name__ is not None and "." in __name__:
    from cpp.parsers.CPP14Parser import CPP14Parser
else:
    from cpp.parsers.CPP14Parser import CPP14Parser

# ABC rules for C++

ASSIGNMENTS = (
    # Occurrence of an assignment operator (exclude constant declarations and default parameter assignments)
    #       (=, *=, /=, %=, +=, <<=, >>=, &=, !=, ^=).
    CPP14Parser.RULE_assignmentoperator,
    # (prefix or postfix) (++, --)
    CPP14Parser.RULE_unaryincdecexpression,
    # Initialization of a variable or a nonconstant class member.
    CPP14Parser.RULE_initializer)

BRANCHES = (
    # Occurrence of a function call or a class method call.

    # Occurrence of any goto statement which has a target at a deeper level of nesting than the level to the goto.
    CPP14Parser.RULE_gotostatement,
    # Occurrence of ‘new’ or ‘delete’ operators.
    CPP14Parser.RULE_newexpression,
    CPP14Parser.RULE_deleteexpression)

CONDITIONALS = (
    # Occurrence of a conditional operator (<, >, <=, >=, ==, !=).
    CPP14Parser.RULE_equalityexpression,
    CPP14Parser.RULE_relationalexpression,
    # Occurrence of the following keywords (‘else’, ‘case’, ‘default’, ‘?’, ‘try’, ‘catch’).
    CPP14Parser.RULE_elsestatement,
    CPP14Parser.RULE_casestatement,
    CPP14Parser.RULE_defaultstatement,
    CPP14Parser.RULE_ternaryconditionalexpression,
    CPP14Parser.RULE_tryblock,
    CPP14Parser.RULE_handler,
    # Occurrence of a unary conditional operator.
    CPP14Parser.RULE_unaryconditionalexpression
)


# This class defines a complete listener for a parse tree produced by CPP14Parser.
class Listener(CPP14Listener):
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

    # Enter a parse tree produced by CPP14Parser#newexpression.
    def enterNewexpression(self, ctx: CPP14Parser.NewexpressionContext):
        self.enter(ctx)

    # Enter a parse tree produced by CPP14Parser#deleteexpression.
    def enterDeleteexpression(self, ctx: CPP14Parser.DeleteexpressionContext):
        self.enter(ctx)

    # Enter a parse tree produced by CPP14Parser#equalityexpression.
    def enterEqualityexpression(self, ctx: CPP14Parser.EqualityexpressionContext):
        self.enter(ctx)

    # Enter a parse tree produced by CPP14Parser#ternaryconditionalexpression.
    def enterTernaryconditionalexpression(self, ctx: CPP14Parser.TernaryconditionalexpressionContext):
        self.enter(ctx)

    # Enter a parse tree produced by CPP14Parser#unaryconditionalexpression.
    def enterUnaryconditionalexpression(self, ctx: CPP14Parser.UnaryconditionalexpressionContext):
        self.enter(ctx)

    # Enter a parse tree produced by CPP14Parser#assignmentoperator.
    def enterAssignmentoperator(self, ctx: CPP14Parser.AssignmentoperatorContext):
        self.enter(ctx)

    # Enter a parse tree produced by CPP14Parser#casestatement.
    def enterCasestatement(self, ctx: CPP14Parser.CasestatementContext):
        self.enter(ctx)

    # Enter a parse tree produced by CPP14Parser#defaultstatement.
    def enterDefaultstatement(self, ctx: CPP14Parser.DefaultstatementContext):
        self.enter(ctx)

    # Enter a parse tree produced by CPP14Parser#elsestatement.
    def enterElsestatement(self, ctx: CPP14Parser.ElsestatementContext):
        self.enter(ctx)

    # Enter a parse tree produced by CPP14Parser#gotostatement.
    def enterGotostatement(self, ctx: CPP14Parser.GotostatementContext):
        self.enter(ctx)

    # Enter a parse tree produced by CPP14Parser#initializer.
    def enterInitializer(self, ctx: CPP14Parser.InitializerContext):
        self.enter(ctx)

    # Enter a parse tree produced by CPP14Parser#tryblock.
    def enterTryblock(self, ctx: CPP14Parser.TryblockContext):
        self.enter(ctx)

    # Enter a parse tree produced by CPP14Parser#handler.
    def enterHandler(self, ctx: CPP14Parser.HandlerContext):
        self.enter(ctx)

    # Enter a parse tree produced by CPP14Parser#relationalexpression.
    def enterRelationalexpression(self, ctx: CPP14Parser.RelationalexpressionContext):
        self.enter(ctx)
