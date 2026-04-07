from setuptools import setup, find_packages

setup(
    name             = "decrypt",
    version          = "0.1.2",
    description      = "Pipe programs through decrypt to fool people into thinking you are a hacker",
    long_description = open('README.md').read(),
    author           = "L33T",
    url              = "None",
    packages         = ["decrypt"],
    entry_points     = {'console_scripts': ['decrypt = decrypt.decrypt:main']},
)
