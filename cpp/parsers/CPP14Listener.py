# Generated from /home/meanmail/MyProjects/antlr/cpp/grammars/CPP14.g4 by ANTLR 4.7
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .CPP14Parser import CPP14Parser
else:
    from CPP14Parser import CPP14Parser


# This class defines a complete listener for a parse tree produced by CPP14Parser.
class CPP14Listener(ParseTreeListener):
    # Enter a parse tree produced by CPP14Parser#translationunit.
    def enterTranslationunit(self, ctx: CPP14Parser.TranslationunitContext):
        pass

    # Exit a parse tree produced by CPP14Parser#translationunit.
    def exitTranslationunit(self, ctx: CPP14Parser.TranslationunitContext):
        pass

    # Enter a parse tree produced by CPP14Parser#unqualifiedid.
    def enterUnqualifiedid(self, ctx: CPP14Parser.UnqualifiedidContext):
        pass

    # Exit a parse tree produced by CPP14Parser#unqualifiedid.
    def exitUnqualifiedid(self, ctx: CPP14Parser.UnqualifiedidContext):
        pass

    # Enter a parse tree produced by CPP14Parser#nestednamespecifier.
    def enterNestednamespecifier(self, ctx: CPP14Parser.NestednamespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#nestednamespecifier.
    def exitNestednamespecifier(self, ctx: CPP14Parser.NestednamespecifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#lambdadeclarator.
    def enterLambdadeclarator(self, ctx: CPP14Parser.LambdadeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#lambdadeclarator.
    def exitLambdadeclarator(self, ctx: CPP14Parser.LambdadeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#postfix.
    def enterPostfix(self, ctx: CPP14Parser.PostfixContext):
        pass

    # Exit a parse tree produced by CPP14Parser#postfix.
    def exitPostfix(self, ctx: CPP14Parser.PostfixContext):
        pass

    # Enter a parse tree produced by CPP14Parser#postfixexpression.
    def enterPostfixexpression(self, ctx: CPP14Parser.PostfixexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#postfixexpression.
    def exitPostfixexpression(self, ctx: CPP14Parser.PostfixexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#pseudodestructorname.
    def enterPseudodestructorname(self, ctx: CPP14Parser.PseudodestructornameContext):
        pass

    # Exit a parse tree produced by CPP14Parser#pseudodestructorname.
    def exitPseudodestructorname(self, ctx: CPP14Parser.PseudodestructornameContext):
        pass

    # Enter a parse tree produced by CPP14Parser#unaryexpression.
    def enterUnaryexpression(self, ctx: CPP14Parser.UnaryexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#unaryexpression.
    def exitUnaryexpression(self, ctx: CPP14Parser.UnaryexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#unaryincdecexpression.
    def enterUnaryincdecexpression(self, ctx: CPP14Parser.UnaryincdecexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#unaryincdecexpression.
    def exitUnaryincdecexpression(self, ctx: CPP14Parser.UnaryincdecexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#postfixunaryincdecexpression.
    def enterPostfixunaryincdecexpression(self, ctx: CPP14Parser.PostfixunaryincdecexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#postfixunaryincdecexpression.
    def exitPostfixunaryincdecexpression(self, ctx: CPP14Parser.PostfixunaryincdecexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#newexpression.
    def enterNewexpression(self, ctx: CPP14Parser.NewexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#newexpression.
    def exitNewexpression(self, ctx: CPP14Parser.NewexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#newdeclarator.
    def enterNewdeclarator(self, ctx: CPP14Parser.NewdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#newdeclarator.
    def exitNewdeclarator(self, ctx: CPP14Parser.NewdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#deleteexpression.
    def enterDeleteexpression(self, ctx: CPP14Parser.DeleteexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#deleteexpression.
    def exitDeleteexpression(self, ctx: CPP14Parser.DeleteexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#castexpression.
    def enterCastexpression(self, ctx: CPP14Parser.CastexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#castexpression.
    def exitCastexpression(self, ctx: CPP14Parser.CastexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#shiftexpression.
    def enterShiftexpression(self, ctx: CPP14Parser.ShiftexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#shiftexpression.
    def exitShiftexpression(self, ctx: CPP14Parser.ShiftexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#relationalexpression.
    def enterRelationalexpression(self, ctx: CPP14Parser.RelationalexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#relationalexpression.
    def exitRelationalexpression(self, ctx: CPP14Parser.RelationalexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#equalityexpression.
    def enterEqualityexpression(self, ctx: CPP14Parser.EqualityexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#equalityexpression.
    def exitEqualityexpression(self, ctx: CPP14Parser.EqualityexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#ternaryconditionalexpression.
    def enterTernaryconditionalexpression(self, ctx: CPP14Parser.TernaryconditionalexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#ternaryconditionalexpression.
    def exitTernaryconditionalexpression(self, ctx: CPP14Parser.TernaryconditionalexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#unaryconditionalexpression.
    def enterUnaryconditionalexpression(self, ctx: CPP14Parser.UnaryconditionalexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#unaryconditionalexpression.
    def exitUnaryconditionalexpression(self, ctx: CPP14Parser.UnaryconditionalexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#assignmentexpression.
    def enterAssignmentexpression(self, ctx: CPP14Parser.AssignmentexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#assignmentexpression.
    def exitAssignmentexpression(self, ctx: CPP14Parser.AssignmentexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#assignmentoperator.
    def enterAssignmentoperator(self, ctx: CPP14Parser.AssignmentoperatorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#assignmentoperator.
    def exitAssignmentoperator(self, ctx: CPP14Parser.AssignmentoperatorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#constantexpression.
    def enterConstantexpression(self, ctx: CPP14Parser.ConstantexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#constantexpression.
    def exitConstantexpression(self, ctx: CPP14Parser.ConstantexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#statement.
    def enterStatement(self, ctx: CPP14Parser.StatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#statement.
    def exitStatement(self, ctx: CPP14Parser.StatementContext):
        pass

    # Enter a parse tree produced by CPP14Parser#casestatement.
    def enterCasestatement(self, ctx: CPP14Parser.CasestatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#casestatement.
    def exitCasestatement(self, ctx: CPP14Parser.CasestatementContext):
        pass

    # Enter a parse tree produced by CPP14Parser#elsestatement.
    def enterElsestatement(self, ctx: CPP14Parser.ElsestatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#elsestatement.
    def exitElsestatement(self, ctx: CPP14Parser.ElsestatementContext):
        pass

    # Enter a parse tree produced by CPP14Parser#condition.
    def enterCondition(self, ctx: CPP14Parser.ConditionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#condition.
    def exitCondition(self, ctx: CPP14Parser.ConditionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#forinitstatement.
    def enterForinitstatement(self, ctx: CPP14Parser.ForinitstatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#forinitstatement.
    def exitForinitstatement(self, ctx: CPP14Parser.ForinitstatementContext):
        pass

    # Enter a parse tree produced by CPP14Parser#gotostatement.
    def enterGotostatement(self, ctx: CPP14Parser.GotostatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#gotostatement.
    def exitGotostatement(self, ctx: CPP14Parser.GotostatementContext):
        pass

    # Enter a parse tree produced by CPP14Parser#declaration.
    def enterDeclaration(self, ctx: CPP14Parser.DeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#declaration.
    def exitDeclaration(self, ctx: CPP14Parser.DeclarationContext):
        pass

    # Enter a parse tree produced by CPP14Parser#declspecifierseq.
    def enterDeclspecifierseq(self, ctx: CPP14Parser.DeclspecifierseqContext):
        pass

    # Exit a parse tree produced by CPP14Parser#declspecifierseq.
    def exitDeclspecifierseq(self, ctx: CPP14Parser.DeclspecifierseqContext):
        pass

    # Enter a parse tree produced by CPP14Parser#typespecifier.
    def enterTypespecifier(self, ctx: CPP14Parser.TypespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#typespecifier.
    def exitTypespecifier(self, ctx: CPP14Parser.TypespecifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#trailingtypespecifier.
    def enterTrailingtypespecifier(self, ctx: CPP14Parser.TrailingtypespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#trailingtypespecifier.
    def exitTrailingtypespecifier(self, ctx: CPP14Parser.TrailingtypespecifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#simpletypespecifier.
    def enterSimpletypespecifier(self, ctx: CPP14Parser.SimpletypespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#simpletypespecifier.
    def exitSimpletypespecifier(self, ctx: CPP14Parser.SimpletypespecifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#attributespecifier.
    def enterAttributespecifier(self, ctx: CPP14Parser.AttributespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#attributespecifier.
    def exitAttributespecifier(self, ctx: CPP14Parser.AttributespecifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#balancedtoken.
    def enterBalancedtoken(self, ctx: CPP14Parser.BalancedtokenContext):
        pass

    # Exit a parse tree produced by CPP14Parser#balancedtoken.
    def exitBalancedtoken(self, ctx: CPP14Parser.BalancedtokenContext):
        pass

    # Enter a parse tree produced by CPP14Parser#declarator.
    def enterDeclarator(self, ctx: CPP14Parser.DeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#declarator.
    def exitDeclarator(self, ctx: CPP14Parser.DeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#noptrdeclarator.
    def enterNoptrdeclarator(self, ctx: CPP14Parser.NoptrdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#noptrdeclarator.
    def exitNoptrdeclarator(self, ctx: CPP14Parser.NoptrdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#parametersandqualifiers.
    def enterParametersandqualifiers(self, ctx: CPP14Parser.ParametersandqualifiersContext):
        pass

    # Exit a parse tree produced by CPP14Parser#parametersandqualifiers.
    def exitParametersandqualifiers(self, ctx: CPP14Parser.ParametersandqualifiersContext):
        pass

    # Enter a parse tree produced by CPP14Parser#ptroperator.
    def enterPtroperator(self, ctx: CPP14Parser.PtroperatorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#ptroperator.
    def exitPtroperator(self, ctx: CPP14Parser.PtroperatorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#abstractdeclarator.
    def enterAbstractdeclarator(self, ctx: CPP14Parser.AbstractdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#abstractdeclarator.
    def exitAbstractdeclarator(self, ctx: CPP14Parser.AbstractdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#noptrabstractdeclarator.
    def enterNoptrabstractdeclarator(self, ctx: CPP14Parser.NoptrabstractdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#noptrabstractdeclarator.
    def exitNoptrabstractdeclarator(self, ctx: CPP14Parser.NoptrabstractdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#parameterdeclaration.
    def enterParameterdeclaration(self, ctx: CPP14Parser.ParameterdeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#parameterdeclaration.
    def exitParameterdeclaration(self, ctx: CPP14Parser.ParameterdeclarationContext):
        pass

    # Enter a parse tree produced by CPP14Parser#initializer.
    def enterInitializer(self, ctx: CPP14Parser.InitializerContext):
        pass

    # Exit a parse tree produced by CPP14Parser#initializer.
    def exitInitializer(self, ctx: CPP14Parser.InitializerContext):
        pass

    # Enter a parse tree produced by CPP14Parser#initializerlist.
    def enterInitializerlist(self, ctx: CPP14Parser.InitializerlistContext):
        pass

    # Exit a parse tree produced by CPP14Parser#initializerlist.
    def exitInitializerlist(self, ctx: CPP14Parser.InitializerlistContext):
        pass

    # Enter a parse tree produced by CPP14Parser#memberdeclaration.
    def enterMemberdeclaration(self, ctx: CPP14Parser.MemberdeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#memberdeclaration.
    def exitMemberdeclaration(self, ctx: CPP14Parser.MemberdeclarationContext):
        pass

    # Enter a parse tree produced by CPP14Parser#memberdeclarator.
    def enterMemberdeclarator(self, ctx: CPP14Parser.MemberdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#memberdeclarator.
    def exitMemberdeclarator(self, ctx: CPP14Parser.MemberdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#purespecifier.
    def enterPurespecifier(self, ctx: CPP14Parser.PurespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#purespecifier.
    def exitPurespecifier(self, ctx: CPP14Parser.PurespecifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#basespecifier.
    def enterBasespecifier(self, ctx: CPP14Parser.BasespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#basespecifier.
    def exitBasespecifier(self, ctx: CPP14Parser.BasespecifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#meminitializerlist.
    def enterMeminitializerlist(self, ctx: CPP14Parser.MeminitializerlistContext):
        pass

    # Exit a parse tree produced by CPP14Parser#meminitializerlist.
    def exitMeminitializerlist(self, ctx: CPP14Parser.MeminitializerlistContext):
        pass

    # Enter a parse tree produced by CPP14Parser#templateparameterlist.
    def enterTemplateparameterlist(self, ctx: CPP14Parser.TemplateparameterlistContext):
        pass

    # Exit a parse tree produced by CPP14Parser#templateparameterlist.
    def exitTemplateparameterlist(self, ctx: CPP14Parser.TemplateparameterlistContext):
        pass

    # Enter a parse tree produced by CPP14Parser#templateargumentlist.
    def enterTemplateargumentlist(self, ctx: CPP14Parser.TemplateargumentlistContext):
        pass

    # Exit a parse tree produced by CPP14Parser#templateargumentlist.
    def exitTemplateargumentlist(self, ctx: CPP14Parser.TemplateargumentlistContext):
        pass

    # Enter a parse tree produced by CPP14Parser#tryblock.
    def enterTryblock(self, ctx: CPP14Parser.TryblockContext):
        pass

    # Exit a parse tree produced by CPP14Parser#tryblock.
    def exitTryblock(self, ctx: CPP14Parser.TryblockContext):
        pass

    # Enter a parse tree produced by CPP14Parser#handler.
    def enterHandler(self, ctx: CPP14Parser.HandlerContext):
        pass

    # Exit a parse tree produced by CPP14Parser#handler.
    def exitHandler(self, ctx: CPP14Parser.HandlerContext):
        pass

    # Enter a parse tree produced by CPP14Parser#theoperator.
    def enterTheoperator(self, ctx: CPP14Parser.TheoperatorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#theoperator.
    def exitTheoperator(self, ctx: CPP14Parser.TheoperatorContext):
        pass
