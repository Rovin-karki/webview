from pythonforandroid.recipe import PythonRecipe

class PyWebViewRecipe(PythonRecipe):
    version = '4.4.1'
    url = f'https://github.com/r0x0r/pywebview/archive/{version}.tar.gz'

    depends = ['python3']

recipe = PyWebViewRecipe()
