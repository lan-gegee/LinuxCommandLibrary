# TAGLINE

管理 TeX Live 平台架构

# TLDR

**列出受支持的架构**

```tlmgr arch```

**仅列出已安装项**

```tlmgr arch --installed```

**添加架构**

```tlmgr arch add [x86_64-linux]```

**移除架构**

```tlmgr arch remove [i386-linux]```

# SYNOPSIS

**tlmgr arch** [_action_] [_arch_...]

# PARAMETERS

**--installed**
> 仅显示已安装的架构。

**add** _arch_
> 添加平台二进制文件。

**remove** _arch_
> 移除平台二进制文件。

**list**
> 列出可用架构。

# DESCRIPTION

**tlmgr arch** 管理 TeX Live 的平台支持。安装其他架构的二进制文件可用于跨平台 TeX 发行。TeX Live Manager 的组成部分。

# SEE ALSO

[tlmgr-platform](/man/tlmgr-platform)(1), [tlmgr](/man/tlmgr)(1)
