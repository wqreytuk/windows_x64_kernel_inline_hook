使用示例：

```
-ca DbgPrompt -hba fffff804`481fbc80 -hea fffff804`481fbc8a  -rba '' -mn nt-nt -pn avscan  -comment "break before calling iofcalldriver at IopParseDevice"

```

如果只是hook第三方的驱动，问题不大，但是如果要hook windows自己的内核模块，可能会超出2gb的inline hook jmp指令25ff的上限

对于这种情况，-ca选项就派上用场了，比如我们要hook nt模块的一个函数

如果不使用-ca选项，就会出现超出2gb的问题，25ff没办法跳到目标内存位置，我们使用-ca选项指定一个nt中的内存地址

这里我们使用DbgPrompt函数，这个函数一般是用不上的

-rba指定拦截参数
-hba和-hea指定hook的起始和结束地址
-mn指定模块名称，如果你想使用相对地址，那么这里直接写模块名称就行了，如果你想使用绝对地址，这里就写`模块名称-模块名称`
-pn指定用来hook的驱动的名称
