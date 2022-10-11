names = ['Wahko', 'Eisan', 'Mayphyo']  # iterable
def is_name_long(name):
    if len(name) > 5:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))