num = 368078
n = 0
r = 0 #row
#can definitely be done better
def diff(x, y):
    return x - y if x > y else y - x

while n < num:
    start = n + 2
    n = n + r*8
    r += 1
    corner = n + 1

#row in which the number is
r = r - 1
length = r*2 + 1

l = length - 1
mid_ = 2*(r-1)
corners = [corner, corner - l, corner - 2*l, corner - 3*l]
answer = 0
if num < min(corners):
    first_middle = start + length/2 - 1
    answer = mid_ + diff(first_middle, num)
else:
    answer = l - min([diff(c, num) for c in corners])


#answer
print answer

