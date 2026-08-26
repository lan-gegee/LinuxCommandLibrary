# TAGLINE

移除 shell 函数定义

# TLDR

**移除一个 shell 函数**

```unfunction [function_name]```

**移除多个函数**

```unfunction [function1] [function2]```

**移除匹配模式的函数**

```unfunction -m "[pattern]*"```

**对未定义的名称强制移除而不报错**

```unfunction -f [function_name]```

# SYNOPSIS

**unfunction** [_-fm_] _name_ [_name ..._]

# PARAMETERS

**-m**
> 将每个 _name_ 视为模式（使用标准 zsh 模式匹配），移除所有名称匹配的函数。

**-f**
> 当给定名称不对应已定义的函数时抑制错误。

# DESCRIPTION

**unfunction** 是 zsh 内建命令，用于从当前会话中移除一个或多个 shell 函数的定义。移除后，调用该函数名将导致 "command not found" 错误，除非存在同名的外部命令或别名。

它相当于 bash 中 **unset -f** 的 zsh 等价物，可用于清理函数定义、重新加载修改后的函数文件，或撤销自动加载的函数。

# CAVEATS

仅在 zsh 中可用。在 bash 中请改用 **unset -f**。移除操作仅影响当前 shell 会话，不会修改函数定义文件。移除自动加载的函数后，如果 autoload 注册仍然有效，下次使用时会重新自动加载。

# HISTORY

**unfunction** 在 **zsh** 中作为专门的函数移除命令引入，与 Z Shell 的 **autoload** 和函数定义机制相辅相成。

# SEE ALSO

[autoload](/man/autoload)(1), [unset](/man/unset)(1), [zsh](/man/zsh)(1)
