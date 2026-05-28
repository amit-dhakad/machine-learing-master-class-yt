# import_styles.py - Visualizing different import techniques in Python

# Technique 1: Direct Import
import math
print("1. Direct import (math.sqrt):", math.sqrt(16))  # Output: 4.0

# Technique 2: Specific Import
from math import pi, sin
print("2. Specific import (pi):", pi)                 # Output: 3.14159...

# Technique 3: Aliased Module
import datetime as dt
print("3. Aliased module (dt.date.today):", dt.date.today())

# Technique 3b: Aliased Specific Item
from math import factorial as fact
print("3b. Aliased specific item (fact):", fact(5))    # Output: 120
