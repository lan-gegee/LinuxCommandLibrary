# TAGLINE

PHP 命令行解释器

# TLDR

**运行 PHP 脚本**

```php [script.php]```

**内联执行 PHP 代码**

```php -r 'echo "Hello\n";'```

**启动内置 Web 服务器**

```php -S localhost:8000```

**以指定文档根目录启动内置服务器**

```php -S localhost:8000 -t [/path/to/docroot]```

**进入交互模式（REPL）**

```php -a```

**只检查脚本语法错误而不执行**

```php -l [script.php]```

**显示 phpinfo() 输出**

```php -i```

**显示已加载的模块**

```php -m```

在运行时**设置配置指令**

```php -d [memory_limit=256M] [script.php]```

**使用特定的 php.ini 运行**

```php -c [/path/to/php.ini] [script.php]```

**显示加载了哪些 php.ini 文件**

```php --ini```

# SYNOPSIS

**php** [_options_] [_-f_] [_file_] [_args_]

# PARAMETERS

_FILE_
> 要执行的 PHP 脚本。

**-r** _CODE_
> 执行 PHP 代码（不需要脚本标签）。

**-S** _ADDR:PORT_
> 启动内置开发 Web 服务器。

**-t** _DOCROOT_
> 内置 Web 服务器的文档根目录。

**-a**
> 以交互方式运行（REPL 模式）。

**-l**
> 仅做语法检查（lint），不执行。

**-i**
> 输出 phpinfo() 配置详情。

**-m**
> 显示编译进内核的模块。

**-v**
> 显示版本信息。

**-c** _PATH_
> 使用指定的 php.ini 文件或目录。

**-n**
> 不加载任何 php.ini 文件运行。

**-d** _DIRECTIVE=VALUE_
> 在运行时设置一条 php.ini 指令。

**-e**
> 为调试器/性能分析器生成扩展信息。

**-f** _FILE_
> 解析并执行给定文件（显式形式）。

**--ini**
> 显示 PHP 会查找并加载的配置文件名称。

**-w**
> 输出去除注释和空白后的源码。

**-B** _CODE_
> 在处理 stdin 之前先执行代码（配合 -R/-F）。

**-R** _CODE_
> 对来自 stdin 的每一行输入执行代码。

**-F** _FILE_
> 对来自 stdin 的每一行输入解析并执行文件。

# DESCRIPTION

**php** 是 PHP 解释器的命令行界面。它可以执行 PHP 脚本、运行内联代码、检查文件语法错误，以及启动内置的开发用 Web 服务器。PHP 支持过程式、面向对象和函数式编程范式。

内置 Web 服务器（`-S`）仅用于开发，不应在生产环境中使用。它从当前目录或指定的文档根目录提供文件服务。

# CAVEATS

配置由 php.ini 控制；已加载文件的位置因系统而异（可用 `php --ini` 查找）。扩展的可用性取决于编译期选项和已安装的软件包。内置 Web 服务器是单线程的，不适合生产使用。

# HISTORY

PHP 由 **Rasmus Lerdorf** 于 **1994 年**创建，最初是一组用于跟踪其网络简历访问量的 CGI 二进制程序。后来演变为完整的服务端脚本语言。PHP 5 引入了成熟的对象模型，PHP 7（2015 年）带来重大性能提升。PHP 8（2020 年）增加了 JIT 编译、命名参数和注解属性。

# INSTALL

```dnf: sudo dnf install php```

```pacman: sudo pacman -S php```

```apk: sudo apk add php85```

```brew: brew install php```

```nix: nix profile install nixpkgs#php85```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[composer](/man/composer)(1), [phpunit](/man/phpunit)(1), [pecl](/man/pecl)(1), [php-cs-fixer](/man/php-cs-fixer)(1), [phpize](/man/phpize)(1), [php-config](/man/php-config)(1)
