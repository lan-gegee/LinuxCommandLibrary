# TAGLINE

对 Android APK 文件进行逆向工程

# TLDR

**解码**（反编译）APK

```apktool d [app.apk]```

解码到**指定目录**

```apktool d [app.apk] -o [output_dir]```

**构建**（重新编译）APK

```apktool b [decoded_dir]```

以**指定输出名**构建

```apktool b [decoded_dir] -o [output.apk]```

解码时**不含资源**

```apktool d [app.apk] -r```

解码时**不含源码**

```apktool d [app.apk] -s```

# SYNOPSIS

**apktool** _d_|_b_ [_options_] _apk_|_dir_

# DESCRIPTION

**apktool** 是一款 Android APK 逆向工程工具。它将资源解码为接近原始形态，便于检查和修改 manifest、布局及其他 XML 资源。它还能将 Dalvik 字节码反汇编为 smali。

修改完成后，apktool 可以重新构建 APK，随后需签名才能安装。

# PARAMETERS

**d**, **decode**
> 将 APK 解码到目录

**b**, **build**
> 从目录构建 APK

**-o** _path_, **--output** _path_
> 输出文件/目录

**-r**, **--no-res**
> 不解码资源

**-s**, **--no-src**
> 不解码源码（smali）

**-f**, **--force**
> 强制覆盖现有文件

**--frame-path** _dir_
> 框架文件目录

**-p** _dir_, **--frame-path** _dir_
> 存取框架文件的位置

**--use-aapt2**
> 使用 aapt2 而不是 aapt

# CONFIGURATION

**~/.local/share/apktool/framework/**
> 存放框架文件的目录，供解码和重建时使用。

# CAVEATS

重建的 APK 必须签名后才能安装。某些保护方案可能阻止成功解码。对于被大幅修改过的框架，资源解码可能失败。

# HISTORY

**apktool** 由 Brut.all 创建（Connor Tumbleson 维护其分支），约于 **2010 年**首次发布。它已成为 Android APK 逆向工程的标准工具。

# INSTALL

```apt: sudo apt install apktool```

```brew: brew install apktool```

```nix: nix profile install nixpkgs#apktool```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apksigner](/man/apksigner)(1), [jadx](/man/jadx)(1)
