import h5py
import numpy as np

def read_hdf5_to_numpy(hdf5_file_path, dataset_name):
    with h5py.File(hdf5_file_path, 'r') as hdf5_file:
        dataset = hdf5_file[dataset_name][:]
    return np.array(dataset)

# examples:
# hdf5_file_path = 'your_file.hdf5' 
# dataset_name = 'your_dataset'  
# numpy_array = read_hdf5_to_numpy(hdf5_file_path, dataset_name)
# print(numpy_array)


def save_array_to_hdf5(array, file_path, dataset_name='data'):
    filename=file_path.split('/')[-1].split('.')[0]
    with h5py.File(filename, 'w') as f:
        dset = f.create_dataset(dataset_name, data=array)

# examples:
# numpy_array = np.random.rand(10, 10)
# save_array_to_hdf5(numpy_array, 'my_array.hdf5')

def add_array(array1,array2):
    try:
        combined_array = [item for sublist in [array1, array2] for item in sublist]
    except Exception as err:
        if not array1.shape==array2.shape:
            print("size do not match!%s" % err)
            raise
    return combined_array

def add_hdf5(hdf5array,Hfile_path):
    cnt=0
    for string in hdf5array:
        if not cnt:
            Hmatrix=read_hdf5_to_numpy(string,'data')
            cnt=1
        else:
            array=read_hdf5_to_numpy(string,'data')
            Hmatrix=add_array(Hmatrix,array)
    save_array_to_hdf5(Hmatrix,Hfile_path)
        