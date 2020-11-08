# creates Game class
class Game:
# initialise the class with 1 attribute, the word to score
    def __init__(self, word):
# creates a table scoring each letter
        self.list1 = ["a", "e", "i", "o", "u", "l", "n", "r", "s", "t"]
        self.list2 = ["d", "g"]
        self.list3 = ["b", "c", "m", "p"]
        self.list4 = ["f", "h", "v", "w", "y"]
        self.list5 = ["k"]
        self.list8 = ["j", "x"]
        self.list10 = ["q", "z"]
        self.word = word

# method to count the score
    def calculator(self):
        split_word = list(self.word)
        score = 0

# for loop will parse through each letter in word
# and compare with the attributes of the parent class
        for i in split_word:
            if i in self.list1:
                score+=1
            elif i in self.list2:
                score+=2
            elif i in self.list3:
                score+=3
            elif i in self.list4:
                score+=4
            elif i in self.list5:
                score+=5
            elif i in self.list8:
                score+=8
            elif i in self.list10:
                score+=10
# return the score of the input
        return score

def main(self):
    # required input to calculate score
    word = input("Input the word you wish to score: \n")

    # initialise the class
    count = Game(word.lower())

    # peint the score value of the word
    print(f'Nice work!\n You scored {count.calculator()} points.')

# verify the file is in the main
if __name__ == "__main__":
    main()
