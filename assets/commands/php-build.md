# TAGLINE

从源码构建各版本的 PHP，供 phpenv 使用或独立使用

# TLDR

**列出可用的 PHP 版本**

```php-build --definitions```

**安装指定 PHP 版本**

```php-build [8.2.0] [~/.phpenv/versions/8.2.0]```

**附带 configure 选项安装**

```PHP_BUILD_CONFIGURE_OPTS="--with-openssl" php-build [8.2.0] [/path/to/install]```

**以调试方式安装指定版本**

```php-build -v [8.2.0] [/path/to/install]```

# SYNOPSIS

**php-build** [_options_] _version_ _install-path_

# PARAMETERS

**--definitions**
> 列出可用版本。

**-v**
> 详细模式。

**-i** _file_
> 读取自定义定义。

**--pear**
> 安装 PEAR。

# DESCRIPTION

**php-build** 从源码构建各个 PHP 版本，供 phpenv 使用或独立使用。它负责下载、配置、编译和安装多个 PHP 版本，包括选择正确的 OpenSSL/curl/ICU 依赖，并为旧版本应用补丁。

它通常通过 **phpenv install** 调用，但也可以直接运行，把 PHP 版本安装到任意前缀目录。

# ENVIRONMENT

**PHP_BUILD_CONFIGURE_OPTS**
> 传给 PHP **./configure** 脚本的额外选项。

**PHP_BUILD_EXTRA_MAKE_ARGUMENTS**
> 编译期间传给 **make** 的额外参数。

**PHP_BUILD_ROOT**
> 构建的根目录。

# CAVEATS

编译耗时较长。需要构建依赖。与 phpenv 配合可用于版本管理。

# HISTORY

php-build 是 **phpenv** 生态的一部分，灵感来自 ruby-build，用于管理多个 PHP 版本。

# INSTALL

```dnf: sudo dnf install php```

```pacman: sudo pacman -S php```

```apk: sudo apk add php85```

```brew: brew install php```

```nix: nix profile install nixpkgs#php85```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[phpenv](/man/phpenv)(1), [php](/man/php)(1), [pecl](/man/pecl)(1)
