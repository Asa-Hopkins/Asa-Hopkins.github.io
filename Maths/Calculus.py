import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle, ConnectionPatch
from matplotlib import ticker

plt.rcParams["svg.fonttype"] = 'none'
plt.rcParams['font.size'] = 14
plt.rcParams.update({'errorbar.capsize': 1.5})
plt.rcParams.update({'lines.markeredgewidth': 1.0})

def fmt_digits(x, pos):
    return f'{x:.6f}'

x = np.array([-3,2])
plt.xlabel('x')
plt.ylabel('y')
plt.ylim([-10,10])
plt.xlim([-2,2])
plt.yticks(np.arange(-10,12,2))
plt.hlines(xmin=-10, xmax=10, y = 0, color='black')
plt.vlines(ymin=-10, ymax = 10, x = 0, color='black')
plt.plot(x, 5*x + 2, label = "y = 5x + 2")
plt.grid('minor')
plt.legend()
plt.savefig('CalculusFig1.png', bbox_inches='tight', dpi=300)
plt.cla()

x = np.linspace(-0.1,0.1, num = 1000)
plt.xlabel('x')
plt.ylabel('y')
plt.hlines(xmin=-0.1, xmax=0.1, y = 0, color='black')
plt.vlines(ymin=-0.1, ymax =0.1, x = 0, color='black')
plt.plot(x, abs(x), label = "y = |x|")
plt.legend()
plt.savefig('CalculusFig3.png', bbox_inches='tight', dpi=300)
plt.cla()

x = np.linspace(-0.1,0.1, num = 1000)
plt.xlabel('x')
plt.ylabel('y')
plt.hlines(xmin=-0.1, xmax=0.1, y = 0, color='black', zorder=4)
plt.vlines(ymin=-0.1, ymax =0.1, x = 0, color='black', zorder=4)
plt.plot(x, abs(x), label = "y = |x|")
#plt.scatter(0,0,marker='o',color='black', s = 3, zorder=4)
#plt.rcParams.update({'markers.fillstyle': 'none'})
#plt.scatter(0,0,marker='o',color='red', s=1, zorder=4.1)
plt.legend()
plt.savefig('CalculusFig4.png', bbox_inches='tight', dpi=300)
plt.cla()


plt.xlabel('x')
plt.ylabel('y')
plt.plot([-0.1,0], [-1,-1], color='orange', label = "y = x/|x|")
plt.plot([0,0.1], [1,1], color='orange')
plt.hlines(xmin=-0.1, xmax=0.1, y = 0, color='black', zorder=5)
plt.vlines(ymin=-1, ymax =1, x = 0, color='black', zorder=5)
plt.legend()
plt.savefig('CalculusFig5.png', bbox_inches='tight', dpi=300)
plt.cla()

x = np.linspace(-2,2,1000)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, x**3 - x, label = 'y = x^3 - x')
plt.hlines(xmin=-2, xmax=2, y = 0, color='black')
plt.vlines(ymin=-6, ymax =6, x = 0, color='black')
extreme = np.array([-1/3**0.5,1/3**0.5])
plt.scatter(extreme, extreme**3 - extreme, color = 'orange', marker='x', zorder=4)
plt.legend()
plt.savefig('CalculusFig6.png', bbox_inches='tight', dpi=300)
plt.cla()

#Define the x ranges for each of the 6 figures
#I want a factor 10 zoom each time

ranges = [
    (0.0, 1.0),            # Figure 1
    (0.9, 1.0),            # Figure 2
    (0.985, 0.995),        # Figure 3 (Width 0.01)
    (0.9895, 0.9905),      # Figure 4 (Width 0.001)
    (0.98995, 0.99005),    # Figure 5 (Width 0.0001)
    (0.989995, 0.990005)   # Figure 6 (Width 0.00001)
]

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten() # Flatten to loop easily

for i in range(6):
    ax = axes[i]
    x_start, x_end = ranges[i]
    
    x = np.linspace(x_start, x_end, 2000)
    
    # This function looks awful until you zoom in 100,000x
    y = np.cos(1 / (1.0 - x)) 

    ax.plot(x, y, color='green', label = "cos(1 / (1 - x))", lw=1)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xlim(x_start, x_end)
    ax.set_ylim(-1.2, 1.2)
    if i == 0:
        ax.legend()
    if i > 2:
        ax.set_xticks((ranges[i][0], 0.99, ranges[i][1]))
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(fmt_digits))
    ax.set_title(f"Step {i+1}: Width {round(x_end-x_start, 6)}", fontsize=10, fontweight='bold')
    
    # Draw a red box indicating the next figure's range
    if i < 5:
        next_x_start, next_x_end = ranges[i+1]
        rect = Rectangle(
            (next_x_start, -1.1),           # Bottom-left of box
            next_x_end - next_x_start,      # Width
            2.2,                            # Height
            linewidth=2, edgecolor='red', facecolor='red', alpha=0.15, zorder=3
        )
        ax.add_patch(rect)
        # Add a border to the box
        ax.add_patch(Rectangle((next_x_start, -1.1), next_x_end - next_x_start, 2.2, 
                               linewidth=1.5, edgecolor='red', facecolor='none', zorder=4))

    # Draw flowchart arrows between
    if i < 5:
        # Determine if arrow is pointing right or dropping down to the next row
        if i == 2: # End of first row, move to start of second row
            xyA, xyB = (0.5, 0), (0.5, 1) # Bottom center of Fig 3 to Top center of Fig 4
        else: # Standard left-to-right
            xyA, xyB = (1, 0.5), (0, 0.5) # Right center to Left center
        
        con = ConnectionPatch(
            xyA=xyA, xyB=xyB, 
            coordsA="axes fraction", coordsB="axes fraction",
            axesA=ax, axesB=axes[i+1],
            arrowstyle="-|>,head_width=0.5,head_length=0.8",
            color="red", lw=2, zorder=5
        )
        fig.add_artist(con)
plt.tight_layout(pad=1.0)
plt.savefig('CalculusFig2.png', bbox_inches='tight', dpi=300)
