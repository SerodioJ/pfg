FROM serodioj/dana:v256 AS build_stage

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . PFGElasticity
# RUN env GIT_SSL_NO_VERIFY=true git clone https://github.com/robertovrf/PFGElasticity.git && \
RUN cd PFGElasticity && \
    cd client && dnc . -v && cd .. && \
    cd readn && dnc . -v && cd .. && \
    cd readn-writen && dnc . -v && cd .. && \
    cd writen && dnc . -v && cd .. && \
    cd server && dnc . -v && cd .. && \
    cd distributor && dnc . -sp ../server -v && cd .. && \
    find . -name '*.dn' -type f -delete

FROM serodioj/dana:v256

WORKDIR /app

COPY --from=build_stage /app/PFGElasticity/client/ /app/client

COPY --from=build_stage /app/PFGElasticity/readn /app/readn

COPY --from=build_stage /app/PFGElasticity/readn-writen /app/readn-writen

COPY --from=build_stage /app/PFGElasticity/writen /app/writen

COPY --from=build_stage /app/PFGElasticity/distributor /app/distributor
