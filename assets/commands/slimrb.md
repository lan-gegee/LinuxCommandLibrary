# TAGLINE

将 Slim 模板编译为 HTML

# TLDR

**将 Slim 编译为 HTML**

```slimrb [template.slim]```

**编译到文件**

```slimrb [template.slim] [output.html]```

**美化输出**

```slimrb -p [template.slim]```

**带 Rails 支持**

```slimrb -r [template.slim]```

**从 stdin 编译**

```echo "[h1 Hello]" | slimrb```

# SYNOPSIS

**slimrb** [_-p_] [_-r_] [_options_] [_input_] [_output_]

# PARAMETERS

**-p**, **--pretty**
> 美化输出 HTML。

**-r**, **--rails**
> Rails 模式。

**-e**, **--erb**
> 从 ERB 转换。

**-l**, **--logic-less**
> 无逻辑模式。

**-t**, **--translator**
> 翻译模式。

# DESCRIPTION

**slimrb** 是 Slim 模板语言的命令行编译器。Slim 是一个轻量级的 Ruby 模板引擎，将 HTML 标记精简到最少。它读取 Slim 文件并将其渲染为 HTML、ERB 或原始 Ruby 代码，便于查看和调试。

Slim 采用基于缩进的嵌套并省去闭合标签，生成的模板比等价的 HTML 或 ERB 短得多。该编译器支持用于调试的美化输出、Rails 兼容的代码生成，以及转换为 ERB 格式以便在不直接支持 Slim 的场景中使用。

该工具与 Ruby 的 Tilt 模板接口集成，可用于 Rails、Sinatra 和其他基于 Rack 的框架。插件可以通过无逻辑模板、翻译支持等功能扩展语法。

# CAVEATS

需要 Ruby。需要 Slim gem。属于 Ruby 专用的模板方案。

# HISTORY

**slimrb** 是 **Slim** 的 CLI 编译器，Slim 是一个快速轻量的 Ruby 模板引擎。

# SEE ALSO

[erb](/man/erb)(1), [haml](/man/haml)(1), [ruby](/man/ruby)(1)
