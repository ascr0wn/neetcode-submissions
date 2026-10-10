class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for word in strs:
            alpha_count = [0] * 26
            for character in word:
                alpha_count[ord(character) - ord("a")] += 1
            alpha_word = tuple(alpha_count)
            my_dict.setdefault(alpha_word, []).append(word)  
            # look for alpha_word, if found just append, if not found, make one, insert default value '[]' and then append.
        return list(my_dict.values())

        # instead of sorting, using an array of 26 size that counts all occurance of any character in the word.
        # not using result and count separately, built into the dict using smart programming logic!
