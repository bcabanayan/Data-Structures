class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # add the value to the end of the array
    self.storage.append(value)
    # bubble it up
    self._bubble_up(len(self.storage) - 1)


  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    # while at least one child node exists....(meaning there's a parent node)
    while index > 0:
      # find the parent index, using the parent index formula
      parent = (index - 1)//2
      # if the value at index is greater than the value at the parent index...
      if self.storage[index] > self.storage[parent]:
        # swap the values at each index...
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        # ...and then update the index of the value that was just swapped
        index = parent
      # otherwise, if value is not greater, then break the bubble up function
      else:
        break

  def _sift_down(self, index):
    pass
