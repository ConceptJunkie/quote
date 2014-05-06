#!/usr/bin/env python

import argparse
import codecs
import random
import string
import struct
import sys


#//**********************************************************************
#//
#//  globals/constants
#//
#//**********************************************************************

PROGRAM_NAME = "qsort"
VERSION = "3.0.0"
COPYRIGHT_MESSAGE = "copyright (c) 2014 (1999), Rick Gutleber (rickg@his.com)"

lineLength = 80


#//******************************************************************************
#//
#//  generateSortKey
#//
#//******************************************************************************

def generateSortKey( s ):
    result = s.strip( )
    result = ' '.join( result.split( ) )

    for char in string.punctuation:
        result = result.replace( char, '' )

    result = result.lower( )

    return result


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

            if quoteCount % 100 == 0:
                print( quoteCount, end='\r', file=sys.stderr )

            quote = ''
        else:
            quote += line.rstrip( ) + '\n'

    print( quoteCount, file=sys.stderr )

    for quote in sorted( quoteList, key=generateSortKey ):
        print( quote, end='' )
        print( '%' )


#//**********************************************************************
#//
#//  __main__
#//
#//**********************************************************************

if __name__ == '__main__':
    main( )

