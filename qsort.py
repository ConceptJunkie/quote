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

PROGRAM_NAME = "qsort"
VERSION = "3.0.alpha1"
COPYRIGHT_MESSAGE = "copyright (c) 2014 (1999), Rick Gutleber (rickg@his.com)"

lineLength = 80


#//******************************************************************************
#//
#//  generateSortKey
#//
#//******************************************************************************

def generateSortKey( s ):
    # Ignore leading and trailing spaces
    s = s.strip( )
    # All space types are equivalent
    s = ' '.join( s.split( ) )
    # case insentsitive
    s = s.lower( )

    return s


#//**********************************************************************
#//
#//  main
#//
#//**********************************************************************

def main( ):
    parser = argparse.ArgumentParser( prog=PROGRAM_NAME, description=PROGRAM_NAME + ' - ' + VERSION + ' - ' + COPYRIGHT_MESSAGE )

    parser.add_argument( 'input', default='quote.txt' )
    #parser.add_argument( 'output', default='quote.sorted.txt' )

    args = parser.parse_args( )

    inputFile = args.input

    quote = ''
    quoteList = [ ]
    quoteCount = 0

    for line in codecs.open( inputFile, 'rU', 'ascii', 'replace' ):
        if line == '%\r\n':
            quoteCount += 1
            quoteList.append( quote )

            if quoteCount % 400 == 0:
                print( quoteCount, end='\r', file=sys.stderr )

            quote = ''
        else:
            quote += line

    quoteCount = 1

    print( file=sys.stderr )

    for quote in sorted( quoteList, key=generateSortKey ):
        #print( quoteCount, file=sys.stderr )
        print( quote, end='' )
        print( '%' )
        quoteCount += 1


#//**********************************************************************
#//
#//  __main__
#//
#//**********************************************************************

if __name__ == '__main__':
    main( )

