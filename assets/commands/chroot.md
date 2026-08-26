# TAGLINE

为命令更改根目录

# TLDR

**以不同的根目录运行命令**

```sudo chroot [path/to/new_root] [command]```

**在新根目录中运行交互式 Shell**

```sudo chroot [path/to/new_root]```

**指定要运行的自定义 Shell**

```sudo chroot [path/to/new_root] /bin/bash```

**为命令指定用户和组**

```sudo chroot --userspec=[user:group] [path/to/new_root] [command]```

**chroot 后切换到指定目录**

```sudo chroot [path/to/new_root] /bin/sh -c "cd /home && ls"```

# SYNOPSIS

**chroot** [_OPTION_] _NEWROOT_ [_COMMAND_ [_ARG_]...]

# DESCRIPTION

**chroot** 将调用进程的根目录更改为指定路径，并在该环境中运行一个命令。所有以 **/** 开头的路径查找都将相对于新的根目录进行。

如果未指定命令，chroot 会运行 **SHELL** 环境变量指定的 Shell，默认为 **/bin/sh**。

新的根目录必须包含被执行命令所需的全部文件、库和设备节点。

# PARAMETERS

**NEWROOT**
> 用作新根文件系统的目录

**COMMAND**
> 在 chroot 环境中运行的命令

**ARG**
> 传递给命令的参数

**--userspec=**_USER:GROUP_
> 指定运行所用的用户和组（名称或 ID）

**--groups=**_GROUPS_
> 指定附加组

**--skip-chdir**
> 不将工作目录切换到 /

# CAVEATS

需要 root 权限或 **CAP_SYS_CHROOT** 能力。它并非为安全沙箱而设计——特权用户可以通过创建目录并使用相对路径逃逸。已打开的文件描述符可能提供 chroot 之外的访问。

新根目录必须包含必要的文件：**/bin/sh** 或指定命令、所需的共享库（可用 **ldd** 检查），以及必要时如 **/dev/null** 等设备节点。

# HISTORY

**chroot** 系统调用起源于贝尔实验室的 **Version 7 Unix**（1979 年），最初用于构建和测试新版本的系统。GNU coreutils 版本在 Linux 系统上提供标准的命令行界面。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[arch-chroot](/man/arch-chroot)(1), [pivot_root](/man/pivot_root)(8), [unshare](/man/unshare)(1)

# RESOURCES

```[Source code](https://github.com/coreutils/coreutils)```

```[Documentation](https://www.gnu.org/software/coreutils/manual/html_node/chroot-invocation.html)```

<!-- verified: 2026-06-22 -->
