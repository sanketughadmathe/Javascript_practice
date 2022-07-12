# function addUpTo(n) {
#   let total = 0;
#   for (let i = 0; i < n; i++) {
#     // const element = n[i];
#     total += n;
#   }
#   return total
# }

# var t1 = performance.now()
# addUpTo(1000000000)
# var t2 = performance.now()
# console.log(`Time Elapsed: ${(t2 -t1)/100} seconds`)

# import the builtin time module
import time

# Grab Currrent Time Before Running the Code

def addUpTo(n):
  total = 0

  for i in range(n):
    total += n;
  # total = n * (n+1) / 2
  print(f"Total {total} Ends")
  # pass

start = time.time()
print(addUpTo(100000000))
end = time.time()
#Subtract Start Time from The End Time
total_time = end - start
print(f"Time Elapsed: {total_time} seconds")