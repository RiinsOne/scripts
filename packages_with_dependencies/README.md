## Python script which allow to download recursively all .deb packages's dependencies of application.


#### Download or copy script and run it with one or more arguments
```{r, engine='bash', count_lines}
$python3 get_depends.py nano htop
```

#### It will create a folder with the app name and move all their dependecies there.
```{r, engine='bash', count_lines}
$ls
get_depends.py  htop  nano

$ls htop/
gcc-6-base_6.0.1-0ubuntu1_amd64.deb
htop_2.0.1-1ubuntu1_amd64.deb
libc6_2.23-0ubuntu11_amd64.deb
libgcc1_1%3a6.0.1-0ubuntu1_amd64.deb
libncursesw5_6.0+20160213-1ubuntu1_amd64.deb
libtinfo5_6.0+20160213-1ubuntu1_amd64.deb
```
