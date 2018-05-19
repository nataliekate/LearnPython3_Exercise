formatter = "{} {} {} {} {}"
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\v\b* Grass
'''
print(formatter.format(tabby_cat, persian_cat, '\n', backslash_cat, fat_cat))