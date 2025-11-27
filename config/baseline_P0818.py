site_configuration = {
    "systems": [
        {
            "name": "NESOParticlesReframe",
            "descr": "Runs NESO-Particles tests.",
            "hostnames": [
                "P0818",
            ],
            "modules_system": "tmod4",
            "max_local_jobs": 2,
            "stagedir": "/dev/shm/reframe",
            "partitions": [
                {
                    "max_jobs": 2,
                    "name": "default",
                    "descr": "Example partition",
                    "scheduler": "local",
                    "launcher": "mpirun",
                    "environs": [
                        "acpp_omp_library_only",
                        "acpp_omp_accelerated",
                        "acpp_openmpi_omp_accelerated",
                        "acpp_llvm_cuda",
                        "acpp_nvcxx_cuda",
                        "acpp_generic_cuda",
                        "intel-oneapi",
                    ],
                    "prepare_cmds": [
                        "source /etc/profile.d/modules.sh",
                        "export ACPP_PERSISTENT_RUNTIME=1",
                        "export ACPP_ADAPTIVITY_LEVEL=0",
                        "export ACPP_APPDB_DIR=/dev/shm/acpp",
                        "export ACPP_RT_NO_JIT_CACHE_POPULATION=1",
                    ],
                }
            ],
        }
    ],
    "environments": [
        {
            "name": "acpp_omp_library_only",
            "features": ["sycl"],
            "cc": "gcc",
            "cxx": "g++",
            "features": [],
            "extras": {
                "cmake_configuration": [
                    "-DNESO_PARTICLES_SINGLE_COMPILED_LOOP=ON",
                    "-DACPP_TARGETS=omp.library-only",
                    "-DCMAKE_BUILD_TYPE=Release",
                ],
                "NUM_BUILD_WORKERS": 32,
                "NUM_MPI_RANKS": 8,
                "env_vars": {
                    "NESO_PARTICLES_LOOP_LOCAL_SIZE": 1,
                    "OMP_NUM_THREADS": 2,
                    "NESO_PARTICLES_DEVICE_AWARE_MPI": "ON",
                    "NESO_PARTICLES_TEST_TMP_DIR": "/tmp/neso-particles-test/acpp_omp_library_only",
                },
            },
            "modules": [
                "reframe/NP-acpp-llvm-cuda",
            ],
        },
        {
            "name": "acpp_omp_accelerated",
            "features": ["sycl"],
            "cc": "gcc",
            "cxx": "g++",
            "features": [],
            "extras": {
                "cmake_configuration": [
                    "-DACPP_TARGETS=omp.accelerated",
                    "-DCMAKE_BUILD_TYPE=Release",
                ],
                "NUM_BUILD_WORKERS": 32,
                "NUM_MPI_RANKS": 8,
                "env_vars": {
                    "OMP_NUM_THREADS": 2,
                    "NESO_PARTICLES_DEVICE_AWARE_MPI": "ON",
                    "NESO_PARTICLES_TEST_TMP_DIR": "/tmp/neso-particles-test/acpp_omp_accelerated",
                },
            },
            "modules": [
                "reframe/NP-acpp-llvm-cuda",
            ],
        },
        {
            "name": "acpp_openmpi_omp_accelerated",
            "features": ["sycl"],
            "cc": "gcc",
            "cxx": "g++",
            "features": [],
            "extras": {
                "cmake_configuration": [
                    "-DACPP_TARGETS=omp.accelerated",
                    "-DCMAKE_BUILD_TYPE=Release",
                ],
                "NUM_BUILD_WORKERS": 32,
                "NUM_MPI_RANKS": 8,
                "env_vars": {
                    "OMP_NUM_THREADS": 2,
                    "NESO_PARTICLES_DEVICE_AWARE_MPI": "ON",
                    "NESO_PARTICLES_TEST_TMP_DIR": "/tmp/neso-particles-test/acpp_openmpi_omp_accelerated",
                },
            },
            "modules": [
                "reframe/NP-acpp-openmpi-llvm-cuda",
            ],
        },
        {
            "name": "acpp_llvm_cuda",
            "features": ["sycl"],
            "cc": "gcc",
            "cxx": "g++",
            "features": [],
            "extras": {
                "cmake_configuration": [
                    "-DACPP_TARGETS=cuda:sm_89",
                    "-DCMAKE_BUILD_TYPE=Release",
                ],
                "NUM_BUILD_WORKERS": 32,
                "NUM_MPI_RANKS": 4,
                "env_vars": {
                    "OMP_NUM_THREADS": 1,
                    "NESO_PARTICLES_TEST_TMP_DIR": "/tmp/neso-particles-test/acpp_llvm_cuda",
                },
            },
            "modules": [
                "reframe/NP-acpp-llvm-cuda",
            ],
        },
        {
            "name": "acpp_nvcxx_cuda",
            "features": ["sycl"],
            "cc": "gcc",
            "cxx": "g++",
            "features": [],
            "extras": {
                "cmake_configuration": [
                    "-DACPP_TARGETS=cuda-nvcxx",
                    "-DCMAKE_BUILD_TYPE=Release",
                ],
                "NUM_BUILD_WORKERS": 24,
                "NUM_MPI_RANKS": 4,
                "env_vars": {
                    "OMP_NUM_THREADS": 1,
                    "NESO_PARTICLES_TEST_TMP_DIR": "/tmp/neso-particles-test/acpp_nvcxx_cuda",
                },
            },
            "modules": [
                "reframe/NP-acpp-nvcxx-cuda",
            ],
        },
        {
            "name": "acpp_generic_cuda",
            "features": ["sycl"],
            "cc": "gcc",
            "cxx": "g++",
            "features": [],
            "extras": {
                "cmake_configuration": [
                    "-DACPP_TARGETS=generic",
                    "-DCMAKE_BUILD_TYPE=Release",
                ],
                "NUM_BUILD_WORKERS": 32,
                "NUM_MPI_RANKS": 4,
                "env_vars": {
                    "OMP_NUM_THREADS": 1,
                    "ACPP_VISIBILITY_MASK": "cuda",
                    "NESO_PARTICLES_TEST_TMP_DIR": "/tmp/neso-particles-test/acpp_generic_cuda",
                },
            },
            "modules": [
                "reframe/NP-acpp-generic",
            ],
        },
        {
            "name": "intel-oneapi",
            "features": ["sycl"],
            "cc": "icx",
            "cxx": "icpx",
            "features": [],
            "extras": {
                "cmake_configuration": [
                    "-DCMAKE_BUILD_TYPE=Release",
                ],
                "NUM_BUILD_WORKERS": 32,
                "NUM_MPI_RANKS": 16,
                "env_vars": {
                    "OMP_NUM_THREADS": 2,
                    "I_MPI_PIN_DOMAIN": "2:scatter",
                    "NESO_PARTICLES_DEVICE_AWARE_MPI": "ON",
                    "NESO_PARTICLES_TEST_TMP_DIR": "/tmp/neso-particles-test/intel-oneapi",
                },
            },
            "modules": [
                "reframe/NP-intel-oneapi",
            ],
        },
    ],
}
