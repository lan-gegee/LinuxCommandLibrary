# TAGLINE

管理 pacman 用于防止并发操作的 libalpm 数据库锁文件

# TLDR

**锁定**数据库

```sudo paclock```

将**锁文件路径**写到标准输出（不实际加锁）

```paclock --print```

**解锁**数据库

```sudo paclock --unlock```

显示**帮助**

```paclock --help```

# SYNOPSIS

**paclock** [_options_]

# PARAMETERS

**--unlock**
> 移除数据库锁而不是创建锁

**--print**
> 仅打印锁文件路径而不执行任何操作

**--run** _command_
> 在数据库保持锁定的情况下运行命令，然后解锁

**--config** _file_
> 使用备用的 pacman 配置文件

**--dbpath** _path_
> 使用备用的数据库路径

**--root** _path_
> 使用备用的安装根目录

**--help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**paclock** 管理 libalpm 数据库锁文件，pacman 用它防止并发的软件包管理操作。它允许手动锁定或解锁数据库，适用于需要独占访问数据库的脚本，或者用于清理残留的失效锁。

锁文件可防止多个 pacman 进程同时修改软件包数据库而导致损坏。通常 pacman 会自动处理锁定，但 paclock 在需要时提供了直接控制手段。

# CAVEATS

修改锁文件需要 root 权限。在 pacman 运行期间手动解锁可能导致数据库损坏。请谨慎使用；除非正在排查具体问题，否则应优先让 pacman 自动管理锁。

# HISTORY

属于 **pacutils**，Andrew Gregory 编写的 pacman 工具集。为高级使用场景提供显式的锁管理，也可用于恢复因 pacman 进程崩溃而遗留的失效锁文件。

# SEE ALSO

[pacman](/man/pacman)(8), [pactrans](/man/pactrans)(8), [flock](/man/flock)(1)
