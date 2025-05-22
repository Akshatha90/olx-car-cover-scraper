
curl -s "https://www.amfiindia.com/spages/NAVAll.txt" | awk -F ';' 'BEGIN {OFS="\t"} NR>1 && NF>=5 && $1 != "" {print $4, $5}' > amfi_data.tsv