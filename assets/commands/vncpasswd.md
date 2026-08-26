# TAGLINE

创建或更改 VNC 密码文件

# TLDR

**为当前用户设置 VNC 密码（交互式提示）**

```vncpasswd```

**将密码写入指定文件**

```vncpasswd [~/.vnc/passwd]```

**使用过滤模式从标准输入创建密码**

```echo "[password]" | vncpasswd -f > [~/.vnc/passwd]```

**从标准输入同时设置完全控制密码和只读密码**

```printf "[password]\n[viewpassword]\n" | vncpasswd -f > [~/.vnc/passwd]```

# SYNOPSIS

**vncpasswd** [_options_] [_passwd-file_]

# PARAMETERS

**-f**
> 过滤模式：从标准输入读取明文密码，将加密后的版本写到标准输出。此模式下过短或为空的密码会被静默接受。

_passwd-file_
> 密码文件的路径。默认为 $XDG_CONFIG_HOME/tigervnc/passwd 或 ~/.vnc/passwd，取决于 VNC 实现。

# DESCRIPTION

**vncpasswd** 用于创建或更改 VNC 服务器用于身份验证的密码文件。不带参数运行时，它会提示输入密码并将其存入 ~/.vnc/passwd。

交互模式下密码至少需要 6 个字符（-f 过滤模式接受任意长度）。由于采用基于 DES 的编码方式，只有前 8 个字符有效。存储的密码只是经过混淆处理，并非安全加密。

过滤模式（-f）从标准输入读取明文密码并将加密版本输出到标准输出，适合在脚本中创建密码文件。最多可以提供两个以换行符分隔的密码：第一个用于完全控制，第二个用于只读访问。

# SECURITY

密码文件的权限被设为仅所有者可读写（600）。这种混淆很弱；任何能访问该文件的人都可以还原出密码。网络身份验证采用挑战-应答机制，可防止网络嗅探。

# CAVEATS

只有前 8 个字符有效。密码混淆并非安全加密。文件权限对安全至关重要。不同的 VNC 实现可能带有略有差异的 vncpasswd 工具。

# HISTORY

**vncpasswd** 源自 AT&T 最初的 VNC（Virtual Network Computing）实现。各种 VNC 实现（TightVNC、TigerVNC、RealVNC）都包含各自的版本，细节略有不同，但密码文件格式相互兼容。

# INSTALL

```dnf: sudo dnf install tigervnc```

```pacman: sudo pacman -S tigervnc```

```apk: sudo apk add tigervnc```

```zypper: sudo zypper install tigervnc```

```nix: nix profile install nixpkgs#tigervnc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vncserver](/man/vncserver)(1), [vncviewer](/man/vncviewer)(1), [x11vnc](/man/x11vnc)(1), [xvnc](/man/xvnc)(1)
