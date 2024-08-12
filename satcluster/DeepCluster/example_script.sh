#!/bin/bash

#PBS -lwalltime=72:00:00
#PBS -lselect=1:ncpus=32:mem=250gb:ngpus=1:gpu_type=RTX6000

DIR="~/Raster_data/A_Da_De_Ki/"
ARCH="vgg16" #or alexnet/vgg16
LR=0.01
WD=-5
CLUSTERING=Kmeans #Kmeans
K=16 #10000
WORKERS=4
EXP="/~/experiments/ADDK_k16_imgnet_lr001_sf/"
BATCH=128
RESUME="~/experiments/ADDK_k16_imgnet_lr001_sf/checkpoint.pth.tar"

#RESUME="checkpoints/checkpoint_0.0.pth.tar"
#FEPOCH=2
FNAME="~/experiments/ADDK_k16_imgnet_lr001_epoch20_"
mkdir -p ${EXP}

module load anaconda3/personal

#CUDA_VISIBLE_DEVICES=0 
python3 ~GitHub/deepcluster-master/main_sfeatures.py ${DIR} --exp ${EXP} --arch ${ARCH} \
  --lr ${LR} --wd ${WD} --k ${K} --sobel --clustering ${CLUSTERING} --verbose --batch ${BATCH} --workers ${WORKERS} --resume ${RESUME} --features_name ${FNAME} --features_epoch ${FEPOCH}
