from distutils.core import setup

setup(
    name='chimera_ctioenviroment',
    version='0.0.1',
    packages=['chimera_ctioenviroment', 'chimera_ctioenviroment.instruments'],
    scripts=[],
    install_requires=['mysql', 'requests>=2.8.1', 'xmltodict'],
    url='http://github.com/astroufsc/chimera-ctioenviroment',
    license='GPL v2',
    author='William Schoenell',
    author_email='william@iaa.es',
    description='Chimera plugin for the CTIO weather station and seeing monitor'
)
