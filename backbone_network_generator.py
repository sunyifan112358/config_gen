from network_writer import NetworkWriter
class BackboneNetworkGenerator(object):

  def __inif__(self):
    pass

  def generate(self, config):
    pass

  def create_network_writer(self, config):
    writer = NetworkWriter();
    writer.config = config
    writer.set_network_name(self.name)
    return writer

  def write_gpu_switches(self, writer):
    for i in range(0, self.num_gpu):
      writer.add_switch('gpu-switch' + str(i))
  
  def write_cpu_switch(self, writer):
    writer.add_switch('cpu-switch')


