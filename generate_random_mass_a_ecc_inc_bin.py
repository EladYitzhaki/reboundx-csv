import rebound
import reboundx
import numpy as np
import os

def lognuniform(low=0, high=1, size=None, base=np.e):
    return np.power(base, np.random.uniform(low, high, size))

for j in range(10):
    filename = "ma_log_ei_rayleigh{}.bin".format(j)

    # Create a rebound simulation
    sim = rebound.Simulation()

    # Fixing units of G so all in AU SolarMass and year
    sim.G = 4*np.pi**2

    # Add a particle at the origin with sun mass 1 and 3 jupiter like planet
    sim.add(m=1., hash= 'Sun like')

    # Based on https://arxiv.org/pdf/astro-ph/0703160.pdf
    sim.add(primary=sim.particles[0], m=lognuniform(-1,1,None,10), a=lognuniform(-1,2,None,10),
            e=np.random.rayleigh(0.1, None), inc=np.random.rayleigh(3, None),
            Omega=np.random.uniform(0, 2 * np.pi), omega=np.random.uniform(0, 2. * np.pi),
            f=np.random.uniform(0, 2 * np.pi), hash=1)
    sim.add(primary=sim.particles[0], m=lognuniform(-1,1,None,10), a=lognuniform(-1,2,None,10),
            e=np.random.rayleigh(0.1, None), inc=np.random.rayleigh(3, None),
            Omega=np.random.uniform(0, 2 * np.pi), omega=np.random.uniform(0, 2. * np.pi),
            f=np.random.uniform(0, 2 * np.pi), hash=2)
    sim.add(primary=sim.particles[0], m=lognuniform(-1,1,None,10), a=lognuniform(-1,2,None,10),
            e=np.random.rayleigh(0.1, None), inc=np.random.rayleigh(3, None),
            Omega=np.random.uniform(0, 2 * np.pi), omega=np.random.uniform(0, 2. * np.pi),
            f=np.random.uniform(0, 2 * np.pi), hash=3)

    #radius
    # g/cm^3 =1.7*10^6 M_SUN/AU^3 ????
    rho_sun = 1.4 * 1.7e6
    rho_rock = 5.5 * 1.7e6
    rho_gas = 1.3 * 1.7e6
    # r= (3*m/4*pi*rho)^(1/3)
    ps = sim.particles
    orbs = sim.calculate_orbits(primary=sim.particles[0])
    # ps[0].r = 0.00465 # AU for the sun
    ps[0].r = np.power((3 / (4 * np.pi) * ps[0].m / rho_sun), 1 / 3)
    for i in range(len(orbs)):
        p = orbs[i]
        ps[i + 1].r = np.power((3 / (4 * np.pi) * ps[i + 1].m / rho_gas), 1 / 3)

    # Move all particles to the-center-of-momentum frame.
    sim.move_to_com()

# Integrate for 100y?
    sim.automateSimulationArchive(filename, interval=1, deletefile=True)
    sim.integrate(0)

    for o in sim.calculate_orbits(primary=sim.particles[0]): print(o)
