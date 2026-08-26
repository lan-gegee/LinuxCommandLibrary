# TAGLINE

修复 SELinux 文件安全上下文

# TLDR

**恢复**整个系统的 SELinux 上下文

```fixfiles restore```

在**下次启动**时重新标记文件系统

```fixfiles onboot```

**强制重置**可定制文件的上下文

```fixfiles -F restore```

恢复**指定 RPM** 软件包的上下文

```fixfiles -R package1,package2 restore```

只处理在某日期**之后创建**的文件

```fixfiles -N "2024-01-01" restore```

**详细**输出

```fixfiles -v restore```

重新标记前先**绑定挂载**文件系统

```fixfiles -M restore```

# SYNOPSIS

**fixfiles** [_options_] {**restore**|**check**|**onboot**|**relabel**|**verify**}

# DESCRIPTION

**fixfiles** 用于修复系统中文件的 SELinux 安全上下文。它是 restorecon 和 setfiles 的封装脚本，提供了便捷的全系统重新标记功能。

# PARAMETERS

**-B**
> 记录当前日期，供以后配合 restore 使用，以加快标记速度

**-F**
> 强制重置可定制文件的上下文

**-f**
> 不经确认直接清空 /tmp 目录

**-R PACKAGES**
> 找出特定 RPM 软件包内的文件并恢复其上下文

**-C FILECONTEXT**
> 与先前的 file_contexts 做比较，恢复受影响的文件

**-N DATE**
> 只处理在指定日期（YYYY-MM-DD HH:MM）之后创建的文件

**-M**
> 重新标记前先把文件系统绑定挂载

**-v**
> 详细模式；运行 restorecon 时用 -v 代替 -p

**restore**
> 将文件上下文恢复为默认值

**check**
> 仅检查文件上下文，不做修改

**onboot**
> 安排在下次启动时重新标记

**relabel**
> 重新标记整个文件系统

**verify**
> 校验文件上下文是否符合策略

# CONFIGURATION

**/etc/selinux/[policy]/contexts/files/file_contexts**
> 默认的 SELinux 文件上下文规则，为各路径定义安全标签。

# CAVEATS

全盘重新标记文件系统可能耗时很久。先用 -B 搭配 onboot，再执行 restore，可以加快之后的重新标记速度。前提是系统已启用 SELinux。

# HISTORY

**fixfiles** 属于 **policycoreutils** 软件包，为基于 Red Hat 的系统提供 SELinux 文件上下文管理工具。

# INSTALL

```apt: sudo apt install policycoreutils```

```dnf: sudo dnf install policycoreutils```

```zypper: sudo zypper install policycoreutils```

```nix: nix profile install nixpkgs#policycoreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[restorecon](/man/restorecon)(8), [setfiles](/man/setfiles)(8), [chcon](/man/chcon)(1)

# RESOURCES

```[Source code](https://github.com/SELinuxProject/selinux)```

<!-- verified: 2026-07-15 -->
