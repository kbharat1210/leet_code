nums1 = [1,2,4,0,0,0]
nums2 = [2,5,6]

m = 3
n = 3

last = m+n-1
m = m-1
n = n-1

while m>= 0 and n>=0:
    if nums1[m]>nums2[n]:
        nums1[last] = nums1[m]
        m -= 1
    else:
        nums1[last] = nums2[n]
        n -= 1
    last -= 1

while n >=0:
    nums1[last] = nums2[n]
    n,last = n-1, last-1

print(nums1)