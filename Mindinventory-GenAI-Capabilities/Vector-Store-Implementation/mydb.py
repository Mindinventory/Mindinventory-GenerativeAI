from numpy.linalg import norm
import heapq
import numpy as np

class MydB:

  # creating my own vector database
  def __init__(self):
    self.database= {}
    self.indexes= {}

  # add vector to the database
  def insert_vector(self, id, data):
    self.database[id]= data
    self.update_index(id, data)

  # return vector
  def retrieve_vector(self, id):
    return self.database.get(id)

  # update id of the added vector
  def update_index(self, id, data1):
    for index, data2 in self.database.items():
      if id not in self.indexes:
        self.indexes[id]= {}
      self.indexes[index][id]= self.find_similiarity(data1, data2)

  # calculate cosine similiarity
  def find_similiarity(self, vector1, vector2):
    return np.dot(vector1,vector2)/(norm(vector1)*norm(vector2))

  # retrieve similiar vectors
  def find_similiar_vectors(self, input):
    buffer= []
    for id, data in self.database.items():
      buffer.append((id, self.find_similiarity(input, data)))
    heapq.heapify(buffer)
    return heapq.nlargest(1, buffer)
