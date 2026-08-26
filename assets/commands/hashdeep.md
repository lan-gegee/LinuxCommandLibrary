# TAGLINE

同时为文件和目录计算多个加密哈希

# TLDR

**递归计算文件的 MD5 和 SHA-256 哈希**

```hashdeep -r [path/to/directory]```

**计算指定的哈希类型**（md5、sha1、sha256、tiger、whirlpool）

```hashdeep -c [sha256] [path/to/files]```

**创建文件的哈希清单**

```hashdeep -r [path/to/directory] > [manifest.txt]```

**对照已知的哈希清单审计文件**

```hashdeep -r -a -k [manifest.txt] [path/to/directory]```

**找出匹配**清单中哈希的文件

```hashdeep -r -m -k [manifest.txt] [path/to/directory]```

**找出不匹配**清单中哈希的文件

```hashdeep -r -x -k [manifest.txt] [path/to/directory]```

计算哈希时**显示进度指示器**

```hashdeep -r -e [path/to/directory]```

# SYNOPSIS

**hashdeep** [_-c alg_] [_-k file_] [_-amxwMXrespblvv_] [_files_]

**hashdeep** -c _alg1_,_alg2_ -r _directory_

# PARAMETERS

**-c** _ALG_
> 使用指定算法计算哈希（md5、sha1、sha256、tiger、whirlpool）；默认为 md5,sha256

**-r**
> 递归模式；遍历所有子目录

**-k** _FILE_
> 加载已知哈希文件用于比对

**-a**
> 审计模式；对照已知哈希比较文件

**-m**
> 正向匹配；只显示与已知哈希匹配的文件

**-x**
> 反向匹配；只显示不在已知哈希中的文件

**-M**
> 类似 -m，但同时打印每个匹配文件的哈希

**-X**
> 类似 -x，但同时打印每个不匹配文件的哈希

**-w**
> 审计时显示匹配到的是哪个已知文件

**-e**
> 显示进度指示器和剩余时间估计

**-s**
> 安静模式；抑制错误消息

**-b**
> bare 模式；在输出中剥离目录路径

**-l**
> 使用相对文件路径而不是绝对路径

**-p** _SIZE_
> 分段模式；计算哈希前先把文件切分成块

**-v**
> 详细模式；重复使用可获得更多信息

**-j** _NUM_
> 使用指定数量的线程

**-d**
> 以 DFXML 格式输出

**-h**
> 显示帮助信息

**-V**
> 显示版本号

# DESCRIPTION

**hashdeep** 可同时为文件和目录计算多个加密哈希。与单一哈希工具不同，它默认同时计算 MD5 和 SHA-256，通过多算法提供更强的验证能力。

该工具尤其擅长文件完整性验证和数字取证。它可以创建已知完好文件的清单，然后对系统进行审计，检测出被修改、新增或删除的文件。审计模式报告的文件状态包括：MATCH 表示相同，MISMATCH 表示被修改，MISSING 表示已被删除，NEW 表示新增。

输出遵循兼容 DFXML 的 hashdeep 格式，包含文件大小、哈希值和路径。该格式之后可以通过 **-k** 加载用于再次验证。借助递归扫描和可选的多线程，它能高效处理庞大的目录树。

# CAVEATS

MD5 和 SHA-1 等哈希算法存在已知的碰撞漏洞，不应依赖它们做安全关键的验证。当完整性至关重要时，请使用 SHA-256 或更强的算法。特别大的文件计算哈希可能耗时很久。该工具按顺序读取文件，可能受 I/O 性能限制。

# HISTORY

hashdeep 由 **Jesse Kornblum** 编写，属于取证哈希工具集 **md5deep** 的一部分。它首次发布于 **2003 年**，专为需要验证文件完整性和检测篡改行为的数字取证调查人员设计。引入多哈希能力是为了弥补单个算法的弱点。该项目常用于执法部门的数字取证以及企业数据完整性验证。

# INSTALL

```apt: sudo apt install hashdeep```

```zypper: sudo zypper install hashdeep```

```brew: brew install hashdeep```

```nix: nix profile install nixpkgs#hashdeep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[md5sum](/man/md5sum)(1), [sha256sum](/man/sha256sum)(1)
