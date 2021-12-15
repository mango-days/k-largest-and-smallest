array = [ 7 , 10 , 4 , 3 , 20 , 15 ]
k = 3

array_small = array .copy ()
array_large = array .copy ()

for index in range ( 1 , k ) :
    array_small .remove ( min ( array_small ) )
    array_large .remove ( max ( array_large ) )
    
print ( k , "smallest element =", min ( array_small ) )
print ( k , "largest element =", max ( array_large ) )
