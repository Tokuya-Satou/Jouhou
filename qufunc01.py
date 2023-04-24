import random
from sympy import *

x = Symbol('x')

# aを含む二次関数の式をランダムに生成する関数
def create_quadratic_equation():
    a = Symbol('a')

    # 1次の係数にaを含む二次関数を生成
    f = random.choice([-1, 1]) * (a - random.randint(1, 10)) * x**2 \
        + random.choice([-1, 1]) * x \
        + random.randint(-10, 10)
    return f

# 二次関数の式と頂点の座標を出力する関数
def print_equation_and_vertex():
    f = create_quadratic_equation()
    # 頂点の座標を計算
    vertex = (-Rational(f.coeff(x, 1)) / (2 * f.coeff(x, 2)), f.subs(x, -f.coeff(x, 1) / (2 * f.coeff(x, 2))))
    # 結果を出力
    print("f(x) = {}".format(f))
    print("頂点の座標: {}".format(vertex))

# 3つの二次関数の式と頂点の座標を出力
for i in range(3):
    print_equation_and_vertex()
    print()
