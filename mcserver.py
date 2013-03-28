#
# title		Minecraft Server Automation Script
#
# description	Script to automate the installation of a minecraft server, and Java
#
# authors	Kenneth Andrews, Tanner Gibson
#
# licence	Gnu General Public License v2.0
#
# Copyright	2013 Kenneth Andrews, Tanner Gibson
#..........................................................................................
import sys
import urllib

print "Minecraft Server install script"

install = raw_input ("would you like to install minecraft server? (y)es (n)o: ")
if install == ("n"):
	sys.exit()

print "Vannillia is the origional Server straight from minecraft.net, Bukkit is oriented towards modders. if you are unsure choose vanilla"
server_type = raw_input ("Which version would you like to download? 1-2: ")

if server_type == ("1"):
	url = ("https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft_server.jar")
if server_type == ("2"):
	url = ("http://dl.bukkit.org/downloads/craftbukkit/get/01845_1.4.7-R1.0/craftbukkit.jar")

source = urllib.urlopen(url).read()
filename = ("mcserver.jar")
file = open(filename,'w')
file.write(source)
file.close()


java = raw_input("Would you like the script to try and automatically install java?: ")
if java == ("y"):
	if sys.platform == ("win32"):
                #install windows java
		pass
	elif sys.platform == ("linux") or sys.platform == ("linux2"):
		#install linux java
		pass
	else:
		print ("Sorry, the script was unable to detect your operating system. please install java manually.")
else:
	pass

admin = raw_input("Name of Admin?: ")


print "If you are unsure of whitelist choose no"
whitelist = raw_input("enable whitelist?: (y)es (n)o ")

if whitelist == ("y"):
	whitelist_names = raw_input("User names of whitelisted players. serparate players with ','")

elif whitelist == ("n"):
	pass

monsters = raw_input("enable monsters?: ")

animals = raw_input("spawn animals?: ")

npc = raw_input("spawn NPCs?: ")

structures = raw_input("generate structures?: ")

pvp = raw_input("enable pvp?: ")

print "Only disable this option if you will be playing without internet"
online = raw_input("enable online mode?: ")

print "if a character dies their banned from the server"
hardcore = raw_input("enable hardcore mode?: ")

print "if not sure set to 25565"
port = raw_input("port number?: ")

print "disable if not sure"
rcon = raw_input("enable rcon?: ")

print "used for generating maps, if unsure leave blank"
seed = raw_input("map seed?: ")

print "URL link for Texture pack download, if unsure leave blank"
texture = raw_input("texture pack?: ")

print "if unsure disable"
query = raw_input("enable query?: ")

print "(1.survival) (2.creative)"
gamemode = raw_input("gamemode?: ")

print "(1.easy) (2.normal) (3.hard)"
difficulty = raw_input("difficulty? 1-3")

print "Message to apear on server list"
motd = raw_input("MODT?: ")

print "reccomended 256"
build = raw_input("build height?: ")

print "(1.default) (2.flatland) default reccomended"
Map_type = raw_input("map type? 1-2: ")

print "if not sure leave blank"
generator_settings = raw_input("generator settings?: ")

print "reccomended 10"
view = raw_input("view distance?: ")

#write to file ./server.properties & ./whitelist & ./op

#create batch/bash script in server directory to start server
#create desktop shortcut with icon to startup script

start_server = raw_input("Would you like to start your server now? (y)es (n)o: ")
#	if yes
#		start startup script

