"""
End-to-End Multi-Lingual Optical Character Recognition (OCR) Solution
"""
from io import open
from setuptools import setup

with open('requirements.txt', encoding="utf-8-sig") as f:
    requirements = f.readlines()

def readme():
    with open('README.md', encoding="utf-8-sig") as f:
        README = f.read()
    return README

setup(
    name='easyocr-digit',
    packages=['easyocr'],
    include_package_data=True,
    version='0.0.2',
    install_requires=requirements,
    entry_points={"console_scripts": ["easyocr= easyocr.cli:main"]},
    license='Apache License 2.0',
    description='Minimal EasyOCR fork for digit recognition (CPU-only)',
    long_description=readme(),
    long_description_content_type="text/markdown",
    author='Ilya Radinsky',
    author_email='radinsky.ilya@gmail.com',
    url='https://github.com/IlyaRadinsky/easyocr',
    download_url='https://github.com/IlyaRadinsky/easyocr.git',
    keywords=['ocr optical character recognition deep learning neural network'],
    classifiers=[
        'Development Status :: 5 - Production/Stable'
    ],

)
