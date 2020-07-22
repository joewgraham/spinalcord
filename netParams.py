from netpyne import specs, sim

netParams = specs.NetParams()

netParams.propVelocity = 100.0       # propagation velocity (um/ms)
netParams.probLengthConst = 100      # length constant for conn probability (um)
#netParams.defaultThreshold = -20    # voltage threshold to count as a spike (mV)



netParams.popParams['LF1'] = {
    "cellModel": "",
    "cellType": "mn_s",
    "numCells": 100,
    "xRange": [-200, -300],
    "yRange": [0, 10000],
    "zRange": [0, 100],
    "pop": "LF",
    "xnormRange": [-2.0, -3.0],
    "ynormRange": [0.0, 100.0],
    "znormRange": [0.0, 1.0],
}



netParams.popParams['LF2'] = {
    "cellModel": "",
    "cellType": "mn_s",
    "numCells": 100,
    "xRange": [-200, -300],
    "yRange": [5000, 15000],
    "zRange": [0, 100],
    "pop": "LF",
    "xnormRange": [-2.0, -3.0],
    "ynormRange": [0.0, 100.0],
    "znormRange": [0.0, 1.0],
}



netParams.popParams['LF3'] = {
    "cellModel": "",
    "cellType": "mn_s",
    "numCells": 100,
    "xRange": [-200, -300],
    "yRange": [10000, 20000],
    "zRange": [0, 100],
    "pop": "LF",
    "xnormRange": [-2.0, -3.0],
    "ynormRange": [0.0, 100.0],
    "znormRange": [0.0, 1.0],
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




