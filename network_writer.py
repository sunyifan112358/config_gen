class LinkWriter(object):
  def __init__(self):
    pass
  
  def write(self, config, source, dest, bandwidth = None):
   config.write((
      '\n[Network.' + self.name + '.Link.' + source + '-' + dest + ']\n'
      'Type = Bidirectional\n'
      'Source = ' + source + '\n'
      'Dest = ' + dest + '\n'
     )) 
   if bandwidth != None:
     config.write('Bandwidth = ' + str(bandwidth) + '\n')

class NodeWriter(object):
  def __init__(self):
    pass

  def write(self, config, node_name):
    config.write((
        '\n[Network.' + self.name + '.Node.' + node_name + ']\n'
        'Type = EndNode\n'
      ))


class SwitchWriter(object):
  def __init__(self):
    pass

  def write(self, config, switch_name):
    config.write((
        '\n[Network.' + self.name + '.Node.' + switch_name + ']\n'
        'Type = Switch\n'
      ))


class BusWriter(object):
  def __init__(self):
    pass

  def write(self, config, bus_name, bandwidth = None):
    config.write((
        '\n[Network.' + self.name + '.Node.' + bus_name + ']\n'
        'Type = Bus\n'
      ))
    if bandwidth != None:
     config.write('Bandwidth = ' + str(bandwidth) + '\n')

class NetworkWriter(object):
  def __init__(self):
    self.link_writer = LinkWriter()
    self.node_writer = NodeWriter()
    self.switch_writer = SwitchWriter()
    self.bus_writer = BusWriter()

  def set_network_name(self, name):
    self.name = name
    self.link_writer.name = name
    self.node_writer.name = name
    self.switch_writer.name = name
    self.bus_writer.name = name

  def write_head(self, fix_delay = None):
    self.config.write((
        '\n[Network.' + self.name + ']\n'
        'DefaultInputBufferSize = 4096000\n'
        'DefaultOutputBufferSize = 4096000\n'
        'DefaultBandwidth = 4096000\n'
        'Frequency = 1000\n'
      ))
    if fix_delay != None:
      self.config.write('NetFixDelay = ' + str(fix_delay) + '\n')

  def connect(self, source, dest, bandwidth = None):
    self.link_writer.write(self.config, source, dest, bandwidth)

  def add_node(self, name):
    self.node_writer.write(self.config, name)

  def add_bus(self, name, bandwidth = None):
    self.bus_writer.write(self.config, name, bandwidth)

  def add_switch(self, name):
    self.switch_writer.write(self.config, name)
 




