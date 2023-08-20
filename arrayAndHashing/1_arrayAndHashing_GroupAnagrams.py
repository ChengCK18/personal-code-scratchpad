class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main_dict = {}
        for index, phrase in enumerate(strs):
            ordered_phrase_str = ""
            ordered_phrase_list = sorted(phrase)
            ordered_phrase_str = ordered_phrase_str.join(ordered_phrase_list)


            if(ordered_phrase_str in main_dict.keys()):
                main_dict[ordered_phrase_str].append(phrase)
            else:
                main_dict[ordered_phrase_str] = [phrase]


        result = []
        for unique_phrase in main_dict.keys():
            result.append(main_dict[unique_phrase])

        return result








