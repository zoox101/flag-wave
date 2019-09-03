
from FlagWaver.FlagWaver import FlagWaver

GRADIENT = "source/color_flag_mask.gif"
WHITE = "source/white_flag.gif"
SHADOW = "source/white_flag_shadow.gif"

flag_waver = FlagWaver(GRADIENT, WHITE, SHADOW)
flag_waver.create_gif('Target.png')
