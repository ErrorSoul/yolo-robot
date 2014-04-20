from subprocess import Popen, PIPE, STDOUT
from subprocess import check_output, call
import time

PASSWORD = "godIS5\n"

apt = "sudo apt-get "  #empty chr in the end for concat str
update = "update"
inst = "install"
rem = "autoremove"


repos = ( "sudo add-apt-repository ppa:snwh/moka-icon-theme-daily",
          "sudo add-apt-repository ppa:numix/ppa",
          "sudo add-apt-repository ppa:noobslab/icons",

          "sudo add-apt-repository ppa:upubuntu-com/nitrux",
         
          "sudo add-apt-repository ppa:tualatrix/next",
          )

apps = ("moka-icon-theme",
        "moka-icon-theme-symbolic", 
        "moka-icon-theme-extras",
        "numix-icon-theme",
        "numix-icon-theme-circle",
        "zoncolor-icons",
        "nitruxos",
        "git",
        "indicator-datetime",
        "ubuntu-tweak",
        "preload",
    ) 

rem_apps = ("unity-lens-music unity-lens-photos "\
            "unity-lens-gwibber unity-lens-shopping unity-lens-video")

def install(command, password=PASSWORD, debug=True):
    if not password.endswith('\n'):
        password += '\n'

    command = command.split()

    if "sudo" in command:
        command.insert(1, "-S")

    if debug:
        print "password --> {0}".format(password)
        print "command  --> {0}".format(command)

    p =  Popen(command, stdin=PIPE, stdout=PIPE)
    if 'install' in command or "autoremove" in command:
	p_stdout = p.communicate('yes\n')[0]
   	print p_stdout
	p.wait()
	time.sleep(5)
    else:
	p_stdout = p.communicate(password)[0]
    	print p_stdout
    	p.wait()
    

install_active = lambda x: lambda y: lambda z : x(y, z)
install_active = install_active(map)(install)
    
def add_repos():
    install_active(repos)

def remove():
    apps_remove = apt + rem + ' ' + rem_apps
    #f = lambda x : apps_remove + x
    #app_rem = map(f, rem_apps)
    install(apps_remove)
        

def upd():
    upd = apt + update
    install(upd)

def install_apps():
    app_inst = apt + inst + " "
    f = lambda x : app_inst + x 
    app_inst = map(f, apps )
    install_active(app_inst)

def main():
    
    add_repos()
    #upd()
    #install_apps()

    remove()
    
    
    

if __name__=="__main__":
    main()













