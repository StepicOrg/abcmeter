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

    # Enter a parse tree produced by CPP14Parser#lambdacapture.
    def enterLambdacapture(self, ctx: CPP14Parser.LambdacaptureContext):
        pass

    # Exit a parse tree produced by CPP14Parser#lambdacapture.
    def exitLambdacapture(self, ctx: CPP14Parser.LambdacaptureContext):
        pass

    # Enter a parse tree produced by CPP14Parser#idexpression.
    def enterIdexpression(self, ctx: CPP14Parser.IdexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#idexpression.
    def exitIdexpression(self, ctx: CPP14Parser.IdexpressionContext):
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

    # Enter a parse tree produced by CPP14Parser#capturelist.
    def enterCapturelist(self, ctx: CPP14Parser.CapturelistContext):
        pass

    # Exit a parse tree produced by CPP14Parser#capturelist.
    def exitCapturelist(self, ctx: CPP14Parser.CapturelistContext):
        pass

    # Enter a parse tree produced by CPP14Parser#capture.
    def enterCapture(self, ctx: CPP14Parser.CaptureContext):
        pass

    # Exit a parse tree produced by CPP14Parser#capture.
    def exitCapture(self, ctx: CPP14Parser.CaptureContext):
        pass

    # Enter a parse tree produced by CPP14Parser#lambdadeclarator.
    def enterLambdadeclarator(self, ctx: CPP14Parser.LambdadeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#lambdadeclarator.
    def exitLambdadeclarator(self, ctx: CPP14Parser.LambdadeclaratorContext):
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

    # Enter a parse tree produced by CPP14Parser#unaryoperator.
    def enterUnaryoperator(self, ctx: CPP14Parser.UnaryoperatorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#unaryoperator.
    def exitUnaryoperator(self, ctx: CPP14Parser.UnaryoperatorContext):
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

    # Enter a parse tree produced by CPP14Parser#noptrnewdeclarator.
    def enterNoptrnewdeclarator(self, ctx: CPP14Parser.NoptrnewdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#noptrnewdeclarator.
    def exitNoptrnewdeclarator(self, ctx: CPP14Parser.NoptrnewdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#newinitializer.
    def enterNewinitializer(self, ctx: CPP14Parser.NewinitializerContext):
        pass

    # Exit a parse tree produced by CPP14Parser#newinitializer.
    def exitNewinitializer(self, ctx: CPP14Parser.NewinitializerContext):
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

    # Enter a parse tree produced by CPP14Parser#pmexpression.
    def enterPmexpression(self, ctx: CPP14Parser.PmexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#pmexpression.
    def exitPmexpression(self, ctx: CPP14Parser.PmexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#multiplicativeexpression.
    def enterMultiplicativeexpression(self, ctx: CPP14Parser.MultiplicativeexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#multiplicativeexpression.
    def exitMultiplicativeexpression(self, ctx: CPP14Parser.MultiplicativeexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#additiveexpression.
    def enterAdditiveexpression(self, ctx: CPP14Parser.AdditiveexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#additiveexpression.
    def exitAdditiveexpression(self, ctx: CPP14Parser.AdditiveexpressionContext):
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

    # Enter a parse tree produced by CPP14Parser#andexpression.
    def enterAndexpression(self, ctx: CPP14Parser.AndexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#andexpression.
    def exitAndexpression(self, ctx: CPP14Parser.AndexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#exclusiveorexpression.
    def enterExclusiveorexpression(self, ctx: CPP14Parser.ExclusiveorexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#exclusiveorexpression.
    def exitExclusiveorexpression(self, ctx: CPP14Parser.ExclusiveorexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#inclusiveorexpression.
    def enterInclusiveorexpression(self, ctx: CPP14Parser.InclusiveorexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#inclusiveorexpression.
    def exitInclusiveorexpression(self, ctx: CPP14Parser.InclusiveorexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#logicalandexpression.
    def enterLogicalandexpression(self, ctx: CPP14Parser.LogicalandexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#logicalandexpression.
    def exitLogicalandexpression(self, ctx: CPP14Parser.LogicalandexpressionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#logicalorexpression.
    def enterLogicalorexpression(self, ctx: CPP14Parser.LogicalorexpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#logicalorexpression.
    def exitLogicalorexpression(self, ctx: CPP14Parser.LogicalorexpressionContext):
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

    # Enter a parse tree produced by CPP14Parser#expression.
    def enterExpression(self, ctx: CPP14Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#expression.
    def exitExpression(self, ctx: CPP14Parser.ExpressionContext):
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

    # Enter a parse tree produced by CPP14Parser#defaultstatement.
    def enterDefaultstatement(self, ctx: CPP14Parser.DefaultstatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#defaultstatement.
    def exitDefaultstatement(self, ctx: CPP14Parser.DefaultstatementContext):
        pass

    # Enter a parse tree produced by CPP14Parser#selectionstatement.
    def enterSelectionstatement(self, ctx: CPP14Parser.SelectionstatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#selectionstatement.
    def exitSelectionstatement(self, ctx: CPP14Parser.SelectionstatementContext):
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

    # Enter a parse tree produced by CPP14Parser#iterationstatement.
    def enterIterationstatement(self, ctx: CPP14Parser.IterationstatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#iterationstatement.
    def exitIterationstatement(self, ctx: CPP14Parser.IterationstatementContext):
        pass

    # Enter a parse tree produced by CPP14Parser#forinitstatement.
    def enterForinitstatement(self, ctx: CPP14Parser.ForinitstatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#forinitstatement.
    def exitForinitstatement(self, ctx: CPP14Parser.ForinitstatementContext):
        pass

    # Enter a parse tree produced by CPP14Parser#jumpstatement.
    def enterJumpstatement(self, ctx: CPP14Parser.JumpstatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#jumpstatement.
    def exitJumpstatement(self, ctx: CPP14Parser.JumpstatementContext):
        pass

    # Enter a parse tree produced by CPP14Parser#gotostatement.
    def enterGotostatement(self, ctx: CPP14Parser.GotostatementContext):
        pass

    # Exit a parse tree produced by CPP14Parser#gotostatement.
    def exitGotostatement(self, ctx: CPP14Parser.GotostatementContext):
        pass

    # Enter a parse tree produced by CPP14Parser#declarationseq.
    def enterDeclarationseq(self, ctx: CPP14Parser.DeclarationseqContext):
        pass

    # Exit a parse tree produced by CPP14Parser#declarationseq.
    def exitDeclarationseq(self, ctx: CPP14Parser.DeclarationseqContext):
        pass

    # Enter a parse tree produced by CPP14Parser#declaration.
    def enterDeclaration(self, ctx: CPP14Parser.DeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#declaration.
    def exitDeclaration(self, ctx: CPP14Parser.DeclarationContext):
        pass

    # Enter a parse tree produced by CPP14Parser#declspecifier.
    def enterDeclspecifier(self, ctx: CPP14Parser.DeclspecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#declspecifier.
    def exitDeclspecifier(self, ctx: CPP14Parser.DeclspecifierContext):
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

    # Enter a parse tree produced by CPP14Parser#typespecifierseq.
    def enterTypespecifierseq(self, ctx: CPP14Parser.TypespecifierseqContext):
        pass

    # Exit a parse tree produced by CPP14Parser#typespecifierseq.
    def exitTypespecifierseq(self, ctx: CPP14Parser.TypespecifierseqContext):
        pass

    # Enter a parse tree produced by CPP14Parser#trailingtypespecifierseq.
    def enterTrailingtypespecifierseq(self, ctx: CPP14Parser.TrailingtypespecifierseqContext):
        pass

    # Exit a parse tree produced by CPP14Parser#trailingtypespecifierseq.
    def exitTrailingtypespecifierseq(self, ctx: CPP14Parser.TrailingtypespecifierseqContext):
        pass

    # Enter a parse tree produced by CPP14Parser#simpletypespecifier.
    def enterSimpletypespecifier(self, ctx: CPP14Parser.SimpletypespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#simpletypespecifier.
    def exitSimpletypespecifier(self, ctx: CPP14Parser.SimpletypespecifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#thetypename.
    def enterThetypename(self, ctx: CPP14Parser.ThetypenameContext):
        pass

    # Exit a parse tree produced by CPP14Parser#thetypename.
    def exitThetypename(self, ctx: CPP14Parser.ThetypenameContext):
        pass

    # Enter a parse tree produced by CPP14Parser#decltypespecifier.
    def enterDecltypespecifier(self, ctx: CPP14Parser.DecltypespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#decltypespecifier.
    def exitDecltypespecifier(self, ctx: CPP14Parser.DecltypespecifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#enumkey.
    def enterEnumkey(self, ctx: CPP14Parser.EnumkeyContext):
        pass

    # Exit a parse tree produced by CPP14Parser#enumkey.
    def exitEnumkey(self, ctx: CPP14Parser.EnumkeyContext):
        pass

    # Enter a parse tree produced by CPP14Parser#enumeratorlist.
    def enterEnumeratorlist(self, ctx: CPP14Parser.EnumeratorlistContext):
        pass

    # Exit a parse tree produced by CPP14Parser#enumeratorlist.
    def exitEnumeratorlist(self, ctx: CPP14Parser.EnumeratorlistContext):
        pass

    # Enter a parse tree produced by CPP14Parser#attributespecifierseq.
    def enterAttributespecifierseq(self, ctx: CPP14Parser.AttributespecifierseqContext):
        pass

    # Exit a parse tree produced by CPP14Parser#attributespecifierseq.
    def exitAttributespecifierseq(self, ctx: CPP14Parser.AttributespecifierseqContext):
        pass

    # Enter a parse tree produced by CPP14Parser#attributespecifier.
    def enterAttributespecifier(self, ctx: CPP14Parser.AttributespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#attributespecifier.
    def exitAttributespecifier(self, ctx: CPP14Parser.AttributespecifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#attributelist.
    def enterAttributelist(self, ctx: CPP14Parser.AttributelistContext):
        pass

    # Exit a parse tree produced by CPP14Parser#attributelist.
    def exitAttributelist(self, ctx: CPP14Parser.AttributelistContext):
        pass

    # Enter a parse tree produced by CPP14Parser#attribute.
    def enterAttribute(self, ctx: CPP14Parser.AttributeContext):
        pass

    # Exit a parse tree produced by CPP14Parser#attribute.
    def exitAttribute(self, ctx: CPP14Parser.AttributeContext):
        pass

    # Enter a parse tree produced by CPP14Parser#balancedtokenseq.
    def enterBalancedtokenseq(self, ctx: CPP14Parser.BalancedtokenseqContext):
        pass

    # Exit a parse tree produced by CPP14Parser#balancedtokenseq.
    def exitBalancedtokenseq(self, ctx: CPP14Parser.BalancedtokenseqContext):
        pass

    # Enter a parse tree produced by CPP14Parser#balancedtoken.
    def enterBalancedtoken(self, ctx: CPP14Parser.BalancedtokenContext):
        pass

    # Exit a parse tree produced by CPP14Parser#balancedtoken.
    def exitBalancedtoken(self, ctx: CPP14Parser.BalancedtokenContext):
        pass

    # Enter a parse tree produced by CPP14Parser#initdeclaratorlist.
    def enterInitdeclaratorlist(self, ctx: CPP14Parser.InitdeclaratorlistContext):
        pass

    # Exit a parse tree produced by CPP14Parser#initdeclaratorlist.
    def exitInitdeclaratorlist(self, ctx: CPP14Parser.InitdeclaratorlistContext):
        pass

    # Enter a parse tree produced by CPP14Parser#declarator.
    def enterDeclarator(self, ctx: CPP14Parser.DeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#declarator.
    def exitDeclarator(self, ctx: CPP14Parser.DeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#ptrdeclarator.
    def enterPtrdeclarator(self, ctx: CPP14Parser.PtrdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#ptrdeclarator.
    def exitPtrdeclarator(self, ctx: CPP14Parser.PtrdeclaratorContext):
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

    # Enter a parse tree produced by CPP14Parser#cvqualifier.
    def enterCvqualifier(self, ctx: CPP14Parser.CvqualifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#cvqualifier.
    def exitCvqualifier(self, ctx: CPP14Parser.CvqualifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#abstractdeclarator.
    def enterAbstractdeclarator(self, ctx: CPP14Parser.AbstractdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#abstractdeclarator.
    def exitAbstractdeclarator(self, ctx: CPP14Parser.AbstractdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#ptrabstractdeclarator.
    def enterPtrabstractdeclarator(self, ctx: CPP14Parser.PtrabstractdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#ptrabstractdeclarator.
    def exitPtrabstractdeclarator(self, ctx: CPP14Parser.PtrabstractdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#noptrabstractdeclarator.
    def enterNoptrabstractdeclarator(self, ctx: CPP14Parser.NoptrabstractdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#noptrabstractdeclarator.
    def exitNoptrabstractdeclarator(self, ctx: CPP14Parser.NoptrabstractdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#abstractpackdeclarator.
    def enterAbstractpackdeclarator(self, ctx: CPP14Parser.AbstractpackdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#abstractpackdeclarator.
    def exitAbstractpackdeclarator(self, ctx: CPP14Parser.AbstractpackdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#noptrabstractpackdeclarator.
    def enterNoptrabstractpackdeclarator(self, ctx: CPP14Parser.NoptrabstractpackdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#noptrabstractpackdeclarator.
    def exitNoptrabstractpackdeclarator(self, ctx: CPP14Parser.NoptrabstractpackdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#parameterdeclarationclause.
    def enterParameterdeclarationclause(self, ctx: CPP14Parser.ParameterdeclarationclauseContext):
        pass

    # Exit a parse tree produced by CPP14Parser#parameterdeclarationclause.
    def exitParameterdeclarationclause(self, ctx: CPP14Parser.ParameterdeclarationclauseContext):
        pass

    # Enter a parse tree produced by CPP14Parser#parameterdeclarationlist.
    def enterParameterdeclarationlist(self, ctx: CPP14Parser.ParameterdeclarationlistContext):
        pass

    # Exit a parse tree produced by CPP14Parser#parameterdeclarationlist.
    def exitParameterdeclarationlist(self, ctx: CPP14Parser.ParameterdeclarationlistContext):
        pass

    # Enter a parse tree produced by CPP14Parser#parameterdeclaration.
    def enterParameterdeclaration(self, ctx: CPP14Parser.ParameterdeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#parameterdeclaration.
    def exitParameterdeclaration(self, ctx: CPP14Parser.ParameterdeclarationContext):
        pass

    # Enter a parse tree produced by CPP14Parser#functiondefinition.
    def enterFunctiondefinition(self, ctx: CPP14Parser.FunctiondefinitionContext):
        pass

    # Exit a parse tree produced by CPP14Parser#functiondefinition.
    def exitFunctiondefinition(self, ctx: CPP14Parser.FunctiondefinitionContext):
        pass

    # Enter a parse tree produced by CPP14Parser#functionbody.
    def enterFunctionbody(self, ctx: CPP14Parser.FunctionbodyContext):
        pass

    # Exit a parse tree produced by CPP14Parser#functionbody.
    def exitFunctionbody(self, ctx: CPP14Parser.FunctionbodyContext):
        pass

    # Enter a parse tree produced by CPP14Parser#initializer.
    def enterInitializer(self, ctx: CPP14Parser.InitializerContext):
        pass

    # Exit a parse tree produced by CPP14Parser#initializer.
    def exitInitializer(self, ctx: CPP14Parser.InitializerContext):
        pass

    # Enter a parse tree produced by CPP14Parser#braceorequalinitializer.
    def enterBraceorequalinitializer(self, ctx: CPP14Parser.BraceorequalinitializerContext):
        pass

    # Exit a parse tree produced by CPP14Parser#braceorequalinitializer.
    def exitBraceorequalinitializer(self, ctx: CPP14Parser.BraceorequalinitializerContext):
        pass

    # Enter a parse tree produced by CPP14Parser#initializerclause.
    def enterInitializerclause(self, ctx: CPP14Parser.InitializerclauseContext):
        pass

    # Exit a parse tree produced by CPP14Parser#initializerclause.
    def exitInitializerclause(self, ctx: CPP14Parser.InitializerclauseContext):
        pass

    # Enter a parse tree produced by CPP14Parser#initializerlist.
    def enterInitializerlist(self, ctx: CPP14Parser.InitializerlistContext):
        pass

    # Exit a parse tree produced by CPP14Parser#initializerlist.
    def exitInitializerlist(self, ctx: CPP14Parser.InitializerlistContext):
        pass

    # Enter a parse tree produced by CPP14Parser#bracedinitlist.
    def enterBracedinitlist(self, ctx: CPP14Parser.BracedinitlistContext):
        pass

    # Exit a parse tree produced by CPP14Parser#bracedinitlist.
    def exitBracedinitlist(self, ctx: CPP14Parser.BracedinitlistContext):
        pass

    # Enter a parse tree produced by CPP14Parser#classname.
    def enterClassname(self, ctx: CPP14Parser.ClassnameContext):
        pass

    # Exit a parse tree produced by CPP14Parser#classname.
    def exitClassname(self, ctx: CPP14Parser.ClassnameContext):
        pass

    # Enter a parse tree produced by CPP14Parser#classkey.
    def enterClasskey(self, ctx: CPP14Parser.ClasskeyContext):
        pass

    # Exit a parse tree produced by CPP14Parser#classkey.
    def exitClasskey(self, ctx: CPP14Parser.ClasskeyContext):
        pass

    # Enter a parse tree produced by CPP14Parser#memberdeclaration.
    def enterMemberdeclaration(self, ctx: CPP14Parser.MemberdeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#memberdeclaration.
    def exitMemberdeclaration(self, ctx: CPP14Parser.MemberdeclarationContext):
        pass

    # Enter a parse tree produced by CPP14Parser#memberdeclaratorlist.
    def enterMemberdeclaratorlist(self, ctx: CPP14Parser.MemberdeclaratorlistContext):
        pass

    # Exit a parse tree produced by CPP14Parser#memberdeclaratorlist.
    def exitMemberdeclaratorlist(self, ctx: CPP14Parser.MemberdeclaratorlistContext):
        pass

    # Enter a parse tree produced by CPP14Parser#memberdeclarator.
    def enterMemberdeclarator(self, ctx: CPP14Parser.MemberdeclaratorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#memberdeclarator.
    def exitMemberdeclarator(self, ctx: CPP14Parser.MemberdeclaratorContext):
        pass

    # Enter a parse tree produced by CPP14Parser#virtspecifierseq.
    def enterVirtspecifierseq(self, ctx: CPP14Parser.VirtspecifierseqContext):
        pass

    # Exit a parse tree produced by CPP14Parser#virtspecifierseq.
    def exitVirtspecifierseq(self, ctx: CPP14Parser.VirtspecifierseqContext):
        pass

    # Enter a parse tree produced by CPP14Parser#purespecifier.
    def enterPurespecifier(self, ctx: CPP14Parser.PurespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#purespecifier.
    def exitPurespecifier(self, ctx: CPP14Parser.PurespecifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#basespecifierlist.
    def enterBasespecifierlist(self, ctx: CPP14Parser.BasespecifierlistContext):
        pass

    # Exit a parse tree produced by CPP14Parser#basespecifierlist.
    def exitBasespecifierlist(self, ctx: CPP14Parser.BasespecifierlistContext):
        pass

    # Enter a parse tree produced by CPP14Parser#basespecifier.
    def enterBasespecifier(self, ctx: CPP14Parser.BasespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#basespecifier.
    def exitBasespecifier(self, ctx: CPP14Parser.BasespecifierContext):
        pass

    # Enter a parse tree produced by CPP14Parser#classordecltype.
    def enterClassordecltype(self, ctx: CPP14Parser.ClassordecltypeContext):
        pass

    # Exit a parse tree produced by CPP14Parser#classordecltype.
    def exitClassordecltype(self, ctx: CPP14Parser.ClassordecltypeContext):
        pass

    # Enter a parse tree produced by CPP14Parser#accessspecifier.
    def enterAccessspecifier(self, ctx: CPP14Parser.AccessspecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#accessspecifier.
    def exitAccessspecifier(self, ctx: CPP14Parser.AccessspecifierContext):
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

    # Enter a parse tree produced by CPP14Parser#templateparameter.
    def enterTemplateparameter(self, ctx: CPP14Parser.TemplateparameterContext):
        pass

    # Exit a parse tree produced by CPP14Parser#templateparameter.
    def exitTemplateparameter(self, ctx: CPP14Parser.TemplateparameterContext):
        pass

    # Enter a parse tree produced by CPP14Parser#templateargumentlist.
    def enterTemplateargumentlist(self, ctx: CPP14Parser.TemplateargumentlistContext):
        pass

    # Exit a parse tree produced by CPP14Parser#templateargumentlist.
    def exitTemplateargumentlist(self, ctx: CPP14Parser.TemplateargumentlistContext):
        pass

    # Enter a parse tree produced by CPP14Parser#templateargument.
    def enterTemplateargument(self, ctx: CPP14Parser.TemplateargumentContext):
        pass

    # Exit a parse tree produced by CPP14Parser#templateargument.
    def exitTemplateargument(self, ctx: CPP14Parser.TemplateargumentContext):
        pass

    # Enter a parse tree produced by CPP14Parser#typenamespecifier.
    def enterTypenamespecifier(self, ctx: CPP14Parser.TypenamespecifierContext):
        pass

    # Exit a parse tree produced by CPP14Parser#typenamespecifier.
    def exitTypenamespecifier(self, ctx: CPP14Parser.TypenamespecifierContext):
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

    # Enter a parse tree produced by CPP14Parser#exceptiondeclaration.
    def enterExceptiondeclaration(self, ctx: CPP14Parser.ExceptiondeclarationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#exceptiondeclaration.
    def exitExceptiondeclaration(self, ctx: CPP14Parser.ExceptiondeclarationContext):
        pass

    # Enter a parse tree produced by CPP14Parser#exceptionspecification.
    def enterExceptionspecification(self, ctx: CPP14Parser.ExceptionspecificationContext):
        pass

    # Exit a parse tree produced by CPP14Parser#exceptionspecification.
    def exitExceptionspecification(self, ctx: CPP14Parser.ExceptionspecificationContext):
        pass

    # Enter a parse tree produced by CPP14Parser#typeidlist.
    def enterTypeidlist(self, ctx: CPP14Parser.TypeidlistContext):
        pass

    # Exit a parse tree produced by CPP14Parser#typeidlist.
    def exitTypeidlist(self, ctx: CPP14Parser.TypeidlistContext):
        pass

    # Enter a parse tree produced by CPP14Parser#rightShift.
    def enterRightShift(self, ctx: CPP14Parser.RightShiftContext):
        pass

    # Exit a parse tree produced by CPP14Parser#rightShift.
    def exitRightShift(self, ctx: CPP14Parser.RightShiftContext):
        pass

    # Enter a parse tree produced by CPP14Parser#rightShiftAssign.
    def enterRightShiftAssign(self, ctx: CPP14Parser.RightShiftAssignContext):
        pass

    # Exit a parse tree produced by CPP14Parser#rightShiftAssign.
    def exitRightShiftAssign(self, ctx: CPP14Parser.RightShiftAssignContext):
        pass

    # Enter a parse tree produced by CPP14Parser#theoperator.
    def enterTheoperator(self, ctx: CPP14Parser.TheoperatorContext):
        pass

    # Exit a parse tree produced by CPP14Parser#theoperator.
    def exitTheoperator(self, ctx: CPP14Parser.TheoperatorContext):
        pass
