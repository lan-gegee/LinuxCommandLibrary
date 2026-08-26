# TAGLINE

加密且节省带宽的备份工具

# TLDR

**备份目录**到远程位置

```duplicity [/path/to/source] [sftp://user@host/backup]```

**增量备份**

```duplicity --full-if-older-than [30D] [/path/to/source] [file:///backup/destination]```

**从备份恢复**

```duplicity restore [sftp://user@host/backup] [/path/to/restore]```

**恢复指定文件**

```duplicity restore --file-to-restore [relative/path/file] [backup_url] [/path/to/restore]```

**列出备份中的文件**

```duplicity list-current-files [backup_url]```

**对照源数据校验备份**

```duplicity verify [backup_url] [/path/to/source]```

**删除旧备份**

```duplicity remove-older-than [60D] [backup_url]```

**使用 GPG 密钥加密**

```duplicity --encrypt-key [KEY_ID] [/source] [destination]```

# SYNOPSIS

**duplicity** [_options_] _source_ _destination_

# DESCRIPTION

**duplicity** 是一款创建加密、节省带宽的备份工具。它用 librsync 生成只包含文件变更部分的增量归档，并用 GnuPG 进行加密和签名。

备份可以存放在本地或各种远程后端，包括 SFTP、S3、Google Cloud Storage、Azure、WebDAV 等等。加密与增量传输的结合使 duplicity 特别适合通过不可信网络进行远程/云备份。

它会周期性地创建全量备份，之后的增量备份只存储变更内容。这样既能实现任意时间点恢复，又能把存储和带宽占用降到最低。

# PARAMETERS

**full**
> 强制全量备份。

**incremental**
> 强制增量备份。

**restore**
> 从备份恢复。

**verify**
> 校验备份完整性。

**list-current-files**
> 列出当前备份中的文件。

**remove-older-than** _time_
> 删除早于指定时间的备份集。

**remove-all-but-n-full** _n_
> 只保留 n 个全量备份。

**--full-if-older-than** _time_
> 若上一次全量备份早于指定时间，则执行全量备份。

**--encrypt-key** _key_id_
> 用于加密的 GPG 密钥。

**--sign-key** _key_id_
> 用于签名的 GPG 密钥。

**--no-encryption**
> 完全禁用加密。

**--include** _pattern_
> 包含匹配模式的文件。

**--exclude** _pattern_
> 排除匹配模式的文件。

**--file-to-restore** _path_
> 恢复指定文件。

**-t** _time_, **--restore-time** _time_
> 从指定时间点恢复。

**--tempdir** _path_
> 使用指定目录存放临时文件。

**--progress**
> 显示上传进度和预计上传时间。

**--verbosity** _level_
> 设置详细程度（0-9，默认 3）。

# CAVEATS

加密备份需要 GPG 口令（脚本场景可使用 PASSPHRASE 环境变量）。首次备份始终是全量的，可能耗时较长。恢复单个文件需要下载多个增量包。后端凭据可能需要另行配置。

# HISTORY

**duplicity** 由 **Ben Escoto** 于 **2002 年**创建，是一个加密备份方案。它将 rsync 高效的增量传输算法与 GnuPG 加密相结合。该项目由多位贡献者持续维护，并扩展支持了大量云存储后端。它至今仍是安全自动化备份的热门选择。

# INSTALL

```apt: sudo apt install duplicity```

```dnf: sudo dnf install duplicity```

```pacman: sudo pacman -S duplicity```

```apk: sudo apk add duplicity```

```zypper: sudo zypper install duplicity```

```brew: brew install duplicity```

```nix: nix profile install nixpkgs#duplicity```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rdiff-backup](/man/rdiff-backup)(1), [rsync](/man/rsync)(1), [gpg](/man/gpg)(1), [restic](/man/restic)(1)
