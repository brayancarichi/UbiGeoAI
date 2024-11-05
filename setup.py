from setuptools import setup

setup(
    name='ubigeoai',
    version='0.1',
    packages=['ubigeoai'],
    description='Libreria que automatiza la ubicacion espacial de los Bounding Boxes',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='GEOINFORMATICA UACJ',
    author_email='brayanmurillogutierrez988@outlook.es',
    url='https://github.com/brayancarichi/UbiGeoAI.git',
    install_requires=[
        'fastai',
'geopandas',
'imutils',
'ipython',
'matplotlib',
'numpy',
'opencv_python',
'opencv_python_headless',
'pandas',
'Pillow'
'rasterio',
'scikit_learn',
'seaborn',
'Shapely',
'skimage',
'supervision',
'tqdm',
'ultralytics',
    ],
)