# TAGLINE

以 32 位十六进制值显示当前主机的唯一标识符

# TLDR

**显示主机 ID**

```hostid```

**显示版本**

```hostid --version```

**显示帮助**

```hostid --help```

# SYNOPSIS

**hostid** [_option_]

# PARAMETERS

**--help**
> 显示帮助后退出。

**--version**
> 显示版本后退出。

# DESCRIPTION

**hostid** 以 32 位十六进制值显示当前主机的唯一标识符。若 **/etc/hostid** 存在，则打印其中存储的值；否则通过 **gethostid**(3) 函数根据机器的主机名和 IP 地址推导。该标识符在历史上被软件授权方案使用，在现代 Linux 系统上基本是一项遗留特性。

# CAVEATS

该值**不保证跨机器唯一**，尤其是当它由主机名推导而非来自固定的 **/etc/hostid** 文件时。它没有任何安全价值，不应作为硬件指纹使用。

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

[hostname](/man/hostname)(1), [uname](/man/uname)(1)

# RESOURCES

```[Source code](https://git.savannah.gnu.org/cgit/coreutils.git)```

```[Documentation](https://www.gnu.org/software/coreutils/manual/coreutils.html)```

<!-- verified: 2026-07-19 -->
