"""
init.py

Usage:
    python init.py

MPI usage:
    mpiexec -n 4 nrniv -python -mpi init.py
"""

#import matplotlib; matplotlib.use('Agg')  # to avoid graphics error in servers
import shutil
import os
from netpyne import sim


cfg, netParams = sim.readCmdLineArgs()

sim.initialize(simConfig=cfg, netParams=netParams)
sim.net.createPops()
sim.net.createCells()
sim.net.connectCells()
sim.net.addStims()
sim.setupRecording()
sim.runSim()
sim.gatherData()
sim.saveData()
sim.analysis.plotData()

# netpyne_geppetto.netParams = netParams
# netpyne_geppetto.simConfig = cfg

runFiles = ["netParams.py", "cfg.py", "init.py", "batch.py"]
for runFile in runFiles:
	shutil.copy(runFile, cfg.saveFolder)



sim.analysis.plotTraces(include=[0], showFig=cfg.showFig, saveFig=cfg.saveFig)
sim.analysis.iplotTraces(include=[0], showFig=cfg.showFig, saveFig=False)

sim.analysis.plotConn(feature='strength', includePre=['LF1', 'LF2', 'LF3'], includePost=['LF1', 'LF2', 'LF3'], groupBy='pop', orderBy='y', showFig=cfg.showFig, saveFig=cfg.saveFig)
sim.analysis.iplotConn(feature='strength', includePre=['LF1', 'LF2', 'LF3'], includePost=['LF1', 'LF2', 'LF3'], groupBy='pop', orderBy='y', showFig=cfg.showFig, saveFig=False)

sim.analysis.plotConn(feature='weight', groupBy='cell', orderBy='y', showFig=cfg.showFig, saveFig=cfg.saveFig)
sim.analysis.iplotConn(feature='weight', groupBy='cell', orderBy='y', showFig=cfg.showFig, saveFig=False)

sim.analysis.plot2Dnet(showConns=False, showFig=cfg.showFig, saveFig=cfg.saveFig)
sim.analysis.plot2Dnet(showConns=True, showFig=cfg.showFig, saveFig=cfg.saveFig)
sim.analysis.iplot2Dnet(radius=100, showConns=False, showFig=cfg.showFig, saveFig=False)

sim.analysis.plotRaster(orderBy="y", showFig=cfg.showFig, saveFig=cfg.saveFig)
sim.analysis.iplotRaster(orderBy="y", showFig=cfg.showFig, saveFig=False)