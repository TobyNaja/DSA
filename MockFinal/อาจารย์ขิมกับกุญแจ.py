def main():
    word = input()
    true_word = ""  
    last_seen = {ch: idx for idx, ch in enumerate(word)}
    
    for i, ch in enumerate(word):
        if ch not in true_word:
            while true_word and true_word[-1] > ch and last_seen[true_word[-1]] > i:
                true_word = true_word[:-1]
            true_word += ch 
    print(true_word)
main()