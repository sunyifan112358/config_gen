from network_writer import NetworkWriter

class UmhL2GmNetworkGenerator(object):
  
  def __init__(self):
    pass

  def generate(self, config):

    writer = NetworkWriter()
    writer.set_network_name('si-net-l2-gm')
    writer.config = config

    self.write_network_head(writer)
    self.write_gm_nodes(writer)
    self.write_l2_nodes(writer)
    self.write_gddr_buses(writer)
    self.connect_gm_to_gddr(writer)
    self.connect_l2_to_gddr(writer)

  def write_network_head(self, writer):
    writer.write_head()

  def write_l2_nodes(self, writer):
    for i in range(self.num_l2):
      writer.add_node('l2n' + str(i))

  def write_gm_nodes(self, writer):
    for i in range(self.num_l2):
      writer.add_node('gm-' + str(i))

  def write_gddr_buses(self, writer):
    for i in range(self.num_l2):
      writer.add_bus('gddr-' + str(i), self.gddr_bandwidth)

  def connect_gm_to_gddr(self, writer):
    for i in range(self.num_l2):
      writer.connect('gm-' + str(i), 'gddr-' + str(i))

  def connect_l2_to_gddr(self, writer):
    for i in range(self.num_l2):
      writer.connect('l2n' + str(i), 'gddr-' + str(i))

