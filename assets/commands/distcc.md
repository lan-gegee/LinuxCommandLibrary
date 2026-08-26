# TAGLINE

跨网络主机进行分布式 C/C++ 编译

# TLDR

**使用 distcc 编译**

```distcc [gcc] -c [file.c] -o [file.o]```

**设置用于分发的主机**

```export DISTCC_HOSTS="[host1] [host2] [localhost]"```

**配合 make 使用 distcc**

```make -j [8] CC="distcc gcc"```

**监控编译**

```distccmon-text [1]```

**显示主机状态**

```distcc --show-hosts```

# SYNOPSIS

**distcc** [_compiler_] [_args_]

# DESCRIPTION

**distcc** 将 C/C++ 编译任务分布到网络中的多台机器上。它把预处理输出发送到远程主机进行编译，通过在可用 CPU 之间并行化来加速大型构建。

该工具作为编译器包装器，根据主机的可用性和负载决定本地编译还是远程编译。对支持 CC 变量覆盖的构建系统而言它是透明的。

# PARAMETERS

**--show-hosts**
> 打印 distcc 将要使用的主机列表，然后退出。

**--scan-includes**
> 打印将要发送到服务器的文件列表，然后退出。

**--version**
> 显示 distcc 客户端版本。

**-j**
> 打印并发级别（服务器数量乘以每台主机的上限）。

**--help**
> 显示帮助信息。

# ENVIRONMENT

**DISTCC_HOSTS**：以空格分隔的主机列表
**DISTCC_DIR**：覆盖状态目录
**DISTCC_LOG**：日志文件路径
**DISTCC_VERBOSE**：启用详细日志

# HOST SPECIFICATION

**hostname**：简单主机名
**hostname:port**：带自定义端口
**hostname/limit**：限制发往该主机的作业数
**@hostname**：SSH 模式
**--localslots=N**：本地作业槽位

# CONFIGURATION

**~/.distcc/hosts**
> 用于分布式编译的 distcc 主机列表。

**/etc/distcc/hosts**
> 系统级 distcc 主机配置。

**~/.distcc/state**
> 存放 distcc 日志和临时文件的状态目录。

# CAVEATS

所有主机需要相同版本的编译器。对小文件而言网络延迟会增加开销。预处理始终在本地完成。头文件必须在本地可用。

# HISTORY

**distcc** 由 **Martin Pool** 于 **2002** 年在 Linuxcare 创建。它满足了加速 Linux 内核和大型项目构建的需求。该工具在开源开发中被广泛使用，后来交由社区维护。

# INSTALL

```apt: sudo apt install distcc```

```dnf: sudo dnf install distcc```

```pacman: sudo pacman -S distcc```

```apk: sudo apk add distcc```

```zypper: sudo zypper install distcc```

```brew: brew install distcc```

```nix: nix profile install nixpkgs#distcc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[distccd](/man/distccd)(1), [ccache](/man/ccache)(1), [make](/man/make)(1), [gcc](/man/gcc)(1)

# RESOURCES

```[Source code](https://github.com/distcc/distcc)```

```[Homepage](https://www.distcc.org)```

<!-- verified: 2026-07-11 -->
