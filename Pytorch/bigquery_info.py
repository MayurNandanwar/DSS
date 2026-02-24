In every query engine, computation and storage is coupled but in 
big query this 2 thing is de-coupled.

In google cloud for storage there is colossus which similar or successer of google file storage
where you can store file and default replica of that file automatically created 

For computation there is Drimil, which has architecture like 
rootnode, mixer node( nodes available after roofnode and before leafnode called successer),
and leaf nodes

in leafnode, data reading happen ex. data treading from multiple tables available in storage,
in mixers, data aggregation happen when have complex query you have,
In rootnode coordinate with is leafnode and mixers. 

How make network between this 2  colossus and Drimmer for that Jupyter  is there, which is netwrok protocol high speed network protocol called it as petabyte jupyter network.
    
Big Query is Column oriented called capasitor means as here reading happen column wise 
if you have to aggregate salary and if reading happen row wise then IT will slower the Process BECAUSE OF number of columns,
and here i just aggregate the salary only then column oriented scan or read only salary column and then perform operation instead of reading rows and unnecessary columns.

whole architecture is orchestrate or scheduled by Borg which is orchestrator.

Summary: Big Query stores the data in format of column oriented. Bigquery , hive, redshift, hbase, casandra also column oriented


In BigQuery, database called dataset and inside that dataset we can create table view partition etc.

in partition, 3 types 
    1) integer range: means 1 to 10 in 1 partition then 11 to 20 in 2nd partition etc. when data is not comming in given range then data will go in unpartitioned partition create it self.
    2) Time Unit Column: shoud be date, time stamp and Datetime type is allow. when date is null it will create null partition if null value come in partition column.
    3) injestion partition : at what time you injest data it will create partition.

null partition is for all three , if partition colum valu came null then that record will added to null partition.
and out of range will add to unpartitioned table.

