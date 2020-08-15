#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    
    a = 0
    while (a < n * n * n):
        a = a + n * n

O(n): 
    as the input grows so does the time it takes. If n is 1 the function runs once if n is 3 then the first loop a = 9, then 27; if n is 5 after 5 loops n will equal 125 the same as `5*5*5`

b)

    sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1

O(n log n) because we have two loops and the first one is O(n) while the second one runs half as many time as n -> O(log n)

c)

    def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

0(n)
because its running code for every bunny if there are 2 bunnies it get called 2 times 
## Exercise II


    define a function that takes n amount of floors
        starting from the first floor   walk up one store
        on each floor drop the egg
            if it doesn't break than go up one more floor
            else if it breaks 
                stop going up and return the floor 


the runtime of my algorithm is O(n) because the time is linear to the amount of floors

