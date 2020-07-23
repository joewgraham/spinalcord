import os
import shutil
from netpyne import specs

overwrite_latest = False



cfg = specs.SimConfig()
cfg.simLabel = "sim"

cfg.showFig = False
cfg.saveFig = True

cfg.duration = 2000
cfg.dt = 0.025
cfg.verbose = False
cfg.recordStep = 0.1
cfg.defaultThreshold = -20

cfg.saveJson = True
cfg.saveDataInclude = ['simData', 'simConfig', 'netParams', 'net']


simNumber = 0
tempSaveFolder = os.path.join('output', cfg.simLabel + '_' + str(simNumber))
saveFolder = tempSaveFolder
while os.path.isdir(tempSaveFolder):
    simNumber +=1
    tempSaveFolder = os.path.join('output', cfg.simLabel + '_' + str(simNumber))
    saveFolder = tempSaveFolder
    if overwrite_latest:
        if not os.path.isdir(tempSaveFolder):
            saveFolder = os.path.join('output', cfg.simLabel + '_' + str(simNumber - 1))
            shutil.rmtree(saveFolder)
cfg.saveFolder = saveFolder

cfg.invertedYCoord = False
cfg.allowSelfConns = True

cfg.hParams = {"celsius": 22, "v_init": -75, "clamp_resist": 0.001}

cfg.recordCells = [0, 100, 200]

cfg.recordTraces = {"V_soma": {"sec": "soma", "loc": 0.5, "var": "v"}}
cfg.recordTraces["iK_soma"] = {"sec": "soma", "loc": 0.5, "var": "ik"}
cfg.recordTraces["iNa_soma"] = {"sec": "soma", "loc": 0.5, "var": "ina"}
cfg.recordTraces["iL_soma"] = {"sec": "soma", "loc": 0.5, "var": "i_pas"}


## Membrane properties
cfg.pas_e       = -75
cfg.pas_g       = 0.01     # Default: 0.0001
cfg.namot_gbar  = 0.2      # Default: 0.02
cfg.kamot_gbar  = 0.02     # Default: 0.02
cfg.kdrmot_gbar = 0.02     # Default: 0.02


## ICLamp0 settings
cfg.IClamp0_del   = 100
cfg.IClamp0_dur   = 100
cfg.IClamp0_amp   = 0.05
cfg.IClamp0_conds = {"cellList": [0,]}
cfg.IClamp0_sec   = "soma"
cfg.IClamp0_loc   = 0.5


## Connectivity
cfg.distScale = 10.0
cfg.connScale = 1.0
cfg.connWeight = 0.003




