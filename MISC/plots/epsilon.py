import numpy as np
import matplotlib.pyplot as plt


def eps(s, t_current, t_membran):
    return (1/(1-t_current/t_membran))*(np.exp(-s/t_membran) - np.exp(-s/t_current))

def plot_eps(ax, t_current, t_membran):
    x = np.linspace(0, 100, num=1000)
    print(t_current, t_membran)
    if t_current != t_membrane and t_current != 0 and t_membran != 0:
        ax.plot(x, eps(x, t_current, t_membran), label=r'$\tau_c = %.0f, \tau_m = %.0f$' % (t_current, t_membran))
        ax.legend(prop={'size':12})
    ax.set_xlabel('time in ms')
    ax.set_ylabel('current in mV')
    ax.set_ylim([0, 1.5])


if __name__ == "__main__":
    t_currents = [5, 10, 20]
    t_membranes = [6, 50, 200]

    for i, t_current in enumerate(t_currents):
        for j, t_membrane in enumerate(t_membranes):
            ax = plt.subplot2grid((len(t_currents), len(t_membranes)), (i, j))
            plot_eps(ax, t_current, t_membrane)

    plt.suptitle(r'The epsilon function $\epsilon(s)$ for different values of $\tau_c$ and $\tau_m$', fontsize=16)
    plt.show()
