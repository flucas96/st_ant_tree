import setuptools


with open('README.md') as f:
    long_desc = f.read()

setuptools.setup(
    name="st_ant_tree",
    version="0.0.14",
    author="",
    author_email="",
    description="Streamlit Component for ANT Tree",
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url="https://github.com/flucas96/st_ant_tree",
    license="MIT",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)