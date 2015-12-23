from network_writer import NetworkWriter
class CpuLocalNetworkGenerator(object):

  def __init__(self):
    pass

  def create_network_writer(self, config):
    writer = NetworkWriter()
    writer.set_network_name(self.name)
    writer.config = config
    return writer

  def generate(self, config):
    writer = self.create_network_writer(config)
    self.write_mm(writer)
    self.write_ddr_buses(writer)
    self.connect_dram_to_ddr_bus(writer)
    self.connect_ddr_bus_to_cpu_switch(writer)

  def write_mm(self, writer):
    for i in range(0, self.num_cpu_memory_controller):
      writer.add_node('mm-' + str(i))

  def write_ddr_buses(self, writer):
    for i in range(0, self.num_cpu_memory_controller):
      writer.add_bus('ddr-bus-' + str(i), bandwidth = self.cpu_bus_bandwidth)

  def connect_dram_to_ddr_bus(self, writer):
    for i in range(0, self.num_cpu_memory_controller):
      writer.connect('ddr-bus-' + str(i), 'mm-' + str(i))

  def connect_ddr_bus_to_cpu_switch(self, writer):
    for i in range(0, self.num_cpu_memory_controller):
      writer.connect('ddr-bus-' + str(i), 'cpu-switch')
