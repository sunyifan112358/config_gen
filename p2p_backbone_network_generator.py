from backbone_network_generator import BackboneNetworkGenerator

class P2pBackboneNetworkGenerator(BackboneNetworkGenerator):

  def __init__(self):
    super(P2pBackboneNetworkGenerator, self).__init__()
    self.p2p_bandwidth = 20;

  def generate(self, config):
    writer = self.create_network_writer(config)
    self.write_gpu_switches(writer)
    self.write_cpu_switch(writer)
    self.write_connections(writer)

  def write_connections(self, writer):
    for i in range(0, self.num_gpu):
      for j in range(0, i):
        writer.connect('gpu-switch-' + str(i), 
            'gpu-switch-' + str(j),
            bandwidth = self.p2p_bandwidth)
      writer.connect('gpu-switch-' + str(i), 'cpu-switch',
          bandwidth = self.p2p_bandwidth)
