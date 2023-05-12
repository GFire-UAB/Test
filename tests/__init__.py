from . import test_modules 

modules = ['discretization', 'reconstruction', 'propagation/surface', 'propagation/crown', 'propagation/spotting', 'outputs', 'inputs', 'tests', '']

for module in modules.copy():
	modules.append('tests/'+module)

modules_dict = {'discretization': 'Discretization', 'reconstruction': 'Reconstruction', 'propagation/surface': 'Surface propagation', 'propagation/crown': 'Crown propagation', 'propagation/spotting': 'Spotting', 'outputs': 'Outputs', 'inputs': 'Inputs', 'tests': 'Tests', '': 'Organization'}

for module in modules_dict.copy():
	modules_dict['tests/' + module] = modules_dict[module]
