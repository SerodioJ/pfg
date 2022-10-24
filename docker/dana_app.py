# HPCCM Dana App recipe
Stage0 += baseimage(image="serodioj/dana:v256", _as="build_stage")
Stage0 += packages(ospackages=["git"])
Stage0 += workdir(directory="/app")
Stage0 += shell(
    commands=[
        "env GIT_SSL_NO_VERIFY=true git clone https://github.com/robertovrf/PFGElasticity.git",
        "cd PFGElasticity",
        "cd client && dnc . -v && cd ..",
        "cd readn && dnc . -v && cd ..",
        "cd readn-writen && dnc . -v && cd ..",
        "cd writen && dnc . -v && cd ..",
        "cd server && dnc . -v && cd ..",
        "cd distributor && dnc . -sp ../server -v && cd ..",
        "find . -name '*.dn' -type f -delete",
    ]
)

Stage1 += baseimage(image="serodioj/dana:v256")
Stage1 += workdir(directory="/app")
Stage1 += copy(
    _from="build_stage", src="/app/PFGElasticity/client/", dest="/app/client"
)
Stage1 += copy(_from="build_stage", src="/app/PFGElasticity/readn", dest="/app/readn")
Stage1 += copy(
    _from="build_stage", src="/app/PFGElasticity/readn-writen", dest="/app/readn-writen"
)
Stage1 += copy(_from="build_stage", src="/app/PFGElasticity/writen", dest="/app/writen")
Stage1 += copy(
    _from="build_stage", src="/app/PFGElasticity/distributor", dest="/app/distributor"
)
