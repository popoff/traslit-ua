# coding: utf8

import re


def transliterate(string):
    capital_letters = {u'А': u'A',
                       u'Б': u'B',
                       u'В': u'V',
                       u'Г': u'H',
                       u'Ґ': u'G',
                       u'Д': u'D',
                       u'Е': u'E',
                       u'З': u'Z',
                       u'И': u'Y',
                       u'І': u'I',
                       u'Ї': u'I',
                       u'Й': u'Y',
                       u'К': u'K',
                       u'Л': u'L',
                       u'М': u'M',
                       u'Н': u'N',
                       u'О': u'O',
                       u'П': u'P',
                       u'Р': u'R',
                       u'С': u'S',
                       u'Т': u'T',
                       u'У': u'U',
                       u'Ф': u'F',
                       u'Ь': u'',
                       u"'": u"", }

    capital_letters_transliterated_to_multiple_letters = {u'Є': u'Ie',
                                                          u'Ж': u'Zh',
                                                          u'Х': u'Kh',
                                                          u'Ц': u'Ts',
                                                          u'Ч': u'Ch',
                                                          u'Ш': u'Sh',
                                                          u'Щ': u'Shch',
                                                          u'Ю': u'Iu',
                                                          u'Я': u'Ia', }

    capital_letters_in_first_position = {u'Є': u'Ye',
                                         u'Ї': u'Yi',
                                         u'Й': u'Y',
                                         u'Ю': u'Yu',
                                         u'Я': u'Ya', }   

    lower_case_letters = {u'а': u'a',
                          u'б': u'b',
                          u'в': u'v',
                          u'г': u'h',
                          u'ґ': u'g',
                          u'д': u'd',
                          u'е': u'e',
                          u'є': u'ie',
                          u'ж': u'zh',
                          u'з': u'z',
                          u'и': u'y',
                          u'і': u'i',
                          u'ї': u'i',
                          u'й': u'i',
                          u'к': u'k',
                          u'л': u'l',
                          u'м': u'm',
                          u'н': u'n',
                          u'о': u'o',
                          u'п': u'p',
                          u'р': u'r',
                          u'с': u's',
                          u'т': u't',
                          u'у': u'u',
                          u'ф': u'f',
                          u'х': u'kh',
                          u'ц': u'ts',
                          u'ч': u'ch',
                          u'ш': u'sh',
                          u'щ': u'shch',
                          u'ь': u'',
                          u"'": u"",
                          u'ю': u'iu',
                          u'я': u'ia', }

    lower_case_letters_in_first_position = {u'є': u'ye',
                                              u'ї': u'yi',
                                              u'й': u'y',
                                              u'ю': u'yu',
                                              u'я': u'ya', }   


    for cyrillic_string, latin_string in capital_letters_transliterated_to_multiple_letters.items():
        string = re.sub(r'{0:s}([а-я])'.format(cyrillic_string), r'%s\1' % latin_string, string)

    for dictionary in (capital_letters, lower_case_letters):

        for cyrillic_string, latin_string in dictionary.items():
            string = string.replace(cyrillic_string, latin_string)

    for cyrillic_string, latin_string in capital_letters_transliterated_to_multiple_letters.items():
        string = string.replace(cyrillic_string, latin_string.upper())

    return string
