
#! throughput  = how many read and write we can perform per second.

# database like sql database has low throughput ex uber example : 1000 driver's per second location,fare,analytics, is inserted in databse 
#so here for single person 3 operation is performed in database so for 1000 driver =3000 operation will perform and
#uber has multiple drivers in all india. so database is not suitable because of low throughput 

#! kafka has high throughput and because of this kafka will not down, but kafka is not alternative solution of database.
#!because kafka can send millions of data because of high throughput but not store large amount of data for longtime it stores temporary 

#! we will use both kafka + database, 
## we have producers who produce the data ex. driver produces speed , fare, location, and data goes to kafka , in kafka we have consumer like company server , customer server which consume the data from kafka in bulk base 
# and this raw data will be dump in database and further we can do analysis on that data , in database for faster retrival of 
# data we can do partitioning based on area or region etc


#! diff between kafka and database 
# --> kafka has high throughput but low storage and database has low throughput and high storage 
# --> we can not query in kafka where as in database we can.

#!Note: 1 consumer can take data from multiple partitions but , if have multiple consumers and 1 partition then , only one consumer can get data from single partition in kafka architecture

#! self balancing happen on consumer group level: ex if have 4 partition and have 1 consumer group has 5 consumer then , using self balancing 4 partition assign to 4 consumer and 1 remains idle 
#! lets say have 2 group of consumer 1 group has 5 consumer and second has 1 consumer then 4 partition will assign to 4 consumer and 1 remain idle in group 1 , in 
#! group 2 all partition assign to the 1 consumer because of only 1 consumer available.

#!Note : Kafka is Queue and Pub/Sub based : ex. if have 4 partition and 1 group of consumer has 4 consumer then each partition has 1 consumer server, called queue 
#! pub/sub: 4 partition , 3 consumer group, 2 group has 4 consumer, last has 1 consumer  : so this 4 partition assign to 2 group of 4 consumer this is pub/sub, last group has 1 consumer so all the partition will assign to that consumer.
#! so this partition assigning to each consumer handled by zookeeper


#! why need kafka and can we increase throughput in database 
#--> because kafka store data in RAM and it is temporary storage if by chance computer gets restart then no data will appear in RAM where database run on secondary memory ssd if restart happen data will not loose , if we use database for store data it took time 

#but if we do it for database then this problem can arise and we loose the important data when goes down and also we use database for 
#reading the data and more like join the table , set primary key ,foreign key , database use datastructure and algorithm for optimaly query the data.

# kafka is just like consume the raw data and send it to consumer and then consumer can perform the cleaning the data and analytics on it and store then in database 
# so in database we store the data optimal way so we can further use this or retrieve faster.
#2) in database we store the data structured way where as service like kafka ,redis service is for unstructure data,where data generated unstructured way

# kafka is running continuously if your database goes down for 2 or 3 min , its ok data available in kafka , so once database 
# goes up again fetch data by consumer and further process on that data goes on and you will not loose data.

#! so main purpose of database is to not to provide throughput but provide the mechanism where optimally we can store the data and retrive the data.