# A function that removes one occurrence of a given item from a list w/o using .pop() or .remove()
# If the item is not present in the list, output should be ‘The item is not in the list’.

def remove_item(list_items, item_to_remove):
    ''' Remove first occurrence of item from list
    Returns: if the item is in the list: list with first occurrence of item removed
    if the item is not in the list: str 'The item is not in the list'''
    if item_to_remove not in list_items:
        response_string ='The item is not in the list.'
        return response_string
    
    new_list_items = []
    list_removed_items = []
    for item in list_items:
        if item != item_to_remove:
            new_list_items.append(item)
        elif item == item_to_remove and item not in list_removed_items:
            list_removed_items.append(item)
        elif item == item_to_remove and item in list_removed_items:
            new_list_items.append(item)
    return new_list_items
    

