def flat_generator(list_of_list):
    for item in list_of_list:
        if type(item) == list:
            for i in flat_generator(item):
                yield i
        else:
            yield item
