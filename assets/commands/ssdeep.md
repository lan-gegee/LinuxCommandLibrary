# TLDR

**计算文件的模糊哈希**

```ssdeep [file1] [file2]```

**递归计算哈希**

```ssdeep -r [directory/]```

**比较文件**并显示匹配结果

```ssdeep -p [file1] [file2] [file3]```

**将文件与已知哈希匹配**

```ssdeep -m [known_hashes.txt] [files_to_check]```

**比较两个哈希文件**

```ssdeep -k [known.txt] [computed.txt]```

**设置匹配阈值**（0-100）

```ssdeep -p -t [50] [files]```

**以 CSV 格式输出**

```ssdeep -c [files]```

# SYNOPSIS

**ssdeep** [**-m** _file_] [**-k** _file_] [**-vprdsblcxag**] [**-t** _val_] [_files_]

# PARAMETERS

**-m** _file_
> 从文件加载已知哈希，与输入文件计算出的哈希进行匹配。

**-k** _file_
> 将文件中的已知签名与输入文件中预先计算的签名进行比较。

**-p**
> 美观匹配模式。将所有输入文件两两比较。

**-d**
> 将每个文件与已知集合匹配，然后将其哈希加入已知集合。

**-r**
> 递归模式。遍历所有子目录。

**-t** _val_
> 匹配阈值（0-100）。只显示高于该分数的匹配。默认：0。

**-a**
> 无论分数高低，显示所有匹配。

**-v**
> 详细模式。计算哈希时向 stderr 打印文件名。

**-b**
> 输出中使用不带路径的纯文件名。

**-l**
> 输出中使用相对路径。

**-c**
> 以 CSV 格式输出。

**-s**
> 静默模式。抑制警告信息。

**-x**
> 签名文件匹配。将输入文件视为签名文件，并与已知集合进行比较。

**-g**
> 聚类模式。把相似文件归入关联项目的簇。

# DESCRIPTION

**ssdeep** 计算上下文触发的分段哈希（CTPH），也称为模糊哈希。与加密哈希对微小差异的输入产生完全不同的输出不同，模糊哈希能够识别相似但不完全相同的文件。

该工具适用于恶意软件分析、识别被篡改的文档、查找近似重复文件以及数字取证。匹配分数大于零的两个文件共享某些相同的字节序列。分数范围为 0（不匹配）到 100（非常相似或相同）。

输出格式包括块大小、两个哈希分量和文件名。此输出可以保存起来，之后配合 **-m** 或 **-k** 选项用于匹配。

# CAVEATS

在验证文件的精确完整性时，模糊哈希不能替代加密哈希。小文件可能无法产生有意义的模糊哈希。匹配分数只是近似值；用于取证时可能需要人工核实。如果文件经过大幅重构，该工具无法检测出相似性。

# HISTORY

**ssdeep** 由 Jesse Kornblum 基于 Andrew Tridgell 博士为垃圾邮件检测开发的 spamsum 算法创建。该项目同时提供命令行工具和供编程调用的 **libfuzzy** 库。它被广泛用于数字取证、恶意软件分析和安全研究。该工具以 GNU 通用公共许可证发布。

# INSTALL

```apt: sudo apt install ssdeep```

```dnf: sudo dnf install ssdeep```

```pacman: sudo pacman -S ssdeep```

```apk: sudo apk add ssdeep```

```zypper: sudo zypper install ssdeep```

```brew: brew install ssdeep```

```nix: nix profile install nixpkgs#ssdeep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[md5sum](/man/md5sum)(1), [sha256sum](/man/sha256sum)(1), [hashdeep](/man/hashdeep)(1)

# RESOURCES

```[Source code](https://github.com/ssdeep-project/ssdeep)```

```[Homepage](https://ssdeep-project.github.io/ssdeep/)```

<!-- verified: 2026-06-10 -->
