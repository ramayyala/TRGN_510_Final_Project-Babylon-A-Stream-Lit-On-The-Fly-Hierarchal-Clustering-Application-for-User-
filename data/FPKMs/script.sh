for file in *.txt
do
  sed -i '1s/^/gene_id	FPKM\n/' $file
done
