# TAGLINE

现代化的磁盘用量与剩余空间工具

# TLDR

**显示所有已挂载文件系统**的磁盘用量

```duf```

**只显示本地文件系统**

```duf --only local```

**显示指定挂载点**

```duf [/] [/home]```

**显示所有文件系统**，包括特殊文件系统

```duf --all```

**隐藏特定文件系统类型**

```duf --hide-fs tmpfs,devtmpfs```

**以 JSON 输出**

```duf --json```

**按使用率排序**

```duf --sort usage```

**显示 inode** 而非磁盘空间

```duf --inodes```

**选择要显示的列**

```duf --output mountpoint,size,used,avail,usage```

# SYNOPSIS

**duf** [_options_] [_paths_...]

# DESCRIPTION

**duf**（Disk Usage/Free）是 df 命令的现代替代品，提供色彩丰富、对用户友好的终端界面。它以整齐的表格形式显示已挂载文件系统的磁盘用量和剩余空间。

该工具用颜色标识的使用率条提供清晰的视觉呈现，一眼就能看出快满的文件系统。它按类型（本地、网络、特殊）对文件系统分组，条理更清晰。

duf 自动处理各种文件系统类型和单位，以人类可读的格式显示大小。它支持多种输出格式，包括便于脚本处理的 JSON。

# PARAMETERS

**--all**
> 包含伪文件系统、重复文件系统和不可访问的文件系统。

**--only** _devices_ / **--hide** _devices_
> 只显示或隐藏特定的**设备组**：`local`、`network`、`fuse`、`special`、`loops`、`binds`。逗号分隔。

**--only-fs** _types_ / **--hide-fs** _types_
> 只显示或隐藏特定的**文件系统类型**，如 `ext4` 或 `tmpfs`。

**--only-mp** _paths_ / **--hide-mp** _paths_
> 只显示或隐藏特定的**挂载点**。支持通配符。

**--inodes**
> 列出 inode 使用情况而非块使用情况。

**--json**
> 将每个设备输出为 JSON。

**--output** _fields_
> 选择要显示的列，逗号分隔。

**--sort** _field_
> 按某列排序。默认为 `mountpoint`。

**--style** _style_
> 表格样式：`unicode` 或 `ascii`。

**--theme** _theme_
> 配色主题：`dark`、`light` 或 `ansi`。

**--width** _n_
> 最大输出宽度。

**--avail-threshold** _sizes_
> available 列的着色阈值（黄色、红色）。默认为 `10G,1G`。

**--usage-threshold** _fractions_
> 使用率条的着色阈值（黄色、红色），以 0 到 1 的比例表示。默认为 `0.5,0.9`。

**--warnings**
> 将警告打印到标准错误。

# CAVEATS

分组相关的标志很容易混淆。**--only** 和 **--hide** 接受的是*设备组*（`local`、`network`、`fuse`、`special`、`loops`、`binds`），而不是文件系统类型或路径。文件系统类型要用 **--only-fs**/**--hide-fs**，路径要用 **--only-mp**/**--hide-mp**。

duf 是一个展示工具，不是脚本中的 `df` 替代品：它的表格是给人看的，颜色和制表线字符会破坏任何解析程序。当输出要喂给其他程序时，请使用 **--json**。

默认情况下它会省略伪文件系统，因此你期望看到的某个挂载可能需要 **--all** 才会出现。挂起的网络文件系统会让 duf 阻塞，与 `df` 完全一样，因为两者都必须对挂载点执行 stat。

# HISTORY

**duf** 由 **Christian Muehlhaeuser** 于 **2020 年**用 Go 编写，属于那波重新审视古老 Unix 工具的浪潮之一——它们追问的是"如果终端拥有颜色、Unicode 和宽屏，这个工具会是什么样"，而 `df` 问世时这些都不存在。它迅速流行起来，因为阅读 `df` 输出对许多人来说是一种日常小烦恼，而 duf 分组、彩色编码的表格消除了这种烦恼。

# INSTALL

```apt: sudo apt install duf```

```dnf: sudo dnf install duf```

```pacman: sudo pacman -S duf```

```zypper: sudo zypper install duf```

```brew: brew install duf```

```nix: nix profile install nixpkgs#duf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[df](/man/df)(1), [du](/man/du)(1), [ncdu](/man/ncdu)(1), [dust](/man/dust)(1), [dua](/man/dua)(1)

# RESOURCES

```[Source code](https://github.com/muesli/duf)```

<!-- verified: 2026-07-14 -->
