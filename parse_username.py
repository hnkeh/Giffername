#Python imports.
import enchant

class UsernameParser:
    def __init__(self, username, dictionary_language):
        #Values.
        self.enchant_dictionary = enchant.Dict(dictionary_language)
        self.username = username

    #Private functions.
    #Returns word combinations.
    def _get_search_list(self, username):
        _output_list = []
        _index = 0
        #Words with more lenght than 2.
        while (len(username) - _index) > 2:

            _end_char = len(username) - _index
            #Creating combinations.        
            for _start_char in range(_index + 1):
                _current_word = username[_start_char:_end_char]
                _output_list.append(_current_word)
                _end_char += 1
                                                        
            _index += 1

        return _output_list

    #Words from username.
    def _get_wordlist(self, username):
        _output_list = []
        search_list = self._get_search_list(username)
    
        for current_search in search_list:
            #Word searching.
            if self.enchant_dictionary.check(current_search):
                _output_list.append(current_search)

        return _output_list

    #Public functions.
    #Gathering words from username and returns list.
    def get_words_in_username(self):
        
        return self._get_wordlist(self.username)

