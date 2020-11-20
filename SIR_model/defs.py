from SIR_model import Simulator

PARAMS = {
    'n_agents':1000,
    'sick_agents':100,
    'b_shape':(40,40),
    'beta': 1,
    'gamma': .1,
    'death_risk': .90,
    'disease_spread_distance':5,
    'moving_range':10,
    'time_steps':25
}

def sim(n):
    print('Sim started')
    simulator = Simulator(**PARAMS	, nr=n)
    simulator.start_sim()
    return simulator.file_to_store_data
