import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yxq_stock",
    version="0.1",
    author="Yang Xuanzhou",
    author_email="",
    description="predict one's stock",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lc930627/yxq_stock",
    packages=setuptools.find_packages(),
    install_requires=['Pillow>=5.1.0', 'numpy==1.14.4'],
    entry_points={
        'console_scripts':[
          'yxq_stock=yxq_stock:main'  
        ],
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)