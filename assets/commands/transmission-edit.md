# TAGLINE

修改种子文件的元数据

# TLDR

**向种子添加 tracker**

```transmission-edit -a [http://tracker.example.com/announce] [file.torrent]```

**删除 tracker**

```transmission-edit -d [http://tracker.example.com/announce] [file.torrent]```

**替换 tracker** URL 子串

```transmission-edit -r [old_tracker] [new_tracker] [file.torrent]```

**显示种子文件中当前的 tracker**

```transmission-edit -s [file.torrent]```

# SYNOPSIS

**transmission-edit** [_options_] _torrent_file_

# PARAMETERS

**-a**, **--add** _url_
> 添加 tracker 通告 URL（若尚未存在）。

**-d**, **--delete** _url_
> 删除 tracker 通告 URL。

**-r**, **--replace** _old_ _new_
> 在通告 URL 中执行子串查找并替换。

**-s**, **--list**
> 显示当前的 tracker。

**-h**, **--help**
> 显示帮助并退出。

# DESCRIPTION

**transmission-edit** 是一个用于修改 .torrent 文件通告 URL 的命令行工具。它可以添加、删除或替换现有种子文件中的 tracker URL。**-r** 选项执行子串匹配，当 tracker 更换域名或你的密钥变更时非常有用。它是 Transmission BitTorrent 客户端套件的一部分。

# INSTALL

```apt: sudo apt install transmission-cli```

```dnf: sudo dnf install transmission-cli```

```pacman: sudo pacman -S transmission-cli```

```apk: sudo apk add transmission-extra```

```brew: brew install transmission-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[transmission-cli](/man/transmission-cli)(1), [transmission-create](/man/transmission-create)(1), [transmission-show](/man/transmission-show)(1), [transmission-daemon](/man/transmission-daemon)(1), [transmission-remote](/man/transmission-remote)(1)
