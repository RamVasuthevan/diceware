from random import randint
from string import Template
from typing import Generator, Union, Optional, List

class diceware_class(object):

    def __init__(self,dic_path: str="../diceware/word_list/sindresorhus.txt"):
        self.dic_path=dic_path
        self.word_list=self.read_word_list(dic_path)
        self.value_lsts={"$W":self.word_list,"$S":"!\"#%&'()*+,-./:;<=>?@[\\]^_`{|}~","$N":"0123456789"}

    def read_word_list(self,dict_path: str="diceware/word_list/sindresorhus.txt")->list:
        word_lst = []

        with open(dict_path, "r") as f:
            word_lst = f.read().splitlines()

        return word_lst

    def create_password(self,word_lst: list=None,template:str="$W$N $W%N $W")->str:
        if word_lst is None:
            word_lst=self.read_word_list(self.dic_path)

        password = template

        password=self.replace(password,"$W",self.create_generator(self.word_list))
        password=self.replace(password,"$N",self.create_generator("0123456789"))
        password=self.replace(password,"$S",self.create_generator("$:!#%&'()*+,-./:;<=>?@[]^_`{|}~"))
        return password

    def create_generator(self,defult_lst: Union[List,str]):
        def generator(lst:Optional[Union[list,str]]=None):
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
