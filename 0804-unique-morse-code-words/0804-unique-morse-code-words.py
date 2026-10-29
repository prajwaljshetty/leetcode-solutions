
class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse_codes = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
            "....", "..", ".---", "-.-", ".-..", "--", "-.",
            "---", ".--.", "--.-", ".-.", "...", "-", "..-",
            "...-", ".--", "-..-", "-.--", "--.."
        ]

        unique_encodings = set()

        for word in words:
            encoded_word = ""

            for character in word:
                encoded_word += morse_codes[ord(character) - ord("a")]

            unique_encodings.add(encoded_word)

        return len(unique_encodings)
