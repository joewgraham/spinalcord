import os
from netpyne import specs

cfg = specs.SimConfig()

cfg.simLabel = "spinalcord"

cfg.duration = 1000
cfg.dt = 0.025
cfg.verbose = False
cfg.recordStep = 0.1

cfg.showFig = False
cfg.saveFig = True

simNumber = 0
saveFolder = os.path.join('output', cfg.simLabel + '_' + str(simNumber))
while os.path.isdir(saveFolder):
    simNumber +=1
    saveFolder = os.path.join('output', cfg.simLabel + '_' + str(simNumber))
cfg.saveFolder = saveFolder

cfg.invertedYCoord = False
cfg.allowSelfConns = True

cfg.hParams = {"celsius": 37, "v_init": -65, "clamp_resist": 0.001}

cfg.recordCells = [0,]

cfg.recordTraces = {"v_soma": {"sec": "soma", "loc": 0.5, "var": "v"}}

