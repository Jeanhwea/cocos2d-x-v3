#!/usr/bin/python
# ----------------------------------------------------------------------------
# MultiLanguage: Get the multi-language strings for console.
#
# Author: Bin Zhang
#
# License: MIT
# ----------------------------------------------------------------------------
'''
Get the multi-language strings for console.
'''

import cocos
import os
import sys
import json
import locale

def get_current_path():
    if getattr(sys, 'frozen', None):
        ret = os.path.realpath(os.path.dirname(sys.executable))
    else:
        ret = os.path.realpath(os.path.dirname(__file__))

    return ret

class MultiLanguage(object):
    CONFIG_FILE_NAME = 'strings.json'
    DEFAULT_LANGUAGE = 'en'
    instance = None

    @classmethod
    def get_available_langs(cls):
        info = cls.get_instance().cfg_info
        ret = []
        if info is not None:
            for key in info.keys():
                if isinstance(key, str):
                    ret.append(key)

        return ret

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = MultiLanguage()

        return cls.instance

    @classmethod
    def get_string(cls, key, fmt_value=None):
        fmt = cls.get_instance().get_current_string(key)
        if fmt_value is None:
            ret = fmt
        else:
            ret = fmt % fmt_value

        return ret


    @classmethod
    def set_language(cls, lang):
        cls.get_instance().set_current_language(lang)

    def __init__(self):
        cfg_file_path = os.path.join(get_current_path(), MultiLanguage.CONFIG_FILE_NAME)

        try:
            sys_lang, self.encoding = locale.getdefaultlocale()
        except:
            sys_lang = None
            self.encoding = None
            pass

        if self.encoding is None:
            self.encoding = 'utf-8'

        if sys_lang is None:
            cur_lang_key = MultiLanguage.DEFAULT_LANGUAGE
        else:
            cur_lang_key = self.get_lang_key(sys_lang)

        # get the strings info
        if os.path.isfile(cfg_file_path):
            f = open(cfg_file_path, encoding='utf-8')
            self.cfg_info = json.load(f)
            f.close()

            if cur_lang_key in self.cfg_info:
                self.cur_lang_strings = self.cfg_info[cur_lang_key]
            else:
                self.cur_lang_strings = None

            if MultiLanguage.DEFAULT_LANGUAGE in self.cfg_info:
                self.default_lang_strings = self.cfg_info[MultiLanguage.DEFAULT_LANGUAGE]
            else:
                self.default_lang_strings = None
        else:
            self.cfg_info = None
            self.cur_lang_strings = None
            self.default_lang_strings = None

    def get_lang_key(self, sys_lang):
        sys_lang_info = sys_lang.split('_')
        lang = sys_lang_info[0]
        lang = lang.lower()
        region = None
        if len(sys_lang_info) > 1:
            region = sys_lang_info[1]
            region = region.lower()

        if lang == 'zh':
            if (region is None) or (region == 'cn'):
                ret = lang
            else:
                ret = 'zh_tr'
        else:
            ret = lang

        return ret

    def has_key(self, key, strings_info):
        ret = False
        if strings_info is not None and key in strings_info:
            ret = True

        return ret

    def set_current_language(self, lang):
        if (self.cfg_info is not None) and (lang in self.cfg_info):
            self.cur_lang_strings = self.cfg_info[lang]
        else:
            cocos.Logging.warning(MultiLanguage.get_string('COCOS_WARNING_LANG_NOT_SUPPORT_FMT', lang))

    def get_encoding(self):
        return self.encoding

    def get_current_string(self, key):
        if self.cur_lang_strings is not None and key in self.cur_lang_strings:
            ret = self.cur_lang_strings[key]
        elif self.default_lang_strings is not None and key in self.default_lang_strings:
            ret = self.default_lang_strings[key]
        else:
            ret = key

        return ret
