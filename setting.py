from argparse import ArgumentParser

class Setting:

  def __init__(self):
    self._parser = ArgumentParser(
        description='Configuration file generator')
  
  def register_arguments(self):
    self._parser.add_argument('--num-cpu-mem-controller', default=2)
    self._parser.add_argument('--num-gpu', default=4)
    self._parser.add_argument('--num-cu-per-gpu', default=16, type=int)
    self._parser.add_argument('--network', default='umh', 
        choices=['umh', 'zc', 'nc'])
    self._parser.add_argument('--gm-block-size', default=64, type=int)
    self._parser.add_argument('--technology', default='pcie',
        choices=['pcie', 'p2p'])
    self._parser.add_argument('--cpu-bus-bandwidth', default=12)

  def parse_arguments(self):
    self._args = self._parser.parse_args()
    self.num_cpu_memory_controller = self._args.num_cpu_mem_controller
    self.num_gpu = self._args.num_gpu
    self.num_cu_per_gpu = self._args.num_cu_per_gpu
    self.network = self._args.network
    self.gm_block_size = self._args.gm_block_size
    self.technology = self._args.technology
    self.cpu_bus_bandwidth = self._args.cpu_bus_bandwidth
