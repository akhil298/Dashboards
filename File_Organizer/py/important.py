import os
import shutil
import tkinter

path=input('Enter the path:')
files=os.listdir(path)
for file in files:
    filename,extension =os.path.splitext(file)
    extension=extension[1:]
    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
print('''



                I made your work easily :)


                                        ''')
while True:
    print('1.Show the Directries')
    print('2.Delete a Directory..?')
    print('3.Make a new Directory..?')
    print('4.Do you want to exit')

            
    choice=input()

            
    if choice=='1':
        coo=os.listdir(path)
        print(coo,sep='       ',end='.')
        print() 
                
    elif choice=='2':
        try:
            name=input("Enter the Directory Name to Delete:")
            final=os.path.join(path,name.strip())
            os.rmdir(final)
            print("Sucessfully Deleted the file")
        except FileNotFoundError as di:
            #exception problem
            print("The directory is not present")

                    
    elif choice=='3':
        try:
            name=input("Enter the Directory Name to Create:")
            os.mkdir(name.strip())
            print("Created")
        except FileExistsError as dup:
            print("The file already exists")
    elif choice=='4':
        break
