# TAGLINE

在不解密的前提下检查 age 加密文件

# TLDR

**查看** age 文件的元数据

```age-inspect [secrets.age]```

**从标准输入读取**

```cat [secrets.age] | age-inspect```

显式使用短横线**从标准输入读取**

```age-inspect - < [secrets.age]```

为脚本输出**机器可读的 JSON**

```age-inspect --json [secrets.age]```

**打印版本**并退出

```age-inspect --version```

# SYNOPSIS

**age-inspect** [**--json**] [_INPUT_]

# DESCRIPTION

**age-inspect** 报告由 **age**(1) 生成的文件的元数据，而不执行任何解密操作。它会解析 age 文件头，识别文件格式版本，列出用于封装文件密钥的 recipient stanza 类型（例如 `X25519`、`scrypt`、`ssh-ed25519` 或后量子的 `mlkem768x25519`），并报告是否使用了 ASCII armor 封装。

当输入是普通文件（而非管道）时，该工具还会打印大小明细：头部、armor 开销、加密开销和载荷，从而无需提供身份密钥即可估计受保护数据的大小。由于不需要任何密钥材料，**age-inspect** 可以安全地运行在来自不可信方的文件上，用来判断哪些接收者能够解密它们，或者审计存放归档机密的目录。

如果省略 _INPUT_ 或将其设为 `-`，则从标准输入读取文件。

# PARAMETERS

**--json**
> 以 JSON 对象形式输出检查结果，便于程序化处理（recipient 类型、后量子标志、armor 标志以及各大小字段）。

**--version**
> 打印 **age-inspect** 版本并退出。

# CAVEATS

**age-inspect** 绝不会解密载荷，因此它无法告诉你某个身份能否成功解密，只能说明存在哪些 recipient stanza 类型。对于可寻址（seekable）的文件，大小数值是精确的；从管道读取时，载荷大小会报告为未知。该工具是在版本 **1.3.0** 中加入官方 **age** 发行版的；更早的版本只附带 `age` 和 `age-keygen`。

# HISTORY

**age-inspect** 随 **Filippo Valsorda** 的 **age** 参考实现一同分发。它在 **2025** 年的 **age 1.3.0** 中推出，同期加入了对后量子 `mlkem768x25519` recipient 类型的支持，使人们不必拆封文件就能分析归档的 age 文件（recipient 构成、armor 与大小）。

# INSTALL

```apt: sudo apt install age```

```dnf: sudo dnf install age```

```pacman: sudo pacman -S age```

```apk: sudo apk add age```

```zypper: sudo zypper install age```

```brew: brew install age```

```nix: nix profile install nixpkgs#age```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[age](/man/age)(1), [age-keygen](/man/age-keygen)(1), [gpg](/man/gpg)(1), [openssl](/man/openssl)(1)
