#!/usr/bin/env python

import argparse
import codecs
import random
import struct
import sys


#//**********************************************************************
#//
#//  globals/constants
#//
#//**********************************************************************

PROGRAM_NAME = "qsearch"
VERSION = "0.0.0"
COPYRIGHT_MESSAGE = "copyright (c) 2015, Rick Gutleber (rickg@his.com)"


#//**********************************************************************
#//
#//  main
#//
#//**********************************************************************

def main( ):
    #print( PROGRAM_NAME + ' ' + VERSION, end='\n', file=sys.stderr )
    #print( "    Quote file must consist of ASCII quotes, each separated by a line containing", end='\n', file=sys.stderr )
    #print( "    only \"%\".", end='\n', file=sys.stderr )

    parser = argparse.ArgumentParser( prog=PROGRAM_NAME, description=PROGRAM_NAME + ' - ' + VERSION + ' - ' + COPYRIGHT_MESSAGE )

    #parser.add_argument( '-f', '--fortune', action='store_true', help="output fortune(6) format" )
    parser.add_argument( 'quoteFile', default='quote.txt' )

    args = parser.parse_args( )

    quoteFile = args.quoteFile

    offset = 0
    quoteCount = 1

    dash = False
    lineCount = 1

    for line in codecs.open( quoteFile, 'rU', 'ascii', 'replace' ):
        line = line.strip( )

        if len( line ) > 1:
            if line[ 0 ] == '-':
                if dash:
                    print( lineCount )
                else:
                    dash = True
            else:
                dash = False
        else:
            dash = False

        lineCount += 1


#//**********************************************************************
#//
#//  __main__
#//
#//**********************************************************************

if __name__ == '__main__':
    #try:
        main( )
    #except:
    #    pass

