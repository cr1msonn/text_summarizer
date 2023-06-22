import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ =   "0.0.0"

REPO_NAME = "text_summarizer"
AUTOR_USER_NAME = "cr1msonn"
SRC_REPO =  "text_summarizer"
AUTHOR_EMAIL = "crmsonda@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    long_description=long_description,
    long_description_content_type="text/markdown",
        url=f"https://github.com/{AUTOR_USER_NAME}/{REPO_NAME}",
        packages=setuptools.find_packages(where='src'),
        classifiers=[
            "Programming Language :: Python :: 3"],