isort $(find pyexcel_odsw -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
black -l 79 pyexcel_odsw
black -l 79 tests
