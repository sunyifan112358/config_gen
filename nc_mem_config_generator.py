from mem_config_generator import MemConfigGenerator

class NcMemConfigGenerator(MemConfigGenerator):

  def __init__(self):
    super(NcMemConfigGenerator, self).__init__()

  def generate(self):
    config = self.open_config_file()
    self.write_general_section(config)
    self.write_l1v_geometry(config)
    self.write_l1s_geometry(config)
    self.write_l2_geometry(config)
    self.write_l1v_cache(config)
    self.write_l1s_cache(config)
    self.write_l2_cache(config)
    self.write_gm(config)

  def write_l2_cache(self, config):
    num_l2 = self.num_l2_per_gpu * self.num_gpu
    for i in range(0, num_l2):
      config.write((
          '\n[Module l2n' + str(i) + ']\n'
          'Type = Cache\n'
          'Geometry = si-geo-l2\n'
          'HighNetwork = si-net-l1-l2\n'
          'HighNetworkNode = l2n' + str(i) + '\n'
          'LowNetwork = si-net-l2-gm\n'
          'LowNetworkNode = l2n' + str(i) + '\n'
          'AddressRange = ADDR DIV ' + str(self.gm_block_size) + ''
          ' MOD ' + str(self.num_l2_per_gpu) + ''
          ' EQ ' + str(i % self.num_l2_per_gpu) + '\n'
          'LowModules = '
        ))
      for j in range(0, num_l2):
        config.write('gm-' + str(j) + ' ')
      config.write('\n')

  def write_gm(self, config):
    num_l2 = self.num_l2_per_gpu * self.num_gpu
    for i in range(0, num_l2):
      config.write((
          '\n[Module gm-' + str(i) + ']\n'
          'Type = MainMemory\n'
          'BlockSize = ' + str(self.gm_block_size) + '\n'
          'Latency = ' + str(self.mm_latency) + '\n'
          'HighNetwork = si-net-l2-gm\n'
          'HighNetworkNode = gm-' + str(i) + '\n'
          'Ports = 4\n'
          'AddressRange = ADDR DIV ' + str(self.gm_block_size) + ''
          ' MOD ' + str(num_l2) + ''
          ' EQ ' + str(i) + '\n'
        ))


