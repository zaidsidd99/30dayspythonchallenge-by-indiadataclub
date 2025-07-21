# class meta (type):
#     def __new__(self,class_name,bases,attrs):
#         print (attrs)
#         return type(class_name,bases,attrs)


# class cat(metaclass=meta):

#     x=3
#     y=8




#  Enforce a naming convention with a metaclass ?


# Step 1: Create the metaclass
class CheckNames(type):  # Must inherit from 'type' to work as a metaclass
    def __new__(cls, name, bases, attrs):
        for attr_name in attrs:
            # Skip special or private methods (like __init__)
            if not attr_name.startswith('_') and not attr_name.islower():
                raise ValueError(f"Attribute '{attr_name}' must be lowercase")
        # Create the class normally
        return super().__new__(cls, name, bases, attrs)

# Step 2: Create a class using that metaclass
class Person(metaclass=CheckNames):
    name = "Alice"    # ✅ OK
    age = 25          # ✅ OK
    # Name = "Wrong"  ❌ Uncomment this line to see the error

print("Class created successfully!")

