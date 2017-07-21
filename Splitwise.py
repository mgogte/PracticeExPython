# Splitwise
#test comment
n,k = raw_input().split() #n items ordered, anna did not eat kth item
arr = raw_input().split() #prices of n items
anna_paid = raw_input().split() # anna paid this amount
anna_paid = int(anna_paid[0])
sum = 0 #stores what she should have paid
k = int(k)
for a in arr:
    sum = sum + int(a)
sum = (sum - int(arr[k]))/2



if (anna_paid - sum) == 0:
    print 'bon appetite'
else:
    print anna_paid - sum