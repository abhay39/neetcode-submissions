class Solution:
    def isValid(self, s: str) -> bool:
        temp=[]

        if len(s)%2==1:
            return False

        for i in list(s):
            if i =='(' or i=='{' or i=='[':
                temp.append(i)

            else:
                if len(temp)==0:
                    return False
                x=temp.pop()

                if x=='(' and i!=')':
                    return False
                elif x=='{' and i!='}':
                    return False
                elif x=='[' and i!=']':
                    return False
        return len(temp)==0