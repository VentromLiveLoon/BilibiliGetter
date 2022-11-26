#!/bin/bash

if pyinstaller --version
then
    pyinstaller main.py 
else
    echo "Please install the pyinstaller"
    exit
fi

rm -rfv $HOME/.local/share/bilibiliGetter
mkdir -p $HOME/.local/share/
cp -rfv ./dist/main/ $HOME/.local/share/bilibiliGetter
ln -s $HOME/.local/share/bilibiliGetter/main $HOME/.local/bin/bilibiliGetter




echo    "W    W                               WWWWW                        W  W  W"  
echo    "W    W                               W                            W  W  W"  
echo    "W    W                               W                            W  W  W"  
echo    "W    W   WWWW   W   W   WWWW         W      W    W  W WWW         W  W  W"  
echo    "WWWWWW       W  W   W  W    W        WWWW   W    W  WW   W        W  W  W"  
echo    "W    W   WWWWW  W   W  WWWWWW        W      W    W  W    W        W  W  W"  
echo    "W    W  W    W   W W   W             W      W    W  W    W        W  W  W"  
echo    "W    W  W   WW   W W   W    W        W      W   WW  W    W               " 
echo    "W    W   WWW W    W     WWWW         W       WWW W  W    W        W  W  W"  


echo "Done"
echo "                                                               Made by Live_Windstorm"