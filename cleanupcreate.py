import re 
pattern = re.compile(r"(^LOCATION\s+'.'|^TBLPROPERTIES\s+\(.?\)|^PARTITIONED BY \(__Partition_Year__, __Is_Active__\))\s*\)", re.MULTILINE | re.DOTALL)
# Use re.sub to replace matched lines with an empty string


no_cata = str.replace('spark_catalog.','').replace('USING delta','').replace('CREATE TABLE', 'CREATE TABLE IF NOT EXISTS').replace('Create database','create database if not exists ')
'USING delta'

clean = re.sub(pattern, '', no_cata)
for i in clean.split(';'):
    print(f'spark.sql("""{i}""")')