import math


def sq_root(a):

            h=a
            l=0
            res=0
            while (l<=h):
                mid=l+(h-l)//2
                if(mid*mid==a):
                    return int(mid)
                elif (mid*mid < a):
                    l=mid+1
                    res=mid
                else:
                    h=mid-1
            return int(res)
print(sq_root(8))

