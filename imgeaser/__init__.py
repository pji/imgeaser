"""
__init__
~~~~~~~~

Initialization for the imgeaser module.
"""
from imgeaser.imgeaser import *
from imgeaser import imgeaser
from imgeaser.utility import get_prefixed_functions


# Create a dictionary to allow easier discovery and validation of
# the eases available in the module.
eases = get_prefixed_functions('ease_', imgeaser)