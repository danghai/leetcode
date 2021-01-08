class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dict_t = collections.defaultdict(int)
        for domain in cpdomains:
            count, name_domain = domain.split()
            count = int(count)
            frag = name_domain.split('.')
            for i in range(len(frag)):
                dict_t['.'.join(frag[i:])] += count
        ans = []
        for key, val in dict_t.items():
            ans.append('{} {}'.format(val, key))
        return ans
