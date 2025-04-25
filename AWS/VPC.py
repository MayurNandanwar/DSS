
#! Vertual private cloud(VPC): ex. in company every dekstop can communicate with each other so file sharing or other sharing things can be easilty done 
#!for that you set network , when we make instance in aws doe that also required to set networking , where you set : answer is VPC 

#! VPC simply means you are going to create network
#! when you create VPC then it is a Private, 
# Private IP address ranges are 10.0.0.0 to 10.255.255.255,
#                             172.16.0.0 to 172.31.255.255, 
#                         and 192.168.0.0 to 192.168.255.255.

#! ip address can define only in 32 byte.
#! size of this VPC is 32 bit mean 192 has size 8 byte, 168 has 8byte , 0 has 8 byte and 0 has 8 byte
# ex 192.168.0.0 in binary 11000000 10101000 00000000 00000000
# ex 192.168.255.255 in binary 11000000.10101000.11111111.11111111

#! CIDR(Classless Inter-Domain Routing) : value can be 8,16,24 means lets say 8 then first 8 byte is fixed, in 192.168.255.255 ip 192 will be fixed and remaining will change
#! lets say 16, in 192.168.255.255 ip 192.168 will fixed and remaining will be change
# ex. in your company you want 100 server can share thing like file sharing how you will give ip to this pc
# if i choose 192.168.0.0 ip so from 192.168.0.0 to 192.168.0.255 , ip to 100 pc can be assign so for that only changes 
# occures in last 8 bit and first 24 byte is fixed so we can set CIDR 24.

#! why required CIDR?: because due to population ex i have 4 mobile , my mother brother has also mobile , i have wifi so only i required so many IP 
#! and because of population use this devices iot require IP for that requires CIDR ans also IPV6 came size of this ipv6 is 128 byte.

#! VPC created region level whereas subnet created in availability zone.

#!ex in sybercafe many pc available and half of that pc connected with diff subnet and others connected with diff subnet.
#!how to do this
# ex my main network is 192.168.0.0 to 192.168.255.255 where CIDR is 16 so 192.168 is fixed.
# subnet1 = Network1 is 192.168.1.0 - 192.168.1.255
# subnet2 = network2 is 192.168.2.0 - 192.168.2.255
#this is how we can set total 255 subnet 

#! sensitive information should be in private instance like database , application server so and using public instance 
#! which has internet access we can coordinate with private server.


#! how to internet make available in private instance ?
#-> create instance attach private Subnet in which net is not available 
#-> create instance attach public subnet in which net is available 
#-> create nat instance attach public subnet --> create elastic ip and attach it to nat instance and then 
#-> go to private instance go to subnat and rout table attached to that subnat and add route '0.0.0.0/0' and target  is nat instance 
# right click on nat instance --> networking --> change source/destination check

#! note :now what happen you are sending request from private like google.com then it goes to internet using nat instance and from net 
#! response back to the nat instance and nat instance ip send back to private ip  

#!Note : jump server : jis server ko aap private server or instance ko access karneke liye use karte ho use jump server bolenge

#!