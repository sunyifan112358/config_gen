class L1L2NetworkGenerator(object):

  def __init__(self):
    self.name = 'si-net-l1-l2'

  def generate(self, config):
    self.write_general_section(config)
    self.write_l1v_nodes(config)
    self.write_l1s_nodes(config)
    self.write_l2_nodes(config)

  def write_general_section(self, config):
    config.write((
        '\n[Network.' + self.name + ']\n'
        'DefaultInputBufferSize = 4096000\n'
        'DefaultOutputBufferSize = 4096000\n'
        'DefaultBandwidth = 4096000\n'
        'NetFixDelay = 1\n'
        'Frequency = 1000\n'
      ))

  def write_l1v_nodes(self, config):
    num_l1v = self.num_gpu * self.num_cu_per_gpu
    for i in range(0, num_l1v):
      config.write((
        '\n[Network.' + self.name + '.Node.l1v' + str(i) + ']\n'
        'Type = EndNode\n'
        ))

  def write_l1s_nodes(self, config):
    num_l1s = self.num_gpu * self.num_l2_per_gpu
    for i in range(0, num_l1s):
      config.write((
        '\n[Network.' + self.name + '.Node.l1s' + str(i) + ']\n'
        'Type = EndNode\n'
        ))

  def write_l2_nodes(self, config):
    num_l2 = self.num_gpu * self.num_l2_per_gpu
    for i in range(0, num_l2):
      config.write((
        '\n[Network.' + self.name + '.Node.l2' + str(i) + ']\n'
        'Type = EndNode\n'
        ))


    
    
