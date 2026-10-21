class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        keyMap = {
            c : ""
            for c in key if c != " "
        }

        cursor = 0

        for c in key :
            if c != " " and keyMap.get(c) == "" :
                keyMap[ c ] = chr(ord("a") + cursor) 
                cursor += 1

        return "".join([keyMap[c] if c != " " else " " for c in message])
        
