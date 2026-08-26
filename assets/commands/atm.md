# TAGLINE

生成并处理 MIDI 旋律文件

# TLDR

**显示帮助**

```atm -h```

从音高序列**生成单个 MIDI** 文件

```atm gen single 'C:4,D:4,E:4,F:4,G:4,A:4,B:4,C:5' [test.mid]```

**暴力生成**旋律并存入 gzip tar（分区深度 2）

```atm gen tar-gz -p [2] 'C:4,D:4,E:4,F:4,G:4,A:4,B:4,C:5' [8] [output.tar]```

**定位旋律所在的分区**

```atm partition -p [2] 'C:4,C:4,C:4,C:4,C:4,C:4,C:4,C:5'```

**估算**存储后端的大小

```atm estimate --help```

# SYNOPSIS

**atm** *subcommand* [*options*] [*args*]

# DESCRIPTION

**atm**（**atm-cli**）是一款用于生成和处理 MIDI 文件的命令行工具。它为 All the Music, LLC 开发，帮助生成大规模旋律集合（包括暴力枚举的范围），并将输出组织到分区的存储后端中。它基于 **libatm** Rust 库。

子命令：

- **gen** – 生成旋律（单个文件或批量后端，如 tar/gzip 布局）
- **partition** – 将音高序列映射到给定方案下的分区路径
- **estimate** – 估算存储后端的输出大小

音高序列使用 音符:**八度** 标记并以逗号分隔（例如 **C:4,D:4,E:4**）。

从源码构建：克隆仓库，执行 **git submodule update --init**，然后执行 **cargo build --release**。运行 **cargo run --release -- -h** 可在不安装的情况下查看用法。

# PARAMETERS

**gen single** *melody* *outfile*

> 为给定的音高序列写出一个 MIDI 文件。

**gen** *backend* ...

> 批量生成到 tar、tar-gz 或 **atm gen --help** 中记载的其他后端。**-p** 设置分区深度（限制每个目录的文件数）。

**partition** [**-p** *depth*] *melody*

> 打印该旋律所在的分区目录（默认深度为 1）。

**estimate**

> 通过估算输出大小来辅助选择存储后端。

**-h**, **--help** / **-V**, **--version**

> 帮助与版本信息。

# CAVEATS

专为批量旋律生成设计，并非通用 DAW 或多轨 MIDI 编辑器。编译需要 Rust 工具链和子模块。长序列的输出量会呈阶乘级增长；请谨慎使用 **estimate** 和分区后端。许可证为 CC BY 4.0（非公有领域），与部分 ATM 数据集不同。

# SEE ALSO

[timidity](/man/timidity)(1), [fluidsynth](/man/fluidsynth)(1), [sox](/man/sox)(1)

# RESOURCES

```[Source code](https://github.com/allthemusicllc/atm-cli)```

```[Homepage](http://allthemusic.info)```

```[Documentation](https://allthemusicllc.github.io/atm-cli/atm/index.html)```

<!-- verified: 2026-07-19 -->
