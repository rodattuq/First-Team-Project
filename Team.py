class Team:

    def __init__(self):
	self.word = raw_input('enter a string: ')
	"this my change..! zane/zain!!"

        """ Asks for the user input for a noun and stores the noun in
        the instance variable self.word.  Remember a noun is a person,
        place, or thing. """
        # TODO by person 3
        pass

    def reverse_input(self):
	p = self.word
	p = p[::-1]
	return p
        """ Changes self.word to its reverse.  For example if
        self.word is 'apples', then it becomes 'selppa'."""
        # TODO by person 1
        pass
    
    def print_in_sentence(self):
	print 'Today I dreamt of', self.word ,'while walking on the beach.'

        """ Insert self.word in the sentence 'Today I dreamt of
        <self.word> while walking on the beach.' replacing <self.word>
        for the noun that was chosen during class construction. """
	  # TODO by person 2
        pass

t = Team()
print t.reverse_input()
t.print_in_sentence()

