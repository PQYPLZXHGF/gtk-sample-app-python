from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('hello.py', base=base)
]

setup(name='hello',
      version = '1.0',
      description = '',
      options = dict(build_exe = buildOptions),
      executables = executables)
