import numpy as np
import matplotlib.pyplot as plt

g = 9.81


# Problem 1
def calculate_buoyancy(volume, density_fluid):
    return density_fluid * volume * g


# Problem 2
def will_it_float(volume, mass):
    if mass / volume < 1000:
        return True
    else:
        return False


# Problem 3
def calculate_pressure(depth):
    return depth * g * 1000


# Problem 4
def calculate_acceleration(force, mass):
    return force / mass


# Problem 5
def calculate_angular_acceleration(torque, I):
    return torque / I


# Problem 6
def calculate_torque(F_magnitude, F_direction, radius):
    F_direction = F_direction * (np.pi / 180)
    return radius * F_magnitude * np.sin(F_direction)


# Problem 7
def calculate_moment_of_inertia(mass, radius):
    return mass * radius**2


# Problem 8
def calculate_auv_acceleration(F_magnitude, F_angle, mass, volume, thruster_distance):
    return (
        np.sqrt(
            (np.sin(F_angle) * F_magnitude + volume * g * 1000) ** 2
            + (np.cos(F_angle) * F_magnitude) ** 2
        )
        / mass
    )


# MAYBE??? SEPERATED X AND Y COMPONENTS
# np.sqrt((np.sin(F_angle) * F_magnitude + volume * g * 1000) ** 2 + (np.cos(F_angle) * F_magnitude) ** 2) / mass
# OR
# np.sqrt((F_magnitude * thruster_distance * np.sin(F_angle)) ** 2 + (volume * g * 1000) ** 2) / mass


def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, inertia, thruster_distance
):
    return (F_magnitude * thruster_distance * np.sin(F_angle)) / inertia


# Problem 9
def calculate_auv2_acceleration(T, alpha, theta, mass):
    xComp = 0
    yComp = 0

    for i in T:
        xComp = xComp + np.cos(alpha) * i
        yComp = yComp + np.sin(alpha) * i

    return np.sqrt(xComp**2 + yComp**2) / mass


def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia):
    distance = np.sqrt(L**2 + l**2)
    torque = distance * -T[0] * np.sin(alpha)
    torque = torque + distance * T[1] * np.sin(alpha)
    torque = torque + distance * -T[2] * np.sin(alpha)
    torque = torque + distance * T[3] * np.sin(alpha)
    return torque / inertia


# Problem 10
def simulate_auv2_motion(T, alpha, L, l, mass, inertia, dt, t_final, x0, y0, theta0):
    t = np.array[t_final / dt + 1]
    X = np.array[t_final / dt + 1]
    Y = np.array[t_final / dt + 1]
    theta = np.array[t_final / dt + 1]
    v = np.array[t_final / dt + 1]
    omega = np.array[t_final / dt + 1]
    a = np.array[t_final / dt + 1]

    # distance = np.sqrt(L**2 + l**2)
    t[0] = 0
    a[0] = 0
    omega[0] = 0
    theta[0] = theta0
    v[0] = 0
    X[0] = x0
    Y[0] = y0

    for i in range(1, t_final / dt + 1):
        t[i] = i / (1 / dt)
        a[i] = calculate_auv2_acceleration(T, alpha, theta[i])
        omega[i] = (
            omega[i - 1]
            + calculate_auv2_angular_acceleration(T, alpha, L, l, inertia) * dt
        )
        theta[i] = theta[i - 1] + omega[i] * dt
        v[i] = v[i - 1] + a[i] * dt
        X[i] = X[i - 1] + np.cos(theta[i]) * v[i]
        Y[i] = Y[i - 1] + np.sin(theta[i]) * v[i]

        return (t, X, Y, theta, v, omega, a)


def plot_auv2_motion(t, X, Y, theta, v, omega, a):
    plt.plot(X, Y)
    plt.show()
