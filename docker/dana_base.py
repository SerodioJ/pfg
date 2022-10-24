# HPCCM recipe for Dana Base Image
dana_dist = {
    "ubuntu64": "https://www.projectdana.com/download/ubu64",
    "raspi": "https://www.projectdana.com/download/raspi",
}

dana = USERARG.get("DANA", "ubuntu64")

if dana not in dana_dist:
    raise ValueError("Invalid Dana Distribution")

Stage0 += baseimage(image="ubuntu:18.04")
Stage0 += packages(ospackages=["wget", "unzip"])
Stage0 += shell(
    commands=[
        "mkdir /opt/dana",
        "cd /opt/dana",
        f"wget --no-check-certificate {dana_dist[dana]} -O dana_dist",
        "unzip dana_dist",
        "rm dana_dist",
        "chmod +x dana dnc",
    ]
)

Stage0 += environment(
    variables={
        "DANA_HOME": "/opt/dana",
        "PATH": "$PATH:/opt/dana",
    }
)
