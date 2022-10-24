#!/bin/bash

hpccm --recipe dana_base.py > dana_base.ubuntu64.Dockerfile
hpccm --recipe dana_base.py > dana_base.raspi.Dockerfile --userarg DANA=raspi