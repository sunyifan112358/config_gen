from setting import Setting
from si_config_generator import SiConfigGenerator
from mem_config_generator import MemConfigGenerator
from umh_mem_config_generator import UmhMemConfigGenerator
from zc_mem_config_generator import ZcMemConfigGenerator
from nc_mem_config_generator import NcMemConfigGenerator

def main():
  settings = get_settings()
  generate_si_config(settings)
  generate_memory_config(settings)

def get_settings():
  settings = Setting()
  settings.register_arguments()
  settings.parse_arguments()
  return settings

def generate_si_config(settings):
  si_gen = SiConfigGenerator()
  si_gen.num_gpu = settings.num_gpu
  si_gen.num_cu_per_gpu = settings.num_cu_per_gpu
  si_gen.generate()

def generate_memory_config(settings):
  mem_gen = get_memory_config_generator(settings)
  mem_gen.num_cpu_memory_controller = settings.num_cpu_memory_controller
  mem_gen.set_gm_block_size = settings.gm_block_size
  mem_gen.generate()

def get_memory_config_generator(settings):
  if settings.network == 'umh':
    return UmhMemConfigGenerator()
  elif settings.network == 'zc':
    return ZcMemConfigGenerator()
  elif settings.network == 'nc':
    return NcMemConfigGenerator()
  else:
    raise Exception('Unsupported network type: ' + settings.network)

def generate_network_config():
  pass

if __name__ == "__main__":
  main()
