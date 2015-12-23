from l1_l2_network_generator import L1L2NetworkGenerator
from pcie_backbone_network_generator import PcieBackboneNetworkGenerator
from p2p_backbone_network_generator import P2pBackboneNetworkGenerator
from cpu_local_network_generator import CpuLocalNetworkGenerator
from nc_l2_gm_network_generator import NcL2GmNetworkGenerator
from zc_l2_mm_network_generator import ZcL2MmNetworkGenerator
from umh_l2_gm_network_generator import UmhL2GmNetworkGenerator
from umh_gm_mm_network_generator import UmhGmMmNetworkGenerator

class NetConfigGenerator(object):

  def __init__(self):
    self.num_l2_per_gpu = 4
    self.gddr_bandwidth = 38

  def open_config_file(self):
    return open('net-config.ini', 'w')

  def generate(self):
    config = self.open_config_file()
    self.generate_l1_l2_network(config)

    if self.network == 'nc':
      self.generate_nc_l2_gm_network(config)
    elif self.network == 'zc':
      self.generate_zc_l2_mm_network(config)
    elif self.network == 'umh':
      self.generate_umh_l2_gm_network(config)
      self.generate_umh_gm_mm_network(config)
    else:
      raise Exception("Unknown network " + self.network)
    
  def generate_l1_l2_network(self, config):
    generator = L1L2NetworkGenerator()
    generator.num_gpu = self.num_gpu
    generator.num_cu_per_gpu = self.num_cu_per_gpu
    generator.num_l2_per_gpu = self.num_l2_per_gpu
    generator.generate(config)

  def generate_nc_l2_gm_network(self, config):
    generator = NcL2GmNetworkGenerator()
    generator.num_l2 = self.num_l2_per_gpu * self.num_gpu
    generator.num_l2_per_gpu = self.num_l2_per_gpu
    generator.gddr_bandwidth = self.gddr_bandwidth
    generator.generate(config)
    self.generate_backbone_network(config, 'si-net-l2-gm')

  def generate_zc_l2_mm_network(self, config):
    generator = ZcL2MmNetworkGenerator()
    generator.num_l2 = self.num_l2_per_gpu * self.num_gpu
    generator.num_l2_per_gpu = self.num_l2_per_gpu
    generator.generate(config)
    self.generate_cpu_local_network(config, 'si-net-l2-mm')
    self.generate_backbone_network(config, 'si-net-l2-mm')

  def generate_umh_l2_gm_network(self, config):
    generator = UmhL2GmNetworkGenerator()
    generator.num_l2 = self.num_l2_per_gpu * self.num_gpu
    generator.gddr_bandwidth = self.gddr_bandwidth
    generator.generate(config)

  def generate_umh_gm_mm_network(self, config):
    generator = UmhGmMmNetworkGenerator()
    generator.num_l2 = self.num_l2_per_gpu * self.num_gpu
    generator.num_l2_per_gpu = self.num_l2_per_gpu
    generator.generate(config)
    self.generate_cpu_local_network(config, 'si-net-gm-mm')
    self.generate_backbone_network(config, 'si-net-gm-mm')

  def generate_cpu_local_network(self, config, name):
    generator = CpuLocalNetworkGenerator()
    generator.num_cpu_memory_controller = self.num_cpu_memory_controller
    generator.name = name
    generator.cpu_bus_bandwidth = self.cpu_bus_bandwidth
    generator.generate(config)

  def generate_backbone_network(self, config, name):
    generator = self.get_backbone_network_generator()
    generator.num_gpu = self.num_gpu
    generator.name = name
    generator.generate(config)
      
  def get_backbone_network_generator(self):
    if self.technology == 'pcie':
      return PcieBackboneNetworkGenerator()
    elif self.technology == 'p2p':
      return P2pBackboneNetworkGenerator()
    else:
      raise Exception("Unknown technology " + self.techonology)
    

