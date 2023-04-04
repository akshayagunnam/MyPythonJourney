"""You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
For example, the word "apple" becomes "applema".
If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.
Return the final sentence representing the conversion from sentence to Goat Latin."""
class Solution:
    def toGoatLatin(self, s: str) -> str:
        vowel=["a","e","i","o","u","A","E","I","O","U"]
        s = s.split(" ")
        for i in range(len(s)):
            if s[i][0] not in vowel:
                s[i] = s[i][1:len(s[i])] + s[i][0] + "ma" + (i+1)* "a"
            else:
                s[i] = s[i] + "ma" + (i+1) * "a"
        return " ".join(s)
