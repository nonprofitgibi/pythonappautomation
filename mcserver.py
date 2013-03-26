#
# title		Minecraft Server Automation Script
#
# description	Script to automate the installation of a minecraft server, and Java
#
# authors	Kenneth Andrews, Tanner Gibson
#
# licence	GPL.V2
#..........................................................................................

print "Minecraft Server install script"

print "would you like to install Minecraft Server?"

install = raw_input ("would you like to install minecraft server? (y)es (n)o: ")
#if yes continue, if no close

print "Vannillia is the origional Server straight from minecraft.net, Bukkit is oriented towards modders. if you are unsure choose vanilla"
server_type = raw_input ("Which version would you like to download? 1-2: ")

#if user chose vanillia download from minecraft.net
#if user chose Bukkit download from Bukkit.org

#check to see if Java is installed
	#if no install java

admin = raw_input("Name of Admin?: ")

print "If you are unsure of whitelist choose no"
whitelist = raw_input("enable whitelist?")
	if yes
	#ask for user input - names for white list

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
	if yes
	start startup script

exit
