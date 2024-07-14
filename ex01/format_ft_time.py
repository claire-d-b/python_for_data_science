# L'epoch est le point de départ du temps, le résultat de time.gmtime(0)
# est le 1er janvier 1970 à 00:00:00 (UTC) pour toutes les plateformes.
from time import time
from datetime import date


print("{:,}".format(time()))
scientific_notation = "{:.2e}".format(time())
print(scientific_notation)
# .2e specifies the format: e for scientific notation and 2 for
# two decimal places.
print(date.today().strftime("%B %d %Y"))
