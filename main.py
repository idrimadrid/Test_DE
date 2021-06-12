from extract import *
from transform import *
from load import *

# Extracting csv files
med, clt, pub, pub_json = read_files()
# transformation and processing
med = process_drugs(med)
pub = process_pub(pub, pub_json)
clt = process_cli(clt)
#
gen_json(med, pub, clt)
