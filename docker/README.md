# Docker Config

Dockerfiles are generated using HPCCM tool, that can be installed using Python's `pip` (pip install hpccm).

To generate the Dockerfiles just run 
```
./generate_dana_base.sh
```

Note that to build images for different platforms, you can either build it using specific hardware (build ARMv7 image on a Raspberry PI) or try to use the Docker's `buildx`
command setting the `platform` flag to the target platform.