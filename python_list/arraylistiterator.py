# coding = utf-8


class ArrayListIterator(object):
    """
    Represents the list iterator for an array list.
    """
    def __init__(self, backing_store):
        """
        Set the initial state of the list iterator.
        """
        self.backing_store = backing_store
        self.mod_count = backing_store.get_mod_count()
        self.first()

    def first(self):
        """
        Resets the cursor to the beginning of the backing store.
        :return:
        """
        self.cursor = 0
        self.last_item_pos = -1

    def has_next(self):
        """
        Returns True if the iterator has a next item or False otherwise.
        :return:
        """
        return self.cursor < len(self.backing_store)

    def next(self):
        """
        Preconditions: has_next returns True.
        The list has not been modified except by this iterator's mutators.
        Returns the current item and avances the cursor. to the next item.
        :return:
        """
        if not self.has_next():
            raise ValueError("No next item in list iterator")
        if self.mod_count != self.backing_store.get_mod_count():
            raise AttributeError("Illegal modification of backing store")
        self.last_item_pos = self.cursor
        self.cursor += 1
        return self.backing_store(self.last_item_pos)

    def last(self):
        """
        Moves the cursor to the end of the backing store.
        :return:
        """
        self.cursor = len(self.backing_store)
        self.last_item_pos = -1

    def has_previous(self):
        """
        Returns True if the iterator has a previous item or False otherwis.
        :return:
        """
        return self.cursor > 0

    def previous(self):
        """
        Preconditions: has_previous returns True.
        The list has not been modified except by this iterator's mutators.
        Returns the current item and moves the cursor to the previous items.
        :return:
        """
        if not self.has_previous():
            raise ValueError("No previous item in list iterator")
        if self.mod_count != self.backing_store.get_mod_count():
            raise AttributeError("Illegal modification of backing store")
        self.cursor -= 1
        self.last_item_pos = self.cursor
        return self.backing_store(self.last_item_pos)

    def replace(self, item):
        """
        Preconditions: the current position is defined.
        The list has not been modified except by ths iterator's mutators.
        :param item:
        :return:
        """
        if self.last_item_pos == -1:
            raise AttributeError("The current position is undefined.")
        if self.mod_count != self.backing_store.get_mod_count():
            raise AttributeError("List has been modified illegally.")
        self.backing_store[self.last_item_pos] = item
        self.last_item_pos = -1

    def insert(self, item):
        """
        Preconditons: The list has not been modified except by thsi iterator's mutators.
        :param item:
        :return:
        """
        if self.mod_count != self.backing_store.get_mod_count():
            raise AttributeError("List has been modified illegally.")
        if self.last_item_pos == -1:
            self.backing_store.add(item)
        else:
            self.backing_store.insert(self.last_item_pos, item)
        self.last_item_pos = -1
        self.mod_count += 1

    def remove(self):
        """
        Preconditions: te curent position is defined.
        The list has not been modified except by this iterator's mutators
        :return:
        """
        if self.last_item_pos == -1:
            raise AttributeError("The current position is undefined.")
        if self.mod_count != self.backing_store.get_mod_count():
            raise AttributeError("List has been modified illegally.")
        item = self.backing_store.pop(self.last_item_pos)
        # If the item removed was obtained via next, move cursor back
        if self.last_item_pos < self.cursor:
            self.cursor -= 1
        self.mod_count += 1
        self.last_item_pos = -1
