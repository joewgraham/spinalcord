import os
import shutil
import time
from mpi4py import MPI
from netpyne import specs
from netpyne.batch import Batch 



overwrite_latest = False

runType = 'mpi_bulletin' # Either 'hpc_slurm' or 'mpi_bulletin'

saveFolder = 'output' 
dataFolder = 'batch_data'
figFolder  = 'batch_figures'

params = specs.ODict()

params['connScale'] = [0.2, 1.0, 2]
params['connWeight'] = [0.0025, 0.003, 0.0035]

#params['IClamp0_amp'] = [0.04, 0.05, 0.06]
#params['pas_e']       = [-80, -75, -70]

#params['kamot_gbar']  = [0.01, 0.02, 0.04]
#params['kdrmot_gbar'] = [0.01, 0.02, 0.04]

#params['namot_gbar'] = [0.02, 0.2, 2.0]
#params['pas_g']       = [0.001, 0.01, 0.1]

#params['kamot_gbar']  = [0.01, 0.02, 0.04]
#params['kamot_gbar']  = [0.01, 0.02, 0.04]


def batchRun(params):

    rank = MPI.COMM_WORLD.Get_rank()
    if rank == 0:
        batchNumber = 0
        batchLabel = 'batch_' + str(batchNumber)
        tempBatchFolder = os.path.join(saveFolder, batchLabel)
        batchFolder = tempBatchFolder
        while os.path.isdir(tempBatchFolder):
            batchNumber +=1
            batchLabel = 'batch_' + str(batchNumber)
            tempBatchFolder = os.path.join(saveFolder, batchLabel)
            batchFolder = tempBatchFolder
            if overwrite_latest:
                if not os.path.isdir(tempBatchFolder):
                    batchLabel = 'batch_' + str(batchNumber - 1)
                    batchFolder = os.path.join(saveFolder, batchLabel)
                    shutil.rmtree(batchFolder)
        batchSaveFolder = os.path.join(batchFolder, dataFolder)
        if not os.path.isdir(batchSaveFolder):
            os.makedirs(batchSaveFolder, exist_ok=True)
        runFiles = ["netParams.py", "cfg.py", "init.py", "batch.py"]
        for runFile in runFiles:
            shutil.copy(runFile, batchFolder)
    else:
        time.sleep(5)
        batchNumber = 0
        batchLabel = 'batch_' + str(batchNumber)
        tempBatchFolder = os.path.join(saveFolder, batchLabel)
        batchFolder = tempBatchFolder
        while os.path.isdir(tempBatchFolder):
            batchNumber +=1
            batchLabel = 'batch_' + str(batchNumber)
            tempBatchFolder = os.path.join(saveFolder, batchLabel)
            batchFolder = tempBatchFolder
            if not os.path.isdir(tempBatchFolder):
                batchLabel = 'batch_' + str(batchNumber - 1)
                batchFolder = os.path.join(saveFolder, batchLabel)
            
        batchSaveFolder = os.path.join(batchFolder, dataFolder)



    b = Batch(params=params, cfgFile='cfg.py', netParamsFile='netParams.py')
    b.batchLabel = batchLabel 
    b.method = 'grid'
    b.saveFolder = batchSaveFolder
    
    if runType == 'hpc_slurm':
        b.runCfg = {'type': 'hpc_slurm',
                    'allocation': allocation, 
                    'walltime': '00:30:00',
                    'nodes': 4,
                    'coresPerNode': 48,
                    'email': 'joe.w.graham@gmail.com',
                    'folder': os.path.abspath('.'),
                    'script': 'init.py', 
                    'mpiCommand': 'ibrun',
                    'skip': True,
                    'custom': '#SBATCH -p skx-normal'}
    elif runType == 'mpi_bulletin':
        b.runCfg = {'type': 'mpi_bulletin', 
                    'script': 'init.py', 
                    'skip': True}
    else:
        raise Exception("Problem in batch file: runType must be either 'hpc_slurm' or 'mpi_bulletin'.")

    # Run batch simulations
    b.run()

    return batchLabel


# Main code
if __name__ == '__main__':
    
    batchLabel = batchRun(params) 
    import batch_analysis as bp
    loadedBatch = bp.plot_vtraces(batchLabel)
    out = bp.plot_traces(loadedBatch, ['iNa_soma', 'iK_soma', 'iL_soma'], cellIDs=[0, 100, 200], param_labels=None, title=None, filename=None, save=True, outputdir=None)

    os.system("say 'batch completed'")

