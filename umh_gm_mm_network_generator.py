from network_writer import NetworkWriter

class UmhGmMmNetworkGenerator(object):
  
  def __init__(self):
    pass

  def generate(self, config):

    writer = NetworkWriter()
    writer.set_network_name('si-net-gm-mm')
    writer.config = config

    self.write_network_head(writer)
    self.write_gm_nodes(writer)
    self.connect_gm_to_gpu_switch(writer)

  def write_network_head(self, writer):
    writer.write_head()

  def write_gm_nodes(self, writer):
    for i in range(self.num_l2):
      writer.add_node('gm-' + str(i))

  def connect_gm_to_gpu_switch(self, writer):
    for i in range(self.num_l2):
      gpu_id = i / self.num_l2_per_gpu
      writer.connect('gm-' + str(i), 
          'gpu-switch-' + str(gpu_id))

