# TAGLINE

移动和重命名文件与目录

# TLDR

**将文件移动到目录**

```mv [source] [directory/]```

**重命名文件**

```mv [oldname.txt] [newname.txt]```

**将多个文件移动到目录**

```mv [file1] [file2] [directory/]```

**覆盖前进行确认**

```mv -i [source] [destination]```

**不覆盖已有文件**

```mv -n [source] [destination]```

**移动并显示执行过程**

```mv -v [source] [destination]```

**移动时备份已有的目标文件**

```mv --backup=numbered [source] [destination]```

# SYNOPSIS

**mv** [_options_] _source_... _destination_

# PARAMETERS

**-i**, **--interactive**
> 覆盖已有文件前先提示确认。

**-f**, **--force**
> 覆盖前不做提示。优先级高于 **-i** 和 **-n**。

**-n**, **--no-clobber**
> 不覆盖已有文件。优先级高于 **-i** 和 **-f**。

**-v**, **--verbose**
> 打印每个正在移动的文件的名称。

**-u**, **--update**
> 仅当源文件比目标文件新、或目标不存在时才移动。

**--backup**[=_CONTROL_]
> 为每个已有的目标文件创建备份。CONTROL 可为 numbered、existing、simple 或 none。

**-S**, **--suffix** _SUFFIX_
> 覆盖常规的备份后缀（默认 ~）。

**-t**, **--target-directory** _DIRECTORY_
> 将所有源文件移入指定目录。

**-T**, **--no-target-directory**
> 将目标视为普通文件而非目录。

# DESCRIPTION

**mv** 移动和重命名文件与目录。当源和目标位于同一文件系统上时，它执行原子性的重命名操作。跨文件系统移动时，它会先复制数据再删除原文件。

重命名本质上就是在同一目录内移动文件。将文件移动到某个目录中，会使其以相同的基名出现在该目录内。

如果给出多个源文件，最后一个参数必须是目录，所有源文件都会被移入其中。

# CAVEATS

**mv** 默认直接覆盖已存在的目标文件且不发出警告。请使用 **-i** 或 **-n** 防止意外丢失数据。跨文件系统移动不是原子操作：文件先被复制，然后原文件才被删除。

# HISTORY

**mv** 是最早的 Unix 命令之一，自 1971 年的 Version 1 AT&T Unix 起就已存在。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cp](/man/cp)(1), [rm](/man/rm)(1), [rename](/man/rename)(1), [rsync](/man/rsync)(1), [install](/man/install)(1)
