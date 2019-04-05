# CppQuickCompile

The basic premise behind this is you can write in any old text editor but you don't then need to compile your program and run it by hand this script just 
waits for you to save and then compiles and excutes it all in one go.

Currently waits for CTRL + S but that can be changed at line 70 for whatever you want it to be

There are two modes, Compile Everything and Watchfile. Compile everything will compile everything and watchfile (CTRL - F9) will ask for a file to watch
and only compile that single file

Uses Pynput (Python Module), and gcc (Calls g++)

To use just put it in the same folder as you source code files

I just run the script as is in a seprate terminal window while I type in my editor of choice. 


