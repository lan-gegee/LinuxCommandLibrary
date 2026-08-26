# TAGLINE

查找给定文件路径的默认 SELinux 安全上下文

# TLDR

查找绝对路径的**持久安全上下文**设置

```matchpathcon [/path/to/file]```

将查找限制为**特定文件类型**上的设置

```matchpathcon -m [file|dir|pipe|chr_file|blk_file|lnk_file|sock_file] [/path/to/file]```

**校验**持久上下文与当前上下文是否一致

```matchpathcon -V [/path/to/file]```

# SYNOPSIS

**matchpathcon** [_options_] _path_...

# PARAMETERS

**-m _type_**
> 将查找限制为特定文件类型：file、dir、pipe、chr_file、blk_file、lnk_file 或 sock_file

**-V**
> 校验当前上下文是否符合预期的持久上下文

**-n**
> 输出中不显示路径

**-N**
> 不在策略中查找上下文

**-P _policy_path_**
> 使用备用的策略根路径

# DESCRIPTION

**matchpathcon** 根据文件上下文配置，查找给定文件路径的默认 SELinux 安全上下文。它显示的是按照 SELinux 策略文件**应当**具有的上下文，而不管其当前上下文如何。

这对诊断 SELinux 问题很有用——将预期上下文（来自 matchpathcon）与实际上下文（来自 **ls -Z**）进行对比，就能发现文件是否被错误标记。

**-V**（verify）选项直接比较预期上下文和实际上下文，报告可能导致 SELinux 拒绝访问的不匹配情况。

# CAVEATS

仅适用于启用了 SELinux 的系统。查找基于文件路径模式而非实际的文件属性。一个路径可能匹配多个模式；以最具体的模式为准。此命令显示的是策略默认值，而不是运行时覆盖。

# INSTALL

```apt: sudo apt install selinux-utils```

```dnf: sudo dnf install libselinux-utils```

```apk: sudo apk add libselinux-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[semanage-fcontext](/man/semanage-fcontext)(8), [restorecon](/man/restorecon)(8), [chcon](/man/chcon)(1), [secon](/man/secon)(1), [ls](/man/ls)(1)
