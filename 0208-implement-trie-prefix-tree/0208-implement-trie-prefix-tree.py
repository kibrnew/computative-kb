class Trienode:
    def __init__(self):
        self.child=[None for _ in range(26)]
        self.end=False
        
class Trie:

    def __init__(self):
        self.root=Trienode()
        
    def insert(self, word: str) -> None:
        
        cur = self.root
        
        for i in word:
            ind=ord(i)-ord("a")
            if not cur.child[ind]:
                cur.child[ind]=Trienode()
            cur=cur.child[ind]
        
        cur.end=True
        
    def search(self, word: str) -> bool:
        
        cur=self.root
        
        for i in word:
            ind=ord(i)-ord("a")
            if not cur.child[ind]:
                return False
            cur=cur.child[ind]

        if not cur.end:
            return False
        
        return True 
                
        

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for i in prefix:
            ind=ord(i)-ord("a")
            if not cur.child[ind]:
                return False
            cur=cur.child[ind]
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)