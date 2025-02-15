import numpy as np
import os

_base_ = "../../default.py"

##################################################
### NARUTO (General)
##################################################
general = dict(
    dataset  = "MP3D",
    scene    = "GdvgFV5R1Z5",
    num_iter = 5000,
)

##################################################
### Directories
##################################################
dirs = dict(
    data_dir = "data/",
    result_dir = "",
    cfg_dir = os.path.join("configs", general['dataset'], general['scene'])
)


##################################################
### Simulator
##################################################
if _base_.sim["method"] == "habitat":
    _base_.sim.update(
        habitat_cfg = os.path.join(dirs['cfg_dir'], "habitat.py")
    )

##################################################
### SLAM
##################################################
if _base_.slam["method"] == "coslam":
    _base_.slam.update(
        room_cfg        = f"{dirs['cfg_dir']}/coslam.yaml",   # Co-SLAM room configuration
        active_planning = True,                             # enable/disable active planning
        active_ray      = True,                             # enable/disable active ray sampling
        
        SLAMData_dir = None, 

        start_c2w = np.array([
            [ 1,  0,  0,  0],
            [ 0,  1,  0,  0],
            [ 0,  0,  1,  1],
            [ 0,  0,  0,  1]])
    )

##################################################
### Planner
##################################################
planner = dict(
    up_dir = np.array([0, 0, 1]), # up direction for planning pose
)

##################################################
### Visualization
##################################################
visualizer = dict(
    vis_rgbd        = True,                             # visualize RGB-D

    ### mesh related ###
    mesh_vis_freq = 500,                                # mesh save frequency
)

