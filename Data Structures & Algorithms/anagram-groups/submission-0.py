class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        count = 0
        result = []
        for str in strs:
            temp_str = ''.join(sorted(str))
            if temp_str in my_dict:
                temp_count = my_dict[temp_str]
                result[temp_count].append(str)
            else:
                my_dict[temp_str] = count
                result.append([str])
                count += 1
        return result