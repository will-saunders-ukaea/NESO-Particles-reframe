import reframe as rfm
import reframe.utility.sanity as sn
import os


@rfm.simple_test
class NESOParticlesBuild(rfm.CompileOnlyRegressionTest):
    def __init__(self):
        self.descr = "Build and run tests."
        self.valid_systems = ["NESOParticlesReframe"]
        self.executable = "test/testNESOParticles"
        self.sourcesdir = os.path.join(
            os.path.dirname(__file__),
            "..",
            "NESO-Particles",
        )
        self.build_system = "CMake"

    @run_before("compile")
    def prepare_build(self):
        cmake_flags = self.current_environ.extras["cmake_configuration"]
        self.build_system.config_opts = cmake_flags
        self.build_system.max_concurrency = self.current_environ.extras[
            "NUM_BUILD_WORKERS"
        ]
        self.build_system.make_opts += ["testNESOParticles"]

    @sanity_function
    def validate_build(self):
        return os.path.exists(self.executable)


@rfm.simple_test
class NESOParticlesTest(rfm.RunOnlyRegressionTest):
    test_binaries = fixture(NESOParticlesBuild, scope="environment")
    valid_systems = ["NESOParticlesReframe"]
    valid_prog_environs = ["*"]

    @run_before("run")
    def setup_omp_env(self):
        self.executable = os.path.join(
            self.test_binaries.stagedir, "test", "testNESOParticles"
        )
        procinfo = self.current_partition.processor
        self.num_tasks = self.current_environ.extras["NUM_MPI_RANKS"]
        self.num_cpus_per_task = procinfo.num_cores
        self.env_vars = {
            "OMP_NUM_THREADS": self.current_environ.extras["OMP_NUM_THREADS"]
        }

    @sanity_function
    def validate_solution(self):
        return sn.assert_not_found(r"FAILED", self.stdout)
