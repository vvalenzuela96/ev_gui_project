import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1'
PACKAGE_NAME = 'error_visor_gui'
AUTHOR = 'Victor Valenzuela M'
AUTHOR_EMAIL = 'vi.valenzuelam@gmail.com'
URL = 'https://github.com/vvalenzuela96/error_visor_gui_project'

LICENSE = 'MIT'
DESCRIPTION = 'Librería de apoyo gráfico para error_visor'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"


INSTALL_REQUIRES = [
      'error_visor'
      ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)