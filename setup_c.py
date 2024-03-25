from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from src.python.util.util import Util

sourcefiles = Util.get_files_list_by_extension(f'{Util.get_project_root()}/src/cython/', ".pyx")
sourcefiles = [file[0].replace(f'{Util.get_project_root()}/', '') for file in sourcefiles]
ext_modules = [Extension(file.replace('/', '.').replace('.pyx', ''), [file]) for file in sourcefiles]

setup(
    name='Jeronimo Costa Penha',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules,
)
