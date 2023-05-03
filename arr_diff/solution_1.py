class Solution(object):
    def findDifference(self, nums1, nums2):
        finalArr = []
        arr1 = []
        arr2 = []

        for i in nums1:
            if i not in nums2:
                if i in arr1:
                    continue
                else:    
                    arr1.append(i)

        for j in nums2:
            if j not in nums1:
                if j in arr2:
                    continue
                else:
                    arr2.append(j)

                
        finalArr.append(arr1)
        finalArr.append(arr2)

        return(finalArr)