import sys
sys.path.append("D:/Pyhton/PythonSelenium/PythonSeleniumGIT/Basic/Module&Package/Pack1")
import Module1
import Module2

Module1.enterName()
Module2.show()

from Module1 import *
from Module2 import *

Module1.enterName()
Module2.show()