class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedstr = ""
        for word in strs: 
            precodestr = word + "~"
            encodedstr += precodestr
        return encodedstr

    def decode(self, s: str) -> List[str]:
        decodedlist = []
        currword =""
        for char in s:
            if char == "~":
                #if currword:
                decodedlist.append(currword)
                currword = ""
                continue
            currword += char
        if not s:
            return []
        if not decodedlist:
            return [""]
        return decodedlist
            
            
                





