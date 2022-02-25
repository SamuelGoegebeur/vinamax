import shutil
import os

def create_files(N):
# Replace the target string
    for k in range(1,N):
        with open('C:\\Users\\SamuelGGB\\go\\src\\vinamax\\MPI\\1D.go', 'r') as file :
            filedata = file.read()

        print(k)
        filedata = filedata.replace('k := 0', 'k := {}'.format(k))
        # Write the file out again
        with open('C:\\Users\\SamuelGGB\\go\\src\\vinamax\\MPI\\Systemfunction\\1D_Systemfunction_k{}.go'.format(k), 'w') as file:
            file.write(filedata)
    # Write the file out again

def create_folder(N):
    directory = 'C:\\Users\\SamuelGGB\\go\\src\\vinamax\\MPI\\Systemfunction\\'
    for k in range(1,N):
        folder = '1D_Systemfunction_k{}.out\\'.format(k)
        for _, _, filename in os.walk(directory+folder):
            shutil.move(directory+folder+filename[0],directory+'50 steps\\'+filename[0])

#create_files(50)          
#create_folder(50)


def create_folder2(N):
    directory = 'C:\\Users\\SamuelGGB\\go\\src\\vinamax\\MPI\\Systemfunction\\50 steps\\'
    for _, _, filename in os.walk(directory):
        for i in range(len(filename)):
            a = filename[i].split('@')
            print(a)
            #print(a[1])
            #print('101MNPs_of_radius30_@x'+a[1]+'xt')
            os.rename(directory+filename[i],directory+a[0]+'@x'+a[1])
            

create_folder2(2)
