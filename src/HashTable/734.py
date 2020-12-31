class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False
        dict_t = collections.defaultdict(list)
        for pair in similarPairs:
            dict_t[pair[0]].append(pair[1])
            dict_t[pair[1]].append(pair[0])
        for i in range(len(sentence1)):
            word1, word2 = sentence1[i], sentence2[i]
            if word1 != word2 and not word1 in dict_t[word2]:
                return False
        return True
