import ExpressionTreeBuilder as expressionTreeBuilderLib
import ExpressionParser as expressionParserLib
import EvaluateExpression as evaluateExpressionLib

def test_for_evaluating_tree():
    s = "(11+22-(33/44/55-66)-(77*88-99*109))"
    sList = expressionParserLib.getListFromExpression(s)
    # s = "(" + s
    # s += ")"
    root = expressionTreeBuilderLib.buildFromList(sList)
    root.display()
    evaluateExpressionLib.evaluateExpressionTree(root)