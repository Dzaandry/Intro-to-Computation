def isPalindrome(s):
	"""Assumes s is a string
	   return True if letters in s form a palindrome; False
	   otherwise. Non-letters and capitalization ignored."""

	def toChars(s):
		s = s.lower()
		letters = ''

		for c in s:
			if c in 'abcdefghijklmnopqrstuvwxyz':
				letters += c
		return letters

	def isPal(s):
		if len(s) <= 1:
			return True
		else:
			return (s[0] == s[-1]) and isPal(s[1: -1])

	return isPal(toChars(s))

