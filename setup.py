from setuptools import setup
from setuptools import find_packages

setup(
  name = "VKStuff",
  description = "Набор утилит для работы со стеной паблика ВК",
  url = "https://github.com/Atronar/VKStuff",
  version = "20.06.14.0",
  author = "ATroN",
  author_email = "master.atron@gmail.com",
  python_requires='>=3.6',
  platforms = ["Windows"],
  packages = find_packages(),
  install_requires = ["vk_api","PyQt5","pywin32","opencv-python","numpy","FileOptimizerPy"],
  include_package_data = True,
  classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Operating System :: Microsoft :: Windows",
    "Topic :: Utilities",
    "Programming Language :: Python :: 3",
    "Natural Language :: Russian"
  ]
)
