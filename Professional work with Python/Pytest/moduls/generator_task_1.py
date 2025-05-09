def flat_generator(list_of_lists):
    for list_ in list_of_lists:
        for item in list_:
            yield item
