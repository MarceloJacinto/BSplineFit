from distutils.core import setup

setup(
    name = 'my_python_package',
    packages = ['my_python_package'],
    version = '1.0.0',  # Ideally should be same as your GitHub release tag varsion
    description = 'A uniform cubic B-spline regression library',
    author = 'MarceloJacinto',
    author_email = 'marcelo.jacinto@tecnico.ulisboa.pt',
    url = 'https://github.com/MarceloJacinto/BSplineFit',
    download_url = 'https://github.com/MarceloJacinto/BSplineFit',
    keywords = ['BSpline', 'CubicBSplineFit'],
    classifiers = [],
)