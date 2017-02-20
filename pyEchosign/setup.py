from setuptools import setup

setup(
    name='pyEchosign',
    version='0.1.0dev',
    packages=['utils', 'classes', 'exceptions'],
    url='https://gitlab.com/jensastrup/pyEchosign',
    license='MIT',
    author='Jens Astrup',
    author_email='jensaiden@gmail.com',
    description='Connect to the Echosign API without constructing HTTP requests',
    long_description=open('../README.rst').read(),
    install_requires=['requests>=2.12.4, <3.0.0', 'arrow>=0.10.0, <1.0.0'],
    tests_require=['coverage', 'nose'],
    keywords='adobe echosign',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Office/Business',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Natural Language :: English'
    ]
)