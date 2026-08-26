# TAGLINE

从损坏的 bzip2 文件中恢复数据

# TLDR

从损坏的文件中**恢复**数据

```bzip2recover [damaged.bz2]```

# SYNOPSIS

**bzip2recover** _file.bz2_

# DESCRIPTION

**bzip2recover** 尝试从损坏的 bzip2 压缩文件中恢复数据。它的工作方式是从损坏的 .bz2 文件中提取完好的数据块，有可能恢复部分或大部分数据。

当 bzip2 文件损坏且正常解压失败时，该工具很有用。

# OPERATION

该工具会：
1. 扫描损坏的 **.bz2** 文件以寻找有效的块边界。
2. 将每个完好的块写入一个单独的文件，命名为 **rec0000N**_input_**.bz2**（例如 **rec00001damaged.bz2**、**rec00002damaged.bz2**）。
3. 每个恢复出来的单块文件随后可用 **bunzip2** 独立解压。

# WORKFLOW

```bash
# Attempt recovery
bzip2recover damaged.bz2

# Creates: rec00001damaged.bz2, rec00002damaged.bz2, ...

# Decompress each recovered block
bunzip2 rec*damaged.bz2

# Concatenate the decompressed blocks in order
cat rec*damaged > recovered.txt
```

# FEATURES

- 块级恢复
- 不修改原始文件
- 可处理部分损坏的文件
- 为每个完好块生成一个 **.bz2** 文件

# CAVEATS

无法恢复损坏块内部的数据——只保存由完好 48 位块起始/结束标记界定的完整块。第一个块通常无法恢复，因为其前导位位于文件头中。仅对使用大于默认值的块大小压缩的文件有效（恢复需要多个块）。恢复出的块必须手动解压并按顺序拼接。备份远比恢复可靠。

# HISTORY

自 **2000 年** bzip2 1.0 版起，**bzip2recover** 就随 bzip2 一同提供，用于帮助从损坏中恢复。

# INSTALL

```apt: sudo apt install bzip2```

```dnf: sudo dnf install bzip2```

```pacman: sudo pacman -S bzip2```

```apk: sudo apk add bzip2```

```zypper: sudo zypper install bzip2```

```brew: brew install bzip2```

```nix: nix profile install nixpkgs#bzip2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bzip2](/man/bzip2)(1), [bunzip2](/man/bunzip2)(1), [ddrescue](/man/ddrescue)(1)
