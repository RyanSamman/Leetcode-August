class WordDictionary:
    def __init__(self):
        self.dict = {}

    def addWord(self, word: str) -> None:
        currNode = self.dict
        for c in word:
            if c not in currNode:
                currNode[c] = {}
            currNode = currNode[c]
        currNode['\0'] = {}

    def search(self, word: str) -> bool:
        def deepSearch(currNode, word):
            if len(word) == 0: return '\0' in currNode
            if word[0] == '.': return any([deepSearch(currNode[key], word[1:]) for key in currNode.keys()])
            if word[0] in currNode: return deepSearch(currNode[word[0]], word[1:])
            return False

        return deepSearch(self.dict, word)



if __name__ == "__main__":
    obj = WordDictionary()
    x = ["addWord","addWord","addWord","addWord","addWord","addWord","addWord","addWord","search","search","search","search","search","search","search","search","search","search"]
    y = [["ran"],["rune"],["runner"],["runs"],["add"],["adds"],["adder"],["addee"],["r.n"],["ru.n.e"],["add"],["add."],["adde."],[".an."],["...s"],["....e."],["......."],["..n.r"]]
    for i in range(len(x)):
        if x[i] == "addWord":
            obj.addWord(y[i][0])
        elif x[i] == "search":
            print(obj.search(y[i][0]))
