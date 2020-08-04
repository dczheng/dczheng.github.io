#!/usr/bin/env python3

from PIL import Image
import sys
import os

fn = sys.argv[1]

im = Image.open( fn )

t = fn.split( '.' )
if len(t) < 2:
    print( "ERROR" )
    sys.exit(1)

if t[-1] == "png":
    sys.exit(0)

fn_out = ''.join( t[:-1] ) + '.png'
print( "%s -> %s."%(fn, fn_out) )

im.save( fn_out, 'png' )
os.remove( fn )
