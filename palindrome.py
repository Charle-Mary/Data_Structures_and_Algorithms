def isPalindrome(word):
    if len(word) == 1 or len(word) == 0:
        return True
    elif word[0] == word[-1] and isPalindrome(word[1:-1]):
        return True
    else:
        return False



print(isPalindrome('abba'))







class MyClass:
    edu = 'educative'

    @classmethod
    def classmethd(cls):
        return cls.edu

    def __init__(self, ken=None):
        self.ken = ken


clas = MyClass(5)

print(clas.ken)

print(MyClass.classmethd())