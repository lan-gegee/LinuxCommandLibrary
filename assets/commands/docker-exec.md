# TAGLINE

在运行中的容器内执行命令

# TLDR

**在容器内运行命令**

```docker exec [container] [command]```

**打开交互式 shell**

```docker exec -it [container] /bin/bash```

**以指定用户身份运行**

```docker exec -u [root] [container] [command]```

**设置环境变量**

```docker exec -e [VAR=value] [container] [command]```

**在指定目录中运行**

```docker exec -w [/path] [container] [command]```

# SYNOPSIS

**docker** **exec** [_options_] _container_ _command_ [_args..._]

# PARAMETERS

**-d**, **--detach**
> 在后台运行命令。

**-i**, **--interactive**
> 保持 STDIN 打开。

**-t**, **--tty**
> 分配伪终端。

**-u**, **--user** _user_
> 用户名或 UID。

**-w**, **--workdir** _dir_
> 容器内的工作目录。

**-e**, **--env** _list_
> 设置环境变量。

**--env-file** _file_
> 从文件读取环境变量。

**--detach-keys** _sequence_
> 覆盖从容器分离所用的按键序列。

**--privileged**
> 授予扩展权限。

# DESCRIPTION

**docker exec** 在运行中的容器的现有环境里执行新命令，在容器的命名空间和 cgroup 内创建一个新进程。这与 **docker run** 有本质区别——后者会创建一个全新的容器。

最常见的用法是用 **docker exec -it container /bin/bash** 打开交互式 shell 进行调试，直接访问容器的文件系统和运行中的进程。通过 **docker exec** 执行的命令会继承容器的环境，但可以通过用户、工作目录和环境变量等选项进行定制。

**--privileged** 标志授予扩展能力，适合系统管理任务，但由于它会削弱容器隔离性，应谨慎使用。

# CAVEATS

容器必须处于运行状态。命令会继承容器的环境。交互式 shell 需将 **-it** 配合使用。**--privileged** 标志会降低容器隔离性，应尽量少用。

# INSTALL

```apt: sudo apt install docker-cli```

```dnf: sudo dnf install docker-cli```

```pacman: sudo pacman -S docker```

```apk: sudo apk add docker-cli```

```zypper: sudo zypper install docker```

```brew: brew install docker```

```nix: nix profile install nixpkgs#docker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker-container-exec](/man/docker-container-exec)(1), [docker-run](/man/docker-run)(1)
