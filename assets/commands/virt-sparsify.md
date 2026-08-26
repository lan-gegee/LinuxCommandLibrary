# TAGLINE

将虚拟机磁盘镜像稀疏化

# TLDR

通过复制到新文件对磁盘镜像进行稀疏化

```virt-sparsify [path/to/input.qcow2] [path/to/output.qcow2]```

创建**压缩**的稀疏镜像

```virt-sparsify --compress [path/to/image.qcow2] [path/to/new_image.qcow2]```

**原地**稀疏化（无需额外磁盘空间）

```virt-sparsify --in-place [path/to/image.img]```

稀疏化的同时**转换**格式

```virt-sparsify --convert [qcow2|raw|vdi] [path/to/input] [path/to/output]```

将镜像内的特定分区清零并稀疏化

```virt-sparsify --zero [/dev/sda2] [path/to/input] [path/to/output]```

# SYNOPSIS

**virt-sparsify** [_OPTIONS_] _indisk_ _outdisk_

**virt-sparsify** [_OPTIONS_] **--in-place** _disk_

# PARAMETERS

**--compress**
> 压缩输出文件。仅适用于 qcow2 格式。与 **--in-place** 不兼容。

**--in-place**
> 原地稀疏化镜像而不创建副本。效率更高，但可回收的空间可能略少。与 **--convert**、**--compress** 和 **-o** 不兼容。

**--convert** _FORMAT_
> 将输出转换为指定格式（qcow2、raw、vdi、vmdk 等）。默认与输入格式相同。

**--format** _FORMAT_
> 声明输入磁盘镜像的格式（raw、qcow2 等）。未指定时会自动检测。处理不受信任的镜像时应显式设置。

**--ignore** _filesystem_|_volgroup_
> 不对指定的文件系统或卷组上的空闲空间清零。使用 **--in-place** 时，该文件系统会被完全跳过。可多次指定。卷组名称不带 `/dev/` 前缀。

**--zero** _partition_|_logvol_
> 将指定分区或逻辑卷的全部内容清零。设备上的所有数据都会丢失，但稀疏化效果最大化。

**--tmp** _block\_device_|_directory_|**prebuilt:**_file_
> 设置复制过程中使用的临时 overlay 文件的位置。`prebuilt:` 形式接受一个刚格式化好的 qcow2 文件，并以输入磁盘作为其后备文件（由 oVirt 使用）。

**--check-tmpdir** _ignore_|_continue_|_warn_|_fail_
> 控制临时目录空间不足时的行为。默认为 `warn`（警告并提示确认）。

**-o** _option_[,_option_,...]
> 向 **qemu-img** 传递输出选项以微调输出格式。所有选项放在单个 **-o** 标志中，以逗号分隔。

**-q**, **--quiet**
> 禁用进度条和非必要输出。

**--machine-readable**[=_format_]
> 输出便于程序解析的格式，启用结构化的进度和状态消息。

**--key** _ID_:**key:**_KEY_|**file:**_file_|**clevis**
> 通过字符串、文件名或 Clevis 网络绑定解密，为指定磁盘、分区或逻辑卷提供 LUKS 加密密钥。

**--keys-from-stdin**
> 从标准输入读取加密口令，而不是在终端提示输入。

**-v**, **--verbose**
> 启用详细的调试消息。

**-V**, **--version**
> 显示版本号并退出。

**-x**
> 启用 libguestfs API 调用跟踪。

# DESCRIPTION

**virt-sparsify** 通过将客户机文件系统内部的空闲块清零，然后创建稀疏副本，使虚拟机磁盘镜像变得稀疏（精简配置）。这可以显著减小镜像文件的磁盘占用。

在复制模式（默认）下，输入镜像保持不变，生成一个新的稀疏输出镜像。可以使用 **--convert** 更改输出格式，使用 **--compress** 进行压缩。

在 **--in-place** 模式下，直接修改镜像而无需额外磁盘空间，代价是可能回收的空间略少。

# CAVEATS

运行 **virt-sparsify** 前必须关闭虚拟机，以免数据损坏。复制模式下，必须有足够的空闲磁盘空间来容纳临时 overlay 和输出镜像。使用 **--in-place** 前请备份原始镜像。该工具不支持运行中的或实时的客户机。

# INSTALL

```apt: sudo apt install guestfs-tools```

```dnf: sudo dnf install guestfs-tools```

```pacman: sudo pacman -S guestfs-tools```

```zypper: sudo zypper install guestfs-tools```

```nix: nix profile install nixpkgs#guestfs-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[virt-resize](/man/virt-resize)(1), [qemu-img](/man/qemu-img)(1), [truncate](/man/truncate)(1)
