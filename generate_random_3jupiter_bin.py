import rebound
import reboundx
import numpy as np
import os

name = "3jupiters"

bins = []
for j in range(96):
    filename = "{0}_{1}.bin".format(name, j)
    bins.append(filename)
    # Create a rebound simulation
    sim = rebound.Simulation()

    # Fixing units of G so all in AU SolarMass and year
    sim.G = 4*np.pi**2

    # Add a particle at the origin with sun mass 1 and 3 jupiter like planet
    sim.add(m=1., hash= 'Sun like')

    # Based on https://arxiv.org/pdf/0801.1368.pdf
    sim.add(primary=sim.particles[0], m=1e-3, a=5., e=0.002, inc=0.5 * np.pi / 180,
            Omega=np.random.uniform(0, 2 * np.pi), omega=np.random.uniform(0, 2. * np.pi),
            f=np.random.uniform(0, 2 * np.pi), hash=1)
    sim.add(primary=sim.particles[0], m=1e-3, a=7.25, e=0.002, inc=1.0 * np.pi / 180,
            Omega=np.random.uniform(0, 2 * np.pi), omega=np.random.uniform(0, 2. * np.pi),
            f=np.random.uniform(0, 2 * np.pi), hash=2)
    sim.add(primary=sim.particles[0], m=1e-3, a=9.5, e=0.002, inc=1.5 * np.pi / 180,
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

    # for o in sim.calculate_orbits(primary=sim.particles[0]): print(o)

with open('{0}_bin_files.txt'.format(name), 'w') as f:
    for bin in bins:
        f.write(bin)
        f.write('\n')
