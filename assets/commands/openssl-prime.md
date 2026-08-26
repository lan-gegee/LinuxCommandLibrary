# TAGLINE

测试数字是否为素数，或生成素数

# TLDR

**检查数字是否为素数**

```openssl prime [number]```

**检查十六进制数**

```openssl prime -hex [hex-number]```

**生成随机素数**

```openssl prime -generate -bits [256]```

**生成安全素数**

```openssl prime -generate -bits [256] -safe```

# SYNOPSIS

**openssl** **prime** [_options_] [_number_]

# PARAMETERS

**-hex**
> 以十六进制输入/输出。

**-generate**
> 生成一个素数。

**-bits** _n_
> 生成时使用的位数。

**-safe**
> 生成安全素数（p 且 (p-1)/2 也是素数）。

**-checks** _n_
> Miller-Rabin 测试的次数。

# DESCRIPTION

**openssl prime** 测试数字是否为素数或生成素数。使用 Miller-Rabin 素性测试。适合需要素数的密码学应用。

# INSTALL

```apt: sudo apt install openssl```

```dnf: sudo dnf install openssl```

```pacman: sudo pacman -S openssl```

```apk: sudo apk add openssl```

```zypper: sudo zypper install openssl```

```brew: brew install openssl```

```nix: nix profile install nixpkgs#openssl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl](/man/openssl)(1)
