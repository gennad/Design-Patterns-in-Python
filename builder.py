#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Example of `builder' design pattern
# Copyright (C) 2011 Radek Pazdera
 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
 
class Director:
    
    """ Controls the construction process.

    Director has a builder associated with him. Director then
    delegates building of the smaller parts to the builder and
    assembles them together.
    """
 
    __builder = None
 
    def setBuilder(self, builder):
        self.__builder = builder
 
    # The algorithm for assembling a car
    def getCar(self):
        car = Car()
 
        # First goes the body
        body = self.__builder.getBody()
        car.setBody(body)
 
        # Then engine
        engine = self.__builder.getEngine()
        car.setEngine(engine)
 
        # And four wheels
        i = 0
        while i < 4:
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)
            i += 1
 
        return car
 
# The whole product
class Car:
    
    """ The final product.

    A car is assembled by the `Director' class from
    parts made by `Builder'. Both these classes have
    influence on the resulting object.
    """
 
    def __init__(self):
        self.__wheels  = list()
        self.__engine  = None
        self.__body    = None
 
    def setBody(self, body):
        self.__body = body
 
    def attachWheel(self, wheel):
        self.__wheels.append(wheel)
 
    def setEngine(self, engine):
        self.__engine = engine
 
    def specification(self):
        print "body: %s" % self.__body.shape
        print "engine horsepower: %d" % self.__engine.horsepower
        print "tire size: %d\'" % self.__wheels[0].size
 
 
class Builder:
 
    """ Creates various parts of a vehicle.

    This class is responsible for constructing all
    the parts for a vehicle.
    """
 
    def getWheel(self): pass
    def getEngine(self): pass
    def getBody(self): pass
 
 
class JeepBuilder(Builder):
 
    """ Concrete Builder implementation.

    This class builds parts for Jeep's SUVs.
    """
 
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel
 
    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine
 
    def getBody(self):
        body = Body()
        body.shape = "SUV"
        return body
 
class NissanBuilder(Builder):
 
    """ Concrete Builder implementation.

    This class builds parts for Nissan's family cars.
    """
 
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 16
        return wheel
 
    def getEngine(self):
        engine = Engine()
        engine.horsepower = 85
        return engine
 
    def getBody(self):
        body = Body()
        body.shape = "hatchback"
        return body
 
# Car parts
class Wheel:
    size = None
 
class Engine:
    horsepower = None
 
class Body:
    shape = None
 
def main():
    jeepBuilder = JeepBuilder()
    nissanBuilder = NissanBuilder()
 
    director = Director()
 
    # Build Jeep
    print "Jeep"
    director.setBuilder(jeepBuilder)
    jeep = director.getCar()
    jeep.specification()
 
    print ""
 
    # Build Nissan
    print "Nissan"
    director.setBuilder(nissanBuilder)
    nissan = director.getCar()
    nissan.specification()
 
if __name__ == "__main__":
    main()

    Write Preview 

Parsed as Markdown Edit in fullscreen
