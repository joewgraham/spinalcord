from netpyne import specs, sim

try:
    from __main__ import cfg
except:
    from cfg import cfg

netParams = specs.NetParams()

netParams.propVelocity = 100.0       # propagation velocity (um/ms)
netParams.probLengthConst = 100      # length constant for conn probability (um)
netParams.defaultThreshold = cfg.defaultThreshold  # voltage threshold to count as a spike (mV)



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
                "diam": 5,
                "L": 5,
                "Ra": 150.0,
                "cm": 1,
            },
            "mechs": {

                "pas": {
                    "g": cfg.pas_g,
                    "e": cfg.pas_e,
                },

                "namot": {
                    "gbar": cfg.namot_gbar,     # Default: 0.02
                },

                "kamot": {
                    "gbar": cfg.kamot_gbar,     # Default: 0.02
                },

                "kdrmot": {
                    "gbar": cfg.kdrmot_gbar,     # Default: 0.02
                },

            },
        },
    },
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
    "probability": str(cfg.distScale) + "* probLengthConst/(probLengthConst + dist_3D *" + str(cfg.distScale) + ") *" + str(cfg.connScale),
    "weight": cfg.connWeight, 
    "delay": "dist_3D/10", 
}

cfg.connScale = 1.0
cfg.distScale = 10.0

netParams.stimSourceParams['IClamp0'] = {
    "type": "IClamp",
    "del": cfg.IClamp0_del,
    "dur": cfg.IClamp0_dur,
    "amp": cfg.IClamp0_amp,
}

netParams.stimTargetParams['IClamp0->target'] = {
    "source": "IClamp0",
    "conds": cfg.IClamp0_conds,
    "sec": cfg.IClamp0_sec,
    "loc": cfg.IClamp0_loc,
}



