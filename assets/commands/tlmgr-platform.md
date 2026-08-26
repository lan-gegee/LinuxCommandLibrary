# TAGLINE

管理 TeX Live 平台二进制文件

# TLDR

**列出平台**

```tlmgr platform list```

**添加平台**

```tlmgr platform add [x86_64-darwin]```

**移除平台**

```tlmgr platform remove [i386-linux]```

**设置当前平台**

```tlmgr platform set [x86_64-linux]```

# SYNOPSIS

**tlmgr platform** _action_ [_platform_...]

# PARAMETERS

**list**
> 列出可用平台。

**add** _platform_
> 添加平台二进制文件。

**remove** _platform_
> 移除平台二进制文件。

**set** _platform_
> 设置当前平台。

# DESCRIPTION

**tlmgr platform** 管理 TeX Live 平台二进制文件。功能与 tlmgr arch 相同。安装多操作系统支持。TeX Live Manager 的组成部分。

# SEE ALSO

[tlmgr-arch](/man/tlmgr-arch)(1), [tlmgr](/man/tlmgr)(1)
