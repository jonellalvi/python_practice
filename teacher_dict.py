# The dictionary will be something like:
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewher
# too!
#
# Your code goes below here.

# Create a function named most_classes that takes a dictionary of teachers and returns the teacher with the most classes.

teacher_dict = { 'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'], 'Kenneth Love': ['Python Basics', 'Python Collections']}

def most_classes(dict):
    max_count = 0
    max_teacher = ''
    for key in dict:
        tot_class =  len(dict[key])
        if tot_class > max_count:
            max_count = tot_class
            max_teacher = key
    return max_teacher   
   
print(most_classes(teacher_dict))
   
  