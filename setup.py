from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    # Extension("src.util.util", ["src/util/util.pyx"]),
    Extension("src.sw.sa_pipeline.stage0_sa", ["src/sw/sa_pipeline/stage0_sa.pyx"]),
    Extension("src.sw.sa_pipeline.stage1_sa", ["src/sw/sa_pipeline/stage1_sa.pyx"]),
    Extension("src.sw.sa_pipeline.stage2_sa", ["src/sw/sa_pipeline/stage2_sa.pyx"]),
    Extension("src.sw.sa_pipeline.stage3_sa", ["src/sw/sa_pipeline/stage3_sa.pyx"]),
    Extension("src.sw.sa_pipeline.stage4_sa", ["src/sw/sa_pipeline/stage4_sa.pyx"]),
    Extension("src.sw.sa_pipeline.stage5_sa", ["src/sw/sa_pipeline/stage5_sa.pyx"]),
    Extension("src.sw.sa_pipeline.stage6_sa", ["src/sw/sa_pipeline/stage6_sa.pyx"]),
    Extension("src.sw.sa_pipeline.stage7_sa", ["src/sw/sa_pipeline/stage7_sa.pyx"]),
    Extension("src.sw.sa_pipeline.stage8_sa", ["src/sw/sa_pipeline/stage8_sa.pyx"]),
    Extension("src.sw.sa_pipeline.stage9_sa", ["src/sw/sa_pipeline/stage9_sa.pyx"]),
    # Extension("src.sw.sa_pipeline.stage10_sa", ["src/sw/sa_pipeline/stage10_sa.pyx"]),
    Extension("src.sw.sa_pipeline.sa_pipeline_sw", ["src/sw/sa_pipeline/sa_pipeline_sw.pyx"]),
]

setup(
    name='Jeronimo Costa Penha',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules,
)
