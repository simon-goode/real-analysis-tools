import sys
from sympy.parsing.latex import parse_latex

def latex_to_sympy(latex_expr):
    try:
        expr = parse_latex(latex_expr)
        return expr
    except Exception as e:
        print(f"Error parsing LaTeX: {e}")
        return None

def latexes_to_sympy(latex_expressions):
    return [latex_to_sympy(expr) for expr in latex_expressions]