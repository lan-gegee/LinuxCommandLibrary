# TAGLINE

初始化 MariaDB 数据目录和系统表

# TLDR

**初始化 MariaDB 数据目录**

```mariadb-install-db```

**以指定用户初始化**

```mariadb-install-db --user=[mysql]```

**使用自定义数据目录初始化**

```mariadb-install-db --datadir=[/var/lib/mysql]```

**以指定基础目录初始化**

```mariadb-install-db --basedir=[/usr]```

# SYNOPSIS

**mariadb-install-db** [_options_]

# PARAMETERS

**--user** _user_
> 数据库文件的属主用户。

**--datadir** _dir_
> 数据目录路径。

**--basedir** _dir_
> MariaDB 基础目录。

**--defaults-file** _file_
> 配置文件。

**--auth-root-authentication-method** _method_
> root 认证方式。

**--skip-test-db**
> 不创建 test 数据库。

# DESCRIPTION

**mariadb-install-db** 初始化 MariaDB 的数据目录和系统表。首次启动服务器前必须执行。它会创建权限表和默认数据库。在 MariaDB 中取代了 mysql_install_db。

# INSTALL

```apt: sudo apt install mariadb-server-core```

```dnf: sudo dnf install mariadb```

```pacman: sudo pacman -S mariadb```

```apk: sudo apk add mariadb```

```zypper: sudo zypper install mariadb```

```brew: brew install mariadb```

```nix: nix profile install nixpkgs#mariadb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mariadb](/man/mariadb)(1)
