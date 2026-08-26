# TAGLINE

生成 128 位随机十六进制数

# TLDR

生成 **128 位随机**十六进制数

```mcookie```

使用**文件**作为额外的熵源

```mcookie --file [path/to/file]```

从文件中最多读取**指定字节数**作为种子

```mcookie --file [path/to/file] --max-size [512]```

显示关于随机性来源的**详细**信息

```mcookie --verbose```

显示**版本**信息

```mcookie --version```

# SYNOPSIS

**mcookie** [_options_]

# DESCRIPTION

**mcookie** 生成一个 128 位随机十六进制数（32 个十六进制字符）。它主要用于生成 X authority cookie，但也可用于任何需要随机数据的场景。

# PARAMETERS

**-f, --file FILE**
> 使用文件内容作为额外的熵源

**-m, --max-size BYTES**
> 从文件中读取的最大字节数

**-v, --verbose**
> 打印关于随机性来源的详细信息

**-V, --version**
> 显示版本信息并退出

**-h, --help**
> 显示帮助文本并退出

# OUTPUT

32 个十六进制字符（128 位随机数据），打印到标准输出，末尾带换行符。

# CAVEATS

以 /dev/urandom 作为主要熵源。是 util-linux 软件包的一部分。输出未经密码学审计；若用于加密密钥生成，请改用 openssl 或 gpg。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add mcookie```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xauth](/man/xauth)(1), [uuidgen](/man/uuidgen)(1), [openssl](/man/openssl)(1)
