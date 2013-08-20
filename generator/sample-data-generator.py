'''
Created on Aug 20, 2013

@author: nils
'''
import argparse
import csv
import os

if __name__ == '__main__':
    help = "Takes a tab-delimited file as input, parses, and"
    help = "%s inputs it into the database\n\nNOTE: All provided indices should be zero-based" % help

    parser = argparse.ArgumentParser(description='Create a sample data set for Refinery.')
    parser.add_argument('name', metavar="name", type=str,
                       help='name of the data set')
    parser.add_argument('--count', '-c', type=int,
                       help='number of sample files')
    parser.add_argument('--lines', '-l', type=int,
                       help='number of 10 character lines in each sample file')
    
    args = parser.parse_args()

    os.mkdir( args.name )
    
    with open(args.name + '/' + args.name + '.txt', 'wb') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t', quoting=csv.QUOTE_MINIMAL)        
        writer.writerow(['Source', 'Data File', 'Name', 'Group1', 'Group10', 'Group100', 'Group1000', 'Group10000', 'Group100000'])        
        
        for i in range( 0, args.count ):
            writer.writerow([(i+1), 'file_%05d.txt' % (i+1), 'File %d' % (i+1), int(i), int(i/10), int(i/100), int(i/1000), int(i/10000), int(i/100000)])
                        
            with open(args.name + '/' + 'file_%05d.txt' % (i+1), 'wb') as datfile:
                for l in range( 0, args.lines ):
                    datfile.write( "0123456789\n" )                
                datfile.close()