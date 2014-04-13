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
def downloader(url,file_name): #this needs to be in a try except thing
        u = urllib2.urlopen(url)
        f = open(file_name, 'wb')
        meta = u.info()
        #print u.info().headers
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)
        raw_input('Press enter to continue')

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
        raw_input("\nYour download has finished, press 'Enter' to continue.")


def writeWhitelist(): #This generates a white-list.txt file in the directory for the server software to use. 
        whitelist_names = raw_input("\n\nUser names of whitelisted players.\nSeparate players with ',' without any spaces (name1,name2,name3): ")
        whitelistSplit = whitelist_names.split(",")
        x = 0
        for name in whitelistSplit:
                whitelistSplit[x] = name.strip(" ")#strips the white space from the front or back of the names
                x += 1
        whitelistLen =  len(whitelistSplit)
        print "\n\nThe following users are now whitelisted: ", whitelistSplit,"\n"
        i=0
        filename = ("white-list.txt")
        target = open(filename, 'w')
        for i in range (0, whitelistLen):
                target.write("%s\n" % whitelistSplit[i])
                i+=1
        target.close

def writeOpsList():
        ops_names = raw_input("\nUser names of Server Operators.\nSeparate players with ',' without any spaces (name1,name2,name3): ")
        opsSplit = ops_names.split(",")
        x = 0
        for name in opsSplit:
                opsSplit[x] = name.strip(" ")#strips the white space from the front or back of the names
                x += 1
        opsLen =  len(opsSplit)
        print "\n\nThe following users are now marked as Operators: ", opsSplit, "\n"
        i=0
        filename = ("ops.txt")
        target = open(filename, 'w')
        for i in range (0, opsLen):
                target.write("%s\n" % opsSplit[i])
                i+=1
        target.close

#this function will ask the user for a yes or no option then return a boolean value
def getBool():
        choice = raw_input("(y)es, (n)o: ")
        
        choice = validateY_N(choice)

        if (choice.lower == 'y'):
                choice = 'true'
        else:
                choice = 'false'
        return choice
        
        

#Prompt user to download needed software
def main():
        print "This program is a Minecraft Server installer script, and will install and set up the minecraft server for you."
        java = raw_input("\nBefore we start, do you currently have the latest version of java installed (y)es or (n)o?\n If you don't know enter \"n\": ")
        java = validateY_N(java)
        if java.lower() == 'y':
                val = serverInstaller()
                if not val:
                        print "Thank you"
                else:
                        val = serverSetup()
                        if val:
                                print "Thank you"
                                
                        
        else:
                print 'Please install the latest version of Java and try agian.\nJava can be downloaded from http://www.java.com/en/download/manual.jsp?locale=en'

        
                

def serverInstaller():
        install = raw_input ("\nDownload the minecraft server software? (y)es or (n)o? ")
        install = validateY_N(install)

        if install.lower == ("n"):
                val = False

        else:
                file_name = "mcserver.jar"
                print "\nChoose the server version you would like to download, and wait for the download to finish..."  
                print "Vanillia is the original Server straight from minecraft.net, Bukkit is oriented towards modders. If you are unsure choose vanilla."
                print "(1. Vanilla)(2. Bukkit)"

                file_name = "minecraft_server.jar"
                server_type = raw_input ("\nWhich version would you like to download? (1 or 2): ")
                server_type = validate1_2(server_type)

                if server_type == ("1"): #Downloads basic Minecraft Server file based on users choice
                        url = ("https://s3.amazonaws.com/Minecraft.Download/versions/1.7.7/minecraft_server.1.7.7.jar")
                        downloader(url,file_name)
                
                if server_type == ("2"): #downloads mod friendly server
                        url = ("http://dl.bukkit.org/downloads/craftbukkit/get/01845_1.4.7-R1.0/craftbukkit.jar")
                        downloader(url,file_name)
                val = True
        return val



#Prompts user to download the most recently available version of java
        ## We should see if there is a way to automatically detect what version of java they are currently using and see if there is a newer version avilable maybe looking into the Java API would be useful for this
#currently I am not going to try to install java and if java is not installed then I will ask for them to install java first then come back and re run this program.
def javaInstaller():
        java = raw_input("Would you like the script to download java? (y)es (n)o: ")
        if java == ("y"):

                if sys.platform == ("win32"): #If OS is detected as windows downloads java.exe
                        java = raw_input ("\nWould you like to try to download the current version of Java for Windows? (y)es (n)o: ")
                        java = validateY_N(java)
                        if java == ("y"):
                                url=("http://download.oracle.com/otn-pub/java/jdk/7u45-b18/jre-7u45-windows-i586-iftw.exe")
                                file_name = url.split('/')[-1]
                                downloader(url)
                                
                        elif java == ("n"):
                                pass

                elif sys.platform == ("linux") or sys.platform == ("linux2"): #If OS is detected as Linux downloads java.tar.gz
                        java = raw_input ("\nIt is reccomended you Install java through your Distribution repo would you like to download Java anyways? (y)es (n)o: ")
                        java = validateY_N(java)
                        if java == ("y"):
                                url = ("http://download.oracle.com/otn-pub/java/jdk/7u45-b18/jre-7u45-linux-i586.tar.gz")
                                file_name = url.split('/')[-1]
                                downloader(url)

                        
                        elif java == ("n"):
                                pass
                elif sys.platform == ("darwin"): #If OS is detected as darwin (Macintosh) downloads java.dmg for mac
                        
                        java = raw_input ("\nWould you like to try to download the current version of Java for Mac? (y)es (n)o: ")
                        java = validateY_N(java)
                        if java == ("y"):
                                url = ("http://download.oracle.com/otn-pub/java/jdk/7u51-b13/jre-7u51-macosx-x64.dmg")
                                file_name = url.split('/')[-1]
                                downloader(url)

                        
                        elif java == ("n"):
                                pass

                else:
                        print ("\nSorry, the script was unable to detect your operating system. Please install java manually by going to: http://www.oracle.com/technetwork/java/javase/downloads/jre7-downloads-1880261.html")


        ## I'm working on finding a way to do this, it won't be easy though. --Fredrick
        #       check for platform again, and decide how to install java based on sys.platform
        #       if sys.platform == ("win32"):
        #       could we just launch the java installer for microsoft --Tanner
        #               install .\java.exe

        #       elif sys.platform == ("linux") or sys.platform == ("linux2"):
        #               extract, and install ./java.tar.gz
        #       could we run either yum or apt-get for this we would have to have adimin privliges and ask for them but it could work --Tanner oh and we would probably be able to ask a linux user to tell us their distro
        

        else:
                pass

#writeOpsList()
def serverSetup():
        worldName = raw_input("\n\nWhat do you want to name your world?  ")

        print "\nEnable whitelist?"
        whitelist = raw_input("If you are unsure of whitelist choose 'n': (y)es (n)o: ")
        whitelist = validateY_N(whitelist)

        if whitelist == ("y"):
                #generates whitelist
                writeWhitelist()

        elif whitelist == ("n"):
                val = False
        ip = urllib2.urlopen('http://ip.42.pl/raw').read()
        print ip
        #FIX>>>>>This is currently not functional. It detects Local host "127.0.0.1" rather than external ipadress -Kenneth Andrews
        #displays the current IP address that Python detects automatically and asks the user if it is correct
        print ("\nNow to set the IP address of the server. The current IP detected by this program is: %s" % ip)

        isCorrectIP= raw_input("Is this your current IP address? If you're not sure search Google for 'What is my IP address?' (y)es (n)o: ")
        isCorrectIP = validateY_N(isCorrectIP)
        if isCorrectIP == ('n'):
               ip = raw_input ('\nPlease enter the IP address of the machine the server is running on: ')
        else:
                ip = urllib2.urlopen('http://ip.42.pl/raw').read()

        print ("\nThe rest of the settings are optional. If you choose 'n' they will be set to defaults")
        generateServerSettings(worldName)


def generateServerSettings(worldName):
        #This gets the manually set options for the server
        options = raw_input("\n\nwould you like to change the default settings? (y)es (n)o: ")
        options = validateY_N(options)

        #FIX>>> Users Must type true/false for most variable or else it will print their inapropriate answer to the prop file. We need to allow for the users to type either yes, true, no or false without a failure
        if options == ("y"):
                print ("\n\nenable monsters?")
                monsters = getBool()
                
                print ("\n\nspawn animals?")
                animals = getBool()
                
                print("\n\nspawn NPCs?")
                npc = getBool()
                
                print("\n\ngenerate structures?")
                structures = getBool()
                
                print("\n\nenable pvp?")
                pvp = getBool()
                
                print "\n\nOnly disable this option if you will be playing without internet"
                print("enable online mode?")
                online = getBool()
                
                print "\n\nif a character dies their banned from the server"
                print("enable hardcore mode?")
                hardcore = getBool()
                
                print "\n\nif not sure set to 25565"
                port = raw_input("port number: ")
                #place in try
                while int(port) < 0 or int(port) > 65535:
                        print "Ports are between 0 and 65535 please enter a valid number"
                        port = raw_input()
                #need function to check for proper input -- Tanner done
                
                print "\n\nChoose no if not sure."
                print("enable rcon?")
                rcon = getBool()
                
                print "\n\nused for generating maps, if unsure leave blank"
                seed = raw_input("map seed: ")
                #need function to check for proper input
                #I don't beleave that seeds really have any restrictions I've looked into it and I'm going to look at the actuall code but
                #I think the only restriction would be the actual length of the seed is too long possibly 256 or something of the sorts -- Tanner
                
                print "\n\nURL link for Texture pack download, if unsure leave blank"
                texture = raw_input("texture pack URL: ")
                #need function to check for proper input, and also is this supposed to download the server pack?
                
                print "\n\nChoose no if not sure"       
                print("enable query?")
                query = getBool()
                
                print "\n\n(1.survival) (2.creative)"
                gamemode = raw_input("gamemode?: ")
                gamemode = validate1_2(gamemode)
                #need function to check for proper input
                
                print "\n\n(0.peacefull)(1.easy) (2.normal) (3.hard)"
                difficulty = raw_input("difficulty? 0-3: ")
                #need function to check for proper input
                
                print "\n\nMessage to apear on server list"
                motd = raw_input("MOTD: ")
                
                print "\n\nreccomended 256"
                build = raw_input("build height?: ")
                #need function to check for proper input
                
                print "\n\n(1.default) (2.flatland) default reccomended"
                Map_type = raw_input("map type? 1-2: ")
                Map_type = validate1_2(Map_type)
                #need function to check for proper input
                #going to create list and check if in list then valid else figure out what they ment or get valid input along with all other string inputs  -- Tanner
                
                print "\n\nIf not sure leave blank"
                generator_settings = raw_input("generator settings: ")
                
                print "\n\nreccomended 10"
                view = raw_input("view distance?: ")
                #need function to check for proper input
                
                print("\n\nallow nether?")
                nether = getBool()
                
                print("\n\nallow flight?")
                flight= getBool()
                
                print("\n\nEnable debugging?")
                debug= getBool()
                
                print "\n\nIf unsure select true"
                print("snooper setting.")
                snooper= getBool()
                
                max_players= raw_input("\n\nmax players: ")
                #need function to check for proper input

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
level-name=%s
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
motd=%s"""%(generator_settings, nether, worldName, query, flight, port, port, Map_type, rcon, seed, ip, build,
        npc, whitelist, debug, animals, texture, snooper, hardcore, online, pvp, difficulty,
        gamemode, max_players, monsters, structures, view, motd))

        filename = ("server.properties")
        target = open(filename, 'w')
        target.write(server_props)
        target.close


        #if system is detected as windows attempt to create a batch file as an easier way to start the program
        if sys.platform == ("win32"):
                #create batch/bash script in server directory to start server
                batch = "java -Xms512M -Xmx1G -jar minecraft_server.jar"
                filename = ("start-server.bat")
                target = open(filename, 'w')
                target.write(batch)
                target.close
                
        print "\n\n\nThe program has finished setting up your server!"
        done = raw_input("Press 'Enter' to exit")
        sys.exit()

def validateY_N(options):
        while not(options.lower() != 'y' or options.lower() != 'n'):
                if options.lower() == 'yes':
                        options = 'y'
                elif options.lower() == 'no':
                        options = 'n'
                else:
                        print "Invalid input please input please try agian"
                        options = raw_input('Please type a "y" for yes or a "n" for no.')
        return options

def validateT_F(options):
        while not(options != 'true' or options != 'false'):
                if options.lower() == 'true':
                        options = 'true'
                elif options.lower() == 'false':
                        options = 'false'
                else:
                        print "invalid input please type either \"true\" or \"false\". "
                        options = raw_input()
        return options

def validate1_2(options):
        while not(options == '1' or options == '2'):
                print server_type, "is not a valid answer"
                options = raw_input("Enter a \"1\" or a \"2\". ")

main()

#create desktop shortcut with icon to startup script

#get python to run the batch file
#               The following is me testing to see if I can get python to start the server.
##start_server = raw_input("Would you like to start your server now? (y)es (n)o: ")
##if start_server == ("y"):
##        import subprocess
##
##        p = subprocess.Popen('start-server.bat', creationflags=subprocess.CREATE_NEW_CONSOLE)
