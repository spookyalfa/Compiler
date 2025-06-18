#include <stdio.h>

void another_magic( int, int );
void run( void );

int main( void )
{
  run();
  return 0;
}

void run( void )
{
  int x, y;
  scanf( "%d %d", &x, &y );

  if( x > 1 && x < 20 )
    if( y > x )
      another_magic( x, y );  
}

void another_magic( int columns, int range )
{
  int i = 1;
  while( i <= range )
    {
      for( int j = 1; j <= columns; j++ )
	{
	  if( i <= range )
	    {
	      if( j != columns )
		printf( "%d ", i );
	      else
		printf( "%d\n", i );
	    }

	  i++;
	}// end for
    }// end while
}
