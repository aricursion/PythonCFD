import numpy
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D
from pylab import figure, axes, pie, title, show
import math

fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
ax.set_xlim(0, 2)
ax.set_ylim(0, 1)
ax.view_init(30, 225)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')


def plot2D(x, y, p, counter):
    X, Y = numpy.meshgrid(x, y)
    surf = ax.plot_surface(X, Y, p[:], rstride=1, cstride=1, cmap=cm.viridis, linewidth=0, antialiased=False)
    pyplot.pause(100)
    # pyplot.savefig("images/blah" + str(counter)+".png")


def laplace2d(p, y, dx, dy, l1norm_target):
    l1norm = 1
    counter = 1
    iterator = 0
    pn = numpy.empty_like(p)

    while l1norm > l1norm_target:
        pn = p.copy()
        p[1:-1, 1:-1] = ((dy**2 * (pn[1:-1, 2:] + pn[1:-1, 0:-2]) +
                          dx**2 * (pn[2:, 1:-1] + pn[0:-2, 1:-1])) /
                         (2 * (dx**2 + dy**2)))

        p[:, 0] = numpy.sin(6*math.pi*y)+1 # p = 0 @ x = 0
        p[:, -1] = numpy.sin(6*math.pi*y)+1 # p = y @ x = 2
        p[0, :] = p[1, :]  # dp/dy = 0 @ y = 0
        p[-1, :] = p[-2, :]  # dp/dy = 0 @ y = 1
        l1norm = (numpy.sum(numpy.abs(p[:]) - numpy.abs(pn[:])) / numpy.sum(numpy.abs(pn[:])))
        
        #pictures of every other frame
        # if iterator % 2 == 0:
        #     plot2D(x, y, p, counter)
        #     iterator = 0
        #     counter += 1
        # iterator +=1

        #pictures of all frames
        # plot2D(x, y, p, counter)
        # iterator = 0
        # counter += 1
        # iterator +=1

    return p


# variable declarations
nx = 100
ny = 100
c = 1
dx = 2 / (nx - 1)
dy = 2 / (ny - 1)


# initial conditions
p = numpy.zeros((ny, nx))  # create a XxY vector of 0's


# plotting aids
x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 1, ny)

# boundary conditions
#Basic Initial
# p[:, 0] = 0  # p = 0 @ x = 0
# p[:, -1] = y  # p = y @ x = 2
# p[0, :] = p[1, :]  # dp/dy = 0 @ y = 0
# p[-1, :] = p[-2, :]  # dp/dy = 0 @ y = 1

#Sin Curves on both y ends
p[0, :] = p[1, :]  # dp/dy = 0 @ y = 0
p[-1, :] = p[-2, :]  # dp/dy = 0 @ y = 1
p[:, 0] = numpy.sin(6*numpy.pi*y)+1.0  # p = sin(6piy)+1 @ x = 0
p[:, -1] = numpy.sin(6*numpy.pi*y)+1.0 # p = sin(6piy)+1 @ x = 2



p = laplace2d(p, y, dx, dy, 1)
plot2D(x,y,p,0)

# p = laplace2d(p, y, dx, dy, 1e-4)
# plot2D(x,y,p,0)