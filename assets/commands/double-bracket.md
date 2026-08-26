# TAGLINE

bash/zsh 的增强条件表达式

# TLDR

**测试条件（bash/zsh 扩展）**

```[[ -f [file] ]] && echo "exists"```

**模式匹配**

```[[ "[string]" == pattern* ]]```

**正则匹配**

```[[ "[string]" =~ ^[0-9]+$ ]]```

**安全的变量比较（无需加引号）**

```[[ $var == "value" ]]```

**组合多个条件**

```[[ -f [file] && -r [file] ]]```

# SYNOPSIS

**[[** _expression_ **]]**

# OPERATORS

**文件测试**：与 **[** 相同（-f、-d、-e、-r、-w、-x 等）

**字符串比较**：
- **==** 或 **=**：模式匹配（glob）
- **!=**：不匹配模式
- **=~**：正则匹配
- **<**, **>**：字典序比较

**数值比较**：-eq、-ne、-lt、-le、-gt、-ge

**逻辑运算**：
- **&&**：与
- **||**：或
- **!**：非

# DESCRIPTION

**[[** 是 bash/zsh 的增强条件表达式。它比 **[** 更安全也更强大。

相对于 **[** 的主要优势：
- 变量不做分词（不加引号的 $var 也是安全的）
- 用 **==** 和 **!=** 进行模式匹配
- 用 **=~** 进行正则表达式匹配
- **&&** 和 **||** 可以直接用在括号内
- **<** 和 **>** 无需转义

```bash
# Pattern matching
[[ $file == *.txt ]] && echo "text file"

# Regex matching
if [[ $email =~ ^[A-Za-z]+@[A-Za-z]+\.[A-Za-z]+$ ]]; then
    echo "Valid email format"
fi

# No quoting needed
[[ $var == "test" ]]  # Safe even if var is empty
```

# CAVEATS

**[[** 是 bash、zsh 和 ksh 的保留字，但**不是 POSIX**。带有 `#!/bin/sh` shebang 的脚本必须改用 **[**，因为 Debian 和 Ubuntu 上 `/bin/sh` 是 `dash`，遇到 `[[` 会报语法错误。

它的引号规则与人们的直觉相反，这也是最常见的 bug 来源：

**==** 的右侧加引号表示字面比较。不加引号时它是 **glob 模式**，所以 `[[ $x == pattern* ]]` 匹配前缀，而 `[[ $x == "pattern*" ]]` 匹配字面的星号。

**=~** 之后的正则**不要**加引号。加了引号模式就变成字面字符串，`[[ $x =~ "^test" ]]` 会查找字符 `^test` 而不是锚定匹配。如果模式需要包含空格，把它存进变量。

其正则方言是 **ERE**，捕获组保存在 `BASH_REMATCH` 数组里，整体匹配位于第 0 个元素。

**<** 和 **>** 按字典序而非数值比较字符串：`[[ 10 < 9 ]]` 为真。数字请用 `((` `))` 或 `-lt`/`-gt` 运算符。

# HISTORY

**[[** 起源于 **Korn shell**（ksh88），David Korn 加入它是为了修复 `test` 命令长期存在的陷阱：`[` 只是一个普通命令，其参数会经历分词和 glob 展开，这就是为什么空变量或未设置的变量会让 `[ $x = y ]` 变成语法错误。把这一结构改为保留字后，shell 可以在展开之前解析它，这正是免除防御性引号的原因。

bash 在 2.02 版（**1998 年**）采纳了它，zsh 也支持，如今它已成为无 POSIX 要求脚本的标准做法。它曾被提议纳入 POSIX 但遭到拒绝，因此 `[` 仍是唯一可移植的选择。

# SEE ALSO

[test](/man/test)(1), [bash](/man/bash)(1), [zsh](/man/zsh)(1), [ksh](/man/ksh)(1), [double-parenthesis](/man/double-parenthesis)(1)
