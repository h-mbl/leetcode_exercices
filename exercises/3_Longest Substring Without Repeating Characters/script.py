class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        element = {}
        for i in range(len(s)):
            for j in range(i, len(s)):
                tmp = s[i:j+1]
                longueur = len(tmp)
                tmp_set = set(tmp)
                if len(tmp_set) != longueur : break
                element[i] = longueur
        try :
            cle_plus_grande_valeur = max(element, key=element.get)
            return  element[cle_plus_grande_valeur]
        except : return 0

solution = Solution()

resultat = solution.lengthOfLongestSubstring("jxdlnaaij")
print(resultat)