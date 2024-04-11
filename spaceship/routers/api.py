from fastapi import APIRouter
import numpy as np

MATRIX_SIZE = 10

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get('/matrix')
def matrix() -> dict:
    matrix_a = np.random.rand(MATRIX_SIZE, MATRIX_SIZE)
    matrix_b = np.random.rand(MATRIX_SIZE, MATRIX_SIZE)
    result = np.dot(matrix_a, matrix_b)
    return {
        "matrix_a": matrix_a.tolist(),
        "matrix_b": matrix_b.tolist(),
        "product": result.tolist()
    }