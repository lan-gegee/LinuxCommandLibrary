# TAGLINE

编译为 HTML 的模板语言

# TLDR

**将 Haml 文件渲染为 HTML**（打印到标准输出）

```haml render [input.haml]```

**渲染并将结果保存到文件**

```haml render [input.haml] > [output.html]```

**从 stdin 渲染**

```cat [input.haml] | haml render -```

**显示编译后的 Ruby 源码**而不执行它

```haml compile [input.haml]```

不执行代码，只**检查 Haml 语法**

```haml compile --check [input.haml]```

**显示解析后的语法树**

```haml parse [input.haml]```

**显示已安装的 Haml 版本**

```haml version```

# SYNOPSIS

**haml** _command_ [_options_] _file_

# PARAMETERS

**render** _file_
> 渲染 Haml 模板并将生成的 HTML 打印到标准输出。使用 **-** 表示从 stdin 读取。

**compile** _file_
> 打印模板编译后的 Ruby 源码，而不是执行它。

**-c**, **--check**
> 与 **compile** 搭配使用时，只解析并验证生成的 Ruby；打印 "Syntax OK" 或错误信息，而不是源码。

**temple** _file_
> 打印用于生成 Ruby 代码的中间 Temple 表达式。

**parse** _file_
> 打印解析后的抽象语法树。

**version**
> 打印已安装的 Haml 版本。

**-r**, **--require** _file_
> 在渲染前引入 Ruby 库（仅限 render 命令）。

**-I**, **--load-path** _path_
> 向 Ruby 的加载路径添加目录（仅限 render 命令）。

**--no-escape-html**
> 禁用对 `=` 输出的自动转义（转义默认开启）。

**--no-escape-attrs**
> 禁用对属性值的自动转义（转义默认开启）。

# DESCRIPTION

**HAML**（HTML Abstraction Markup Language）是一种编译为 HTML 的模板语言。它使用缩进表示嵌套，并为 HTML 元素、属性和内嵌 Ruby 提供了简洁的语法。

自 Haml 6 起，引擎构建在 Temple 之上，`haml` 可执行文件是一个基于子命令的 CLI（render、compile、temple、parse、version），而不是单一的一组选项。

HAML 通常通过独立的 `haml-rails` gem 在 Ruby on Rails 应用中使用，但也可以独立用于任何 HTML 生成场景。

# HAML SYNTAX

```haml
%html
  %head
    %title My Page
  %body
    %h1 Hello World
    %p.intro Welcome!
    #content
      %ul
        - items.each do |item|
          %li= item
```

# CAVEATS

需要 Ruby。该语言对空白字符敏感；缩进错误会导致失败。CLI 的子命令（render、compile、temple、parse）取代了旧的单次调用 `haml input output` 风格以及 Haml 6 中的 `--rails`、`--style` 等选项；为 Haml 3/4/5 编写的脚本需要更新。

# HISTORY

HAML 由 **Hampton Catlin** 于 **2006 年**创建，属于 Ruby 生态的一部分。Haml 6（2022 年）用基于 Temple 构建的编译器取代了原来的手写编译器，围绕 Thor 子命令重写了 CLI，并移除了 html4/xhtml 输出格式选项。

# INSTALL

```apt: sudo apt install ruby-haml```

```pacman: sudo pacman -S ruby-haml```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[erb](/man/erb)(1), [slim](/man/slim)(1), [pug](/man/pug)(1)

# RESOURCES

```[Source code](https://github.com/haml/haml)```

```[Homepage](https://haml.info/)```

```[Documentation](https://haml.info/docs.html)```

<!-- verified: 2026-07-17 -->
