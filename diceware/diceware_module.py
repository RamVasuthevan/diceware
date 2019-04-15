from random import randint
from string import Template

class diceware_class(object):

    def __init__(self):
        self.word_list=self.read_word_list()
        self.value_lsts={"$W":self.word_list,"$U":[x.capitalize() for x in self.word_list],"$S":"!\"#%&'()*+,-./:;<=>?@[\\]^_`{|}~","$N":"0123456789"}


    def read_word_list(self,path: str="../diceware/word_list/sindresorhus.txt")->list:
        word_lst = []

        with open(path, "r") as f:
            word_lst = f.read().splitlines()

        return word_lst

    def create_password(self,word_lst: list=None,template:str="$U$N $U $U$S $U")->str:
        if word_lst is None:
            word_lst=self.read_word_list()

        password = template

        for key, value in self.value_lsts.items():
            password=self.replace(password,key,self.create_generator(value))

        return password

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
