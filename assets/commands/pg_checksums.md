# TAGLINE

启用、禁用或校验数据校验和

# TLDR

**启用校验和**

```pg_checksums -e -D [data_dir]```

**禁用校验和**

```pg_checksums -d -D [data_dir]```

**验证校验和**

```pg_checksums -c -D [data_dir]```

# SYNOPSIS

**pg_checksums** [_options_] [**-D**] _datadir_

# PARAMETERS

**-D**, **--pgdata** _dir_
> 数据目录。

**-c**, **--check**
> 验证校验和。

**-e**, **--enable**
> 启用校验和。

**-d**, **--disable**
> 禁用校验和。

**-v**, **--verbose**
> 详细输出。

**-P**, **--progress**
> 显示进度。

# DESCRIPTION

**pg_checksums** 用于启用、禁用或验证数据校验和。校验和能够检测数据损坏。运行前必须先停止服务器。生产数据库建议启用。

# CAVEATS

启用或禁用校验和之前必须停止服务器。

# INSTALL

```dnf: sudo dnf install postgresql17```

```apk: sudo apk add postgresql17```

```zypper: sudo zypper install postgresql17```

```nix: nix profile install nixpkgs#pg_checksums```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_amcheck](/man/pg_amcheck)(1), [initdb](/man/initdb)(1)
