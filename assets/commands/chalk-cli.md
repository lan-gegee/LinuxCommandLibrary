# TAGLINE

带颜色和格式的终端字符串样式化工具

# TLDR

**用颜色修饰文本**

```chalk red "Hello World"```

**应用多种样式**

```chalk red bold "Important text"```

**使用模板语法**

```chalk -t "{red.bold Unicorns} are {blue fun}"```

**从 stdin 读取**

```echo "text" | chalk --stdin green```

**在模板中取消某个样式**

```chalk -t "{red text {~red normal}}"```

**输出时不换行**

```chalk -n yellow "No newline"```

**演示所有样式**

```chalk --demo```

# SYNOPSIS

**chalk** [_options_] _style_... _string_

**echo** _string_ **| chalk** **--stdin** _style_...

# DESCRIPTION

**chalk-cli** 是一款为终端字符串添加颜色和格式的命令行工具。它封装了流行的 Node.js Chalk 库，让 shell 脚本和命令行也能使用其样式化能力。

样式包括前景色和背景色（标准色和高亮变体），以及 bold、dim、italic、underline、inverse、strikethrough 等文本修饰。多种样式可以组合使用，模板语法还允许对单个字符串的不同部分应用不同样式。

输入可以来自命令参数或 stdin，因此非常适合在 shell 管道中高亮输出或构建多彩的 CLI 界面。

# PARAMETERS

**-t**, **--template**
> 使用模板语法实现嵌套样式

**--stdin**
> 从 stdin 读取输入

**-n**, **--no-newline**
> 输出后不追加换行符

**--demo**
> 展示所有可用样式的演示

**-c**, **--color**
> 强制启用颜色支持

# STYLES

**Colors**
> black, red, green, yellow, blue, magenta, cyan, white, gray

**Bright colors**
> redBright, greenBright, yellowBright 等

**Background**
> bgRed, bgGreen, bgBlue 等

**Modifiers**
> bold, dim, italic, underline, inverse, strikethrough

# TEMPLATE SYNTAX

模板支持内联嵌套样式：

```
{red.bold text}
{red red {~red normal}}  # ~ negates style
```

# INSTALLATION

```npm install --global chalk-cli```

# CAVEATS

需要 Node.js。颜色支持取决于终端能力。在管道中使用时可用 --color 强制着色。

# INSTALL

```brew: brew install chalk-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tput](/man/tput)(1), [printf](/man/printf)(1)

# RESOURCES

```[Source code](https://github.com/chalk/chalk-cli)```

<!-- verified: 2026-06-22 -->
