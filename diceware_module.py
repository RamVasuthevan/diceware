from random import randint
from string import Template

class diceware_class(object):

    def __init__(self):
        self.word_list=self.read_word_list()

    def read_word_list(self,path: str="diceware/word_list/sindresorhus.txt")->list:
        word_lst = []

        with open(path, "r") as f:
            word_lst = f.read().splitlines()

        return word_lst

    def create_password(self,word_lst: list=None,template:str="$W$S$W$N$N$N$W$W")->str:
        if word_lst is None:
            word_lst=self.read_word_list()

        password = template

        password=self.replace(password,"$W",self.get_word)
        password=self.replace(password,"$N",self.get_number)
        password=self.replace(password,"$S",self.get_special_character)
        return password

    def get_word(self,word_lst:list=None):
        if word_lst is None:
            word_lst=self.read_word_list()

        while True:
            yield word_lst[randint(0,len(word_lst)-1)]
        return

    def get_number(self, number="0123456789"):
        while True:
            yield number[randint(0,len(number)-1)]
        return

    def get_special_character(self, special_characters="!\"#%&'()*+,-./:;<=>?@[\\]^_`{|}~"):
        while True:
            yield special_characters[randint(0,len(special_characters)-1)]
        return

    def replace(self,template:str,old_substring:str,itr):
        while old_substring in template:
            template=template.replace(old_substring,next(itr()),1)
        return template
