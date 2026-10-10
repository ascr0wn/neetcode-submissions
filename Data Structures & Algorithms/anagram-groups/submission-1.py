class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for word in strs:
            alpha_count = [0] * 26
            for character in word:
                alpha_count[ord(character) - ord('a')] += 1
            alpha_word = tuple(alpha_count)
            if alpha_word in my_dict:
                my_dict[alpha_word].append(word)
            else:
                my_dict[alpha_word] = [word]
        return list(my_dict.values())

        # instead of sorting, using an array of 26 size that counts all occurance of any character in the word.
        # not using result and count separately, built into the dict using smart programming logic!