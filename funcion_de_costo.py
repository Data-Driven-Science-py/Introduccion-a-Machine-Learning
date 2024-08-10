from numpy.typing import NDArray
from typing import Tuple

w: float
b: float

def modelo(x: NDArray) -> NDArray:
    return x*w + b

def funcion_de_costo(x: NDArray, y: NDArray, ) -> NDArray:
    # Error medio cuadratico
    return (modelo(x,y) - y).pow(2).mean()


