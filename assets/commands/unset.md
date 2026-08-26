# TAGLINE

移除 shell 变量或函数

# TLDR

**取消设置变量**

```unset [VARIABLE]```

**取消定义函数**

```unset -f [function_name]```

**取消设置多个变量**

```unset [VAR1] [VAR2]```

**显式取消变量（而非函数）**

```unset -v [VARIABLE]```

# SYNOPSIS

**unset** [_-f_] [_-v_] _name_ ...

# PARAMETERS

**-f**
> 取消函数定义。

**-v**
> 取消变量（默认）。

**-n**
> 取消 nameref 变量本身，而不是它所引用的变量。

_name_
> 要取消设置的名称。

# DESCRIPTION

**unset** 是一个 shell 内建命令，用于从当前 shell 环境中移除变量和函数定义。默认移除变量，而使用 **-f** 标志则改为移除函数定义。

取消设置一个变量会将其从环境中完全移除，这与把它设为空字符串不同——后者变量仍有定义但值为空。对于需要区分"变量是否存在"与"变量是否有值"的脚本来说，这一区别很重要。取消导出的变量也会将其从子进程继承的环境中移除。

unset 所做的更改仅影响当前 shell 会话。在 shell 启动文件（如 ~/.bashrc）中定义的变量和函数会在新会话启动时恢复。只读变量无法被取消设置。

# CAVEATS

shell 内建命令（POSIX）。无法取消只读变量（返回错误）。更改仅影响当前 shell 会话。-n 选项是 bash 的扩展，并非所有 POSIX shell 都支持。

# HISTORY

**unset** 是标准的 shell 内建命令，用于从 shell 环境中移除变量和函数。

# SEE ALSO

[export](/man/export)(1), [set](/man/set)(1), [env](/man/env)(1)
