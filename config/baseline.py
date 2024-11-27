site_configuration = {
    'systems': [
        {
            'name': 'NESOParticlesReframe',
            'descr': 'Runs NESO-Particles tests.',
            'hostnames': ['L0211-XU'],
            'modules_system': 'tmod4',
            'partitions': [
                {
                    'name': 'default',
                    'descr': 'Example partition',
                    'scheduler': 'local',
                    'launcher': 'local',
                    'environs': ['acpp_omp_library_only'],
                    'prepare_cmds': ["source /usr/local/Modules/init/profile.sh"]
                }
            ]
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
                    "-DCMAKE_BUILD_TYPE=RelWithDebInfo"
                ]
            },
            "modules": ["reframe/NP-acpp-llvm-cuda",]
        },
    ]
}
