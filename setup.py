from cx_Freeze import setup, Executable
import sys

buildOpt = dict(packages=['selenium', 'pandas', 'os', 'scholarMain', 'scholar', 'commonFunc'], excludes=[])
exe = [Executable("main.py")]

setup(
    name='ScrapPapers',
    version ='0.1',
    author='SeokJin',
    description='This is a program that scrap papers.',
    options=dict(build_exe=buildOpt),
    executables = exe
)