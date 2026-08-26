# TAGLINE

整盘（disc-at-once）模式刻录与读取 CD

# TLDR

**读取** CD 并将内容写入文件

```cdrdao read-cd --device [/dev/cdrom] --read-raw [image.toc]```

**将**光盘镜像**写入** CD-R

```cdrdao write --device [/dev/cdrom] --speed [8] [image.toc]```

**模拟**刻录而不实际烧录

```cdrdao simulate --device [/dev/cdrom] [image.toc]```

直接**复制**一张 CD

```cdrdao copy --source-device [/dev/cdrom] --device [/dev/cdrw] [image.toc]```

**擦除** CD-RW 光盘

```cdrdao blank --device [/dev/cdrw] --blank-mode minimal```

**显示**目录表

```cdrdao show-toc [image.toc]```

# SYNOPSIS

**cdrdao** _command_ [_options_] _toc-file_

# DESCRIPTION

**cdrdao** 以整盘（disc-at-once，DAO）模式读写 CD。与逐轨（track-at-once）刻录不同，DAO 一次性写完整张光盘，音轨之间没有间隙，保留精确的扇区时序和子通道数据。因此它是制作音频 CD 精确副本的首选工具——在这类场景中音轨衔接非常重要。

该工具使用 TOC（Table of Contents，目录表）文件来描述光盘布局，可以表示复杂的光盘结构，包括多区段光盘、混合模式光盘以及带隐藏音轨或非标准间隙的 CD。相比 cue sheet，TOC 格式对光盘布局的控制更精细。

典型工作流程是：先用 `read-cd` 读取光盘生成 TOC 文件和二进制镜像，再用 `write` 将镜像写回。`simulate` 命令执行一次不实际烧录的演练。

# COMMANDS

**read-cd**
> 将 CD 读取为镜像和 TOC 文件

**write**
> 将镜像写入光盘

**copy**
> 光盘对拷

**simulate**
> 模拟刻录操作

**show-toc**
> 显示 TOC 文件内容

**read-toc**
> 分析每条音轨并创建 TOC 文件，而不读取音频/数据

**blank**
> 擦除 CD-RW 光盘

**unlock**
> 在刻录或模拟失败后解锁刻录机设备

# PARAMETERS

**--device** _device_
> CD/DVD 设备路径

**--read-raw**
> 以原始模式读取（保留全部数据）

**--driver** _name_
> 使用指定的设备驱动

**--speed** _n_
> 设置刻录速度

**--source-device** _device_
> 源 CD 设备路径（用于 copy 命令）

**--eject**
> 操作完成后弹出光盘

**--overburn**
> 允许写入超过介质容量的数据

**--multi**
> 写入后不关闭区段，以便追加更多区段

**--blank-mode** _mode_
> CD-RW 的擦除模式（minimal 或 full）

# CAVEATS

写入操作需要 CD/DVD 刻录机。原始读取模式并非对所有光驱都有效。复制保护可能阻止读取某些光盘。

# INSTALL

```apt: sudo apt install cdrdao```

```dnf: sudo dnf install cdrdao```

```pacman: sudo pacman -S cdrdao```

```apk: sudo apk add cdrdao```

```zypper: sudo zypper install cdrdao```

```brew: brew install cdrdao```

```nix: nix profile install nixpkgs#cdrdao```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wodim](/man/wodim)(1), [cdrecord](/man/cdrecord)(1), [genisoimage](/man/genisoimage)(1)
