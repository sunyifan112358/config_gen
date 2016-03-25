from backbone_network_generator import BackboneNetworkGenerator

class PcieBackboneNetworkGenerator(BackboneNetworkGenerator):

  def __init__(self):
    super(PcieBackboneNetworkGenerator, self).__init__()

  def generate(self, config):
    writer = self.create_network_writer(config)
    self.write_gpu_switches(writer)
    self.write_cpu_switch(writer)
    self.write_pcie_bus(writer)
    self.write_connections(writer)

  def write_pcie_bus(self, writer):
    writer.add_bus('pcie-bus', bandwidth = 15)

  def write_connections(self, writer):
    for i in range(0, self.num_gpu):
      writer.connect('gpu-switch-' + str(i), 'pcie-bus')
    writer.connect('cpu-switch', 'pcie-bus')
