#Hello
#Merge two dictionaries into a single dictionary.
student={'Tushar':89,
         'Vasu':99,
        'Vrukshit':22,
        'Jigesh':27,
        'Vivek':20
        }

student2={'utsav':93,
          'sagar':57,
          'Anil':45}
student.update(student2)
print("Merge dictionary is :",student)