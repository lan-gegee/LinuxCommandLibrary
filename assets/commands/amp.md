# TAGLINE

受 Vi/Vim 启发的终端文本编辑器

# TLDR

**打开文件**进行编辑

```amp [path/to/file]```

**打开多个文件**

```amp [file1] [file2]```

**打开目录**浏览文件

```amp [path/to/directory]```

# SYNOPSIS

**amp** [_files..._|_directory_]

# DESCRIPTION

**amp** 是一款面向终端的模式化文本编辑器，灵感来自 Vim，但追求简洁与零配置。它开箱即用，内置所有必备功能且没有插件系统：支持大多数语言的语法高亮、文件查找器（Space）、用于快速导航的跳转模式（f）、符号跳转（Enter）、Git 集成、灵活的基于 YAML 的键位映射、主题支持以及保存时自动格式化。

amp 使用 Rust 编写，采用类 Vi 的模式界面（普通、插入、可视、命令模式），按键绑定符合习惯。它支持 24 位色彩、系统集成剪贴板（包括 Wayland），并可通过 **z** 挂起回到 Shell。

# CONFIGURATION

配置通过 amp 配置目录中的 YAML 文件完成。可配置项包括 **theme**、**tab_width**、**soft_tabs**、**line_length_guide**、**line_wrapping**、按文件类型的设置、自定义键位映射以及保存时格式化工具。

# CAVEATS

使用自定义许可证而非标准开源许可证。从源码构建需要 libxcb、openssl、zlib、cmake 和 python3。设计上不提供插件系统。

# HISTORY

**amp** 由 **Jordan MacDonald**（jmacdonald）创建。他因对 Vim 感到失望，于 2015 年前后启动了这个项目。项目使用 Rust 编写，2024 年发布至 0.7.1 版。自创建以来，MacDonald 一直将 amp 作为日常编辑器使用。

# INSTALL

```aur: yay -S amp```

```zypper: sudo zypper install amp```

```brew: brew install amp```

```nix: nix profile install nixpkgs#amp```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[vim](/man/vim)(1), [kakoune](/man/kakoune)(1), [helix](/man/helix)(1), [nano](/man/nano)(1)
