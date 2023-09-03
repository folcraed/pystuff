from random import random, randint, seed

s = "{:>5d} times {:^6.2f} is {:>5.2f}"
print( s.format( 1, 3.75, 1 * 3.75 ) )
print( s.format( 2, 3.75, 2 * 3.75 ) )
print( s.format( 3, 3.75, 3 * 3.75 ) )
print( s.format( 4, 3.75, 4 * 3.75 ) )
print( s.format( 5, 3.75, 5 * 3.75 ) )

seed()
print( "A random number between 1 and 10 is", randint( 1, 10) )
print( "Another is", randint( 1, 10) )
seed( 0 )
print( "3 random numbers are: {:.2f} {:.2f} {:.2f}".format( random(), random(), random() ))
seed( 0 )
print( "The same 3 numbers are:", random(), random(), random() )
