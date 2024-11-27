site_configuration = {
    "systems": [
        {
            "name": "NESOParticlesReframe",
            "descr": "Runs NESO-Particles tests.",
            "hostnames": ["L0211-XU"],
            "modules_system": "tmod4",
            "max_local_jobs": 1,
            "partitions": [
                {
                    "max_jobs": 1,
                    "name": "default",
                    "descr": "Example partition",
                    "scheduler": "local",
                    "launcher": "mpirun",
                    "environs": [
                        "acpp_omp_library_only",
                        "acpp_omp_accelerated",
                        "acpp_llvm_cuda",
                    ],
                    "prepare_cmds": [
                        "source /usr/local/Modules/init/profile.sh"
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
                "NUM_BUILD_WORKERS": 12,
                "OMP_NUM_THREADS": 2,
                "NUM_MPI_RANKS": 12,
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
                "NUM_BUILD_WORKERS": 12,
                "OMP_NUM_THREADS": 2,
                "NUM_MPI_RANKS": 12,
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
                "NUM_BUILD_WORKERS": 12,
                "OMP_NUM_THREADS": 2,
                "NUM_MPI_RANKS": 6,
            },
            "modules": [
                "reframe/NP-acpp-llvm-cuda",
            ],
        },
    ],
}
