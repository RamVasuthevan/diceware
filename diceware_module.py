from random import randint
import os
from string import Template
from typing import Generator, Union, Optional, List

import sys

class diceware_class(object):

    def __init__(self, dic_path = None,format=None,numbers=None,spec_char=None):
        self.dic_path = dic_path
        self.format = format
        self.numbers = numbers
        self.spec_char= spec_char

        if self.dic_path is None:
            self.dic_path = os.path.abspath(os.path.join(os.path.abspath(__file__),"..","word_list","sindresorhus.txt"))

        if self.format is None:
            self.format = "&U&S &U&N &U &U"

        if self.numbers is None:
            self.numbers="0123456789"

        if self.spec_char is None:
            self.spec_char="!\"#%&'()*+,-./:;<=>?@[\\]^_`{|}~"

        self.word_list = self.read_word_list(dic_path)
        self.value_lsts = {"&W": self.word_list, "&U": [x.title() for x in self.word_list],"&N":self.numbers,"&S":self.spec_char}


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
