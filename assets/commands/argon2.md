# TAGLINE

使用 Argon2 算法对密码进行哈希

# TLDR

对密码进行**哈希**

```echo -n "password" | argon2 [salt] -e```

用 **Argon2id** 变体做哈希

```echo -n "password" | argon2 [salt] -id -e```

用**自定义参数**做哈希

```echo -n "password" | argon2 [salt] -t [3] -m [16] -p [4] -e```

**输出原始字节**而非编码形式

```echo -n "password" | argon2 [salt] -r```

**固定为 Argon2 版本 13**（现行标准）

```echo -n "password" | argon2 [salt] -v [13] -e```

# SYNOPSIS

**argon2** _salt_ [_-d_|_-i_|_-id_] [_-t iterations_] [_-m memory_] [_-p parallelism_] [_-l length_] [_-e_|_-r_] [_-v_ _10|13_]

# DESCRIPTION

**argon2** 是 Argon2 密码哈希算法的命令行工具。Argon2 是 2015 年密码哈希竞赛（Password Hashing Competition）的获胜者，提供强健的内存困难型密码哈希，可抵抗 GPU 和 ASIC 攻击。

该工具支持 Argon2d（数据相关）、Argon2i（数据无关）和 Argon2id（混合）三种变体。

# PARAMETERS

**-d**
> 使用 Argon2d（数据相关，抗 GPU）。默认为 Argon2i。

**-i**
> 使用 Argon2i（数据无关，抗侧信道）。未指定变体标志时即为默认。

**-id**
> 使用 Argon2id（混合；推荐用于密码哈希）。

**-t** _N_
> 时间开销（迭代次数）。默认：_3_。

**-m** _N_
> 内存开销，表示为 2^_N_ KiB。默认：_12_（4 MiB）。

**-p** _N_
> 并行度（线程数）。默认：_1_。

**-l** _N_
> 输出哈希长度，单位字节。默认：_32_。

**-e**
> 只输出编码后的哈希（PHC 字符串格式）。

**-r**
> 只输出原始哈希字节。

**-v** _10|13_
> Argon2 算法版本。默认：_13_。

**-h**
> 显示工具用法并退出。

# CAVEATS

盐值必须作为位置参数提供，且应至少为 8 个随机字节。更高的内存/时间开销可提升安全性，但会增加计算时间。密码哈希推荐使用 Argon2id。此 CLI 只做哈希——没有内置的验证模式；请使用理解 PHC 编码输出的库来验证哈希。

# HISTORY

**Argon2** 由 Alex Biryukov、Daniel Dinu 和 Dmitry Khovratovich 设计，于 **2015** 年赢得密码哈希竞赛。OWASP 推荐将其用于密码哈希。

# INSTALL

```apt: sudo apt install argon2```

```dnf: sudo dnf install argon2```

```pacman: sudo pacman -S argon2```

```apk: sudo apk add argon2```

```zypper: sudo zypper install argon2```

```brew: brew install argon2```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[openssl](/man/openssl)(1), [bcrypt](/man/bcrypt)(1), [mkpasswd](/man/mkpasswd)(1)
