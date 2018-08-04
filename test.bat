pip freeze
nosetests --with-coverage --cover-package pyexcel_odsw --cover-package tests --with-doctest --doctest-extension=.rst README.rst tests docs/source pyexcel_odsw && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
