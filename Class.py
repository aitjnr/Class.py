class Student:

    change_name = "Peter"
    change_age = 34
    add_track = "UI/UX"
    get_score = ()

    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

Bob = Student("Bob", 26, ["FE","BE"], 20.90)

print ("Formally;")
print ("Bob.name =", Bob.name)
print ("Bob.age = ", Bob.age)
print ("Bob.tracks = ", Bob.tracks)
print ("Bob.score = ", Bob.score)

#
#

Bob.change_name ="Peter"
print("After changing name,")
print("Bob.change_name = ", Bob.change_name)

Bob.change_age = 34
print("After changing age,")
print("Bob.change_age = ", Bob.change_age)

Bob.add_track ="UI/UX"
print("After adding track,")
print("Bob.add_track = ", Bob.add_track)

Bob.get_score = ()
print("After getting score,")
print("Bob.get_score = ", Bob.get_score)



