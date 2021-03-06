import reskit

version = reskit.__version__

from setuptools import setup, find_packages

setup(name='reskit',
      packages=find_packages(),
      version=version,
      description='Researcher kit for reproducible experiments',
      author='Alexander Ivanov, Dmitry Petrov',
      author_email='alexander.radievich@gmail.com,'
                   'to.dmitry.petrov@gmail.com',
      url='https://github.com/neuro-ml/reskit',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved',
          'Programming Language :: Python',
          'Topic :: Software Development',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          ],
      license='new BSD',
      install_requires=[
          'numpy>=1.12.0',
          'scikit-learn>=0.18.1',
          'pandas>=0.19.2'
          ]
      )
