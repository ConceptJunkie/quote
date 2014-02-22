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

PROGRAM_NAME = "qindex"
VERSION = "3.0.1"
COPYRIGHT_MESSAGE = "copyright (c) 2013 (1990), Rick Gutleber (rickg@his.com)"


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
    parser.add_argument( 'indexFile', default='quote.idx' )

    args = parser.parse_args( )

    quoteFile = args.quoteFile
    indexFile = args.indexFile

    #fortuneFormat = args.fortune

    outputFile = open( indexFile, 'wb' )

    offset = 0
    quoteCount = 1

    outputFile.write( struct.pack( 'i', quoteCount ) )  # the final index count will go here when we are finished
    outputFile.write( struct.pack( 'i', offset ) )      # the first quote

    for line in codecs.open( quoteFile, 'rU', 'ascii', 'replace' ):
        offset += len( line )

        if line == '%\r\n':
            outputFile.write( struct.pack( 'i', offset ) )
            quoteCount += 1

            if quoteCount % 400 == 0:
                print( quoteCount, end='\r', file=sys.stderr )

    outputFile.seek( 0 )
    outputFile.write( struct.pack( 'i', quoteCount ) )

    outputFile.close( )

    print( quoteCount - 1, end='\r', file=sys.stderr )


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

