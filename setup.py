from setuptools import setup


install_requires = [
    'nltk'
]

setup(name='piidetector',
      version='0.1',
      description='PII Detection using NLTK and regular expression',
      url='https://github.com/hanymorcos/nltkiidetectorservice.git',
      author='Hany Morcos',
      author_email='hmorcos@donotemail.com',
      license='MIT',
      packages=['piidetector'],
      zip_safe=False,
      entry_points={
            'console_scripts': [
                'piidetector = nltkpiidetector.piidetector:main',
            ],
       },
      include_package_data=True,
      install_requires=install_requires
      )
