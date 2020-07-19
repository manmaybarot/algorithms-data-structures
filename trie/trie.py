# Trie Data Structure


class TrieNode:
    children: dict = {}
    ends: bool = False

    def insert(self, word):
        current = self
        for w in word:
            if w not in current.children:
                current.children[w] = TrieNode()
            current = current.children[w]
        current.ends = True

    def check(self, word):
        current = self
        for w in word:
            if w in current.children:
                current = current.children[w]
            else:
                return False
        return current.ends

    def howmanywords(self, word):
        current = self
        counter = 0
        for w in word:
            current = current.children[w]
            if current.ends:
                counter += 1
        return counter


t = TrieNode()

words = ["w", "wo", "wor", "worl", "world"]
for word in words:
    t.insert(word)

for word in words:
    print(t.howmanywords(word))
