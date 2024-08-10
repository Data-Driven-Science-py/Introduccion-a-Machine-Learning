from numpy.typing import NDArray
from typing import Tuple

def descenso_gradiente_v1(x_n: NDArray, y_n: NDArray, parc_f_x: NDArray, parc_f_y: NDArray, gamma: float) -> Tuple[NDArray, NDArray]:
    # x_{n+1}, y_{n+1} = y_n, x_n - \gamma grad f(x_n, y_n)
    x_n_1 = x_n - gamma * parc_f_x
    y_n_1 = y_n - gamma * parc_f_y
    return x_n_1, y_n_1


def descenso_gradiente_v2(a_n: NDarray, grad_f: NDArray, gamma: float) -> NDArray:
    # a_{n+1} = a_n - \gamma grad f(x_n,y_n)
    return a_n - gamma * grad_f


