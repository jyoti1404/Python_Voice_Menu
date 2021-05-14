
import os
import time
import subprocess
import webbrowser
import getpass
import pyaudio
import speech_recognition as sr

os.system("clear")

print("\n")
os.system("tput setaf 11")
print("\t\t\t  Welcome to our Menu App")

os.system("tput setaf 7")
print("\t\t\t -------------------------\n")
os.system("espeak-ng 'Hello.. My name is Jyoti. This is My place and,    I    will    Help    You   to   Set-Up   Your   Environments   which   are   as   follows ..' ")

def mainaws():
	
	os.system("tput setaf 2")
	print("""Speak 1: for HADOOP SERVICES""")
	os.system("tput setaf 3")
	print("Speak 2: for AWS")	
	os.system("tput setaf 6")
	print("Speak  3: for DOCKER")
	os.system("tput setaf 13")
	print("Speak 4: for WEBSERVER")
	os.system("tput setaf 1")
	print("Speak 5: to Quit")

	os.system("tput setaf 7")

	print("\n")
	os.system('espeak-ng "Read  this   menu  and        Speak  your  valid   choice? "')
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Start Speaking")
		audio = r.listen(source)
		r.pause_threshold = 1
		print("Audio Recorded")
	ach = r.recognize_google(audio)
	print("Your choice: ", ach)
	#ach = input("Enter your choice: ")
	if(int(ach) == 1):
		hadoop()
	elif(int(ach) == 2 or ach == "Tu"):	
		aws()
	elif(int(ach) == 3):	
		docker()
	elif(int(ach) == 4):
		webserver()
	elif(int(ach) == 5):
		os.system("tput setaf 11")
		os.system('espeak-ng "Thank you for using our services. We wish to see you again.. "')
		print("\n\t\t\t   Thank You for Using Our Services !!!")		
		os.system("tput setaf 7")
		print("\t\t\t ----------------------------------------\n")		
		exit()
	else:
		print("Invalid Input...")


#def remote():
#	os.system("clear")
#	print("\n\n")
#	os.system("tput setaf 2")
#	print("\t\t\t\t\tWELCOME TO HADOOP CLUSTER SETUP ")
#	print("\t\t\t\t--------------------------------------------")
#	print("""
#		- Press 1 for HADOOP SERVICES.
#		- Press 2 to quit  """)

#	os.system("tput setaf 9")

#	choice = int(input("\nENTER YOUR CHOICE : "))

#	if choice == 1:

def hadoop():
	os.system("tput setaf 2")
	print("\t\t\t\tWELCOME TO HADOOP WORLD")
	print("\t\t\t\t---------------------------------------")
	os.system('espeak-ng "WELCOME TO HADOOP WORLD.    Read the choices below and Enter your choice.. "')
	print("""
- Speak 1 to know about Hadoop.
- Speak 2 to configure Hadoop Cluster.
- Speak 3 to start services of Hadoop Cluster.
- Speak 4 to stop the services of Hadoop Cluster.
- Speak 5 to configure and launch Client.
- Speak 6 to see the HADOOP CLUSTER REPORT.
- Speak 7 to upload a file to cluster.
- Speak 8 to open webUI of Hadoop in your browser.
- Speak 9 for Hadoop Elasticity with LVM.
- Speak 10 To go back to main menu """)
	
	#ch = int(input("\nENTER YOUR CHOICE : "))
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Start Speaking")
		audio = r.listen(source)
		r.pause_threshold = 1
		print("Audio Recorded")
	ch = r.recognize_google(audio)
	print(ch)

	if(int(ch) == 1):
		print("""The Apache Hadoop software library is a framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. It is designed to scale up from single servers to thousands of machines, each offering local computation and storage. Rather than rely on hardware to deliver high-availability, the library itself is designed to detect and handle failures at the application layer, so delivering a highly-available service on top of a cluster of computers, each of which may be prone to failures.""")
		os.system('espeak-ng """The Apache Hadoop software library is a framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. It is designed to scale up from single servers to thousands of machines, each offering local computation and storage. Rather than rely on hardware to deliver high-availability, the library itself is designed to detect and handle failures at the application layer, so delivering a highly-available service on top of a cluster of computers, each of which may be prone to failures."""')
		print("\n")
	elif(int(ch) == 2):
		print("""
- Press 1 to configure NameNode.
- Press 2 to configure DataNode. """)

		config_choice = int(input("\n ENTER YOUR CHOICE : "))

		if config_choice == 1:
			print("\n\t\t\t---------- CONFIGURATION OF NAMENODE WILL HAPPEN NOW --------------")

			os.system("yum install wget -y")
			rc = subprocess.getstatusoutput("rpm -q hadoop")[0]

			if rc == 1:
				print("\n\n\t\t\t--------- Hadoop software is installing --------- ")
				os.system("wget https://hadoop-arth.s3.ap-south-1.amazonaws.com/hadoop-1.2.1-1.x86_64.rpm")
				os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm")
				print("\n\n\t\t\t--------- HADOOP SUCCESSFULLY INSTALLED !! -----------")
				time.sleep(2)

				print("\n\n\t\t\t--------- JDK software is installing --------- ")
				os.system("wget https://hadoop-arth.s3.ap-south-1.amazonaws.com/jdk-8u171-linux-x64.rpm")
				os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm")
				print("\n\n\t\t\t--------- JDK SUCCESSFULLY INSTALLED !! -----------")
				print("\n\n")

			os.system("hadoop version")

			print("\n\n-------- CONFIGURING NAMENODE ---------")
			time.sleep(1)
			os.system("rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")

			print("\nIf you are configuring the NAMENODE in AWS, enter name_ip as 0.0.0.0")
			name_ip = input("\nENTER THE IP ADDRESS OF NAMENODE : ")
			port_number = int(input("\nENTER THE PORT NUMBER :"))
			datadir = input("\nENTER THE DIRECTORY NAME YOU WANT : ")
			os.system(f"rm -rf /{datadir};mkdir /{datadir};echo 3 >/proc/sys/vm/drop_caches")

			datafile = open("/etc/hadoop/hdfs-site.xml", 'w')
			datafile.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>dfs.name.dir</name>
<value>/{datadir}</value>
</property>

</configuration>''')
			datafile.close()
			datafile1 = open("/etc/hadoop/core-site.xml", 'w')
			datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>fs.default.name</name>
<value>hdfs://{name_ip}:{port_number}</value>
</property>

</configuration>''')
			datafile1.close()
			os.system("tput setaf 2")
			print("\n WHEN PROMPTED TO ENTER YES OR NO , PRESS 'Y' IN CAPITALS' ")
			os.system("hadoop namenode -format")
			os.system("tput setaf 3")

		elif config_choice == 2:
			print("\n\t\t\t---------- CONFIGURATION OF DATANODE WILL HAPPEN NOW --------------")

			os.system("yum install wget -y")
			rc = subprocess.getstatusoutput("rpm -q hadoop")[0]

			if rc == 1:
				print("\n\n\t\t\t--------- Hadoop software is installing --------- ")
				os.system("wget https://hadoop-arth.s3.ap-south-1.amazonaws.com/hadoop-1.2.1-1.x86_64.rpm")
				os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm")
				print("\n\n\t\t\t--------- HADOOP SUCCESSFULLY INSTALLED !! -----------")
				time.sleep(2)

				print("\n\n\t\t\t--------- JDK software is installing --------- ")
				os.system("wget https://hadoop-arth.s3.ap-south-1.amazonaws.com/jdk-8u171-linux-x64.rpm")
				os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm")
				print("\n\n\t\t\t--------- JDK SUCCESSFULLY INSTALLED !! -----------")
				print("\n\n")

			os.system("hadoop version")

			print("\n\n-------- CONFIGURING DATANODE ---------")
			time.sleep(1)
			os.system("rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")

			name_ip = input("\nENTER THE IP ADDRESS OF NAMENODE : ")
			port_number = int(input("\nENTER THE PORT NUMBER :"))
			datadir = input("\nENTER THE DIRECTORY NAME YOU WANT : ")
			os.system(
				f"rm -rf /{datadir};mkdir /{datadir};echo 3 >/proc/sys/vm/drop_caches")
			datafile = open("/etc/hadoop/hdfs-site.xml", 'w')
			datafile.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>dfs.name.dir</name>
<value>/{datadir}</value>
</property>

</configuration>''')
			datafile.close()
			datafile1 = open("/etc/hadoop/core-site.xml", 'w')
			datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>fs.default.name</name>
<value>hdfs://{name_ip}:{port_number}</value>
</property>

</configuration>''')
			datafile1.close()

	elif(int(ch) == 3):
		node = input("\n\t\t YOU CONFFIGURED THIS SYSTEM AS [NAMENODE] OR [DATANODE] ? ").upper()
		if node == "NAMENODE":
			print("\n\t\t\t--------- NAMENODE SERVICES ARE STARTING !! ---------- ")
			os.system("hadoop-daemon.sh start namenode;jps")

		elif node == "DATANODE":
			print("\n\t\t\t--------- DATANODE SERVICES ARE STARTING !! ---------- ")
			os.system("hadoop-daemon.sh start datanode;jps")

		output = input("\n\t\t DO YOU WANT TO MAKE THE SERVICES OF HADOOP PERMANENT ? [Y/N] ").upper()
		if output == "Y":
			file1 = open("/etc/rc.d/rc.local", "a")
			file1.write("\n hadoop-daemon.sh start namenode")
			file1.close()

	elif(int(ch) == 4):
		node = input("\n\t\t YOU CONFFIGURED THIS SYSTEM AS [NAMENODE] OR [DATANODE] ? ").upper()
		if node == "NAMENODE":
			print("\n\t\t\t--------- NAMENODE SERVICES ARE STOPPING !! ---------- ")
			os.system("hadoop-daemon.sh stop namenode;jps")

		elif node == "DATANODE":
			print("\n\t\t\t--------- DATANODE SERVICES ARE STOPPING !! ---------- ")
			os.system("hadoop-daemon.sh stop datanode;jps")

	elif(int(ch) == 5):
		print("\n\n--------------CONFIGURING CLIENT-----------")
		os.system("yum install wget -y")
		rc = subprocess.getstatusoutput("rpm -q hadoop")[0]

		if rc == 1:
			print("\n\n\t\t\t--------- Hadoop software is installing --------- ")
			os.system("wget https://hadoop-arth.s3.ap-south-1.amazonaws.com/hadoop-1.2.1-1.x86_64.rpm")
			os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm")
			print("\n\n\t\t\t--------- HADOOP SUCCESSFULLY INSTALLED !! -----------")
			time.sleep(2)

			print("\n\n\t\t\t--------- JDK software is installing --------- ")
			os.system("wget https://hadoop-arth.s3.ap-south-1.amazonaws.com/jdk-8u171-linux-x64.rpm")
			os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm")
			print("\n\n\t\t\t--------- JDK SUCCESSFULLY INSTALLED !! -----------")
			print("\n\n")

		os.system("hadoop version")

		t.sleep(1)
		os.system("rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
		name_ip = input("\nENTER THE IP ADDRESS OF NAMENODE : ")
		port_number = int(input("\nENTER THE PORT NO :"))
		datafile1 = open("/etc/hadoop/core-site.xml", 'w')
		datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{name_ip}:{port_number}</value>
</property>
</configuration>''')
		datafile1.close()
		os.system("systemctl stop firewalld;setenforce 0")
		print("\n\n\t\t-------------- CLIENT SERVICE STARTED ----------")

		client_choice = input("\n\n\t\t DO YOU WANT TO CHANGE THE BLOCK SIZE [Y/N] : ").upper()
		if client_choice == "Y":
			block_size = input("\n\n\t\t ENTER THE BLOCK SIZE (in MB ) : ")
			block_size = block_size * 1024 * 1024

			datafile1 = open("/etc/hadoop/hdfs-site.xml", 'w')
			datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.block.size</name>
<value>{block_size}</value>
</property>
</configuration>''')
			datafile1.close()

		client_choice = input("\n\n\t\t DO YOU WANT TO CHANGE THE REPLICATION FACTOR [Y/N] : ").upper()
		if client_choice == "Y":
			replication_factor = input("\n\n\t\t ENTER THE REPLICATION FACTOR : ")
			datafile1 = open("/etc/hadoop/hdfs-site.xml", 'w')
			datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.replication</name>
<value>{replication_factor}</value>
</property>
</configuration>''')
			datafile1.close()

	elif(int(ch) == 6):
		os.system("hadoop dfsadmin -report")

	elif(int(ch) == 7):
		filepath = input("\n\n\t\t ENTER THE FILEPATH : ")
		os.system(f"hadoop fs -put /{filepath}  /")

	elif(int(ch) == 8):
		name_ip = input("\n\n\t\t ENTER THE NAMENODE IP : ")
		webbrowser.open(f"http://{name_ip}:50070")

	elif(int(ch) == 9):
		while True:
			print("""\n
- Press 1 : To check how many storage is attached to the OS
- Press 2 : To create Physical Volume
- Press 3 : To display Physical Volume
- Press 4 : To create Volume Group
- Press 5 : To display Volume Group
- Press 6 : To create Logical Volume
- Press 7 : To display Logical Volume
- Press 8 : To format the LV
- Press 9 : To mount the LV
- Press 10 : To exit """)

			ch = int(input("\n ENTER YOUR CHOICE : "))

			if ch == 1:
				os.system("fdisk -l")

			elif ch == 2:
				pv1 = input("Enter the name of storage 1 : ")
				pv2 = input("Enter the name of storage 2 : ")
				os.system("pvcreate {}".format(pv1))
				os.system("pvcreate {}".format(pv2))
                    	
			elif ch == 3:
				pv = input("Enter the name of storage : ")
				os.system("pvdisplay {}".format(pv))
	
			elif ch == 4:
				vgn = input("Give name to the VOLUME GROUP : ")
				pvn1 = input("Enter the name of storage 1 : ")
				pvn2 = input("Enter the name of Storage 2 : ")
				os.system("vgcreate {} {} {}".format(vgn, pvn1, pvn2))

			elif ch == 5:
				vgn1 = input("Enter the name of VOLUME GROUP : ")
				os.sytem("vgdisplay {}".format(vgn1))

			elif ch == 6:
				size = input("Enter size for your LOGICAL VOLUME : ")
				lvn = input("Give name to your LOGICAL VOLUME : ")
				vgn2 = input("Enter name of the VOLUME GROUP : ")
				os.system("lvcreate --size {}G --name {} {}".format(size, lvn, vgn2))

			elif ch == 7:
				os.system("lvdisplay")

			elif ch == 8:
				vgn = input("Enter the name of VOLUME GROUP : ")
				lvn = input("Enter the name of LOGICAL VOLUME : ")
				os.system("mkfs.ext4  /dev/{}/{}".format(vgn, lvn))

			elif ch == 9:
				user_dir = input("\n\n\t\t ENTER THE DIRECTORY USED IN HADOOP CLUSTER : ")
				vgn = input("Enter the name of VOLUME GROUP : ")
				lvn = input("Enter the name of LOGICAL VOLUME : ")
				os.system(f"mount /dev/{vgn4}/{lvn2}  /{user_dir} ")

			elif ch == 10:
				break

			input("\t PRESS ENTER TO CONTINUE -------- ")

	elif(int(ch) == 10):
		mainaws()
	#hadoop()

	#elif choice == 2:
	#	return
	print("\n")
	ext = input("WANT TO RUN AGAIN THE HADOOP MENU[Y/N] : ").upper()
	if ext == "Y":
		hadoop()
	elif ext == "N":
		return mainaws()


#inp = input("\n\n\t\t FOR RUNNING THE HADOOP CLUSTER PRESS Y : ").upper()
#if inp == "Y":
#	remote()


def awsec2():

	while(True):
		os.system("tput setaf 3")
		#os.system('espeak-ng "WELCOME TO AWS WORLD.    Read the choices below and Enter your choice.. "')
		print("""Press 1: to know about EC2 instances
Press 2: to launch an EC2 instance
Press 3: to describe EC2 instances
Press 4: to start an EC2 instance
Press 5: to stop an EC2 instance
Press 6: to terminate an EC2 instance
Press 7: to go back to main menu""")
		os.system("tput setaf 7")
		print("\n")
		ach3 = input("Enter your choice: ")
		print("\n")
		os.system("tput setaf 7")
	
		if(int(ach3) == 1):
			os.system("tput setaf 3")
			print("""Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers. Amazon EC2’s simple web service interface allows you to obtain and configure capacity with minimal friction. It provides you with complete control of your computing resources and lets you run on Amazon’s proven computing environment. """)
			print("\n")
		os.system("tput setaf 7")
				
		if(int(ach3) == 2):
			aimgid = input("Enter your AMI Id: ")
			ainstancetype = input("Enter your Instance type (e.g. t2.micro): ")
			acount = input("Enter no. of instances you want to launch: ")
			asubnet = input("Enter your region subnet: ")
			asecurity = input("Enter the security group ID: ")
			akey = input("Enter your AWS key: ")
			#	os.system(""" aws ec2 run-instances --image-id  {aimgid} --instance-type {ainstancetype} --count {acount} --subnet-id {asubnet} --security-group-ids {asecurity} --key-name {akey} """)
			os.system("tput setaf 3")
			os.system(" aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name {} ".format(aimgid, ainstancetype, acount, asubnet, asecurity, akey))
			print("\n")
		os.system("tput setaf 7")
				
		if(int(ach3) == 3):
			os.system(" aws ec2 describe-instances ")
			print("\n")
		os.system("tput setaf 7")
					
		if(int(ach3) == 4):
			ainstidstart = input("Enter your Instance ID: ")
			os.system(" aws ec2 start-instances --instance-ids {} ".format(ainstidstart))
			print("\n")
		os.system("tput setaf 7")
	
		if(int(ach3) == 5):
			ainstidstop = input("Enter your Instance ID: ")
			os.system(" aws ec2 stop-instances --instance-ids {} ".format(ainstidstop))
			print("\n")
		os.system("tput setaf 7")

		if(int(ach3) == 6):
			ainstidterm = input("Enter your Instance ID: ")
			os.system(" aws ec2 terminate-instances --instance-ids {} ".format(ainstidterm))
			print("\n")
		os.system("tput setaf 7")

		if(int(ach3) == 7):
			return aws()	
		if(int(ach3) >= 8 ):
			os.system("tput setaf 1")
			print("INVALID INPUT")
		os.system("tput setaf 7")


def awsebs():
	while(True):
		os.system("tput setaf 3")
		print("""Press 1: to know about EBS 
Press 2: to create EBS volume
Press 3; to attach EBS to EC2 instance
Press 4: to go back to main menu""")
		os.system("tput setaf 7")
		print("\n")
		ach4 = input("Enter your choice: ")
		print("\n")
		os.system("tput setaf 7")
		if(int(ach4) == 1):
			os.system("tput setaf 3")
			print("""Amazon Elastic Block Store (EBS) is an easy to use, high performance block storage service designed for use with Amazon Elastic Compute Cloud (EC2) for both throughput and transaction intensive workloads at any scale. A broad range of workloads, such as relational and non-relational databases, enterprise applications, containerized applications, big data analytics engines, file systems, and media workflows are widely deployed on Amazon EBS.""")
			print("\n")
		os.system("tput setaf 7")
		
		if(int(ach4) == 2):
			azone = input("Enter your availability zone: ")
			asize = input("Enter the size of your EBS in GiB: ")
			avolume = input("Enter your EBS volume type: ")
			os.system("tput setaf 3")
			os.system(" aws ec2 create-volume --availability-zone {} --size {} --volume-type  {}".format(azone, asize, avolume))
			print("\n")
		os.system("tput setaf 7")
	
		if(int(ach4) == 3):
			adevice = input("Enter your device(e.g. sdb): ")
			ainstanceid = input("Enter your Instance ID: ")
			avolumeid = input("Enter your EBS volume ID: ")
			os.system("tput setaf 3")
			os.system("  aws ec2 attach-volume --device {} --instance-id {} --volume-id {} ".format(adevice, ainstanceid, avolumeid))
			print("\n")
		os.system("tput setaf 7")
		
		if(int(ach4) == 4):
			return aws()
		if(int(ach4) >= 5 ):
			os.system("tput setaf 1")
			print("INVALID INPUT")
		os.system("tput setaf 7")

def awss3():
	while(True):
		os.system("tput setaf 3")
		print("""Press 1: to know about S3 storage
Press 2: to configure S3
Press 3: to upload a file from your local computer to S3 storage
Press 4: to go back to main menu""")
		os.system("tput setaf 7")
		print("\n")
		ach5 = input("Enter your choice: ")
		print("\n")
		os.system("tput setaf 7")
		if(int(ach5) == 1):
			os.system("tput setaf 3")
			print("""S3 bucket is one of the many services provided by AWS. It is nothing but public cloud storage where you can store your files, kind of a folder in your pc but unlike pc, you can access it anywhere you want. S3 is an abbreviation of Simple Storage Service. AWS provides many ways to upload a file on the s3 bucket, which are given below:
1. Upload file using Drag and Drop
2. Upload file using click
3. Upload file using aws CLI in the terminal.""")
			print("\n")
		os.system("tput setaf 7")
	
		if(int(ach5) == 2):
			abname = input("Enter your bucket name: ")
			aregion = input("Enter region where you want S3 bucket: ")
			os.system("tput setaf 3")
			os.system(" aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}".format(abname, aregion, aregion))
			os.system("tput setaf 3")
			print("\n")
		os.system("tput setaf 7")
	
		if(int(ach5) == 3):
			apath = input("Enter path of your file located in your local device: ")
			abucketname = input("Enter your S3 bucket name: ")
			abucketfolder = input("Enter your S3 bucket folder name: ")
			os.system(" aws s3 cp {} s3://{}/{} --acl public-read ".format(apath, abucketname, abucketfolder))
			print("\n")
		os.system("tput setaf 7")

		if(int(ach5) == 4):
			return aws()	
		if(int(ach5) >= 5 ):
			os.system("tput setaf 1")
			print("INVALID INPUT")
		os.system("tput setaf 7")
	

def aws():

	#if(int(ach) == 2):
	
	while(True):
		os.system("tput setaf 3")
		os.system('espeak-ng "WELCOME TO AWS WORLD.    Read the choices below and Enter your choice.. "')
		print("""
Press 1: to know about AWS
Press 2: to install AWS CLI
Press 3: to configure AWS
Press 4: to create a key pair
Press 5: for EC2 instance
Press 6: for EBS volume
Press 7: to create IAM user
Press 8: for S3 storage
Press 9: to create Cloudfront distribution
Press 10: to go back to main menu""")
		os.system("tput setaf 7")
		print("\n")
		#ach2 = input("Enter your choice: ")
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("Start Speaking")
			audio = r.listen(source)
			r.pause_threshold = 1
			print("Audio Recorded")
		ach2 = r.recognize_google(audio)
		print(ach2)		
		print("\n")

		if(int(ach2) == 1):
			os.system("tput setaf 3")
			print("""Amazon Web Services (AWS) is a subsidiary of Amazon providing on-demand cloud computing platforms and APIs to individuals, companies, and governments, on a metered pay-as-you-go basis. As of 2020, AWS comprises more than 175 products and services including computing, storage, networking, database, analytics, application services, deployment, management, mobile, developer tools, and tools for the Internet of Things. The AWS Command Line Interface is a unified tool to manage your AWS services.""")	
			os.system('espeak-ng """Amazon Web Services (AWS) is a subsidiary of Amazon providing on-demand cloud computing platforms and APIs to individuals, companies, and governments, on a metered pay-as-you-go basis. As of 2020, AWS comprises more than 175 products and services including computing, storage, networking, database, analytics, application services, deployment, management, mobile, developer tools, and tools for the Internet of Things. The AWS Command Line Interface is a unified tool to manage your AWS services."""')
			print("\n")
		os.system("tput setaf 7")
			
		if(int(ach2) == 2):
			#os.system("tput setaf 3")
			# os.system("pip3 install --upgrade --user awscli")
			os.system(""" curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" """)
			os.system("""unzip awscliv2.zip""")
			os.system("""sudo ./aws/install""")
			os.system("tput setaf 3")			
			print("\nAWS successfully installed\n\nAWS Version: ")	
			os.system("aws --version")
			print("\n")	
		os.system("tput setaf 7")
		
		if(int(ach2) == 3):
			os.system(" aws configure ")
			print("\n")				
		os.system("tput setaf 7")
	
		if(int(ach2) == 4):
			akey = input("Enter key name: ")
			os.system(" aws ec2 create-key-pair --key-name {} ".format(akey))
			print("\n")
		os.system("tput setaf 7")
	
		if(int(ach2) == 5):
			awsec2()

		if(int(ach2) == 6):
			awsebs()
				
		if(int(ach2) == 7):
			auser = input("Enter your user name: ")
			os.system("tput setaf 3")
			os.system(" aws iam create-user --user-name {} ".format(auser))
			print("\n")
		os.system("tput setaf 7")

		if(int(ach2) == 8):
			awss3()

		if(int(ach2) == 9):
			adomain = input("Enter your domain url: ")
			aobject = input("Enter name of your object: ")
			os.system("tput setaf 3")
			os.system(" aws cloudfront create-distribution  --origin-domain-name  {} --default-root-object {} ".format(adomain, aobject))
			print("\n")
		os.system("tput setaf 7")
			
		if(int(ach2) == 10):
			return mainaws()
		os.system("tput setaf 7")
		
		if(int(ach2) >= 11 ):
			os.system("tput setaf 1")
			print("INVALID INPUT")
		os.system("tput setaf 7")

#docker_info()
def docker_info():
	#sos.system("clear")
	print("""Docker is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels.All containers are run by a single operating system kernel and therefore use fewer resources than virtual machines.The service has both free and premium tiers. The software that hosts the containers is called Docker Engine. Docker Inc. was founded by Solomon Hykes and Sebastien Pahl during the Y Combinator Summer 2010 startup incubator group and launched in 2011. Hykes started the Docker project in France as an internal project within dotCloud, a platform-as-a-service company.It was first started in 2013 and is developed by Docker, Inc. """)
	os.system('espeak-ng """Docker is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels.All containers are run by a single operating system kernel and therefore use fewer resources than virtual machines.The service has both free and premium tiers. The software that hosts the containers is called Docker Engine. Docker Inc. was founded by Solomon Hykes and Sebastien Pahl during the Y Combinator Summer 2010 startup incubator group and launched in 2011. Hykes started the Docker project in France as an internal project within dotCloud, a platform-as-a-service company.It was first started in 2013 and is developed by Docker, Inc."""')
			# exit()

		
#docker_install()
def docker_install():
	os.system("clear")
	rc = subprocess.getstatusoutput("rpm -q docker-ce")[0]
	if ( rc == 1 ):
		os.system("mkdir /etc/yum.repos.d/docker.repo ") 
		docker_repo = open("/etc/yum.repos.d/docker.repo" , 'w')
		docker_repo.write(f''' 
		[docker]
		name=Docker-CE
		baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/
		gpgcheck=0 
		''')
		docker_repo.close()		
		os.system("sudo yum install docker-ce --nobest -y")

	else:
		print("Docker-CE is Already installed in your system")


			
		#docker_services()	
def docker_services():
	os.system("clear")
	while True:		
		os.system("wait(10)")
		os.system("clear")		
		print("""\n
[0]. Status of Docker-CE
[1]. Start Docker-CE
[2]. Stop Docker-CE
[3]. Enable Docker-CE
[4]. Disable Docker-CE	
[5]. Restart Docker-CE	
[6]. Go to Docker Menu
		""") 

		user_service_choice = input("What you want to do? ")	

		if int(user_service_choice) == 0:
			print("\t\t\t Press q to go back")			
			os.system("systemctl status docker.service")
			os.system("tput setaf 6")						
		elif int(user_service_choice) == 1:	
			os.system("systemctl start docker.service")
			os.system("tput setaf 6")						
		elif int(user_service_choice) == 2:
			os.system("systemctl stop docker.service")
			os.system("tput setaf 6")						
		elif int(user_service_choice) == 3:
			os.system("systemctl enable docker.service")
			os.system("tput setaf 6")						
		elif int(user_service_choice) == 4:
			os.system("systemctl disable docker.service")
			os.system("tput setaf 6")						
		elif int(user_service_choice) == 5:
			os.system("systemctl restart docker.service")
			os.system("tput setaf 6")						
		elif int(user_service_choice) == 6:
			return docker()
		else:
			print(" NOT SUPPORTED VALUE ") 
#docker_configure()
def docker_configure():	
	def docker_terminate():
		os.system("clear")
		while True:
			os.system("tput setaf 6")						
			print("""\n
			\t\t\t  CONTAINER TERMINATION MENU
			\t\t\t ****************************
[0]. Particular Docker Container
[1]. Back to Configure Menu
			""")
						
			container_delete = int(input("What you want to do?"))
			if int(container_delete == 0):
				container_name = input("Please enter your container name:-  ")
				os.system("sudo docker container rm {}".format(container_name))
			elif int(container_delete == 1):
				return docker_configure()
			else:
				print(" \t\t\t VALUE NOT SUPPORTED ")



	os.system("clear")
	while True:
		os.system("tput setaf 6")
		print("""\n
\t\t\t    DOCKER-CE MAIN MENU
\t\t\t*******************************				

[0]. Download Docker-CE Image
[1]. Launch Docker-CE Container
[2]. Stop Docker-CE Container
[3]. Terminate Docker-CE Container
[4]. List Docker Containers
[5]. Go to Docker-Services Menu
		""") 
		user_container_choice = int(input("What you want to do?  "))
		if int(user_container_choice == 0):
			image_name = str(input("Please provide image name:-  "))
			os.system("sudo docker pull {}".format(image_name))
		elif int(user_container_choice == 1):
			container_name = str(input("Enter Container name:- "))
			imge_name = str(input("Enter Image name:-  "))
			imge_version = input("Enter Image version:-  ")		
			os.system("sudo docker run -it --name {} {}:{}".format(container_name,imge_name,imge_version))
		elif int(user_container_choice == 2):
			container_name = str(input("Enter Container name:- "))
			os.system("sudo docker stop {}".format(container_name))
		elif int(user_container_choice == 3):	
			docker_terminate()
		elif int(user_container_choice == 4):
			os.system("sudo docker container ps -a")
		elif int(user_container_choice == 5):
			return docker()
		else:
			print(" \t\t\t VALUE NOT SUPPORTED  ")	

#docker_images()
def docker_images():
	def docker_delete_images():
		os.system("clear")
		while True:
			os.system("tput setaf 6")						
			print("""\n
\t\t\t    CONTAINER IMAGE DELETION
\t\t\t ******************************
[0]. Particular Docker Image
[1]. Back to Image Menu
""")
					
			image_delete = int(input("What you want to do? "))
			if int(image_delete == 0):
				image_name = str(input("Enter Image name:-  "))
				image_version = input("Enter Image version:-  ")
				os.system("sudo docker rmi -f {}:{}".format(image_name,image_version))
			elif int(image_delete == 1):
				return docker_images()
			else:
				print("\t\t\t VALUE NOT SUPPORTED  ")



	os.system("clear")
	while True:		
		#os.system("wait(10)")
		#os.system("clear")
		os.system("tput setaf 6")	
		print("""\n 
\t\t\t  DOCKER IMAGE SUB-MENU
\t\t\t ***********************
[0]. List Container Images
[1]. Delete Container Images
[2]. Quit from Docker-CE
[3]. Go to Main Menu
""")

		user_image_choice = int(input("What you want to do? "))
		if int(user_image_choice == 0):
			os.system("sudo docker images -a")
		elif int(user_image_choice == 1):
			docker_delete_images()
		elif int(user_image_choice == 2):
			return docker()
		elif int(user_image_choice == 3):	
			return docker()
		else:
			print("\t\t\t VALUE NOT SUPPORTED  ")

#docker_Launch_any_env()
def docker_launch_any_env():
	os.system("clear")
	con_name = str(input("Enter Container name:- "))
	img_name = str(input("Enter Image name:-  "))
	img_version = input("Enter Image version:-  ")
	what_to_install = input("Which software you want to install ?  ")
	what_to_execute = input("Which software you want to execute?  ")	
	os.system("sudo docker run -dit --network host --name {} {}:{}".format(con_name,img_name,img_version))
	os.system("sudo docker exec -it {} yum install {} -y".format(con_name,what_to_install))
	os.system("sudo docker exec -it {} {}".format(con_name,what_to_execute))
		
		
#docker_main_menu_quit()
def docker_main_menu_quit():
	return mainaws()



#Main Function()
#def docker_main():
def docker():
#Cleaning the terminal window
	os.system("clear")

		#os.system("tput setaf 6")
		#print("\t\t\tWELCOME TO DOCKER-CE CONTAINER ENGINE ")
		#os.system("tput setaf 6")
		#print("\t\t\t************************************* ")


		#Input:passwd
		#passwd = getpass.getpass("Please enter your Password:- ")


		#Authorizing the User 
		#if passwd != "docker":              
		#	 print("INVALID PASSWORD!!!")
		#	 exit()

			 
		#os.system("clear")

		# Main Menu 	
	os.system("tput setaf 6")
	print("\t\t\tWELCOME TO DOCKER-CE CONTAINER ENGINE ")
	os.system("tput setaf 6")
	print("\t\t\t************************************* ")

	
	while True:
		os.system("tput setaf 6")
		os.system('espeak-ng "WELCOME TO DOCKER WORLD.    Read the choices below and Enter your choice.. "')
		print("""\t\t\t \n DOCKER-CE MAIN MENU
					\n
[1]. View Docker-Info
[2]. Install Docker-CE
[3]. View Docker-CE Services
[4]. Configure Docker-CE
[5]. Docker-CE Images	
[6]. Launch any env inside Docker-CE	
[7]. Go to Main Menu
		""") 
		os.system("tput setaf 6")
		print("\t\t\t************************************* ")

		print("\n")
		#user_choice = int(input("Please enter your choice:-  ")) 
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("Start Speaking")
			audio = r.listen(source)
			rr.pause_threshold = 1
			print("Audio Recorded")
		user_choice = r.recognize_google(audio)
		print(user_choice)		
		print("\n")
		
		#Docker-CE Sub-Menu functions
		if int(user_choice) == 1:
			docker_info()
				
		elif int(user_choice) == 2:
			docker_install()	

		elif int(user_choice) == 3:
			docker_services()

		elif int(user_choice) == 4:
			docker_configure()

		elif int(user_choice) == 5:
			docker_images()

		elif int(user_choice) == 6:
			docker_launch_any_env()
				
				
		elif int(user_choice) == 7:
			docker_main_menu_quit()
		
		else:
			os.system("tput setaf 1")		
			print("INVALID INPUT")

	
	os.system("tput setaf 7")

	#docker()



											
def webserver():
	
	while True:
		os.system("tput setaf 13")
		os.system('espeak-ng "WELCOME TO WEBSERVER WORLD.    Read the choices below and Enter your choice.. "')
		print("""\nPress 1: to know about Apache Web Server
Press 2: to configure and install webserver
Press 3: to know the status of webserver"
Press 4: to launch Webserver
Press 5: to go back to main menu""")
		os.system("tput setaf 7")
		print("\n")
		#ch=input("Enter Your Choice: ")
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("Start Speaking")
			audio = r.listen(source)
			r.pause_threshold = 1
			print("Audio Recorded")
		ch = r.recognize_google(audio)
		print(ch)		
		print("\n")

		if(int(ch) == 1):
			os.system("tput setaf 13")
			print("""The Apache HTTP Server Project is an effort to develop and maintain an open-source HTTP server for modern operating systems including UNIX and Windows. The goal of this project is to provide a secure, efficient and extensible server that provides HTTP services in sync with the current HTTP standards.
The Apache HTTP Server ("httpd") was launched in 1995 and it has been the most popular web server on the Internet since April 1996. It has celebrated its 25th birthday as a project in February 2020.""")
			os.system('espeak-ng """The Apache HTTP Server Project is an effort to develop and maintain an open-source HTTP server for modern operating systems including UNIX and Windows. The goal of this project is to provide a secure, efficient and extensible server that provides HTTP services in sync with the current HTTP standards. The Apache HTTP Server ("httpd") was launched in 1995 and it has been the most popular web server on the Internet since April 1996. It has celebrated its 25th birthday as a project in February 2020. """')
			print("\n")	
		elif int(ch)  == 2:
			os.system("tput setaf 13")
			os.system("rpm -q httpd")
		elif int(ch) == 3:
			os.system("tput setaf 13")
			os.system("systemctl status httpd")
		elif int(ch) == 4:
			os.system("tput setaf 13")
			print("""\nPress 1: launch Webserver locally
Press 2: launch Webserver remotely
Press 3: launch Webserver on docker
Press 4: launch Webserver on AWS
Press 5: to go back to webserver menu\n""")
			os.system("tput setaf 7")
			ch=input("Enter Your Choice: ")
			x = "$PWD"
			if int(ch)  == 1:
				os.system("tput setaf 13")
				os.system("systemctl start httpd")
				os.system("systemctl status httpd")
			elif int(ch) == 2:
				print("Enter Host IP, username and password")
				ip = input("IP :")
				userName = input("user :")
				#passwd = input("passwd :")
				os.system("tput setaf 13")
				os.system("ssh {0}@{1} systemctl start httpd".format(userName,ip))
			elif int(ch) == 3:
				os.system("tput setaf 13")
				os.system("docker pull httpd")
				os.system("docker run -dit --name my-apache-app -p 8080:80 -v {}:/usr/local/apache2/htdocs/ httpd".format(x))
			elif int(ch) == 4:
				os.system("tput setaf 13")
				print("Will be update in Next Sprint...")
				os.system("tput setaf 7")
			elif int(ch) == 5:
				return webserver()
		elif int(ch) == 5:
			return mainaws()

		os.system("tput setaf 7")

mainaws()



