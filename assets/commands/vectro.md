# TAGLINE

带 TUI 界面的终端 RPN 计算器

# TLDR

**启动 RPN 计算器**

```vectro```

# SYNOPSIS

**vectro**

# DESCRIPTION

**vectro** 是一款在终端中运行、基于 Bubble Tea TUI 框架的逆波兰表示法（RPN）计算器。输入数字将其压入栈，输入运算符则作用于栈顶元素。界面会自适应终端大小，并在会话之间持久化栈内容，昨天输入的值今天依然可用。

编辑器支持对栈值进行复制/粘贴（yank/paste）、撤销缓冲区，除基本算术运算外还支持三角函数、对数和位运算。小数精度和进制模式（DEC/HEX/BIN）可在 TUI 内选择。

# CAVEATS

不暴露任何命令行选项；配置和按键绑定保存在应用程序管理的配置文件中。与其他 RPN 计算器一样，它没有中缀表达式解析器：必须先输入操作数再输入运算符。

# HISTORY

**vectro** 由 **gurgeous** 创建，使用 **Go** 语言和 **Bubble Tea** TUI 框架编写，以单个静态二进制文件分发。

# SEE ALSO

[bc](/man/bc)(1), [dc](/man/dc)(1), [calc](/man/calc)(1), [qalc](/man/qalc)(1)
