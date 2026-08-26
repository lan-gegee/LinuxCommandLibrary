# TAGLINE

将终端会话录制为 GIF

# TLDR

**开始录制**到 YAML 文件

```terminalizer record [filename]```

**使用自定义配置**文件录制

```terminalizer record [filename] -c [config.yml]```

**使用自定义命令**录制，而非默认 Shell

```terminalizer record [filename] -d "[bash -l]"```

**播放录制**

```terminalizer play [filename.yml]```

**把录制渲染**为动画 GIF

```terminalizer render [filename.yml] -o [output.gif]```

**生成全局配置**文件

```terminalizer init```

**在线分享录制**

```terminalizer share [filename.yml]```

**为录制生成网页播放器**页面

```terminalizer generate [filename.yml]```

# SYNOPSIS

**terminalizer** _command_ [_options_] [_file_]

# PARAMETERS

**record** _FILE_
> 将终端会话录制到 YAML 文件。

**play** _FILE_
> 在终端中回放已录制的会话。

**render** _FILE_
> 把录制渲染为动画 GIF。

**generate** _FILE_
> 生成可分享的 HTML 网页播放器链接。

**share** _FILE_
> 上传录制并分享到 terminalizer.com。

**init**
> 在 `~/.terminalizer/config.yml` 创建全局配置文件。

**config**
> 将默认配置打印到 stdout。

**-c** _FILE_, **--config** _FILE_
> 使用自定义配置文件。

**-d** _COMMAND_, **--command** _COMMAND_
> 运行指定命令而非默认 Shell（record）。

**-k**, **--skip-sharing**
> 录制后跳过分享提示。

**-o** _FILE_, **--output** _FILE_
> 输出文件路径（render）。

**-q** _NUM_, **--quality** _NUM_
> GIF 质量 1-100（render）。

**-s** _NUM_, **--step** _NUM_
> 帧步长；数值越大 GIF 体积越小（render）。

**-r** _NUM_, **--real-timing**
> 按原始录制速度播放（play）。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**terminalizer** 录制终端会话并将其渲染为动画 GIF，方便在文档、README 和教程中分享。它同时捕获按键和终端输出，并以可编辑的 YAML 格式保存录制内容。

录制内容可以在终端中回放、在本地渲染成 GIF，或通过 terminalizer.com 在线分享。YAML 格式允许在渲染最终动画之前编辑时间轴、删除误操作以及自定义外观，包括颜色、字体、窗口边框样式和尺寸。

# CAVEATS

需要 **Node.js**（通过 `npm install -g terminalizer` 安装）。GIF 渲染依赖 Electron，可能占用大量 CPU 和内存。生成的 GIF 可能体积较大；可通过配置中的 `quality` 和 `step` 或命令行标志来平衡大小与流畅度。

# HISTORY

**Terminalizer** 由 **Mohammad Fares（faressoft）** 创建，于 **2017 年**首次作为 npm 包发布。它是 asciinema 的替代方案，优点是无需专用播放器即可生成可分享的 GIF 动画。

# SEE ALSO

[asciinema](/man/asciinema)(1), [script](/man/script)(1), [ttyrec](/man/ttyrec)(1)
