Morse_tab = [".-","-...","-.-.",
             "-..",".","..-.","--.","....",
             "..",".---","-.-",".-..","--",
             "-.","---",".--.","--.-",".-.",
             "...","-","..-","...-",".--",
             "-..-","-.--","--.."]
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        if len(words) == 0:
            return 0
        ans_set = set()
        for word in words:
            morsed = ""
            for c in word:
                morsed += Morse_tab[ord(c) - ord('a')]
            
            ans_set.add(morsed)
        return len(ans_set)
        