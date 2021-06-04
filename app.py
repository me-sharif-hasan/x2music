from spleeter.separator import Separator

# Using embedded configuration.
separator = Separator('spleeter:2stems')
separator.separate_to_file('mc.mp3', 'auo')