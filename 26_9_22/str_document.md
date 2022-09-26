# Mutuable vs Immutuable
### Mutuable
- A mutable object can be changed after it is created
- eg. List, Set, Dictionary
### Immutable
- An immutable object cannot be changed after it is created
- eg. Numbers (int, float, bool,…), Strings, Tuples, Frozen sets

## ID and Type
### ID
- The built-in function id() returns the identity of an object as an integer and usually corresponds to the object’s location in memory
### Type
- The built-in function type() returns the type of an object<br>

Example:


        origin_str="konnichiwa "
        print(origin_str)
        print(type(origin_str))
        print(id(origin_str))

        #Adding new data into an existing string
        new_str= origin_str + "wah ko"
        print(new_str)
        print(id(new_str))

        #Replacing new data
        replaced_str= origin.replace("konnichiwa","konbanwa")
        print(replaced_str)
        print(id(replaced_str))

In this example we can check string is mutable or immutable.

The id of origin_str is not same after adding new data or after replacing with new data. We can check like this:

    id(origin_str)==id(new_str)
    id(origin_str)==id(replaced_str)

If we change the value, the id of the object will be chage. So it is immutable.

