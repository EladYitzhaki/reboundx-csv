import rebound
import reboundx
import numpy as np
import os
import sys
import csv
from rebound import hash as h

full_filename = sys.argv[1] # rebound bin file
filename = os.path.splitext(full_filename)[0]

# output 1: cartisian coordinates, 2: orbital elements, 3: collisions, 4:ejection.
filename1 = "{0}.cart.csv".format(filename)
filename2 = "{0}.orb.csv".format(filename)
filename3 = "{0}.coll.csv".format(filename)
filename4 = "{0}.eject.csv".format(filename)

header = ["time"]
header.append("mass1")
header.append("hash1")
header.append("pxs1")
header.append("pys1")
header.append("pzs1")
header.append("pvxs1")
header.append("pvys1")
header.append("pvzs1")

header.append("mass2")
header.append("hash2")
header.append("pxs2")
header.append("pys2")
header.append("pzs2")
header.append("pvxs2")
header.append("pvys2")
header.append("pvzs2")

header.append("out_mass")
header.append("out_hash")
header.append("out_pxs")
header.append("out_pys")
header.append("out_pzs")
header.append("out_pvxs")
header.append("out_pvys")
header.append("out_pvzs")

with open(filename3, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)

def collision_merge_then_print(sim_pointer, collision):
    sim = sim_pointer.contents  # get simulation object from pointer
    p3 = collision.p1
    p4 = collision.p2

    pmax = max(p3, p4)
    pmin = min(p3, p4)

    p1 = sim.particles[pmin]
    p2 = sim.particles[pmax]
    print(p1, p2)


    list_at_time = [sim.t]
    list_at_time.append(p1.m)
    list_at_time.append(p1.hash.value)
    list_at_time.append(p1.x)
    list_at_time.append(p1.y)
    list_at_time.append(p1.z)
    list_at_time.append(p1.vx)
    list_at_time.append(p1.vy)
    list_at_time.append(p1.vz)

    list_at_time.append(p2.m)
    list_at_time.append(p2.hash.value)
    list_at_time.append(p2.x)
    list_at_time.append(p2.y)
    list_at_time.append(p2.z)
    list_at_time.append(p2.vx)
    list_at_time.append(p2.vy)
    list_at_time.append(p2.vz)

    invmass = (1.0 / (p1.m + p2.m))
    p1.vx = (p1.vx * p1.m + p2.vx * p2.m) * invmass
    p1.vy = (p1.vy * p1.m + p2.vy * p2.m) * invmass
    p1.vz = (p1.vz * p1.m + p2.vz * p2.m) * invmass
    p1.x = (p1.x * p1.m + p2.x * p2.m) * invmass
    p1.y = (p1.y * p1.m + p2.y * p2.m) * invmass
    p1.z = (p1.z * p1.m + p2.z * p2.m) * invmass
    p1.m = p1.m + p2.m
    p1.r = np.power(p1.r * p1.r * p1.r + p2.r * p2.r * p2.r, 1 / 3)

    list_at_time.append(p1.m)
    list_at_time.append(p1.hash.value)
    list_at_time.append(p1.x)
    list_at_time.append(p1.y)
    list_at_time.append(p1.z)
    list_at_time.append(p1.vx)
    list_at_time.append(p1.vy)
    list_at_time.append(p1.vz)

    sim.remove(p2) # remove the second particle with the higher index (p2) from the simulation

    with open(filename3, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(list_at_time)

    return 0  # dont remove here , remove above

# Create a rebound simulation
sim = rebound.Simulation(full_filename)

# Fixing units of G so all in AU SolarMass and year
sim.G = 4*np.pi**2


sim.integrator = "ias15"
# MERCURY like hybrid integrator
# sim.integrator = "mercurius"
# sim.dt = sim.particles[1].P * 0.002  # Timestep a small fraction of innermost planet's period

# Move all particles to the-center-of-momentum frame.
sim.move_to_com()

# Collision
sim.collision = "direct"
sim.collision_resolve = collision_merge_then_print

# Ejection inside the iteretions
orbs = sim.calculate_orbits(primary=sim.particles[0])

# Tides radius

# g/cm^3 =1.7*10^6 M_SUN/AU^3 ????
rho_sun = 1.4*1.7e6
rho_rock = 5.5*1.7e6
rho_gas = 1.3*1.7e6

ps = sim.particles

# r= (3*m/4*pi*rho)^(1/3)
# ps[0].r = 0.00465 # AU for the sun
ps[0].r = np.power((3/(4*np.pi)*ps[0].m/rho_sun), 1/3)
# tctl_tau was 0.04. here 15.5 years for the sun as in eq 8 in https://arxiv.org/pdf/2101.12277.pdf, insted of 1 year

for ii in range(len(orbs)):
    p = orbs[ii]
    ps[ii+1].r = np.power((3/(4*np.pi)*ps[ii+1].m/rho_gas), 1/3)

# Tides (weak tides)
rebx = reboundx.Extras(sim)
tides = rebx.load_force("tides_constant_time_lag")
rebx.add_force(tides)

# under the assumptions of Lu et. al (2023) it is only ok for synchronized circular orbit, of only one plant...
# from https://github.com/dtamayo/reboundx/blob/master/ipython_examples/TidesSpinPseudoSynchronization.ipynb
stellar_Q = 1e6
planet_Q = 1e4

ps[0].params["tctl_k2"] = 0.03
ps[0].params["tctl_tau"] = 1 / (2 * stellar_Q * ps[1].n)
for ij in range(len(orbs)):
    # p = orbs[ij]
    ps[ij+1].r = np.power((3/(4*np.pi)*ps[ij+1].m/rho_gas), 1/3)
    ps[ij+1].params["tctl_k2"] = 0.03
    ps[ij+1].params["tctl_tau"] = 1 / (2 * planet_Q * ps[ij+1].n)

# Integrate for 10My and save every 100y
# write to csv file separated colloums

header = ["time"]
pp = sim.particles
orbs = sim.calculate_orbits(primary=sim.particles[0])
for p in range(len(pp)):
    header.append("mass{0}".format(p))
    header.append("hash{0}".format(p))
    header.append("pxs{0}".format(p))
    header.append("pys{0}".format(p))
    header.append("pzs{0}".format(p))
    header.append("pvxs{0}".format(p))
    header.append("pvys{0}".format(p))
    header.append("pvzs{0}".format(p))
with open(filename1, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)

header = ["time"]
for o in range(len(orbs)):
    header.append("a{0}".format(o+1))
    header.append("e{0}".format(o+1))
    header.append("inc{0}".format(o+1))
    header.append("Omega{0}".format(o+1))
    header.append("omega{0}".format(o+1))
    header.append("f{0}".format(o+1))

with open(filename2, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)

header = ["time"]
header.append("mass")
header.append("distance")
header.append("hash")
header.append("pxs")
header.append("pys")
header.append("pzs")
header.append("pvxs")
header.append("pvys")
header.append("pvzs")

with open(filename4, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)

## Integrate for 100My time units
for ik in range(1000001):
    sim.integrate(ik*100.)

    # Will eject only one at a time
    eject = 0
    # Ejection
    orbs = sim.calculate_orbits(primary=sim.particles[0])
    for jj in range(len(orbs)):
        p = orbs[jj]
        if p.a < 0 and eject == 0:
            # print("particle {} is unbound".format(jj + 1))
            p0 = sim.particles[0]
            p1 = sim.particles[jj + 1]
            dp = p0 - p1  # Calculates the coponentwise difference between particles
            distance = np.sqrt(dp.x * dp.x + dp.y * dp.y + dp.z * dp.z)
            if distance > 1000:
                # print("the unbound particle is {0:5.2f}AU apart of the main star".format(distance))
                list_at_time = [sim.t]
                list_at_time.append(p1.m)
                list_at_time.append(distance)
                list_at_time.append(p1.hash.value)
                list_at_time.append(p1.x)
                list_at_time.append(p1.y)
                list_at_time.append(p1.z)
                list_at_time.append(p1.vx)
                list_at_time.append(p1.vy)
                list_at_time.append(p1.vz)

                with open(filename4, 'a') as file:
                    writer = csv.writer(file)
                    writer.writerow(list_at_time)

                # to do eject look at the example in API
                sim.remove(jj+1)
                sim.move_to_com()
                eject = 1
            # else:
                # print("the unbound particle is {0:5.2f}AU apart of the main star".format(distance))

    orbs = sim.calculate_orbits(primary=sim.particles[0])
    pp = sim.particles
    time = sim.t

    list_at_time = [time]
    for p in pp:
        list_at_time.append(round(p.m,5))
        list_at_time.append(p.hash.value)
        list_at_time.append(round(p.x,5))
        list_at_time.append(round(p.y,5))
        list_at_time.append(round(p.z,5))
        list_at_time.append(round(p.vx,5))
        list_at_time.append(round(p.vy,5))
        list_at_time.append(round(p.vz,5))

    with open(filename1, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(list_at_time)

    list_at_time = [time]
    for o in orbs:
        list_at_time.append(round(o.a,5))
        list_at_time.append(round(o.e,5))
        list_at_time.append(round(o.inc,5)) # in rad ,for deg *180/np.pi
        list_at_time.append(round(o.Omega,5))
        list_at_time.append(round(o.omega,5))
        list_at_time.append(round(o.f,5))

    with open(filename2, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(list_at_time)
        
filename5 = "{0}.time{1}.bin".format(filename, sim.t)
sim.automateSimulationArchive(filename5, interval=1, deletefile=True)
sim.integrate(0)
