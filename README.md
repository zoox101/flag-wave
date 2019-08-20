
 ![Flag Examples](flags.gif)

# Description

A repository containing code to automatically add arbitrary flags to u/\_Reff's flag waver. (I named him Joe)

So I (Shahriyar Shawon) liked how this worked so I wanted to create a package for it. It is now importable to your python scripts.

[Link to PyPi page](https://pypi.org/project/FlagWaver/)

# Installation
 ```bash
pip install FlagWaver
```
#### You will need to download the source folder [download from my GDrive](https://drive.google.com/open?id=1qKoeFYALTW03p353zuZw-cWxEPzlKvlx) along with its content and put it in the same directory as your script that will use the FlagWaver package.

# Get started

```python
from FlagWaver.FlagWaver import FlagWaver

GRADIENT = "source/color_flag_mask.gif"
WHITE = "source/white_flag.gif"
SHADOW = "source/white_flag_shadow.gif"

flag_waver = FlagWaver(GRADIENT,WHITE,SHADOW)
flag_waver.create_gif("path_to_flag_image.png")
```
   



# License

 <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
