class Trienode:
    def __init__(self):
        self.child={}
        self.end=False
        
class Trie:

    def __init__(self):
        self.root=Trienode()
        
    def insert(self, word: str) -> None:
        
        cur = self.root
        
        for ind in word:
            if ind not in cur.child:
                cur.child[ind]=Trienode()

            cur=cur.child[ind]
        
        cur.end=True
        
    def search(self, word: str) -> bool:
        
        cur=self.root
        
        for ind in word:

            if ind not in cur.child:
                return False
            cur=cur.child[ind]

        return cur.end
                
        

    def startsWith(self, prefix: str) -> bool:
        
        cur=self.root
        
        for ind in prefix:
        
            if ind not in cur.child:
                return False
            cur=cur.child[ind]
            
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)