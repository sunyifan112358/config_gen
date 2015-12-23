class CpuLocalNetworkGenerator(object):

  def __init__(self):
    pass

  def generate(self, config):
    self.write_ddr_buses(config)
    self.connect_dram_to_ddr_bus(config)
    self.connect_ddr_bus_to_cpu_switch(config)

  def write_ddr_buses(self, config):
    for i in range(0, self.num_cpu_memory_controller):
      config.write((
          '\n[Network.' + self.name + '.Node.ddr-bus-' + str(i) + ']\n'
          'Type = Bus\n'
          'Bandwitdh = ' + str(self.cpu_bus_bandwidth) + '\n'
          'Lanes = 1\n'
        ))

  def connect_dram_to_ddr_bus(self, config):
    for i in range(0, self.num_cpu_memory_controller):
      config.write((
          '\n[Network.' + self.name + '.Link.'
          'ddr-bus-' + str(i) + '-mm-' + str(i) + ']\n'
          'Type = Bidirectional\n'
          'Source = ddr-bus-' + str(i) + '\n'
          'Dest = mm-' + str(i) + '\n'
        ))

  def connect_ddr_bus_to_cpu_switch(self, config):
    for i in range(0, self.num_cpu_memory_controller):
      config.write((
          '\n[Network.' + self.name + '.Link.'
          'ddr-bus-' + str(i) + '-cpu-switch]\n'
          'Type = Bidirectional\n'
          'Source = ddr-bus-' + str(i) + '\n'
          'Dest = cpu-switch\n'
        ))
