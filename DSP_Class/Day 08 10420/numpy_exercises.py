""" A short script that will contain solutions to numpy exercises
for CS444 numpy exercises. 
"""

import numpy as np

def solve_for_x(A, z):
    """ Solve the equation Ax = z and return the vector x. """
    pass

def print_rows(matrix):
    """ Print the rows of the matrix, one per line. """
    # Reminder: matrix.shape[0] contains the number of rows
    pass

def print_cols(matrix):
    """ Print the columns of the matrix, one per line. """
    # Reminder: matrix.shape[1] contains the number of columns
    pass

def squared_error(X, w, y):
    """ Return the sum squared error for the the provided linear fit. 

    returns: 
      $\sum_{x_i \in X} (x_i \times w^T - y_i)^2$
     
    Arguments: 
       X - An n x m numpy array, one data point per row. 
       w - A length m numpy array containing weights. 
       y - a length n numpy array containing target values. 

    Returns: 
      A single number representing the total squared error. 

    >>> print squared_error(np.array([[-1.0, 1.0, 0], [-2.0, 2.0, 3.0]]),\
                            np.array([1, 1, 1]), np.array([1, 2]))
    2.0

    """
    pass


def main():
    """ This function prints solutions to the questions. 
    """
    # INSTANTIATE YOUR NUMPY ARRAYS HERE FOR Q1-Q3


    # PRINT THE RESULTS OF COMPUTATIONS: 
    print "BA:\n", "REPLACE THIS WITH THE ANSWER"
    
    print "\nAB':\n", "REPLACE THIS WITH THE ANSWER"
    
    print "\nAy:", "REPLACE THIS WITH THE ANSWER"
    
    print "\ny'z:", "REPLACE THIS WITH THE ANSWER"
    

    #HINT: By default np.dot calculates the inner product. 
    #      np.outer can be used to get the outer product. 
    print "\nyz':\n", "REPLACE THIS WITH THE ANSWER"

    # Uncomment this after completing Q2:
    # x = solve_for_x(A, z)
    # print "\nx:", x
    # print "\nShould be z: ",  A.dot(x)

    # Uncomment this after completing Q3:
    # print "\nRows of A:", print_rows(A)
    # print "\nColumns of A:", print_cols(A)


if __name__ == "__main__":
    main()