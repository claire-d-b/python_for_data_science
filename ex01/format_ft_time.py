from time import time
from datetime import date


print("Seconds since January 1, 1970: " + "{:,}".format(time()) + " or " + "{:.2e}".format(time()) + " in scientific notation")
""" .2e specifies the format: e for scientific notation and 2 for
two decimal places. """
print(date.today().strftime("%B %d %Y"))
