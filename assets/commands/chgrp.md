# TAGLINE

更改文件的组所有权

# TLDR

**更改文件的所属组**

```chgrp [group] [path/to/file]```

**递归更改目录的所属组**

```chgrp -R [group] [path/to/directory]```

**使用参考文件更改组**

```chgrp --reference=[path/to/reference_file] [path/to/file]```

**更改符号链接本身的组**

```chgrp -h [group] [path/to/symlink]```

**详细更改组，显示每个处理的文件**

```chgrp -v [group] [path/to/file]```

**更改组，仅在发生更改时显示**

```chgrp -c [group] [path/to/file]```

# SYNOPSIS

**chgrp** [_OPTION_...] _GROUP_ _FILE_...

**chgrp** [_OPTION_...] **--reference=**_RFILE_ _FILE_...

# DESCRIPTION

**chgrp** 将每个指定文件的组所有权更改为给定的组。组可以通过名称或数字 GID 指定。

Linux 中所有文件既属于一个所有者，也属于一个组。**chown** 更改用户所有权，而 **chgrp** 专门处理组所有权的更改。

# PARAMETERS

**-c, --changes**
> 仅在发生更改时报告（类似 verbose 但更安静）

**-f, --silent, --quiet**
> 屏蔽大多数错误信息

**-v, --verbose**
> 为每个处理的文件输出诊断信息

**-h, --no-dereference**
> 影响符号链接本身而非其所指向的文件

**-R, --recursive**
> 递归地操作文件和目录

**--reference=**_RFILE_
> 使用 RFILE 的组而不是指定 GROUP

**递归遍历选项（配合 -R）：**

**-H** - 遍历命令行中的符号链接
**-L** - 遍历所有指向目录的符号链接
**-P** - 不遍历符号链接（默认）

# CAVEATS

只有 root 或文件所有者才能更改组所有权。普通用户只能将文件改为自己所属的组。可使用 **ls -l** 查看当前的组所有权。

# HISTORY

**chgrp** 是标准 Unix 命令，可追溯到早期的 Unix 系统。GNU coreutils 版本由 David MacKenzie 编写，是大多数 Linux 发行版上使用的实现。

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

[chown](/man/chown)(1), [chmod](/man/chmod)(1), [groups](/man/groups)(1), [ls](/man/ls)(1)

# RESOURCES

```[Source code](https://github.com/coreutils/coreutils)```

```[Documentation](https://www.gnu.org/software/coreutils/manual/html_node/chgrp-invocation.html)```

<!-- verified: 2026-06-22 -->
