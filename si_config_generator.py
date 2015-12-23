class SiConfigGenerator:

  def __init__(self):
    self.num_gpu = 4
    self.num_cu_per_gpu = 16

  def get_total_num_cus(self):
    return self.num_gpu * self.num_cu_per_gpu
  
  def generate(self):
    config_file = open("si-config.ini", 'w')
    config_file.write((
        '[ Device ]\n'
        'NumComputeUnits = ' + str(self.get_total_num_cus()) + '\n'
        'Frequency = 800'
    ))

