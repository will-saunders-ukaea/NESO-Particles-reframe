import reframe as rfm
import reframe.utility.sanity as sn
import os

SOURCES_DIR = os.path.join(
    os.path.dirname(__file__),
    "..",
    "NESO-Particles",
)


class NESOParticlesBuild(rfm.CompileOnlyRegressionTest):
    sourcesdir = SOURCES_DIR
    build_system = "CMake"
    executable = os.path.join("test", "testNESOParticles")
    build_locally = False

    @run_before("compile")
    def prepare_build(self):
        cmake_flags = self.current_environ.extras["cmake_configuration"] + [
            "-DNESO_PARTICLES_ENABLE_PETSC=ON",
        ]
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
    build_locally = False
    sourcesdir = SOURCES_DIR

    @run_before("run")
    def setup_omp_env(self):
        self.executable = os.path.join(
            self.test_binaries.stagedir, "test", "testNESOParticles"
        )
        procinfo = self.current_partition.processor
        self.num_tasks = self.current_environ.extras["NUM_MPI_RANKS"]
        self.num_cpus_per_task = procinfo.num_cores
        self.env_vars = {
            "OMP_NUM_THREADS": self.current_environ.extras["OMP_NUM_THREADS"],
            "NESO_PARTICLES_TEST_RESOURCES_DIR": os.path.join(
                SOURCES_DIR, "test", "test_resources"
            ),
        }

    @sanity_function
    def validate_solution(self):
        return sn.assert_not_found(
            r"FAILED", self.stdout
        ) and sn.assert_not_found(r"SKIPPED", self.stdout)
