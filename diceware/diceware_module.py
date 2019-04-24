from random import randint
from string import Template
from typing import Generator, Union, Optional, List

class diceware_class(object):

    def __init__(self, dic_path: str = "../word_list/sindresorhus.txt",format=None,numbers=None,spec_char=None):
        self.dic_path = dic_path
        self.word_list = self.read_word_list(dic_path)
        self.format = format
        self.value_lsts = {"&W": self.word_list, "&U": [x.title() for x in self.word_list],"&N":"0123456789","&S":"!\"#%&'()*+,-./:;<=>?@[\\]^_`{|}~"}

        if format is not None:
            self.format = format

        if numbers is not None:
            self.value_lsts["&N"]=numbers

        if spec_char is not None:
            self.value_lsts["&S"]=spec_char


    def read_word_list(self, dict_path=None)->list:
        if dict_path is None:
            dict_path = self.dic_path

        word_lst = []

        with open(dict_path, "r") as f:
            word_lst = f.read().splitlines()

        return word_lst

    def create_password(self, word_lst: list = None)->str:
        if word_lst is None:
            word_lst = self.read_word_list(self.dic_path)

        password = self.format

        for key, val in self.value_lsts.items():
            password = self.replace(password, key, self.create_generator(val))

        return password

    def create_generator(self, defult_lst: Union[List, str]):
        def generator(lst: Optional[Union[list, str]] = None):
            if lst is None:
                lst = defult_lst
            while True:
                yield lst[randint(0, len(lst) - 1)]
            return
        return generator

    def replace(self, template: str, old_substring: str, generator):
        while old_substring in template:
            template = template.replace(old_substring, next(generator()), 1)
        return template
