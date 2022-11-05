from smmwe import level_string_to_dict, dict_to_level_string

filename = 'ma.swe'
new_author_name = 'YidaozhanYa'

save = level_string_to_dict(open(filename, 'r'))

original_author_name = save['MAIN']['AJUSTES'][0]['user']
save['MAIN']['AJUSTES'][0]['user'] = new_author_name  # Modify author name

level_signed_string = dict_to_level_string(save)

open(filename.replace('.swe', '_modified.swe'), 'w').write(level_signed_string)
print('Author name was changed from ' + original_author_name + ' to ' + new_author_name)
