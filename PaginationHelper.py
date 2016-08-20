# TODO: complete this class
import math


class PaginationHelper:
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return math.ceil(len(self.collection) / self.items_per_page) 

    # returns the number of items on the current page.
    def page_item_count(self, page_index):
        if page_index < 0: return -1
        n = page_index + 1
        k = len(self.collection) // self.items_per_page
        if n <= k:
            return self.items_per_page
        elif n == k+1 and len(self.collection) % self.items_per_page != 0:
            return len(self.collection) % self.items_per_page
        else:
            return -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index in range(len(self.collection)):
            j = item_index + 1
        else:
            return -1
        return math.ceil(j / self.items_per_page)


b = range(1, 25)
c = PaginationHelper(b, 10)
print(c.page_count())
