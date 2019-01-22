import mypack
#from mypack import utils as mp_utils #is the same as the line below
import mypack.utils as mp_utils
from mypack.utils.io import read_selig #but shouldn't do this. Better to do import mypack.utils.io as my_io; my_io.read_selig().
from mypack.calcs #no custom name; or from mypack import calcs but this loses the parent package name
mypack.calcs.get_lift()
