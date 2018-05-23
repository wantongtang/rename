# coding=utf-8

import os

import random
import string


src_path = "../data_unnamed/"
dst_path="../cry/"



def file_rename(src_path,dst_path):
	for root,dirs,files in os.walk(src_path):
		k = 0
		home_name = ''.join(random.sample(string.ascii_letters + string.digits, 8)).lower()
		for single_file in files:
			src_file = ("%s/%s"%(root,single_file))
			dst_file  = dst_path +  home_name+"_nohash_"+str(k)+".wav"
			k+=1
			os.system("cp -rf %s  %s "%(src_file,dst_file))


file_rename(src_path,dst_path)
#file_name("../data_unnamed/")
