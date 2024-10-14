#!/usr/bin/env python3

class Dog:
    approved_breeds = ["Bulldog", "Poodle", "Beagle", "Terrier", "Pug"]

    def __init__(self, name=None, breed=None):
        self._name = None
        self._breed = None
        if name is not None:
            self.name = name
        if breed is not None:
            self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value not in self.approved_breeds:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = value