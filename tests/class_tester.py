#from ..FlagWaver.FlagWaver import FlagWaver
#from FlagWaver.FlagWaver import FlagWaver
#from FlagWaver.FlagWaver import FlagWaver

# GRADIENT = "flag-wave/tests/source/color_flag_mask.gif"
# WHITE = "flag-wave/tests/source/white_flag.gif"
# SHADOW = "flag-wave/tests/source/white_flag_shadow.gif"

GRADIENT = "source/color_flag_mask.gif"
WHITE = "source/white_flag.gif"
SHADOW = "source/white_flag_shadow.gif"

flag_waver = FlagWaver(GRADIENT, WHITE, SHADOW)
flag_waver.create_gif('France.png')
