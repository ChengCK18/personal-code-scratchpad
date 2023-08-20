class Solution:
    def getUniqueLetterDict(self,phrase:str) -> dict:
        unique_dict = {}
        for letter in phrase:
            if(letter in unique_dict.keys()):
                unique_dict[letter]+=1
            else:
                unique_dict[letter]=1
        return unique_dict

    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return False


        s_dict = self.getUniqueLetterDict(s)
        t_dict = self.getUniqueLetterDict(t)

        s_dict_keys = s_dict.keys()
        t_dict_keys = t_dict.keys()

        unique_len = 0

        for dictKey in t_dict_keys:
            if(dictKey in s_dict_keys and t_dict[dictKey] == s_dict[dictKey]):
                unique_len+=1


        if(unique_len == len(s_dict_keys)):
            return True

        return False



