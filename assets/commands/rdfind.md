# TAGLINE

高效查找并处理重复文件

# TLDR

**查找重复文件**

```rdfind [directory]```

**在多个目录中查找**

```rdfind [dir1] [dir2]```

**删除重复文件**

```rdfind -deleteduplicates true [directory]```

**创建硬链接**

```rdfind -makehardlinks true [directory]```

**创建符号链接**

```rdfind -makesymlinks true [directory]```

**演练运行**

```rdfind -dryrun true [directory]```

**输出结果文件**

```rdfind -outputname [results.txt] [directory]```

# SYNOPSIS

**rdfind** [_-deleteduplicates true_] [_-makehardlinks true_] [_options_] _directories_

# PARAMETERS

**-deleteduplicates** _BOOL_
> 删除重复文件。

**-makehardlinks** _BOOL_
> 用硬链接替换。

**-makesymlinks** _BOOL_
> 用符号链接替换。

**-dryrun** _BOOL_
> 仅模拟。

**-ignoreempty** _BOOL_
> 忽略空文件。

**-removeidentinode** _BOOL_
> 排除 inode 相同的文件。

**-outputname** _FILE_
> 结果文件名。

**-minsize** _BYTES_
> 最小文件大小。

# DESCRIPTION

**rdfind**（redundant data find）使用多阶段检测算法在多个目录树中高效定位重复文件。它先按文件大小分组，再对同大小文件的开头几个字节计算部分校验和，最后只对仍然匹配的文件执行完整校验和，因此在大型文件集上也能保持高效。

识别出重复文件后，rdfind 可以删除它们、将其替换为硬链接（节省磁盘空间的同时保留原路径），或替换为符号链接。结果文件会列出找到的所有重复项供人工审查，而 **-dryrun** 标志可模拟操作而不修改文件系统。按参数顺序最先遇到的文件总是被保留为原件。

# CAVEATS

硬链接只能在同一文件系统上创建。原始文件被移动后符号链接可能失效。删除操作请谨慎。

# HISTORY

**rdfind**（really delete find）为高效重复检测而生。其多阶段算法能快速处理大型文件集。

# INSTALL

```apt: sudo apt install rdfind```

```dnf: sudo dnf install rdfind```

```pacman: sudo pacman -S rdfind```

```apk: sudo apk add rdfind```

```zypper: sudo zypper install rdfind```

```brew: brew install rdfind```

```nix: nix profile install nixpkgs#rdfind```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fdupes](/man/fdupes)(1), [jdupes](/man/jdupes)(1), [duff](/man/duff)(1)
