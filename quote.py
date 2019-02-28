#!/usr/bin/env python

import argparse
import random
import struct
import codecs
#import textwrap


#//**********************************************************************
#//
#//  globals/constants
#//
#//**********************************************************************

PROGRAM_NAME = "quote"
VERSION = "3.3.0"
COPYRIGHT_MESSAGE = "copyright (c) 2019 (1990), Rick Gutleber (rickg@his.com)"

lineLength = 80
itemSize = struct.calcsize( 'i' )


#//**********************************************************************
#//
#//  getOffset
#//
#//**********************************************************************

def getOffset( infile, quoteChoice ):
    # +1 because the first item is the count
    infile.seek( ( quoteChoice + 1 ) * itemSize )
    return struct.unpack( 'i', infile.read( itemSize ) )[ 0 ]


#//**********************************************************************
#//
#//  main
#//
#//**********************************************************************

def main( ):
    parser = argparse.ArgumentParser( prog = PROGRAM_NAME, description = PROGRAM_NAME + ' - ' +
                                      VERSION + ' - ' + COPYRIGHT_MESSAGE, add_help = False,
                                      formatter_class = argparse.RawTextHelpFormatter,
                                      prefix_chars = '-' )

    parser.add_argument( 'quoteFile', default = 'quote.txt' )
    parser.add_argument( 'indexFile', default = 'quote.idx' )

    parser.add_argument( '-q', '--quote', nargs = '?', type = int, action = 'store', default = 0 )
    parser.add_argument( '-n', '--count', nargs = '?', type = int, action = 'store', default = 1 )
    parser.add_argument( '-s', '--search', nargs = '?', type = str, action = 'store', default = '' )

    args = parser.parse_args( )

    quoteFile = args.quoteFile
    indexFile = args.indexFile

    quoteChoice = args.quote - 1   # first quote is #1, not #0
    quotesToPrint = args.count
    searchTerm = args.search

    if quoteChoice != -1 and quotesToPrint > 1:
        print( "-q and -n cannot be used together" )
        return

    offsets = [ ]
    quoteChoices = [ ]

    with open( indexFile, "rb" ) as infile:
        quoteCount = struct.unpack( 'i', infile.read( itemSize ) )[ 0 ]

        if quoteChoice == -1:
            for i in range( quotesToPrint ):
                quoteChoices.append( random.randint( 0, quoteCount ) )
                offsets.append( getOffset( infile, quoteChoices[ -1 ] ) )
        else:
            if quoteChoice > quoteCount:
                print( "-q value is too high.  There are only %d quotes." % quoteCount )
                return

            quoteChoices.append( quoteChoice )
            offsets.append( getOffset( infile, quoteChoices[ -1 ] ) )

    print( "_" * lineLength )
    print( )

#    with codecs.open( quoteFile, 'rU', 'ascii', 'replace' ) as infile:
    with open( quoteFile, "r" ) as infile:
        for i in range( 0, quotesToPrint ):
            infile.seek( offsets[ i ] )

            quote = ''

            for line in infile:
                if line == "%\n":
                    break

                print( line, end='' )

            print( )
            print( "_" * lineLength )
            print( quoteChoices[ i ] + 1 )
            print( )


#//**********************************************************************
#//
#//  __main__
#//
#//**********************************************************************

if __name__ == '__main__':
    main( )

