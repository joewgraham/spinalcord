from netpyne import specs, sim
import colorcet as cc
# DOCUMENTATION ----------------------------------------------------------------
''' Script generated with NetPyNE-UI. Please visit:
    - https://www.netpyne.org
    - https://github.com/MetaCell/NetPyNE-UI
'''

# SCRIPT =======================================================================
netParams = specs.NetParams()
simConfig = specs.SimConfig()

netParams.propVelocity = 100.0    # propagation velocity (um/ms)
netParams.probLengthConst = 100 #150.0 # length constant for conn probability (um)
#netParams.defaultThreshold = -20

# SINGLE VALUE ATTRIBUTES ------------------------------------------------------

# NETWORK ATTRIBUTES -----------------------------------------------------------
netParams.popParams['LF1'] = {
    "cellModel": "",
    "cellType": "mn_s",
    "numCells": 100,
    "xRange": [
        -200,
        -300
    ],
    "yRange": [
        0,
        10000
    ],
    "zRange": [
        0,
        100
    ],
    "pop": "LF",
    "xnormRange": [
        -2.0,
        -3.0
    ],
    "ynormRange": [
        0.0,
        100.0
    ],
    "znormRange": [
        0.0,
        1.0
    ]
}



netParams.popParams['LF2'] = {
    "cellModel": "",
    "cellType": "mn_s",
    "numCells": 100,
    "xRange": [
        -200,
        -300
    ],
    "yRange": [
        5000,
        15000
    ],
    "zRange": [
        0,
        100
    ],
    "pop": "LF",
    "xnormRange": [
        -2.0,
        -3.0
    ],
    "ynormRange": [
        0.0,
        100.0
    ],
    "znormRange": [
        0.0,
        1.0
    ]
}



netParams.popParams['LF3'] = {
    "cellModel": "",
    "cellType": "mn_s",
    "numCells": 100,
    "xRange": [
        -200,
        -300
    ],
    "yRange": [
        10000,
        20000
    ],
    "zRange": [
        0,
        100
    ],
    "pop": "LF",
    "xnormRange": [
        -2.0,
        -3.0
    ],
    "ynormRange": [
        0.0,
        100.0
    ],
    "znormRange": [
        0.0,
        1.0
    ]
}




netParams.cellParams['mn_s'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {
                "diam": 10,
                "L": 10,
                "Ra": 150.0,
                "cm": 1
            },
            "mechs": {
                "hh": {
                    "gnabar": 1.2, #0.12,
                    "gkbar": 0.36, ##0.036,
                    "gl": 0.0003,
                    "el": -54.3
                }
            }
        }
    }
}



netParams.synMechParams['exc'] = {
    "mod": "Exp2Syn",
    "tau1": 0.1,
    "tau2": 1,
    "e": 0
}



netParams.connParams['mn->mn'] = {
    "preConds": {"cellType": ["mn_s"]},
    "postConds": {"cellType": ["mn_s"]},
    "synsPerConn": 1,
    "synMech": "exc",
    "probability": "10 * probLengthConst/(probLengthConst + dist_3D * 10)",
    "weight": 0.003, 
    "delay": "dist_3D/10", 
}



netParams.stimSourceParams['IClamp0'] = {
    "type": "IClamp",
    "del": 20,
    "dur": 5,
    "amp": 1
}



netParams.stimTargetParams['IClamp->gid0'] = {
    "source": "IClamp0",
    "conds": {"cellList": [0,]},
    "sec": "soma",
    "loc": 0.5
}




# NETWORK CONFIGURATION --------------------------------------------------------
simConfig.duration = 1000

simConfig.hParams = {
    "celsius": 37,
    "v_init": -65,
    "clamp_resist": 0.001
}


simConfig.recordCells = [0,]


simConfig.recordTraces = {
    "v_soma": {
        "sec": "soma",
        "loc": 0.5,
        "var": "v"
    }
}


simConfig.simLabel = "spinalcord"
simConfig.filename = "spinalcord_output"

simConfig.analysis = {
    
    "plotTraces": {
        "include": [0,],
        "showFig": True,
        "saveFig": True,
    },
    
    "iplotTraces": {
        "include": [0,],
        "showFig": True,
        "saveFig": False,
    },
    
    "plotConn": {
        #"include": ["all"],
        "feature": "weight",
        "groupBy": "cell",
        "orderBy": "y",
        "showFig": True,
        "saveFig": True,
    },
    
    "iplotConn": {
        #"include": ["all"],
        "feature": "weight",
        "groupBy": "cell",
        "orderBy": "y",
        "showFig": True,
        "saveFig": False,
    },
    
    "plot2Dnet": {
        "showFig": True,
        "saveFig": True,
        "showConns": True,
    },

    "iplot2Dnet": {
        "radius": 100,
        "showFig": True,
        "saveFig": True,
        "showConns": False,
    },
    
    "plotRaster": {
        "orderBy": "y",
        "showFig": True,
        "saveFig": True,
    },
    
    "iplotRaster": {
        "orderBy": "y",
        "showFig": True,
        "saveFig": False,
    },

}

# CREATE SIMULATE ANALYZE  NETWORK ---------------------------------------------

sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)

# sim.analysis.plotTraces(include=[0], showFig=True, saveFig=True)
# sim.analysis.iplotTraces(include=[0], showFig=True, saveFig=True)

# sim.analysis.plotConn(feature='weight', groupby='cell', orderBy='y', showFig=True, saveFig=True)
# sim.analysis.iplotConn(feature='weight', groupby='cell', orderBy='y', showFig=True, saveFig=True)

# sim.analysis.plot2Dnet(showConns=False, showFig=True, saveFig=True)
# sim.analysis.plot2Dnet(showConns=True, showFig=True, saveFig=True)
# sim.analysis.iplot2Dnet(radius=100, showConns=False, showFig=True, saveFig=True)

# sim.analysis.plotRaster(orderBy="y", showFig=True, saveFig=True)
# sim.analysis.iplotRaster(orderBy="y", showFig=True, saveFig=True)


# netpyne_geppetto.netParams = netParams
# netpyne_geppetto.simConfig = simConfig

# END SCRIPT ===================================================================
