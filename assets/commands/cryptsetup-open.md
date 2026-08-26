# TAGLINE

打开并映射 LUKS 加密卷

# TLDR

**打开** LUKS 卷并创建解密映射

```cryptsetup open [/dev/sdXY] [mapping_name]```

使用**密钥文件**代替密码短语

```cryptsetup open -d [path/to/keyfile] [/dev/sdXY] [mapping_name]```

为 SSD 启用 **TRIM** 支持

```cryptsetup open --allow-discards [/dev/sdXY] [mapping_name]```

启用 TRIM 并使其**持久化**

```cryptsetup open --allow-discards --persistent [/dev/sdXY] [mapping_name]```

以**只读**方式打开

```cryptsetup open -r [/dev/sdXY] [mapping_name]```

# SYNOPSIS

**cryptsetup open** [_options_] _device_ _mapping_name_

# DESCRIPTION

**cryptsetup open** 为加密的 LUKS 卷创建解密映射。解密后的设备出现在 /dev/mapper/mapping_name，可以像普通块设备一样使用。

打开之后，映射设备即可被挂载，或与 LVM、文件系统创建等操作配合使用。

# PARAMETERS

**-d, --key-file** _file_
> 使用密钥文件代替密码短语

**--allow-discards**
> 允许 TRIM/discard 命令透传（适用于 SSD）

**--persistent**
> 将选项保存到 LUKS 头中

**-r, --readonly**
> 以只读模式打开

**--type** _type_
> 指定设备类型（luks、luks1、luks2、plain、tcrypt、bitlk）

# CAVEATS

启用 TRIM 后，可能会泄露关于已释放块的最少量信息，进而暴露文件系统类型。不过，出于延长 SSD 寿命的考虑，通常仍建议开启 TRIM，且实际数据依然处于加密状态。

# INSTALL

```apt: sudo apt install cryptsetup-bin```

```dnf: sudo dnf install cryptsetup```

```pacman: sudo pacman -S cryptsetup```

```apk: sudo apk add cryptsetup```

```zypper: sudo zypper install cryptsetup```

```nix: nix profile install nixpkgs#cryptsetup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cryptsetup](/man/cryptsetup)(8), [cryptsetup-luksformat](/man/cryptsetup-luksformat)(8)
