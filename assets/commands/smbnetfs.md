# TAGLINE

用于 SMB 网络浏览的 FUSE 文件系统

# TLDR

在挂载点**挂载** SMB 共享

```smbnetfs [mountpoint]```

使用**自定义配置**文件挂载

```smbnetfs -o config=[~/.smb/smbnetfs.conf] [mountpoint]```

以**调试**输出方式挂载

```smbnetfs -d [mountpoint]```

以**前台**方式挂载

```smbnetfs -f [mountpoint]```

**卸载**

```fusermount -u [mountpoint]```

# SYNOPSIS

**smbnetfs** [_OPTIONS_] _mountpoint_

# PARAMETERS

**-f**
> 以前台方式运行（不守护进程化）。

**-d**
> 启用调试输出（隐含 -f）。

**-o** _options_
> 挂载选项（FUSE 和 smbnetfs 选项）。

**-o config=** _PATH_
> 配置文件的路径（默认：~/.smb/smbnetfs.conf）。

**-o smbnetfs_debug=** _N_
> SMBNetFS 调试级别（N <= 10）。

**-o smb_debug_level=** _N_
> Samba 调试级别（N <= 10）。

**-o smb_timeout=** _T_
> Samba 应答超时时间，单位毫秒（默认：20000）。

**-o smb_tree_scan_period=** _T_
> 网络树扫描间隔，单位秒（默认：300）。

**-o show_$_shares=** _BOOL_
> 显示隐藏共享（默认：off）。

**-h**, **--help**
> 显示帮助。

**-V**, **--version**
> 显示版本。

# DESCRIPTION

**smbnetfs** 是一个 FUSE 文件系统，在 Linux 和 FreeBSD 上提供类似 Windows 网上邻居的功能。它以交互方式挂载 SMB/CIFS 共享，允许通过文件系统层级浏览和访问网络资源。

挂载完成后，进入挂载点即可看到可用的工作组、服务器和共享，它们以目录形式呈现。身份验证会自动处理，或通过配置文件完成。该文件系统与标准文件操作集成，使任何应用程序都能访问网络共享。

# CONFIGURATION

配置目录 **~/.smb** 中至少应包含 **smb.conf**（可从 /etc/samba/ 复制）和 **smbnetfs.conf**。配置内容包括：

- 共享的默认凭据
- 工作组设置
- 特定服务器的身份验证
- 挂载选项

凭据也可以存储在 **~/.smb/smbnetfs.auth** 中，用于对特定服务器或共享进行自动身份验证。如果构建时启用了 libsecret 支持，还可以从密钥环中获取密码。

# CAVEATS

需要内核支持 FUSE。性能可能比直接使用 mount.cifs 挂载慢。配置文件中的身份验证凭据应设置受限的权限。某些 SMB 功能可能无法通过 FUSE 层完全支持。

# HISTORY

**smbnetfs** 作为一个开源项目创建，旨在提供类似 Windows 的便捷网络浏览功能。它基于 FUSE（用户空间文件系统）和 Samba 的 libsmbclient 构建。该项目自 **2000 年代中期**以来一直活跃开发，以 GPL-2.0 许可证发布。

# INSTALL

```apt: sudo apt install smbnetfs```

```pacman: sudo pacman -S smbnetfs```

```nix: nix profile install nixpkgs#smbnetfs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[smbclient](/man/smbclient)(1), [mount.cifs](/man/mount.cifs)(8), [fusermount](/man/fusermount)(1), [samba](/man/samba)(7)
