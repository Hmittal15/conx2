import io
import sys
try:
    import pypandoc
except:
    pypandoc = None

from setuptools import find_packages, setup

with io.open('conx/_version.py', encoding='utf-8') as fid:
    for line in fid:
        if line.startswith('__version__'):
            version = line.strip().split()[-1][1:-1]
            break

with io.open('README.md', encoding='utf-8') as fp:
    long_desc = fp.read()
    if pypandoc is not None:
        try:
            long_desc = pypandoc.convert(long_desc, "rst", "markdown_github")
        except:
            pass


setup(name='conx2',
      version=version,
      description='patch to conx',
      long_description=long_desc,
      author='Dino K',
      author_email='dinorows@gmail.com',
      url='https://github.com/conx2',
      install_requires=['numpy', 'keras>=2.1.3', 'matplotlib',
                        'ipywidgets>=7.0', 'Pillow', 'IPython',
                        'h5py', "svgwrite", "scikit-learn",
                        "tqdm", "requests", "pydot", "cairosvg"],
      packages=find_packages(include=['conx', 'conx.*']),
      include_data_files = True,
      test_suite = 'nose.collector',
      classifiers=[
          'Framework :: IPython',
          ('License :: OSI Approved :: ' +
           'GNU Affero General Public License v3 or later (AGPLv3+)'),
          'Programming Language :: Python :: 3',
      ]
)
