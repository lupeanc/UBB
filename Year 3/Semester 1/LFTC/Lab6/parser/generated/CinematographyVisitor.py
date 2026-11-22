# Generated from grammar/Cinematography.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CinematographyParser import CinematographyParser
else:
    from CinematographyParser import CinematographyParser

# This class defines a complete generic visitor for a parse tree produced by CinematographyParser.

class CinematographyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CinematographyParser#program.
    def visitProgram(self, ctx:CinematographyParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#statement.
    def visitStatement(self, ctx:CinematographyParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#inputStatement.
    def visitInputStatement(self, ctx:CinematographyParser.InputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#outputStatement.
    def visitOutputStatement(self, ctx:CinematographyParser.OutputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#declarationStatement.
    def visitDeclarationStatement(self, ctx:CinematographyParser.DeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#declaredType.
    def visitDeclaredType(self, ctx:CinematographyParser.DeclaredTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:CinematographyParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#expression.
    def visitExpression(self, ctx:CinematographyParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:CinematographyParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:CinematographyParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#comparisonExpression.
    def visitComparisonExpression(self, ctx:CinematographyParser.ComparisonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:CinematographyParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:CinematographyParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#operand.
    def visitOperand(self, ctx:CinematographyParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#constructorCall.
    def visitConstructorCall(self, ctx:CinematographyParser.ConstructorCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#functionCall.
    def visitFunctionCall(self, ctx:CinematographyParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#argumentList.
    def visitArgumentList(self, ctx:CinematographyParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#index.
    def visitIndex(self, ctx:CinematographyParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#ifStatement.
    def visitIfStatement(self, ctx:CinematographyParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#condition.
    def visitCondition(self, ctx:CinematographyParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#logicalOrCondition.
    def visitLogicalOrCondition(self, ctx:CinematographyParser.LogicalOrConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#logicalAndCondition.
    def visitLogicalAndCondition(self, ctx:CinematographyParser.LogicalAndConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#conditionAtom.
    def visitConditionAtom(self, ctx:CinematographyParser.ConditionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#forStatement.
    def visitForStatement(self, ctx:CinematographyParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#forInitialization.
    def visitForInitialization(self, ctx:CinematographyParser.ForInitializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#forAssignment.
    def visitForAssignment(self, ctx:CinematographyParser.ForAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#whileStatement.
    def visitWhileStatement(self, ctx:CinematographyParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#userDatatypeStatement.
    def visitUserDatatypeStatement(self, ctx:CinematographyParser.UserDatatypeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#field.
    def visitField(self, ctx:CinematographyParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#vectorStatement.
    def visitVectorStatement(self, ctx:CinematographyParser.VectorStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#vectorCreation.
    def visitVectorCreation(self, ctx:CinematographyParser.VectorCreationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#vectorAssignment.
    def visitVectorAssignment(self, ctx:CinematographyParser.VectorAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#vector.
    def visitVector(self, ctx:CinematographyParser.VectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#vectorAdd.
    def visitVectorAdd(self, ctx:CinematographyParser.VectorAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#vectorRemoveAtIndex.
    def visitVectorRemoveAtIndex(self, ctx:CinematographyParser.VectorRemoveAtIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#vectorSetAtIndex.
    def visitVectorSetAtIndex(self, ctx:CinematographyParser.VectorSetAtIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#functionStatement.
    def visitFunctionStatement(self, ctx:CinematographyParser.FunctionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#parameters.
    def visitParameters(self, ctx:CinematographyParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#parameter.
    def visitParameter(self, ctx:CinematographyParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#returnStatement.
    def visitReturnStatement(self, ctx:CinematographyParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#type.
    def visitType(self, ctx:CinematographyParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#value.
    def visitValue(self, ctx:CinematographyParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#booleanValue.
    def visitBooleanValue(self, ctx:CinematographyParser.BooleanValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#relationalOperator.
    def visitRelationalOperator(self, ctx:CinematographyParser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CinematographyParser#identifier.
    def visitIdentifier(self, ctx:CinematographyParser.IdentifierContext):
        return self.visitChildren(ctx)



del CinematographyParser