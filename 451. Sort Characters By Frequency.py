class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        string = ""
        final = count.most_common()
        for key, value in enumerate(final):
            for i in range(int(value[1])):
                string+=value[0]
        return string
