source ~/.zshrc
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip uninstall tqdm
pip install tqdm
pip show tqdm
echo alias python='./venv/bin/python' >> venv/bin/activate
echo alias tqdm='./venv/bin/tqdm' >> venv/bin/activate
deactivate
source venv/bin/activate

python src/tester.py

deactivate

rm -rf src/__pycache__
rm -rf venv


