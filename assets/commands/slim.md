# TAGLINE

轻量级 Ruby HTML 模板编译器

# TLDR

**将 Slim 模板转换**为 HTML

```slimrb [input.slim]```

**从 stdin 读取 Slim**并输出 HTML

```echo "[h1 Hello]" | slimrb -s```

**将 Slim 转换为 ERB** 格式

```slimrb -e [input.slim]```

**输出美化后的 HTML**用于调试

```slimrb -p [input.slim]```

**编译为 Ruby 代码**而不执行

```slimrb -c [input.slim]```

**生成 Rails 兼容的代码**

```slimrb --rails [input.slim]```

**向模板传递局部变量**

```slimrb -l "{name: 'World'}" [input.slim]```

处理前**加载 Ruby 库**

```slimrb -r [library] [input.slim]```

# SYNOPSIS

**slimrb** [_options_] [_input_file_]

# PARAMETERS

**-s**, **--stdin**
> 从标准输入而非文件读取内容

**-c**, **--compile**
> 将模板编译为 Ruby 代码而不执行

**-e**, **--erb**
> 将 Slim 模板转换为 ERB 格式

**--rails**
> 生成 Rails 兼容的代码（隐含 --compile）

**-p**, **--pretty**
> 输出带缩进的美化 HTML

**-r**, **--require** _library_
> 处理前加载 Ruby 库或 Slim 插件

**-o**, **--option** _name=code_
> 设置 Slim 引擎选项

**-l**, **--locals** _Hash|YAML|JSON_
> 向模板传递局部变量

**--trace**
> 出错时显示完整的调用栈

**-v**, **--version**
> 显示版本信息

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**slimrb** 是 Slim 模板语言的命令行工具。Slim 是一个轻量级的 Ruby 模板引擎，在保持可读性的同时将 HTML 语法精简到最少。它使用缩进表示嵌套，无需闭合标签。

Slim 语法简洁：**div.container** 会变成 **\<div class="container"\>**，而 **h1= title** 会在 h1 标签中输出 **title** 的值。属性放在圆括号中：**a(href=url) Link**。

该工具可以将模板渲染为 HTML、转换为 ERB 以便在其他场景中使用，或编译为原始 Ruby 代码以便查看。**--pretty** 选项对调试很有用，会生成格式化的 HTML 输出。

Slim 通过 Tilt 与 Rails、Sinatra 以及任何基于 Rack 的框架集成。它是最快的 Ruby 模板引擎之一，生产模式下的性能可与 Erubis 相媲美。

# CAVEATS

Slim 需要安装 Ruby。模板语法对空白字符敏感；混用制表符和空格可能导致意外结果。某些高级 Ruby 表达式可能需要显式的输出标记。

# HISTORY

**Slim** 由 **Andrew Stone**、**Fred Wu** 和 **Daniel Mendler** 于 **2010 年**前后创建，是比 ERB 和 Haml 更整洁的选择。该项目旨在提供极简语法的同时保持与 Ruby 的完整集成。它使用 Temple 框架进行解析和编译。

# INSTALL

```apt: sudo apt install slim```

```dnf: sudo dnf install slim```

```pacman: sudo pacman -S slim```

```apk: sudo apk add slim```

```zypper: sudo zypper install slim```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[erb](/man/erb)(1), [haml](/man/haml)(1), [pug](/man/pug)(1), [ruby](/man/ruby)(1)
