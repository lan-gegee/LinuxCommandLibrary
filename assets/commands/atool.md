# TAGLINE

用统一接口管理多种格式的归档

# TLDR

**解压归档（自动检测格式）**

```atool -x [archive.tar.gz]```

**列出归档内容**

```atool -l [archive.zip]```

**从文件或目录创建归档**

```atool -a [output.tar.gz] [file1] [file2]```

**解压到指定目录**

```atool -X [/path/to/dir] [archive.zip]```

**分别解压当前目录中的每个归档**

```atool -e -x *.zip```

**将归档中的文件打印到标准输出**

```atool -c [archive.tar.gz] [path/inside/archive]```

**显示两个归档之间的差异**

```atool -d [old.tar.gz] [new.tar.gz]```

# SYNOPSIS

**atool** [_-lxacdX_] [_options_] _archive_ [_files_...]

# PARAMETERS

**-l**, **--list**
> 列出归档内容。

**-x**, **--extract**
> 从归档中提取文件。默认情况下，若归档不够"整洁"（没有统一顶层目录），会创建一个唯一的子目录。

**-X** _PATH_, **--extract-to=**_PATH_
> 将归档提取到指定目录。

**-a**, **--add**
> 用提供的文件创建新归档。归档格式根据输出文件的扩展名推断。

**-c**, **--cat**
> 将归档中的单个文件提取到标准输出。

**-d**, **--diff**
> 提取两个归档并对其中内容运行 **diff**(1)。

**-e**, **--each**
> 对其余各个参数逐一执行所请求的操作（适合批量解压）。

**-F** _EXT_, **--format=**_EXT_
> 覆盖自动格式检测。

**-O** _OPT_, **--format-option=**_OPT_
> 向底层归档工具传递额外选项（例如 `-O-mx=9` 设置 7z 的压缩级别）。

**-D**, **--subdir**
> 解压时始终创建子目录，即使归档本身已包含顶层目录。

**-f**, **--force**
> 不询问直接覆盖已存在的文件或归档。

**-S**, **--simulate**
> 只显示将要执行的操作，不实际修改文件系统。

**-E**, **--explain**
> 打印 atool 实际运行的底层命令。

**-p**, **--page**
> 将输出通过分页器显示。

**-q**, **--quiet**
> 降低详细程度。

**-v**, **--verbose**
> 提高详细程度。

**-o** _KEY=VAL_, **--option=**_KEY=VAL_
> 在命令行覆盖某个配置项。

**--config=**_FILE_
> 加载非默认的配置文件。

# RELATED COMMANDS

**aunpack** _archive_
> `atool -x` 的快捷方式；若归档不整洁还会做清理。

**apack** _archive_ _files..._
> `atool -a` 的快捷方式。

**als** _archive_
> `atool -l` 的快捷方式。

**acat** _archive_ _file_
> `atool -c` 的快捷方式。

**adiff** _archive1_ _archive2_
> `atool -d` 的快捷方式。

**arepack** _old_ _new_
> 一步完成归档格式之间的转换。

# SUPPORTED FORMATS

- tar（plain、gzip、bzip2、xz、lzma、zstd、compress）
- zip、jar、war
- rar、7z、lzh、arj、arc
- ar、cpio、shar
- deb、rpm（通过后端工具列出/解压）

# CONFIGURATION

**~/.atoolrc**
> 用户级配置文件，设置默认值和格式偏好。

**/etc/atoolrc**
> 系统级配置文件。

# CAVEATS

需要安装相应的后端工具（tar、unzip、unrar、7z、zstd 等）；atool 只负责调度它们。归档格式检测主要依据文件扩展名，因此当扩展名缺失或有误导性时可能需要使用 **-F**。

# HISTORY

**atool** 由 **Oskar Liljeblad** 使用 Perl 编写，由 GNU 项目发行（nongnu.org/atool）。它的诞生是为了给 Unix 系统上数量繁多的归档格式提供一个统一的前端。

# INSTALL

```dnf: sudo dnf install atool```

```pacman: sudo pacman -S atool```

```zypper: sudo zypper install atool```

```brew: brew install atool```

```nix: nix profile install nixpkgs#atool```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[tar](/man/tar)(1), [unzip](/man/unzip)(1), [7z](/man/7z)(1), [unrar](/man/unrar)(1), [unar](/man/unar)(1), [zip](/man/zip)(1), [gzip](/man/gzip)(1), [bzip2](/man/bzip2)(1), [xz](/man/xz)(1), [zstd](/man/zstd)(1)
