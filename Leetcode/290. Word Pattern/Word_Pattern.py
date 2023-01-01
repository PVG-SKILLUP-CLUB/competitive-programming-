class Solution:

    def wordPattern(self, pattern: str, s: str) -> bool:

        words=s.split()

        if len(pattern )!=len(words):

            return False

        dict={}

        for i in range(len(pattern)):

            if pattern[i] in dict:

                if dict[pattern[i]]!=words[i]:

                    return False

            elif words[i] in dict.values():

                return False

            else:

                dict[pattern[i]]=words[i]

        return True
