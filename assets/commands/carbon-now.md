# TAGLINE

生成精美的源代码图片

# TLDR

**从文件生成图片**

```carbon-now [file.js]```

**交互模式**

```carbon-now [file.py] --interactive```

**保存到指定位置**

```carbon-now [file.rs] --save-to [~/images]```

**以自定义名称保存**

```carbon-now [file.go] --save-as [my-code]```

**从剪贴板读取**

```carbon-now --from-clipboard```

**将结果复制到剪贴板**

```carbon-now [file.ts] --to-clipboard```

**使用预设**

```carbon-now [file.js] --preset [my-preset]```

**指定的行范围**

```carbon-now [file.py] --start [5] --end [15]```

# SYNOPSIS

**carbon-now** _file_ [_options_]
**carbon-now** --from-clipboard [_options_]

# DESCRIPTION

**carbon-now** 在终端中通过 Carbon 服务（carbon.now.sh）创建精美的源代码图片。它以语法高亮、可定制主题和专业排版来渲染代码，适用于演示文稿、文档和社交媒体。

该工具使用无头浏览器（Playwright）通过 Carbon 网络服务渲染图片。它支持从文件、剪贴板或标准输入读取内容，并可输出到文件或剪贴板。交互模式允许在生成图片前自定义外观设置。预设可以保存常用配置，以保持风格一致。

# PARAMETERS

**-i**, **--interactive**
> 生成前自定义设置

**-s**, **--start** _line_
> 输入的起始行

**-e**, **--end** _line_
> 输入的结束行

**-p**, **--preset** _name_
> 应用已有预设

**--save-to** _path_
> 图片保存位置（默认：当前工作目录）

**--save-as** _name_
> 不含扩展名的图片文件名

**--from-clipboard**
> 从剪贴板读取输入

**--to-clipboard**
> 将图片复制到剪贴板

**--open-in-browser**
> 在浏览器中打开而不保存

**--config** _path_
> 使用其他配置文件

**--settings** _json_
> 覆盖特定设置项

**--disable-headless**
> 以有头模式运行浏览器

**--engine** _name_
> 渲染引擎：chromium、firefox 或 webkit（默认：chromium）

**--skip-display**
> 不在终端中显示图片

# CONFIGURATION

**~/.carbon-now.json**
> 已保存的设置与预设。之前的设置会被自动复用。

# CAVEATS

需要 Node.js 和 npm。渲染依赖无头浏览器（Playwright）。使用 Carbon 服务需要联网。

# SEE ALSO

[silicon](/man/silicon)(1)
