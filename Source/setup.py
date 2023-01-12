from cx_Freeze import setup, Executable

option = {
        'packages' : ['scholarMain', 'scholar', 'commonFunc'],
        'excludes' : [],
        'build_exe': '../build'
}
exe = [Executable("main.py")]

setup(
    name='ScrapPapers',
    version ='0.1',
    author='SeokJin',
    description='This is a program that scrap papers.',
    options=dict(build_exe=option),
    executables = exe
)