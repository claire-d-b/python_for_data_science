source ~/.zshrc
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install --upgrade setuptools wheel

echo alias python='./venv/bin/python' >> venv/bin/activate

deactivate
source venv/bin/activate

pip uninstall ft_package

python setup.py sdist
pip install ./dist/ft_package-0.0.1.tar.gz

python setup.py bdist_wheel
pip install ./dist/ft_package-0.0.1-py3-none-any.whl

pip list
pip install .
pip show -v ft_package

deactivate