import reframe as rfm
import os

@rfm.simple_test
class NESOParticlesBuild(rfm.CompileOnlyRegressionTest):
    def __init__(self):
        self.descr = ('Build and run tests.')
        self.valid_systems = ['NESOParticlesReframe']
        self.valid_prog_environs = ['*']
        self.executable = 'test/testNESOParticles'
        self.sourcesdir = os.path.join(os.path.dirname(__file__), "..", "NESO-Particles", )
        self.build_system = 'CMake'

    @run_before("compile")
    def prepare_build(self):
        print("MARCO")
        print(self.current_environ)
        print(self.current_environ.modules)
        print("POLO")
        cmake_flags = self.current_environ.extras["cmake_configuration"]
        self.build_system.config_opts = cmake_flags
        self.build_system.max_concurrency = self.current_environ.extras["num_build_workers"]
        self.build_system.make_opts += ["testNESOParticles"]

    @sanity_function
    def validate_build(self):
        return True


@rfm.simple_test
class NESOParticlesTest(rfm.RunOnlyRegressionTest):
    stream_binaries = fixture(NESOParticlesBuild, scope='environment')
    valid_systems = ['*']
    valid_prog_environs = ['sycl']

    @run_before('run')
    def setup_omp_env(self):
        self.executable = os.path.join(self.stream_binaries.stagedir, 'stream')
        procinfo = self.current_partition.processor
        self.num_cpus_per_task = procinfo.num_cores
        self.env_vars = {
            'OMP_NUM_THREADS': self.num_cpus_per_task,
            'OMP_PLACES': 'cores'
        }

    @sanity_function
    def validate_solution(self):
        return sn.assert_found(r'Solution Validates', self.stdout)
