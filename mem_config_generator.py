class MemConfigGenerator(object):

  def __init__(self):
    self.num_gpu = 4
    self.num_cu_per_gpu = 16
    self.num_l2_per_gpu = self.num_cu_per_gpu / 4
    self.num_cpu_memory_controller = 2
    self.mm_block_size = 4096
    self.mm_latency = 29

    self.set_l1v_geometry()
    self.set_l1s_geometry()
    self.set_l2_geometry()
    self.set_gm_cache_geometry()

  def open_config_file(self):
    return open('mem-config.ini', 'w')

  def set_l1v_geometry(self):
    self.l1v_block_size = 64
    self.l1v_assoc = 4
    self.l1v_size = 2 ** 14
    self.l1v_latency = 1
    self.l1v_sets = self.l1v_size/self.l1v_assoc/self.l1v_block_size

  def set_l1s_geometry(self):
    self.l1s_block_size = 64
    self.l1s_assoc = 4
    self.l1s_size = 2 ** 15
    self.l1s_latency = 1
    self.l1s_sets = self.l1s_size/self.l1s_assoc/self.l1s_block_size

  def set_l2_geometry(self):
    self.l2_block_size = 64
    self.l2_assoc = 16
    self.l2_size = 2 ** 17
    self.l2_latency = 10
    self.l2_sets = self.l2_size/self.l2_assoc/self.l2_block_size

  def set_gm_cache_geometry(self):
    self.gm_block_size = 64
    self.gm_assoc = 32
    self.gm_size = 2 ** 25
    self.gm_latency = 31
    self.gm_sets = self.gm_size/self.gm_assoc/self.gm_block_size

  def set_gm_block_size(self, size):
    self.gm_block_size = size;
    self.gm_sets = self.gm_size / self.gm_assoc / self.gm_block_size

    if self.mm_block_size < self.gm_block_size:
        self.mm_block_size = self.gm_block_size

  def genreate(self):
    pass

  def write_general_section(self, config):
    config.write((
      '[General]\n'
      'Frequency = 1200\n'
    ))

  def write_l1v_geometry(self, config):
    config.write((
      '\n[CacheGeometry si-geo-vector-l1]\n'
      'Sets = ' + str(self.l1v_sets) + '\n'
      'Assoc = ' + str(self.l1v_assoc) + '\n'
      'BlockSize = ' + str(self.l1v_block_size) + '\n'
      'Latency = ' + str(self.l1v_latency) + '\n'
      'Policy = LRU\n'
      'Ports = 2\n'
    ))

  def write_l1s_geometry(self, config):
    config.write((
      '\n[CacheGeometry si-geo-scalar-l1]\n'
      'Sets = ' + str(self.l1s_sets) + '\n'
      'Assoc = ' + str(self.l1s_assoc) + '\n'
      'BlockSize = ' + str(self.l1s_block_size) + '\n'
      'Latency = ' + str(self.l1s_latency) + '\n'
      'Policy = LRU\n'
      'Ports = 2\n'
    ))

  def write_l2_geometry(self, config):
    config.write((
      '\n[CacheGeometry si-geo-l2]\n'
      'Sets = ' + str(self.l2_sets) + '\n'
      'Assoc = ' + str(self.l2_assoc) + '\n'
      'BlockSize = ' + str(self.l2_block_size) + '\n'
      'Latency = ' + str(self.l2_latency) + '\n'
      'Policy = LRU\n'
      'Ports = 2\n'
    ))

  def write_core_entry(self, config):
    for i in range(0, self.num_gpu * self.num_cu_per_gpu):
      config.write((
          '\n[Entry si-cu-' + str(i) + ']\n'
          'Arch = SouthernIslands\n'
          'ComputeUnit = ' + str(i) + '\n'
          'DataModule = si-vector-l1-' + str(i) + '\n'
          'ConstantDataModule = si-scalar-l1-' + str(i/4) + '\n'
        ))

  def write_gm_cache_geometry(self, config):
    config.write((
      '\n[CacheGeometry si-geo-gm]\n'
      'Sets = ' + str(self.gm_sets) + '\n'
      'Assoc = ' + str(self.gm_assoc) + '\n'
      'BlockSize = ' + str(self.gm_block_size) + '\n'
      'Latency = ' + str(self.gm_latency) + '\n'
      'Policy = LRU\n'
      'Ports = 4\n'
    ))

  def write_l1v_cache(self, config):
    num_l1v = self.num_gpu * self.num_cu_per_gpu
    for i in range(0, num_l1v):
      cpu_id = i / self.num_cu_per_gpu
      config.write((
        '\n[Module si-vector-l1-' + str(i) + ']\n'
        'Type = Cache\n'
        'Geometry = si-geo-vector-l1\n'
        'LowNetwork = si-net-l1-l2\n'
        'LowNetworkNode = l1v' + str(i) + '\n'
        'LowModules = '
      ))

      # Lower modules
      for j in range(0, self.num_l2_per_gpu):
        l2_id = cpu_id * self.num_l2_per_gpu + j
        config.write('l2n' + str(l2_id) + ' ')
      config.write('\n')

  def write_l1s_cache(self, config):
    num_l1s = self.num_gpu * self.num_l2_per_gpu
    for i in range(0, num_l1s):
      cpu_id = i / self.num_l2_per_gpu
      config.write((
        '\n[Module si-scalar-l1-' + str(i) + ']\n'
        'Type = Cache\n'
        'Geometry = si-geo-scalar-l1\n'
        'LowNetwork = si-net-l1-l2\n'
        'LowNetworkNode = l1s' + str(i) + '\n'
        'LowModules = '
      ))

      # Lower modules
      for j in range(0, self.num_l2_per_gpu):
        l2_id = cpu_id * self.num_l2_per_gpu + j
        config.write('l2n' + str(l2_id) + ' ')
      config.write('\n')










