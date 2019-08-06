import numpy as np
from scipy.optimize import linear_sum_assignment
from math import log


def fit_n(crate_dims, box_dims):
    # Num. of boxes (along axis j) that fit along crate axis i, 
    # using log for summation and negated for minimization
    helper = np.vectorize(lambda i, j: -1 * log(crate_dims[i] // box_dims[j]))

    # Create matrix where entry (i,j) corresponds to fitting box axis j along crate axis i
    fit_weights = np.fromfunction(helper, (len(crate_dims), len(box_dims)), dtype=int)
    
    # Find assignment between crate and box axes that minimizes sum of 
    # corresponding matrix entries
    out_inds, in_inds = linear_sum_assignment(fit_weights)

    # Calculate number of boxes (note: using np.prod() runs into overflow issues)
    total = 1
    for (i, j) in zip(out_inds, in_inds):
        total *= crate_dims[i] // box_dims[j]
    return total

print(fit_n([180598, 125683, 146932, 158296, 171997, 204683, 193694, 216231, 177673, 169317, 216456, 220003, 165939, 205613, 152779, 177216, 128838, 126894, 210076, 148407], [1984, 2122, 1760, 2059, 1278, 2017, 1443, 2223, 2169, 1502, 1274, 1740, 1740, 1768, 1295, 1916, 2249, 2036, 1886, 2010]))