# TAGLINE

Arch Linux 软件包构建脚本格式

# TLDR

**构建软件包**

```makepkg```

**构建并安装**

```makepkg -si```

**更新校验和**

```updpkgsums```

**检查 PKGBUILD**

```namcap PKGBUILD```

# SYNOPSIS

用于 Arch Linux 打包的 PKGBUILD 规范文件

# DESCRIPTION

**PKGBUILD** 是一个 shell 脚本，包含 Arch Linux 软件包的构建指令。它定义了元数据、源码以及用于编译和打包软件的函数。

makepkg 使用它来创建 .pkg.tar.zst 软件包。

# BASIC STRUCTURE

```bash
# Maintainer: Name <email>
pkgname=mypackage
pkgver=1.0.0
pkgrel=1
pkgdesc="Description of package"
arch=('x86_64')
url="https://example.com"
license=('GPL')
depends=('dep1' 'dep2')
makedepends=('cmake')
source=("$url/releases/$pkgname-$pkgver.tar.gz")
sha256sums=('SKIP')

build() {
    cd "$pkgname-$pkgver"
    ./configure --prefix=/usr
    make
}

package() {
    cd "$pkgname-$pkgver"
    make DESTDIR="$pkgdir" install
}
```

# VARIABLES

```bash
pkgname     - Package name
pkgver      - Version
pkgrel      - Release number
pkgdesc     - Description
arch        - Architectures
depends     - Runtime dependencies
makedepends - Build dependencies
source      - Source URLs
sha256sums  - Checksums
```

# FUNCTIONS

```bash
prepare()   - Prepare sources
build()     - Compile
check()     - Run tests
package()   - Install to $pkgdir
```

# CAVEATS

文件必须命名为 PKGBUILD。这是 Arch 特有的格式。务必核对校验和。可用 namcap 进行测试。

# HISTORY

PKGBUILD 格式由 **Judd Vinet** 为 **Arch Linux** 设计，使软件包构建变得简单而透明。

# SEE ALSO

[makepkg](/man/makepkg)(8), [pacman](/man/pacman)(8), [namcap](/man/namcap)(1)
