from setuptools import setup

requirements = [
    'numpy',
    'Pillow',
]

setup(
    name='tinimage',
    version='0.1',
    description="Transform simple image to magic image",
    author="Alexander Smirnov",
    author_email='maintheme11@gmail.com',
    url='https://github.com/smirnoval/tinimage',
    packages=[
        'tinimage',
    ],
    package_dir={'tinimage': 'tinimage'},
    entry_points={
        'console_scripts': [
            'tinimage=tinimage:main'
        ]
    },
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='tinimage',
    classifiers=[
        'Development Status :: Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)
