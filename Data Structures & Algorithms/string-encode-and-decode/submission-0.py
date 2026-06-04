class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, encoded: str) -> List[str]:
        result = []
        i = 0

        while i < len(encoded):
            j = i

            # Find the '#'
            while encoded[j] != "#":
                j += 1

            # Length of the next string
            length = int(encoded[i:j])

            # Extract the string
            start = j + 1
            end = start + length

            result.append(encoded[start:end])

            # Move to the next encoded string
            i = end

        return result