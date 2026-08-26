# TAGLINE

更改文件访问权限

# TLDR

**使**文件可执行

```chmod +x [script.sh]```

**设置**特定权限

```chmod 755 [file]```

**移除**写权限

```chmod -w [file]```

**递归**更改

```chmod -R 755 [directory/]```

以符号方式**设置**权限

```chmod u=rwx,g=rx,o=r [file]```

# SYNOPSIS

**chmod** [_options_] _mode_ _file_...

# DESCRIPTION

**chmod**（change mode）修改文件的访问权限。它控制三类用户的读、写、执行权限：文件所有者（user）、文件所属组（group）以及其他所有用户。

权限可以用两种方式指定：使用数字 0-7 的数字（八进制）模式，或使用字母的符号模式（u/g/o/a、+/-/=、r/w/x）。数字模式一次性设置所有权限，而符号模式允许添加或移除单个权限。该命令是 Unix 文件安全与访问控制的基础。

# PARAMETERS

**-R**, **--recursive**
> 递归地更改文件和目录

**-v**, **--verbose**
> 详细输出

**-c**, **--changes**
> 仅报告更改

**--reference=**_file_
> 使用参考文件的权限

# NUMERIC MODE

八进制数字（0-7）：
- **4** - 读
- **2** - 写
- **1** - 执行

**常见模式：**
- **755** - rwxr-xr-x（所有者全权，其他人可读/执行）
- **644** - rw-r--r--（所有者可读/写，其他人只读）
- **600** - rw-------（仅所有者）
- **777** - rwxrwxrwx（全部权限，通常是不好的做法）

# SYMBOLIC MODE

格式：**[ugoa][+-=][rwxXst]**

**对象：**
- **u** - 用户（所有者）
- **g** - 组
- **o** - 其他人
- **a** - 所有

**操作：**
- **+** - 添加权限
- **-** - 移除权限
- **=** - 设置精确权限

**权限：**
- **r** - 读
- **w** - 写
- **x** - 执行
- **X** - 仅对目录执行
- **s** - setuid/setgid
- **t** - 粘滞位

# WORKFLOW

```bash
# Make script executable
chmod +x script.sh

# Set standard file permissions
chmod 644 file.txt

# Set directory permissions
chmod 755 directory/

# Recursive change
chmod -R 755 public_html/

# Remove write for group and others
chmod go-w file.txt

# Add execute for all
chmod a+x program

# Set exact permissions
chmod u=rwx,g=rx,o= private_script
```

# SPECIAL MODES

**Setuid (4000)：**
> 以文件所有者身份运行

**Setgid (2000)：**
> 以文件所属组身份运行，或在目录中继承目录组

**Sticky (1000)：**
> 仅所有者可删除（常用于 /tmp）

示例：`chmod 4755 program`（setuid + rwxr-xr-x）

# CAVEATS

需要所有权或 root 权限。777 权限存在安全风险。递归更改可能破坏系统。符号链接不受影响（某些系统上可用 chmod -h）。对文件与目录执行 execute 的含义不同。

# HISTORY

**chmod** 自 **20 世纪 70 年代初**起就是 Unix 的一部分，实现了由 Dennis Ritchie 和 Ken Thompson 设计的 Unix 权限模型。

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

[chown](/man/chown)(1), [chgrp](/man/chgrp)(1), [umask](/man/umask)(1), [ls](/man/ls)(1)

# RESOURCES

```[Source code](https://github.com/coreutils/coreutils)```

```[Documentation](https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html)```

<!-- verified: 2026-06-22 -->
