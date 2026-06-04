class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result=[]

        left,right=0, len(numbers)-1

        while left<right:
            sum=numbers[left]+numbers[right]
            print("sum",sum)
            if sum==target:
                result.append(numbers[left])
                result.append(numbers[right])
                left+=1
                right-=1
            elif sum<target:
                print("inside sum")
                left+=1
            else:
                print("Inside this")
                right-=1
            print(f"Left {left} right : {right}")
        return result