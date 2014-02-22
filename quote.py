#!/usr/bin/env python

import argparse
import random
import struct


#//**********************************************************************
#//
#//  globals/constants
#//
#//**********************************************************************

PROGRAM_NAME = "quote"
VERSION = "3.1.0"
COPYRIGHT_MESSAGE = "copyright (c) 2013 (1990), Rick Gutleber (rickg@his.com)"


#//**********************************************************************
#//
#//  main
#//
#//**********************************************************************

def main( ):
    parser = argparse.ArgumentParser( prog=PROGRAM_NAME, description=PROGRAM_NAME + ' - ' + VERSION + ' - ' + COPYRIGHT_MESSAGE )

    parser.add_argument( 'quoteFile', default='quote.txt' )
    parser.add_argument( 'indexFile', default='quote.idx' )
    parser.add_argument( 'quote_choice', nargs='?', type=int, default=-1 )

    args = parser.parse_args( )

    quoteFile = args.quoteFile
    indexFile = args.indexFile
    quoteChoice = args.quote_choice

    itemSize = struct.calcsize( 'i' )

    print( "_" * 80 )
    print( )

    with open( indexFile, "rb" ) as infile:
        if quoteChoice == -1:
            quoteCount = struct.unpack( 'i', infile.read( itemSize ) )[ 0 ]
            quoteChoice = random.randint( 0, quoteCount )

        # +1 because the first item is the count
        infile.seek( ( quoteChoice + 1 ) * itemSize )

        offset = struct.unpack( 'i', infile.read( itemSize ) )[ 0 ]

    with open( quoteFile, "r" ) as infile:
        infile.seek( offset )

        for line in infile:
            if line == "%\n":
                break

            print( line, end='' )

    print( )
    print( "_" * 80 )
    print( quoteChoice )


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

