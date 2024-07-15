from time import time
from datetime import date


print("{:,}".format(time()))
scientific_notation = "{:.2e}".format(time())
print(scientific_notation)
""" .2e specifies the format: e for scientific notation and 2 for
two decimal places. """
print(date.today().strftime("%B %d %Y"))
