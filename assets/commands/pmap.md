# TAGLINE

报告进程的内存映射

# TLDR

打印进程的**内存映射**

```pmap 1234```

显示**扩展格式**

```pmap -x 1234```

显示**设备格式**

```pmap -d 1234```

将结果限制在**内存地址范围**内

```pmap -A low,high 1234```

打印**多个进程**的内存映射

```pmap 1234 5678```

显示内核提供的**全部信息**

```pmap -XX 1234```

# SYNOPSIS

**pmap** [_options_] _pid_ [...]

# DESCRIPTION

**pmap** 报告一个或多个进程的内存映射。它展示每个进程如何分配和使用内存，包括映射的文件、堆、栈和共享库。

# PARAMETERS

**-x, --extended**
> 以扩展格式显示更多细节

**-d, --device**
> 显示设备格式的输出

**-q, --quiet**
> 不显示页眉和页脚行

**-A, --range low,high**
> 将结果限制在指定的地址范围内

**-X**
> 提供 -x 选项之外的额外细节

**-XX**
> 显示内核提供的全部信息

**-p, --show-path**
> 在映射列中包含完整文件路径

**-c, --read-rc**
> 加载默认配置

**-C, --read-rc-from file**
> 从指定文件加载配置

**-n, --create-rc**
> 生成新的默认配置

**-N, --create-rc-to file**
> 将配置生成到指定文件

# CAVEATS

退出码 0 表示成功，1 表示失败，42 表示未能找到所有请求的进程。内存值默认以千字节为单位显示。

# HISTORY

**pmap** 是 **procps-ng** 软件包的一部分，为 Linux 提供进程文件系统工具。它从 /proc/[pid]/maps 及相关文件读取信息。

# INSTALL

```apt: sudo apt install procps```

```dnf: sudo dnf install procps-ng```

```pacman: sudo pacman -S procps-ng```

```apk: sudo apk add procps-ng```

```zypper: sudo zypper install procps```

```brew: brew install procps```

```nix: nix profile install nixpkgs#procps```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ps](/man/ps)(1), [pgrep](/man/pgrep)(1), [proc](/man/proc)(5)
