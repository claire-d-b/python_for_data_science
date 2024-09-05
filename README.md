source ~/.zshrc
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip

echo alias python='./venv/bin/python3.10' >> venv/bin/activate

pip install tqdm

echo alias tqdm='./venv/bin/tqdm' >> venv/bin/activate

deactivate
source venv/bin/activate

pip install flake8
alias norminette=flake8

rm -rf ft_package/__pycache__
rm -rf ft_package.egg-info
rm -rf build
rm -rf dist
rm -rf venv
