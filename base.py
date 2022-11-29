#Dictionary for the faces
faces = {'D': (color.white(0, -1, 0)),
         'U': (color.yellow(0,1,0)),
         'F': (color.red(0, 0, 1)),
         'B': (color.orange(0,0,-1)),
         'L': (color.blue(-1, 0, 0)),
         'R': (color.green(1, 0, 0))}


#d = Down
#u = Up
#f = Front
#b = Back
#l = Left
#r = Right

#'w' = White
#'y' = Yellow
#'r' = Red
#'o' = Orange
#'b' = Blue
#'g' = Green

#Centers
d = 'w'
u = 'y'
f = 'r'
b = 'o'
l = 'b'
r = 'g'



#In solved state: the corner pieces(8)
#upper corner pieces
ufr = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': 'g', 'l': ''}
ufl = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'}
ubr = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''}
ubl = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'}


#lower corner pieces
dfr = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': 'g', 'l': ''}
dfl = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': 'b'}
dbr = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': 'g', 'l': ''}
dbl = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': 'b'}

#Edge pieces(12)
#upper edge pieces

uf = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': ''}
ur = {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': 'g', 'l': ''}
ub = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': ''}
ul = {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': '', 'l': 'b'}

#middle edge pieces
mfr = {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': 'g', 'l': ''}
mfl = {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'}
mbr = {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''}
mbl = {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'}

#down edge pieces
df = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': ''}
dr = {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': 'g', 'l': ''}
db = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': ''}
dl = {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': '', 'l': 'b'}
#.
#.
#Initial Solved Cube state