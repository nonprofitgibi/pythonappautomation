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
import urllib2 #for downloading

#This downloads any file passed in through the variable URL
def downloader(url,file_name): #this needs to be in a try except thing
        u = urllib2.urlopen(url)
        f = open(file_name, 'wb')
        meta = u.info()
        #print u.info().headers
        file_size = int(meta.getheaders("Content-Length")[0])
        print ("Downloading: %s Bytes: %s") % (file_name, file_size)
        raw_input('Press enter to continue')

        file_size_dl = 0
        block_sz = 8192
        last = 0
        while True:
                buffer = u.read(block_sz)
                if not buffer:
                        break

                file_size_dl += len(buffer)
                f.write(buffer)
                status = r"[%3.2f%%]" % (file_size_dl * 100. / file_size)
                test = status.strip('\%]').strip('[')
                #if float(test) < 100:
                if float(test) > last and int(float(test))%10 == 0:
                        #last = int(float(test)) + 10
                        #if int(float(test))%10 == 0:
                        print str(int(float(test))) + '%',
                        #print test, last
                        last = int(float(test)) + 10
                                        
        print "done"
        print ""

        f.close()
        raw_input("\nYour download has finished, press 'Enter' to continue.")


def generateWhitelist(): #This generates a white-list.txt file in the directory for the server software to use. 
        whitelist_names = raw_input("\n\nUser names of whitelisted players.\nSeparate players with ',' without any spaces (name1,name2,name3): ")
        whitelistSplit = whitelist_names.split(",")
        x = 0
        for name in whitelistSplit:
                whitelistSplit[x] = name.strip(" ")#strips the white space from the front or back of the names
                x += 1
        whitelistLen =  len(whitelistSplit)
        print "\n\nThe following users are now whitelisted: ", whitelistSplit,"\n"
        print "Accept WhiteList?: "
        whitelist = getBool()
        return whitelist, whitelistSplit
        
def writeWhitelist(whitelist):
        i=0
        filename = ("white-list.txt")
        target = open(filename, 'w')
        for i in range (len(whitelist)):
                target.write("%s\n" % whitelist[i])
                i+=1
        target.close

def generateOpsList():
        ops_names = raw_input("\nUser names of Server Operators.\nSeparate players with ',' without any spaces (name1,name2,name3): ")
        opsSplit = ops_names.split(",")
        x = 0
        for name in opsSplit:
                opsSplit[x] = name.strip(" ")#strips the white space from the front or back of the names
                x += 1
        opsLen =  len(opsSplit)
        print "\n\nThe following users are now marked as Operators: ", opsSplit, "\n"
        print "Accept Ops List?: "
        opslist = getBool()
        return opslist, opsSplit

def writeOpsList(ops):
        i=0
        filename = ("ops.txt")
        target = open(filename, 'w')
        for i in range (len(ops)):
                target.write("%s\n" % ops[i])
                i+=1
        target.close

#this function will ask the user for a yes or no option then return a boolean value
def getBool():
        choice = raw_input("(y)es, (n)o: ")
        
        choice = validateY_N(choice)

        if (choice.lower() == 'y'):
                choice = 'true'
        else:
                choice = 'false'
        return choice
def getInt():
        while True:
                userInt = raw_input('Please enter an integer value: ')
                try:
                        userInt = int(userInt)
                        # if we reach this point, that means we got our number
                        return userInt
                except ValueError:
                        # if we reach this point, that means the input was bad
                        print('Invalid input')       
        

#Prompt user to download needed software
def main():
        print "This program is a Minecraft Server installer script, and will install and set up the minecraft server for you."
        java = raw_input("\nBefore we start, do you currently have the latest version of java installed (y)es or (n)o?\n If you don't know enter \"n\": ")
        java = validateY_N(java)
        if java.lower() == 'y':
                val = serverInstaller()
                if not val:
                        print "Thank you"
                        val = serverSetup()
                else:
                        val = serverSetup()
                        if val:
                                print "Thank you"
                                
                        
        else:
                print 'Please install the latest version of Java and try agian.\nJava can be downloaded from http://www.java.com/en/download/manual.jsp?locale=en'

        
                

def serverInstaller():
        install = raw_input ("\nDownload the minecraft server software? (y)es or (n)o? ")
        install = validateY_N(install)
        print install

        if install == "n":
                val = False

        elif install == "y":
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
        java = validateY_N(java)
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

        print "\nEnable whitelist?: "
        whitelist = raw_input("If you are unsure of whitelist choose 'n': (y)es (n)o: ")
        whitelist = validateY_N(whitelist)

        while whitelist == ("y"):
                #generates whitelist
                T_F, whitelist = generateWhitelist()
                if T_F == "true":
                        writeWhitelist(whitelist)
                        whitelisted = "true"
                        break
                        
        if whitelist == ("n"):
                whitelisted = "false"

        print "\nEnable Ops?: "
        ops = raw_input("If you are unsure of enableing ops list choose \"n\": (y)es (n)o: ")
        ops = validateY_N(ops)
        while ops == ("y"):
                T_F, ops = generateOpsList()
                if T_F == "true":
                        writeOpsList(ops)
                        opsList = 'true'
                        break

        if ops == "n":
                opsList = "false"
        else:
                opsList = "true"

        generateServerSettings(worldName, whitelisted, opsList)


def generateServerSettings(worldName, whitelist, opsList):
        #This gets the manually set options for the server
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

        options = raw_input("\n\nwould you like to change the default settings? (y)es (n)o: ")
        options = validateY_N(options)
        #FIX>>> Users Must type true/false for most variable or else it will print their inapropriate answer to the prop file. We need to allow for the users to type either yes, true, no or false without a failure
        if options == ("y"):
                print ("\n\nenable monsters?")
                monsters = getBool()
                print monsters
                
                print ("\n\nspawn animals?")
                animals = getBool()
                print animals
                
                print("\n\nspawn NPCs?")
                npc = getBool()
                print npc
                
                print("\n\ngenerate structures?")
                structures = getBool()
                print structures
                
                print("\n\nenable pvp?")
                pvp = getBool()
                print pvp
                
                print "\n\nOnly disable this option if you don't want to validate the players."
                print("enable online mode?")
                online = getBool()
                print online
                #online mode can be more than just true or false it can or used to be able to be set to all but that might not be the case anymore and all wasn't any differnt from false
                
                print "\n\nif a character dies their banned from the server"
                print("enable hardcore mode?")
                hardcore = getBool()
                print hardcore
                
                print "\n\nif not sure set to 25565"
                choice = raw_input("Change port number?: ")
                choice = validateY_N(choice)
                print choice               
                if choice == 'y':
                        print "Port number"
                        port = getInt()
                        while port < 0 or port > 65535:
                                print "Ports are between 0 and 65535 please enter a valid number"
                                port = getInt()
                else:
                        port = '25565'
                port =  str(port)
                print port
                #need function to check for proper input -- Tanner done
                
                print "\n\nChoose no if not sure."
                print("enable rcon?")
                rcon = getBool()
                print 
                
                print "\n\nused for generating maps, if unsure leave blank"
                seed = raw_input("Map seed: ")
                #need function to check for proper input
                error = True
                #while error:
                #        seed, error = checkSeed(seed, error)
                #need function to check for proper input, this can only be a set of whole non-negative numbers and or characters.
                                
                print "\n\nChoose no if not sure"       
                print("enable query?")
                query = getBool()
                
                print "\n\n(1.survival) (2.creative)"
                gamemode = raw_input("gamemode?: ")
                gamemode = validate1_2(gamemode)
                #need function to check for proper input
                
                print "\n\n(0.peacefull)(1.easy) (2.normal) (3.hard)"
                difficulty = getInt()
                while difficulty < 0 or difficulty > 3:
                        print 'Difficulty must be between 0 and 3.'
                        print 'Please try again: '
                        difficulty = str(getInt())

                difficulty = str(difficulty)
                #need function to check for proper input
                
                print "\n\nMessage to apear on server list"
                motd = raw_input("MOTD: ")

                print "\n\nreccomended 256"
                print "Build height?: "
                build = getInt()
                
                #to the best of my knowlage 256 is the max anything below that is well acceptable but I wonder what goes on below if you set it negative could it cause issues or what so time for some
                #digging through minecraft source or some research because no one seems to care about a min just a max --Tanner also from the sounds of it bukkit has a build height max of 400 ish
                while build > 256:
                        print "build height max is 256 please try agian"
                        build = getInt()
                build =  str(build)
                
                #need function to check for proper input
                
                print "\n\n(1.default) (2.flatland) default reccomended"
                Map_type = raw_input("map type? 1-2: ")
                Map_type = validate1_2(Map_type)
                #need function to check for proper input
                #going to create list and check if in list then valid else figure out what they ment or get valid input along with all other string inputs  -- Tanner
                
                print "\n\nIf not sure leave blank"
                generator_settings = raw_input("generator settings: ")
                
                print "\n\nreccomended 10"
                print "View distance?: "
                view = getInt()
                #need function to check for proper input
                
                print("\n\nallow nether?")
                nether = getBool()
                
                print("\n\nallow flight?")
                flight= getBool()
                
                print "\n\nIf unsure select true"
                print("Snooper setting.")
                snooper= getBool()

                print ("Max players?: ")
                max_players = str(getInt())
                #need function to check for proper input
                #new settings need to set up q&a for them but its 2am so I'll get it tomorrow
                print ("Op permission level: ")
                oplvl= str(getInt())
                while oplvl > 4 or oplvl < 1:
                        print ("Op permission level can only be number 1 through 4 please try agian")
                        oplvl = str(getInt())
                        
                print ("Announce player achievements?")
                playerAchievements = getBool()
                
                print ("Force gamemode when logging in, default is false?")
                forceGamemode = getBool()
                
                print ("Command Block, default is false")
                commandBlock = getBool()
                
                print ("Spawn Protection time? Measured in minutes.")
                spawnProtection = str(getInt())
                #while spawnProtection > max or < min:
                print ("Rcon port, default 25575?")
                rconPort = str(getInt())
                while port < 0 or port > 65535:
                        print "Ports are between 0 and 65535 please enter a valid number"
                        port = str(getInt())
                
                print ("Query port, default 25565")
                queryPort = str(getInt())
                while port < 0 or port > 65535:
                        print "Ports are between 0 and 65535 please enter a valid number"
                        port = str(getInt())
                
                print ("Rcon password default is blank")
                rconPasword = raw_input()
                #validation loop for passoword is needed
                
                print ("Server name?: ")
                serverName = raw_input()
                
                print ("Resourse kit, default is blank: ")
                resource = raw_input()
                
                print ("How long until player times out")
                playerTimeout = str(getInt())
                #validation loop

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
                snooper= "true"
                max_players= "20"
                #new settings for newer servers
                oplvl="4"
                playerAchievements="true"
                forceGamemode = "false"
                commandBlock = "false"
                spawnProtection = "16"
                rconPort = "25575"
                queryPort = "25565"
                rconPasword = ""
                serverName = "Python generated server"
                resource = ""
                playerTimeout = "0"
                rconPassword = ""
                spawnProtection = "16"



        #write settings to system.properties file
        server_props = ("""generator_settings=%s
op-permission-level=%s
allow-nether=%s
level-name=%s
enable-query=%s
allow-flight=%s
announce-player-achievements=%s
server-port=%s
server-name=%s
query.port=%s
level-type=%s
enable-rcon=%s
rcon.password=%s
rcon.port=%s
force-gamemode=%s
level-seed=%s
server-ip=%s
max-build-height=%s
resource-pack=%s
spawn-ncps=%s
white-list=%s
spawn-animals=%s
hardcore=%s
snooper-enabled=%s
online-mode=%s
pvp=%s
player-idle-timeout=%s
difficulty=%s
enable-command-block=%s
gamemode=%s
max-players=%s
spawn-monsters=%s
generate-structures=%s
view-distance=%s
spawn-protection=%s
motd=%s"""%(generator_settings,oplvl, nether, worldName, query, flight, playerAchievements, port, 
            serverName, queryPort, Map_type, rcon, rconPassword, rconPort, forceGamemode, seed, ip,
            build, resource, npc, whitelist, animals, hardcore, snooper, online, pvp, playerTimeout,
            difficulty, commandBlock, gamemode, max_players, monsters, structures, view,
            spawnProtection, motd))

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
        while not(options.lower() == 'y' or options.lower() == 'n'):
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
                print options, "is not a valid answer"
                options = raw_input("Enter a \"1\" or a \"2\". ")
        return options

def checkSeed(seed,error):
        for val in seed:
                if not val.isaalpha():
                        if int(val) < 0:
                                print "Invalid seed please try agian"
                                return 0, error
        error = False
        return seed, error
                                

main()

#create desktop shortcut with icon to startup script

#get python to run the batch file
#               The following is me testing to see if I can get python to start the server.
##start_server = raw_input("Would you like to start your server now? (y)es (n)o: ")
##if start_server == ("y"):
##        import subprocess
##
##        p = subprocess.Popen('start-server.bat', creationflags=subprocess.CREATE_NEW_CONSOLE)
