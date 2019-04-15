from random import randint
from string import Template

class diceware_class(object):

    def __init__(self):
        self.word_list=self.read_word_list()
        self.value_lsts={"$W":self.word_list,"$S":"!\"#%&'()*+,-./:;<=>?@[\\]^_`{|}~","$N":"0123456789"}

    def read_word_list(self,path: str="diceware/word_list/sindresorhus.txt")->list:
        word_lst = []

        with open(path, "r") as f:
            word_lst = f.read().splitlines()

        return word_lst

    def create_password(self,word_lst: list=None,template:str="$W$N $W%N $W")->str:
        if word_lst is None:
            word_lst=self.read_word_list()

        password = template

        password=self.replace(password,"$W",self.create_generator(self.word_list))
        password=self.replace(password,"$N",self.create_generator("0123456789"))
        password=self.replace(password,"$S",self.create_generator("$:!#%&'()*+,-./:;<=>?@[]^_`{|}~"))
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

    def create_generator(self,defult_lst):
        def generator(lst=None):
            if lst is None:
                lst=defult_lst
            while True:
                yield lst[randint(0,len(lst)-1)]
            return
        return generator

    def replace(self,template:str,old_substring:str,generator):
        while old_substring in template:
            template=template.replace(old_substring,next(generator()),1)
        return template
