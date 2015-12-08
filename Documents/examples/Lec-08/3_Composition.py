#! /usr/bin/env python

import sys, os, math

##
## CLASS DEFINITIONS
##

class Vector3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def distance_between(self, other):
        # Member function: compute the Euclidian distance between this vectory and another
        xsq = (self.x-other.x)*(self.x-other.x)
        ysq = (self.y-other.y)*(self.y-other.y)
        zsq = (self.z-other.z)*(self.z-other.z)
        return math.sqrt(xsq + ysq + zsq)

    def __str__(self):
        return "<%.3f,%.3f,%.3f>" % (self.x, self.y, self.z)

class Particle:
    def __init__(self, mass, pos, vel):
        self.mass = float(mass)
        self.position = pos
        self.velocity = vel

    def distance_between(self, other):
        # Member function: compute the Euclidian distance between this particle and another
        # Delegates that function to the Vector3D class
        return self.position.distance_between(other.position)

    def __str__(self):
        return "{mass=%f, pos=%s, vel=%s}" % (self.mass, self.position, self.velocity)

class ParticleSystem:
    def __init__(self):
        self.particles = []

    def load_from_file(self, filename):
        # Member function: Load a set of particles from a file
        fp = open(filename, "r")
        for line in fp:
            line = line.split(',')

            pos = Vector3D(line[1], line[2], line[3])
            vel = Vector3D(line[4], line[5], line[4])
            p = Particle(line[0], pos, vel)

            self.particles.append(p)

        fp.close()

    def print_particles(self, fp=sys.stdout):
        # Member function: print out the particles contained in this system to the given file
        for p in self.particles:
            fp.write("%s\n" % (str(p),))
        
        
##
## MAIN PROGRAM
##

system = ParticleSystem()
system.load_from_file("particles")

system.print_particles()

print
print "Distance of particles from %s" % (system.particles[0],)
for p in system.particles[1:]:
    dist = system.particles[0].distance_between(p)
    print "Particle %s is %f meters away." % (system.particles[0], dist)

sys.exit(0)


