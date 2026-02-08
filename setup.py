from setuptools import setup, Extension
from Cython.Build import cythonize


modules = [
    Extension('src.py.graph.graph', sources=['src/py/graph/graph.pyx']),
    Extension('src.py.util.util', sources=['src/py/util/util.py'])
]

setup(
    name='cythonTest',
    version='1.0',
    author='jetbrains',
    ext_modules=cythonize(modules),
zip_safe=False
)
