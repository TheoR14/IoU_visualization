import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from sympy import symbols, solve, Eq

def IoU_plot(IoU):
    """
    Plots two overlapping squares corresponding to a given Intersection over Union (IoU) value.

    Parameters
    ----------
    IoU : float
        Desired Intersection over Union value (must be between 0 and 1), used to compute the required
        displacement between the two squares.
    """
    L = 10 # size of the square
    d = symbols('d')

    # equation for IoU
    f = ((L-d)**2)/(2*L**2-(L-d)**2)

    # solve the equation to determine d
    sol = solve(Eq(f, IoU), d)

    # select only the value smaller than the edge length of the rectangle
    for v in sol:
        if v < L:
            d = v


    limit = float(d)+L+1
    fig, ax = plt.subplots()
    square1 = Rectangle((0, 0), L, L, facecolor='none', edgecolor='blue', linewidth=2, label='ground truth')
    square2 = Rectangle((d, d), L, L, facecolor='none', edgecolor='red', linewidth=2, label='prediction')
    ax.add_patch(square1)
    ax.add_patch(square2)
    ax.set_xlim(-1, limit)
    ax.set_ylim(-1, limit)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)
    plt.subplots_adjust(right=0.8)
    plt.title(f'Intersection over Union (IoU) {round(IoU*100, 1)} %')
    plt.show()
