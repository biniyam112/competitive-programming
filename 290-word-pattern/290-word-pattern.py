class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dict = {}
        word_dict = {}
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        for i in range(len(words)):
            if pattern[i] not in pattern_dict:
                if words[i] in word_dict:
                    return False
                pattern_dict[pattern[i]] = words[i] 
                word_dict[words[i]] = pattern[i]
            elif pattern_dict[pattern[i]] != words[i]:
                return False
        return True
                
        