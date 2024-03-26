def reverse_words(s):
        words = []
        spaces = [' ']
        i = 0

        while i < len(s):
            if s[i] not in spaces:
                start_word = i
                while i< len(s) and s[i] not in spaces:
                    i += 1
                words.append(s[start_word:i])
            i += 1
        return " ".join(reversed(words))