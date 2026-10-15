class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = []
        for str in strs:
            length = len(str)
            encoded_list.append(chr(length))
            for char in str:
                encoded_list.append(chr((ord(char) + 5) % 256))
        return "".join(encoded_list)

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        index = 0
        while index < len(s):
            limit = ord(s[index])
            index += 1
            temp = []
            for _ in range(limit):
                temp.append(chr((ord(s[index]) - 5) % 256))
                index += 1
            decoded_list.append("".join(temp))
        return decoded_list
