import random

word_bank =['rizz','ohio','sigma','tiktok','skibidi']

word = random.choice(word_bank)

guessed_word = ['_' ]* len(word)

attempts = 10

while attempts > 0:
    print('\ncurrent word:', ' '.join(guessed_word))

    guess = input('guess a word: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("great guess!")
        break

    else:
        attempts -= 1
        print("wrong guess! attempts left:", str(attempts))
              
    if '_' not in guessed_word:
        print('\ncongratulations!! you guessed the word:', word)
        break
    
else:
    print('\nyou\'ve run out of attempts! the word was:',word)




