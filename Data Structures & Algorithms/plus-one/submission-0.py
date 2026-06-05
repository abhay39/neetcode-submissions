class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val=""
        for i in digits:
            val+=str(i)

        print(val)
        int_val=int(val)+1
        print(int_val)
        result=str(int_val)
        return [int(ch) for ch in result]