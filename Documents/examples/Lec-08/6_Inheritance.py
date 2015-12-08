#! /usr/bin/env python

class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = { }

    def study(self, subject, hours):
        # Default, least specialized, study function
        # Can be specialized or replaced
        if subject not in self.subjects:
            self.subjects[subject] = hours
        else:
            self.subjects[subject] += hours

    def get_total_study_time(self):
        return sum(self.subjects.values())

class UndergradStudent(Student):
    def __init__(self, name):
        # Initialize the base class member variables
        Student.__init__(self, name)
        self.party_hours = 0.0

    def party(self, hours):
        self.party_hours += hours

    def get_total_party_time(self):
        return self.party_hours

    def study(self, subject, hours):
        # Override study() in the Student class to specialize the baehavior
        party_hours = hours * 0.275
        study_hours = hours * 0.725
        
        self.party(party_hours)

        # Call the base class implementation of study
        Student.study(self, subject, study_hours)

    def __str__(self):
        return "Undergrad: %s studied for %f hours and then partied for %f hours." % (self.name, self.get_total_study_time(), self.get_total_party_time())

class GraduateStudent(Student):
    def __init__(self, name, procrastination_factor=0.75):
        Student.__init__(self, name)
        self.procrastination_factor = procrastination_factor
        self.hours_of_thesis_work = 0.0

    def work_on_thesis(self, hours):
        self.hours_of_thesis_work += hours * (1.0 - self.procrastination_factor)
    
    # No specialized version of study

    def __str__(self):
        return "Graduate: %s studied for %f hours and worked for %f hours on a thesis." % (self.name, self.get_total_study_time(), self.hours_of_thesis_work)

ta = GraduateStudent("Michael Goldfarb", .337)
s1 = UndergradStudent("Derf Elwom")
s2 = UndergradStudent("Derfnia Elwom")

s1.study("ECE 364", 12.0)
s2.study("ECE 364", 10.0)
s2.study("MA 266", 2.0)

ta.study("ECE 600", 80.0)
ta.work_on_thesis(20.0)

print ta
print s1
print s2



        
