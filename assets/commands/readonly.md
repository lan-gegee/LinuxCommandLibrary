# TAGLINE

将 shell 变量标记为只读

# TLDR

**将变量设为只读**

```readonly [VAR]="[value]"```

**将已有变量设为只读**

```readonly [VAR]```

**列出只读变量**

```readonly```

**将函数设为只读**

```readonly -f [function_name]```

**将数组设为只读**

```readonly -a [ARRAY]```

# SYNOPSIS

**readonly** [_options_] [_name_[=_value_]...]

# PARAMETERS

**-p**
> 打印只读变量。

**-f**
> 将函数设为只读。

**-a**
> 将数组设为只读。

**-A**
> 将关联数组设为只读。

# DESCRIPTION

**readonly** 是一个 shell 内建命令，它把变量或函数标记为只读，防止修改或 unset。适用于常量以及保护配置值。

# EXAMPLES

```bash
# Create readonly variable
readonly PI=3.14159

# Attempting to change fails
PI=3  # bash: PI: readonly variable

# Make existing readonly
CONFIG_FILE="/etc/app.conf"
readonly CONFIG_FILE

# Readonly function
myfunc() { echo "Hello"; }
readonly -f myfunc

# List all readonly
readonly -p

# Readonly array
readonly -a COLORS=("red" "green" "blue")
```

# IN SCRIPTS

```bash
#!/bin/bash
readonly SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
readonly CONFIG="${SCRIPT_DIR}/config.ini"
readonly VERSION="1.0.0"
```

# CAVEATS

无法 unset 只读变量（直到 shell 退出）。子 shell 不继承只读状态。这是 bash 特有的。

# HISTORY

readonly 是 **POSIX** shell 内建命令，bash 和其他现代 shell 对其做了选项扩展。

# SEE ALSO

[declare](/man/declare)(1), [export](/man/export)(1), [typeset](/man/typeset)(1), [bash](/man/bash)(1)
