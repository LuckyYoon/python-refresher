from physics import *


def plot_auv2_motion(
    Thruster_mag,
    alpha,
    L,
    l,
    mass=100,
    inertia=100,
    dt=0.1,
    t_final=1,
    x0=0,
    y0=0,
    theta0=0,
):

    fig = plt.figure(figsize=(10, 10))
    plt.plot()

    motion = simulate_auv2_motion(
        Thruster_mag, alpha, L, l, mass, inertia, dt, t_final, x0, y0, theta0
    )

    for i in range(int(t_final / dt)):
        plt.gca().add_patch(
            Rectangle(
                (motion[1][i], motion[2][i]),
                2 * l,
                2 * L,
                angle=motion[3][i],
                edgecolor="red",
                facecolor="none",
                lw=4,
            )
        )
        plt.gca().add_patch(
            Rectangle(
                (
                    motion[1][i] + np.cos(motion[3][i]) * np.sqrt(l**2 + L**2),
                    motion[2][i] + np.sin(motion[3][i]) * np.sqrt(l**2 + L**2),
                ),
                l,
                L,
                angle=motion[3][i],
                edgecolor="red",
                facecolor="none",
                lw=4,
            )
        )

    plt.savefig("plot.png")


plot_auv2_motion(
    np.array([0, 0, 300, 300]), np.pi / 4, 1, 1, t_final=1, dt=0.05, inertia=1, mass=1
)
print(
    simulate_auv2_motion(
        np.array([0, 0, 300, 300]),
        np.pi / 4,
        1,
        1,
        t_final=3,
        dt=0.05,
        inertia=1,
        mass=1,
    )
)
