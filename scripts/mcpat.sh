#!/bin/bash

for i in {1..20}
do
./mcpat -infile xmls_gem5/specbzip/specbzip_$i.xml -print_level 5 > mcpat_results/specbzip/specbzip_$i.txt
done

for i in {1..20}
do
./mcpat -infile xmls_gem5/specmcf/specmcf_$i.xml -print_level 5 > mcpat_results/specmcf/specmcf_$i.txt
done

for i in {1..20}
do
./mcpat -infile xmls_gem5/spechmmer/spechmmer_$i.xml -print_level 5 > mcpat_results/spechmmer/spechmmer_$i.txt
done

for i in {1..20}
do
./mcpat -infile xmls_gem5/specsjeng/specsjeng_$i.xml -print_level 5 > mcpat_results/specsjeng/specsjeng_$i.txt
done

for i in {1..20}
do
./mcpat -infile xmls_gem5/speclibm/speclibm_$i.xml -print_level 5 > mcpat_results/speclibm/speclibm_$i.txt
done




