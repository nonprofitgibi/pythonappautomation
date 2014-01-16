#
# title         Minecraft Server Automation Script
#
# description   Script to automate the installation of a minecraft server, and Java
#
# authors       Kenneth Andrews, Tanner Gibson, Fredrick Paulin
#
# licence       Gnu General Public License v2.0
#
# Copyright     2014 Kenneth Andrews, Tanner Gibson, Fredrick Paulin
#..........................................................................................
import sys #for quitting application and looking at operating system
import socket #to find IP address of the machine
import urllib2 #for downloading

#This downloads any file passed in through the variable URL
def downloader(url):
        u = urllib2.urlopen(url)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"[%3.2f%%]" % (file_size_dl * 100. / file_size)
            print status
            print ""

        f.close()
        finishedDownload = raw_input("Your download has finished, press 'Enter' to continue.")

#This generates a white-list.txt file in the directory for the server software to use. 
def writeWhitelist():
        whitelist_names = raw_input("User names of whitelisted players.\nSeparate players with ',' without any spaces (name1,name2,name3): ")
        whitelistSplit = whitelist_names.split(",")
        whitelistLen =  len(whitelistSplit)
        print "The following users are now whitelisted: ", whitelistSplit
        i=0
        filename = ("white-list.txt")
        target = open(filename, 'w')
        for i in range (0, whitelistLen):
                target.write("%s\n" % whitelistSplit[i])
                i+=1
        target.close
        

#Prompt user to download needed software
print "Minecraft Server install script"
install = raw_input ("Download the minecraft server software? (y)es, (n)o, or any other key to exit: ")
if install == ("n"):
        pass
elif install == ("y"):
        file_name = "mcserver.jar"
        print "Choose the server version you would like to download, and wait for the download to finish..."
        print "1. Vanilla\n2. Bukkit"
        print "Vanillia is the origional Server straight from minecraft.net,\nBukkit is oriented towards modders. If you are unsure choose vanilla."

        server_type = raw_input ("Which version would you like to download? (1 or 2): ")

        if server_type == ("1"): #Downloads Minecraft Server file based on users choice
                url = ("https://s3.amazonaws.com/Minecraft.Download/versions/1.7.4/minecraft_server.1.7.4.jar")
                downloader(url)
        
        if server_type == ("2"):
                url = ("http://dl.bukkit.org/downloads/craftbukkit/get/01845_1.4.7-R1.0/craftbukkit.jar")
                downloader(url)
else:
        sys.exit()


#Prompts user to download the most recently available version of java
        ## We should see if there is a way to automatically detect what version of java they are currently using and see if there is a newer version avilable maybe looking into the Java API would be useful for this
java = raw_input("Would you like the script to download java? (y)es (n)o: ")
if java == ("y"):
        print ("Your system has been detected as %s. It is reccomended that you install Java manually before continuing installation of server." % sys.platform)

        if sys.platform == ("win32"): #If OS is detected as windows downloads java.exe
                java = raw_input ("Would you like to try to download the current version of Java for %s? (y)es (n)o: " % sys.platform)
                if java == ("y"):
                        url=("http://download.oracle.com/otn-pub/java/jdk/7u45-b18/jre-7u45-windows-i586-iftw.exe")
                        file_name = url.split('/')[-1]
                        downloader(url)
                        
                elif java == ("n"):
                        pass

        elif sys.platform == ("linux") or sys.platform == ("linux2"): #If OS is detected as Linux downloads java.tar.gz
                java = raw_input ("Would you like to try to download the current version of Java for %s? (y)es (n)o: " % sys.platform)
                if java == ("y"):
                        url = ("http://download.oracle.com/otn-pub/java/jdk/7u45-b18/jre-7u45-linux-i586.tar.gz")
                        file_name = url.split('/')[-1]
                        downloader(url)

                
                elif java == ("n"):
                        pass
        elif sys.platform == ("darwin"): #If OS is detected as darwin (Macintosh) downloads java.dmg for mac
                
                java = raw_input ("Would you like to try to download the current version of Java for %s? (y)es (n)o: " % sys.platform)
                if java == ("y"):
                        url = ("http://download.oracle.com/otn-pub/java/jdk/7u51-b13/jre-7u51-macosx-x64.dmg")
                        file_name = url.split('/')[-1]
                        downloader(url)

                
                elif java == ("n"):
                        pass

        else:
                print ("Sorry, the script was unable to detect your operating system. Please install java manually by going to: http://www.oracle.com/technetwork/java/javase/downloads/jre7-downloads-1880261.html")


## I'm working on finding a way to do this, it won't be easy though. --Fredrick
#       check for platform again, and decide how to install java based on sys.platform
#       if sys.platform == ("win32"):
#               install .\java.exe

#       elif sys.platform == ("linux") or sys.platform == ("linux2"):
#               extract, and install ./java.tar.gz

else:
        pass

admin = raw_input("Name of Admin?: ")

print "If you are unsure of whitelist choose 'n'"
whitelist = raw_input("Enable whitelist?: (y)es (n)o: ")

if whitelist == ("y"):
        #generates whitelist
        writeWhitelist()

elif whitelist == ("n"):
        pass


#displays the current IP address that Python detects automatically and asks the user if it is correct
print "Now to set the IP address of the server. The current IP detected by this program is: %s" % socket.gethostbyname(socket.gethostname())

isCorrectIP= raw_input("Is this your current IP address? If you're not sure search Google for 'What is my IP address?' (y)es (n)o: ")
if isCorrectIP == ('n'):
        ip = raw_input ('Please enter the IP address of the machine the server is running on: ')
else:
        ip = socket.gethostbyname(socket.gethostname())

print ("The rest of the settings are optional. If you choose 'n' they will be set to defaults")




#This gets the manually set options for the server
options = raw_input("would you like to change the default settings? (y)es (n)o: ")

if options == ("y"):
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
        print "(0.peacefull)(1.easy) (2.normal) (3.hard)"
        difficulty = raw_input("difficulty? 0-3: ")
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
        nether = raw_input("allow nether (true), (false)?: ")
        flight= raw_input("allow flight?: ")
        print "Now this one is a hard one if unknown google how to find it we are working on how to find server ip address"
        ip= raw_input("server ip: ")
        debug= raw_input("debugging: ")
        snooper= raw_input("snooper setting: ")
        max_players= raw_input("max player: ")
else:
        ##Default Minecraft server properties via http://minecraft.gamepedia.com/Server.properties as of 1/12/14
        ##Generates values for default set 
        monsters = "true"
        animals = "true"
        npc = "true"
        structures = "true"
        pvp = "true"
        online = "true"
        hardcore = "false"
        port = "25565"
        rcon = "false"
        seed = ""
        texture =""
        query = "false"
        gamemode = "0"
        difficulty = "1"
        motd = "Auto Generated Minecraft Server"
        build = "256"
        Map_type = "1"
        generator_settings = ""
        view = "10"
        nether = "true"
        flight= "false"
        debug= ""
        snooper= "true"
        max_players= "20"      



#write settings to system.properties file
server_props = ("""generator_settings=%s
allow-nether=%s
level-name=world
enable-query=%s
allow-flight=%s
server-port=%s
query.port=%s
evel-type=%s
enable-rcon=%s
level-seed=%s
server-ip=%s
max-build-height=%s
spawn-ncps=%s
white-list=%s
debug=%s
spawn-animals=%s
texture-pack=%s
snooper-enabled=%s
hardcore=%s
online-mode=%s
pvp=%s
difficulty=%s
gamemode=%s
max-players=%s
spawn-monsters=%s
generate-structures=%s
view-distance=%s
spawn-protection=false
motd=%s
"""%(generator_settings, nether, query, flight, port, port, Map_type, rcon, seed, ip, build,
npc, whitelist, debug, animals, texture, snooper, hardcore, online, pvp, difficulty,
gamemode, max_players, monsters, structures, view, motd))

filename = ("server.properties")
target = open(filename, 'w')
target.write(server_props)
target.close


#if system is detected as windows attempt to create a batch file as an easier way to start the program
if sys.platform == ("win32"):
        #create batch/bash script in server directory to start server
        batch = "java -Xms512M -Xmx1G -jar mcserver.jar"
        filename = ("start-server.bat")
        target = open(filename, 'w')
        target.write(batch)
        target.close
        
print "The program has finished setting up your server!"
done = raw_input("Press 'Enter' to exit")
sys.exit()



#create desktop shortcut with icon to startup script

#get python to run the batch file
#               The following is me testing to see if I can get python to start the server.
##start_server = raw_input("Would you like to start your server now? (y)es (n)o: ")
##if start_server == ("y"):
##        import subprocess
##
##        p = subprocess.Popen('start-server.bat', creationflags=subprocess.CREATE_NEW_CONSOLE)
