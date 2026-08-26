# TAGLINE

闪存盘数据完整性校验工具

# TLDR

**读取并校验**闪存盘上的数据

```f3read [/media/flash]```

校验期间**显示进度**

```f3read --show-progress [/media/flash]```

**校验指定范围的**测试文件（如第 5 到第 10 个文件）

```f3read --start-at [5] --end-at [10] [/media/flash]```

从指定文件编号**开始校验**

```f3read --start-at [3] [/media/flash]```

# SYNOPSIS

**f3read** [_options_] _directory_

# PARAMETERS

_DIRECTORY_
> 要校验的闪存盘挂载点。

**--start-at** _N_
> 从文件编号 N 开始。

**--end-at** _N_
> 到文件编号 N 结束。

**--show-progress**
> 读取过程中显示进度。

**--help**
> 显示帮助信息。

# DESCRIPTION

**f3read** 通过读取 f3write 创建的文件来校验闪存盘的数据完整性。它是 F3（Fight Flash Fraud）工具集的一部分，用于检测假冒闪存。

该工具读取校验文件，并将其内容与预期模式进行比对。出现差异说明要么发生了数据损坏，要么是假容量——写入看似成功但数据已丢失。

f3read 与 f3write 配合，构成一组无损测试组合，可以在不丢失数据的情况下验证闪存盘完整性。

# CAVEATS

需要 f3write 写入的文件。只测试测试文件占用的空间。比 f3probe 慢但是无损的。闪存盘必须处于挂载状态。

# HISTORY

f3read 是 **F3**（Fight Flash Fraud）项目的一部分，用于校验闪存完整性。与 f3write 结合，它提供了 f3probe 之外的无损替代方案来测试驱动器容量。

# INSTALL

```apt: sudo apt install f3```

```dnf: sudo dnf install f3```

```apk: sudo apk add f3```

```zypper: sudo zypper install f3```

```brew: brew install f3```

```nix: nix profile install nixpkgs#f3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[f3write](/man/f3write)(1), [f3probe](/man/f3probe)(1), [f3fix](/man/f3fix)(1)
