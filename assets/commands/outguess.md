# TAGLINE

将数据隐藏在 JPEG 图像中的隐写工具

# TLDR

**在图像中嵌入数据**

```outguess -d [secret.txt] [cover.jpg] [output.jpg]```

**提取隐藏数据**

```outguess -r [stego.jpg] [output.txt]```

**使用密码嵌入**

```outguess -k "[password]" -d [secret.txt] [cover.jpg] [output.jpg]```

**使用密码提取**

```outguess -k "[password]" -r [stego.jpg] [output.txt]```

**检查嵌入容量**

```outguess -c [cover.jpg]```

# SYNOPSIS

**outguess** [_options_] [_input_] [_output_]

# PARAMETERS

**-d** _file_
> 要嵌入的数据文件。

**-r**
> 提取模式。

**-k** _key_
> 密码/密钥。

**-c**
> 检查容量。

**-F**
> 强制嵌入。

**-e**
> 使用纠错编码。

# DESCRIPTION

**OutGuess** 是一款将数据隐藏在 JPEG 图像中的隐写工具。它通过保持图像统计特性来抵抗统计分析，使其比简单方法更难被检测。

OutGuess 以维持预期统计分布的方式修改 DCT 系数。

# EXAMPLE

```bash
# Hide message
outguess -k "secret" -d message.txt photo.jpg stego.jpg

# Recover message
outguess -k "secret" -r stego.jpg recovered.txt
```

# CAVEATS

仅支持 JPEG。反复嵌入会降低图像质量。容量取决于图像复杂度。密码提供加密功能。

# HISTORY

OutGuess 由 **Niels Provos** 开发，是一款能抵抗统计隐写分析技术的隐写工具。

# INSTALL

```apt: sudo apt install outguess```

```nix: nix profile install nixpkgs#outguess```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[steghide](/man/steghide)(1), [openstego](/man/openstego)(1)
