## A launcher to start multiple kmer_profile.py iterations
## use python/2.7.1
## Christian Parobek
## Started 4 Feb 2015

downsampling=0.01

for kmer in {20..23}
do

	for seed in {1005..1015}
	do

	bsub python kmer_profile.py \
		--msbwt msBWTs/PjCisse/ msBWTs/hg19/ \
		--kmer $kmer \
		--seed $seed \
		--sampling_rate $downsampling \
		--unique \
		--output pcpVShuman/kmer$kmer-seed$seed-dnsamp$downsampling.txt

	done

done



