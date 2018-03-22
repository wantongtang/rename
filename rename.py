# coding=utf-8

import os

import random
import string

dst_path="../cry/"



def file_name(file_dir):
	for root,dirs,files in os.walk(file_dir):
		k = 0
		for single_file in files:
			src_file = ("%s/%s"%(root,single_file))
			dst_file  = dst_path +  ''.join(random.sample(string.ascii_letters + string.digits, 8)).lower()+"_nohash_"+str(k)+".wav"
			k+=1
			os.system("cp -rf %s  %s "%(src_file,dst_file))


file_name("../data_unnamed/")
