# TAGLINE

arduino-cli 的交互式 TUI 封装

# TLDR

**启动交互式界面**

```aci```

# SYNOPSIS

**aci**

# DESCRIPTION

**arduino-cli-interactive**（以 **aci** 调用）是一个基于 Bash 的终端用户界面，为官方 arduino-cli 工具提供交互式菜单封装。用户无需记忆板卡 FQBN 和命令行参数，即可通过 Charm 的 gum 库驱动的可滚动菜单选择板卡、端口和操作。

该工具支持板卡管理与选择、sketch 的创建/编辑/编译/上传、库管理、ESP8266/ESP32 及第三方板卡核心的安装、内置串口监视器，以及面向初学者的示例代码。

# CAVEATS

需要安装 **arduino-cli** 和 **gum**。初始设置需要安装 Arduino AVR 核心。由于是 Bash Shell 脚本编写，主要面向 Linux 和 macOS。

# HISTORY

**arduino-cli-interactive** 由印度的电子与通信工程专业学生 **Vaishnav-Sabari-Girish** 开发，起因是他对 Linux 上 Arduino IDE 的不满。采用 Apache 2.0 许可证，首次发布于 2024 年 12 月。

# INSTALL

```pacman: sudo pacman -S arduino-cli```

```brew: brew install arduino-cli```

```nix: nix profile install nixpkgs#arduino-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[arduino-cli](/man/arduino-cli)(1), [screen](/man/screen)(1), [minicom](/man/minicom)(1)
