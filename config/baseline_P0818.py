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
            "stagedir": "/tmp/reframe",
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
                        "acpp_llvm_cuda",
                        "intel-oneapi",
                    ],
                    "prepare_cmds": [
                        "source /etc/profile.d/modules.sh",
                        "export CL_CONFIG_CPU_TARGET_ARCH=corei7-avx",
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
                    "-DACPP_TARGETS=omp.library-only",
                    "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
                ],
                "NUM_BUILD_WORKERS": 16,
                "NUM_MPI_RANKS": 8,
                "env_vars": {
                    "OMP_NUM_THREADS": 2,
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
                    "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
                ],
                "NUM_BUILD_WORKERS": 16,
                "NUM_MPI_RANKS": 8,
                "env_vars": {
                    "OMP_NUM_THREADS": 2,
                },
            },
            "modules": [
                "reframe/NP-acpp-llvm-cuda",
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
                    "-DACPP_TARGETS=cuda:sm_61",
                    "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
                ],
                "NUM_BUILD_WORKERS": 16,
                "NUM_MPI_RANKS": 8,
                "env_vars": {
                    "OMP_NUM_THREADS": 1,
                },
            },
            "modules": [
                "reframe/NP-acpp-llvm-cuda",
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
                    "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
                ],
                "NUM_BUILD_WORKERS": 16,
                "NUM_MPI_RANKS": 16,
                "env_vars": {
                    "OMP_NUM_THREADS": 2,
                    "I_MPI_PIN_DOMAIN": "2:scatter",
                },
            },
            "modules": [
                "reframe/NP-intel-oneapi",
            ],
        },
    ],
}
