# TAGLINE

更改当前工作目录

# TLDR

**切换到指定目录**

```chdir [path/to/directory]```

**切换到主目录**

```chdir ~```

**切换到上级目录**

```chdir ..```

**切换到上一个目录**

```chdir -```

# SYNOPSIS

**chdir** [_directory_]

# DESCRIPTION

**chdir** 将 shell 的当前工作目录更改为指定路径。它在功能上与 **cd** 等价，是 zsh、csh 和 tcsh 中的内置命令。

不带参数调用时，它会切换到用户的主目录。如果指定的目录相对于当前目录不存在，则会搜索 **CDPATH** 变量。

# CAVEATS

**chdir** 在 bash 中不可用（应使用 **cd**）。为保证脚本可移植性，请始终使用 **cd**。该命令是 shell 内置命令，不作为独立可执行文件存在。

# HISTORY

**chdir** 是 **Unix** 中目录切换系统调用的原始名称，可追溯到 **1971** 年的**第一版**。**cd** 命令是后来引入的更短别名。**csh**（1978）以及后来的 **zsh** 等 shell 在保留 **cd** 的同时，也将 **chdir** 作为内置命令保留了下来。

# SEE ALSO

[cd](/man/cd)(1), [pushd](/man/pushd)(1), [popd](/man/popd)(1), [pwd](/man/pwd)(1)
