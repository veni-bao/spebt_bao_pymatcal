import sys
import pymatcal
import numpy as np
import h5py
from mpi4py import MPI
import re

def process_angle(angidx, configFname, config, idmap, img_subdivs):
    outFname = "angle"+ str(int(angidx*6)) + '.hdf5'
    config['angle'] += 6
    
    # Open file for MPI parallel write
    f = h5py.File(outFname, 'w', driver='mpio', comm=MPI.COMM_WORLD)
    dset = f.create_dataset('test', (NB, NA), dtype=np.float64)

    # Compute results for this angle
    for idx in range(procTaskIds_recv[0], procTaskIds_recv[1]):
        dset[idmap[idx, 1], idmap[idx, 0]] = pymatcal.get_pair_ppdf(idmap[idx, 0], idmap[idx, 1], img_subdivs, config)

    f.close()

def main(configFname):
    config = pymatcal.get_config(configFname)
    global NA, NB, idmap, img_subdivs
    NA = np.prod(config['img nvx'])
    NB = config['active dets'].shape[0]
    idmap = np.indices((NA, NB)).reshape(2, NA*NB).T
    img_subdivs = pymatcal.get_img_subdivs(config['mmpvx'], config['img nsub'])
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    nprocs = comm.Get_size()

    ntasks = np.prod(config['img nvx']) * config['active dets'].shape[0]
    procTaskIds = pymatcal.get_procIds(ntasks, nprocs)
    global procTaskIds_recv
    procTaskIds_recv = np.empty(2, dtype=np.uint32)
    comm.Scatter(procTaskIds, procTaskIds_recv, root=0)

    # Determine which angles each process should handle
    angles = np.arange(60)
    angles_per_proc = np.array_split(angles, nprocs)
    
    # Each process handles its assigned angles
    for angidx in angles_per_proc[rank]:
        process_angle(angidx, configFname, config, idmap, img_subdivs)

if __name__ == "__main__":
    main(sys.argv[1])
