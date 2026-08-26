# TAGLINE

退出登录 shell

# TLDR

**退出登录 shell**

```logout```

# SYNOPSIS

**logout** [_status_]

# PARAMETERS

_STATUS_
> 退出状态码（可选）。

# DESCRIPTION

**logout** 退出登录 shell。它终止当前的 shell 会话并返回到登录提示符。

该命令是 shell 内置命令，只在登录 shell 中有效，在子 shell 中无效。

# CAVEATS

只在登录 shell 中有效。非登录 shell 请使用 exit。属于 shell 内置命令。

# HISTORY

logout 是 bash 及其他 shell 中可用的 **shell 内置**命令，用于终止登录会话。

# SEE ALSO

[exit](/man/exit)(1), [login](/man/login)(1), [bash](/man/bash)(1)
