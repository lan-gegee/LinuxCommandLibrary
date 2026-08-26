# TAGLINE

生成精美的源代码图片

# TLDR

**从文件创建代码图片**

```carbon-now [file.js]```

**从剪贴板创建图片**

```carbon-now --from-clipboard```

**从 stdin 创建图片**

```echo "const x = 1;" | carbon-now```

**使用交互模式自定义所有设置**

```carbon-now [file.js] --interactive```

**使用已保存的预设配置**

```carbon-now [file.js] -p [dracula]```

**指定输出位置**

```carbon-now [file.js] --save-to [~/Pictures]```

**在浏览器中打开而不保存**

```carbon-now [file.js] --open-in-browser```

**创建图片并复制到剪贴板**

```carbon-now [file.js] --to-clipboard```

# SYNOPSIS

**carbon-now** [_options_] [_file_]

# PARAMETERS

**-i**, **--interactive**
> 启动交互模式，在生成图片前自定义主题、字体、内边距等设置。

**-p**, **--preset** _name_
> 应用 `~/.carbon-now.json` 中保存的预设。默认为 `latest-preset`，它会自动复用上一次运行的设置。

**--save-to** _path_
> 保存图片的目录。默认为当前工作目录。

**--save-as** _name_
> 不带扩展名的图片文件名。默认为源文件名加哈希后缀。

**--from-clipboard**
> 从剪贴板读取代码，而不是文件或 stdin。

**--to-clipboard**
> 将生成的图片复制到剪贴板，而不是保存到磁盘。

**--open-in-browser**
> 在浏览器中打开 Carbon URL 手动完成收尾，而不是下载图片。

**-s**, **--start** _line_
> 输入内容的起始行号。默认：`1`。

**-e**, **--end** _line_
> 输入内容的结束行号。默认：`1000`。

**--settings** _json_
> 以 JSON 字符串覆盖本次运行的部分设置（优先级最高，会覆盖预设和交互模式）。

**--config** _file_
> 使用自定义本地配置文件代替 `~/.carbon-now.json`（只读，更改不会被保存）。

**--engine** _name_
> 要使用的渲染引擎：`chromium`（默认）、`firefox` 或 `webkit`。

**--skip-display**
> 生成后不在终端中内联显示图片。

**--disable-headless**
> 以有头（可见）模式运行 Playwright 浏览器，而不是无头模式。

# DESCRIPTION

**carbon-now-cli** 使用 Carbon 服务（carbon.now.sh）生成精美的源代码图片。它可以从终端自动下载带语法高亮的高质量 PNG 或 SVG 代码图片，主题、字体和背景均可自定义。

输入可以是文件、管道传入的 stdin 或剪贴板内容。文件类型会被自动检测以应用语法高亮。使用 `--interactive` 模式可逐项确认所有视觉设置，或将这些设置保存为 `~/.carbon-now.json` 中的具名预设，之后用 `--preset` 复用。

每次运行的设置都会自动保存为 `latest-preset`，因此后续运行无需任何额外标志即可复用上一次的配置。具名预设会一直保留，直到从 `~/.carbon-now.json` 中手动删除。

`--settings` 标志接受 JSON 字符串，其覆盖优先级仅次于 `--interactive`。导出尺寸（`1x`、`2x`、`4x`）、导出类型（`png`、`svg`）、行号、投影、内边距以及自定义的逐语法元素主题颜色都可以通过预设配置。

# CAVEATS

需要联网才能访问 Carbon 渲染服务。通过 `custom` 预设键设置的自定义主题颜色在使用 `--open-in-browser` 时不会生效，因为它们依赖 Playwright 实例内部的 `localStorage`。图片生成依赖外部服务的可用性。

# HISTORY

Carbon 由 **Dawn Labs** 创建，于 **2017** 年作为生成精美代码图片的 Web 应用上线。carbon-now-cli 是一个社区项目，为该服务提供命令行访问方式。它因能快速生成用于文档、推文和演示的代码图片而无需打开浏览器，深受开发者欢迎。

# INSTALL

```nix: nix profile install nixpkgs#carbon-now-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[silicon](/man/silicon)(1), [pygmentize](/man/pygmentize)(1), [highlight](/man/highlight)(1)
