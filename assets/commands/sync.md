# TAGLINE

将文件系统缓冲区刷写到磁盘

# TLDR

将**所有文件系统缓冲区**刷写到磁盘

```sync```

**同步特定文件**

```sync [path/to/file]```

**只同步数据**（跳过元数据）

```sync -d [path/to/file]```

**同步包含指定文件的文件系统**

```sync -f [path/to/file]```

# SYNOPSIS

**sync** [_OPTION_] [_FILE_]...

# PARAMETERS

**-d**, **--data**
> 只同步文件数据，跳过不必要的元数据

**-f**, **--file-system**
> 同步包含指定文件的文件系统

**--help**
> 显示帮助并退出

**--version**
> 输出版本信息并退出

# DESCRIPTION

**sync** 刷新文件系统缓冲区，强制将被修改的块（脏页）写入磁盘。这确保当前保存在内存中的数据被持久化到存储设备。

出于性能考虑，Linux 会在内存中缓冲写操作，对磁盘 I/O 进行合并与重排。这样做虽然高效，但意味着意外崩溃或断电可能导致数据丢失。sync 强制内核把缓冲的数据写入磁盘，以保证数据完整性。

不带参数调用时，sync 会刷新全系统的所有缓冲区。带 FILE 参数时，则只同步这些文件。

# CAVEATS

sync 保证数据到达设备驱动层，但不保证物理写入磁盘盘片或闪存已完成。对于 SSD 和某些带写入缓存的硬盘，数据可能仍停留在硬盘的内部缓存中。现代工具如 **umount**、**reboot** 和 **shutdown** 会自动调用 sync。

# HISTORY

sync 自 Unix 早期就已是其中一员，用于确保关机或移除介质前的文件系统一致性。由 Jim Meyering 为 GNU coreutils 编写。底层的 sync(2) 系统调用自最初的 Unix 就已存在。

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

[umount](/man/umount)(8), [shutdown](/man/shutdown)(8)
