# TAGLINE

无需安装即可执行软件包

# TLDR

**不安装直接运行软件包**

```pnpx [package] [args]```

**运行特定版本**

```pnpx [package]@[version] [args]```

**以与命令名不同的软件包名运行**

```pnpx --package [package] [command]```

**安装多个软件包**并运行一条命令

```pnpx --package [pkg1] --package [pkg2] [command]```

# SYNOPSIS

**pnpx** [_options_] _package_ [_args_]

# PARAMETERS

_PACKAGE_
> 要执行的软件包。

**--package** _PKG_
> 要安装的软件包（与命令名不同时）。可多次指定。

# DESCRIPTION

**pnpx** 可以在不永久安装的情况下执行 npm 软件包，类似 npx。它会将软件包下载到临时位置，运行指定的命令，之后进行清理。这是 **pnpm dlx** 的已弃用别名；建议直接使用 **pnpm dlx**。

当可执行文件名与软件包名不同时，使用 **--package** 指定软件包名。**@version** 后缀允许运行软件包的特定版本。默认允许 pnpx 执行的软件包运行 postinstall 脚本。

# CAVEATS

**pnpx** 已被弃用，建议改用 **pnpm dlx**。需要安装 pnpm。该命令在 shell 中运行（Unix 上是 /bin/sh，Windows 上是 cmd.exe）。

# INSTALL

```dnf: sudo dnf install pnpm```

```pacman: sudo pacman -S pnpm```

```apk: sudo apk add pnpm```

```zypper: sudo zypper install pnpm```

```brew: brew install pnpm```

```nix: nix profile install nixpkgs#pnpm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pnpm](/man/pnpm)(1), [npx](/man/npx)(1), [yarn-dlx](/man/yarn-dlx)(1)
