import random
import os
H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'

def Banner():
	text1 = B+"""
  _     _               _      _______                __
 (_)   (_)        ____ (_)    (__ _ __)              (__)
 (_)___(_)  ____ (____)(_)__     (_)     ___    ___   (_)
 (_______) (____)(_)__ (____)    (_)    (___)  (___)  (_)
 (_)   (_)( )_( ) _(__)(_) (_)   (_)   (_)_(_)(_)_(_) (_)
 (_)   (_) (__)_)(____)(_) (_)   (_)    (___)  (___) (___) V1.5
"""
	text2 = G+"""
  _______                __     _______                __
 |   |   |.---.-..-----.|  |--.|_     _|.-----..-----.|  |
 |       ||  _  ||__ --||     |  |   |  |  _  ||  _  ||  |
 |___|___||___._||_____||__|__|  |___|  |_____||_____||__| V1.5
"""
	text3 = F+"""
  _   _              _      _____                _
 | | | |            | |    |_   _|              | |
 | |_| |  __ _  ___ | |__    | |    ___    ___  | |
 |  _  | / _` |/ __|| '_ \   | |   / _ \  / _ \ | |
 | | | || (_| |\__ \| | | |  | |  | (_) || (_) || |
 \_| |_/ \__,_||___/|_| |_|  \_/   \___/  \___/ |_| V1.5
"""
	text4 = O+"""
                      _      _____                _
   /\  /\  __ _  ___ | |__  /__   \  ___    ___  | |
  / /_/ / / _` |/ __|| '_ \   / /\/ / _ \  / _ \ | |
 / __  / | (_| |\__ \| | | | / /   | (_) || (_) || |
 \/ /_/   \__,_||___/|_| |_| \/     \___/  \___/ |_| V1.5
"""
	text5 = W+"""
    __  __           __  ______            __
   / / / /___ ______/ /_/_  __/___  ____  / /
  / /_/ / __ `/ ___/ __ \/ / / __ \/ __ \/ /
 / __  / /_/ (__  ) / / / / / /_/ / /_/ / /
/_/ /_/\__,_/____/_/ /_/_/  \____/\____/_/ V1.5
"""
	text6 = B+"""
_  _ ____ ____ _  _ ___ ____ ____ _
|__| |__| [__  |__|  |  |  | |  | |
|  | |  | ___] |  |  |  |__| |__| |___ V1.5
"""

	ran = random.randrange(1,6)
	if ran == 1:
	        print(text1)
	elif ran == 2:
	        print(text2)
	elif ran == 3:
	        print(text3)
	elif ran == 4:
		print(text4)
	elif ran == 5:
	        print(text5)
	elif ran == 6:
		print(text6)
