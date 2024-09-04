source ~/.zshrc
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install --upgrade setuptools wheel

echo alias python='./venv/bin/python3.10' >> venv/bin/activate

pip install tqdm

echo alias tqdm='./venv/bin/tqdm' >> venv/bin/activate

deactivate
source venv/bin/activate

pip install flake8
alias norminette=flake8

pip uninstall ft_package

# Generate Distribution Archive
# This command will create a dist/ directory containing a .tar.gz file, which is your distribution archive.
python setup.py sdist
pip install ./dist/ft_package-0.0.1.tar.gz

# Generate Wheel Distribution
# This command will create a dist/ directory containing a .whl file, which is your wheel distribution archive.
python setup.py bdist_wheel
pip install ./dist/ft_package-0.0.1-py3-none-any.whl

# Difference between both : standard source distribution archive sdist (cross-platform, Python compiles the code during installation) VS  binary distribution format called a wheel (faster installation, platform specific, skips the build step and directly unpacks the pre-built files)

pip list
pip install .
pip show -v ft_package

python ft_package/__init__.py

deactivate

rm -rf ft_package/__pycache__
rm -rf ft_package.egg-info
rm -rf build
rm -rf dist
rm -rf venv
