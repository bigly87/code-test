class Person:

    '''
    A Class to represnt a person.

    Attributes
    -----------
    initial_age : int

    Methoods
    --------
    what_am_i:
        check what category the given 'age' belongs to,
        based the mentioned conditions. 

    year_passes:
        increase the `age` instance variable by 1

    '''

    def __init__(self, inital_age: int):
        '''assign  `initial_age` to `age` after validating the value in`initial_age`'''
        if isinstance(inital_age, int) and (inital_age <= 103):
            self.age = inital_age
            print ("given age is in range and valid")
            print("Your current age is:"+ str (self.age))
        else:
            print("Given input must be an integer AND less/equal than 103")
            self.age = inital_age
        
 
    def what_am_i(self):
        '''check the age instance value and print suited message.
            Error message would be shown if the age value is not validate
        '''
        if isinstance(self.age, int) and (self.age <= 103):
    
            if (self.age >= 13 and self.age<18):
                print("You are a teenager.")

            elif (self.age < 13):
                print("You are young.")

            else:
                print("You are an adult.")

        else:
                print("Age value is not validate")


    def year_passes(self):
        '''if the age value is correct, increase the `age` instance variable by 1.'''
        if isinstance(self.age, int) and (self.age <= 103):
            self.age +=1 
            print("Age value incremented by one, current age is: " + str(self.age) )

        else:
            print("Age value is not validate")


#Ex1:
person1 = Person(103)
person1.what_am_i()
person1.year_passes()

#output:
#your current age is:103
#You are an adult.
#age value incremented by one, current age is: 104

#Ex2:
person1 = Person(4)
person1.what_am_i()
person1.year_passes()

#Output:
#Given age is in range and valid
#your current age is:4
#You are young.
#Age value incremented by one, current age is: 5

#Ex3:
person1 = Person(150)
person1.what_am_i()
person1.year_passes()


#Output
#Given input must be an integer AND less/equal than 103
#Age value is not validate
#Age value is not validate

#Ex4:
person1 = Person("a")
person1.what_am_i()
person1.year_passes()


#Output
#Given input must be an integer AND less/equal than 103
#Age value is not validate
#Age value is not validate



