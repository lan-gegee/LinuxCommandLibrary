# TAGLINE

管理 TeX Live 的系统 PATH 集成

# TLDR

**将 TeX Live 加入 PATH**

```tlmgr path add```

**从 PATH 中移除**

```tlmgr path remove```

# SYNOPSIS

**tlmgr path** _action_

# PARAMETERS

**add**
> 将 TeX Live 添加到系统 PATH。

**remove**
> 将 TeX Live 从系统 PATH 移除。

# DESCRIPTION

**tlmgr path** 管理 TeX Live 与系统 PATH 的集成。在 /usr/local/bin 中创建或移除指向 TeX 程序的符号链接。TeX Live Manager 的组成部分。

# CAVEATS

需要 root 权限。可能与系统的 TeX 软件包冲突。

# SEE ALSO

[tlmgr](/man/tlmgr)(1)
