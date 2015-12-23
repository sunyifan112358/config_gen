from network_writer import NetworkWriter

class ZcL2MmNetworkGenerator(object):
  
  def __init__(self):
    pass

  def generate(self, config):

    writer = NetworkWriter()
    writer.set_network_name('si-net-l2-mm')
    writer.config = config

    self.write_network_head(writer)
    self.write_l2_nodes(writer)
    self.connect_l2_to_gpu_switch(writer)

  def write_network_head(self, writer):
    writer.write_head()

  def write_l2_nodes(self, writer):
    for i in range(self.num_l2):
      writer.add_node('l2-' + str(i))

  def connect_l2_to_gpu_switch(self, writer):
    for i in range(self.num_l2):
      gpu_id = i / self.num_l2_per_gpu
      writer.connect('l2-' + str(i), 
          'gpu-switch-' + str(gpu_id))

