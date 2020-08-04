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

if t[-1] != "png":
    fn_out = ''.join( t[:-1] ) + '.png'
    print( "%s -> %s."%(fn, fn_out) )

    im.save( fn_out, 'png' )
    os.remove( fn )

print( im.size, ' ',  end='' )

w, h = im.size
r = float(w) / h
x = 500
if w > x or h > x:
    if w > h:
        ww = x 
        hh = int( ww / r )
    else:
        hh = x
        ww = int( hh * r )
    im = im.resize( (ww, hh), Image.ANTIALIAS )

print( im.size )
fn_thumb = ''.join( t[:-1] ) + '-thumb.png'
im.save( fn_thumb, 'png' )
