"""
<example>
"""

import teetool as tt  # core
from teetool import helpers  # generate sample trajectories
from teetool import visual_2d  # plot results in Mayavi

# parameters
ntraj = 50
ndim = 2

# build world
new_world = tt.World(name="Example 2D", dimension=ndim)

# add trajectories
for ntype in [1, 2]:
    cluster_name = "toy {0}".format(ntype)
    cluster_data = helpers.get_trajectories(ntype, D=ndim, N=ntraj)
    new_world.addCluster(cluster_data, cluster_name)

# overview
new_world.overview()

# model all trajectories
settings = {}
settings["model_type"] = "resample"
settings["mgaus"] = 100

new_world.buildModel(0, settings)
new_world.overview()  # overview
new_world.buildModel(1, settings)
new_world.overview()  # overview

new_world.buildLogProbality(0)
new_world.overview()  # overview
new_world.buildLogProbality(1)
new_world.overview()  # overview


#  this part is Python 2.7 [ONLY] due to Mayavi / VTK dependencies

for i in [0, 1]:
    # visuals by mayavi
    visual = visual_2d.Visual_2d(new_world)
    # visualise trajectories
    visual.plotTrajectories([i])
    # visualise intersection
    visual.plotLogProbability([i])

# visuals by mayavi
visual = visual_2d.Visual_2d(new_world)
# visualise trajectories
visual.plotTrajectories([0, 1])
# visualise intersection
visual.plotLogProbability([0, 1])

# show [ requires user input ]
visual.show()