# TAGLINE

systemd 文件系统层级结构文档

# TLDR

**查看文件系统层级结构文档**

```man file-hierarchy```

# DESCRIPTION

**file-hierarchy** 是一份 systemd 文档页（man page），描述基于 systemd 的 Linux 系统所采用的文件系统层级结构。它记录了 /、/etc、/usr、/var 等关键位置下各目录的用途。

这不是一个可执行命令，而是一份参考文档，解释文件应当放在哪里以及为什么。

# KEY DIRECTORIES

```
/               Root filesystem
/boot           Boot loader files
/etc            Host-specific configuration
/home           User home directories
/root           Root user's home
/run            Runtime variable data
/srv            Service data
/tmp            Temporary files
/usr            Vendor-supplied OS resources
/usr/bin        Executables
/usr/lib        Libraries
/usr/share      Architecture-independent data
/var            Variable data
/var/cache      Application caches
/var/lib        State information
/var/log        Log files
/var/tmp        Persistent temporary files
```

# SYSTEMD SPECIFICS

- /run 取代 /var/run
- 单元文件位于 /usr/lib/systemd
- 本地覆盖配置位于 /etc/systemd
- 合并式 /usr（bin、sbin、lib 已合并）

# CAVEATS

这是一份文档页，不是可执行命令。其中描述的层级结构是基于 systemd 的发行版所特有的，在其他 Linux 系统上可能有所不同。

# INSTALL

```apt: sudo apt install file```

```dnf: sudo dnf install file```

```pacman: sudo pacman -S file```

```apk: sudo apk add file```

```zypper: sudo zypper install file```

```brew: brew install file```

```nix: nix profile install nixpkgs#file```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mount](/man/mount)(8), [umount](/man/umount)(8)
