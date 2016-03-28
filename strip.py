spam = 'SpamSpamBaconSpamEggsSpamSpam'
# The order of the characters in the string passed to strip() does not matter
# def strip(self, chars=None)
# Return a copy of the string S with leading and trailing whitespace removed.
# If chars is given and not None, remove characters in chars instead
print(spam.strip('ampS'))
print(spam.strip('mapS'))
print(spam.strip('Spam'))
