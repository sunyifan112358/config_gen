from network_writer import NetworkWriter
class L1L2NetworkGenerator(object):

  def __init__(self):
    self.name = 'si-net-l1-l2'

  def create_network_writer(self, config):
    writer = NetworkWriter()
    writer.set_network_name('si-net-l1-l2')
    writer.config = config
    return writer

  def generate(self, config):
    writer = self.create_network_writer(config)
    self.write_general_section(writer)
    self.write_l1v_nodes(writer)
    self.write_l1s_nodes(writer)
    self.write_l2_nodes(writer)

  def write_general_section(self, writer):
    writer.write_head(fix_delay = 1);
    writer.add_switch('l1-l2-switch')

  def write_l1v_nodes(self, writer):
    num_l1v = self.num_gpu * self.num_cu_per_gpu
    for i in range(0, num_l1v):
      writer.add_node('l1v' + str(i))
      writer.connect('l1v' + str(i), 'l1-l2-switch')

  def write_l1s_nodes(self, writer):
    num_l1s = self.num_gpu * self.num_l2_per_gpu
    for i in range(0, num_l1s):
      writer.add_node('l1s' + str(i));
      writer.connect('l1s' + str(i), 'l1-l2-switch')

  def write_l2_nodes(self, writer):
    num_l2 = self.num_gpu * self.num_l2_per_gpu
    for i in range(0, num_l2):
      writer.add_node('l2n' + str(i));
      writer.connect('l2n' + str(i), 'l1-l2-switch')


    
    
