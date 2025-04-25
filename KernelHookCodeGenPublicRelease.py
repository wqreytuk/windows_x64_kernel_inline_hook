windbgHookIns = """
.reload /f f312be6ae61f4caf8305ffedc3a0f762.sys 
u mydriver1!driverentry
far jmp
	;Mark
eq 4cddef71310442818dbd373c59e45bb6 mydriver1!ph
ew 819f5d66ab064d1991d4ab4ed5c31db6 25ff
ed 1+819f5d66ab064d1991d4ab4ed5c31db6 +1 	8d591a5375ee468580ff06c65f2cf77c-455dc6a29c3f4f32a95e2c3a1a1ae79e-6




 mydriver1!ph
eb mydriver1!ph+0 9c
eb mydriver1!ph+1 50
eb mydriver1!ph+2 53
eb mydriver1!ph+3 51
eb mydriver1!ph+4 52
eb mydriver1!ph+5 56
eb mydriver1!ph+6 57
eb mydriver1!ph+7 55
eb mydriver1!ph+8 54
ew mydriver1!ph +9 5041
ew mydriver1!ph +b 5141
ew mydriver1!ph +d 5241
ew mydriver1!ph +f 5341
ew mydriver1!ph +11 5441
ew mydriver1!ph+13 5541
ew mydriver1!ph+15 5641
ew mydriver1!ph +17 5741
eb mydriver1!ph +8 90

push r13
pop rdx
push rdi
pop rcx
 575a5541
59
ed mydriver1!ph +17+2 575a5541
eb mydriver1!ph +17+2 +4 59


// 保护栈空间
sub rsp,0x38
add rsp,0x38
fff803`4aad8aba  38ec8348
kd> dds  fffff803`4aad8afb l1
fffff803`4aad8afb  38c48348
ed mydriver1!ph +5+19 38ec8348
ew mydriver1!ph +4+5+19 b848
ew mydriver1!ph +4+5+1b+8   d0ff
ed mydriver1!ph+4+5+1b+8 +2 38c48348


ew mydriver1!ph+8+5+1b+a  5f41
ew mydriver1!ph+8+5+1b+a +2 5e41
ew mydriver1!ph+8+5+1b+a +4 5d41
ew mydriver1!ph+8+5+1b+a+6  5c41
ew mydriver1!ph+8+5+1b+a +8 5b41
ew mydriver1!ph+8+5+1b+a +a 5a41
ew mydriver1!ph+8+5+1b+a +c 5941
ew mydriver1!ph+8+5+1b+a +e 5841
eb mydriver1!ph+8+5+1b+a-1+11 5d
eb mydriver1!ph+8+5+1b+a-1+12 5f
eb mydriver1!ph+8+5+1b+a-1+13 5e
eb mydriver1!ph+8+5+1b+a-1+14 5a
eb mydriver1!ph+8+5+1b+a-1 +15 59
eb mydriver1!ph+8+5+1b+a-1 +16 5b
eb mydriver1!ph+8+5+1b+a-1 +17 58
eb mydriver1!ph+8+5+1b+a-1 +17 +1 9d
eb mydriver1!ph+8+42 c3


ed mydriver1!ph+0x19  38ec8348
ew mydriver1!ph+0x19 +4 25ff
ed mydriver1!ph+0x19 +4 +2 d745d615b09542e8ba57195ae0a4aa63-mydriver1!ph-0x19-4-6
ed mydriver1!ph+0x19 +4 +2+4 38c48348
ed mydriver1!ph+0x19 90909090
eq mydriver1!ph+0x23 9090909090909090
ew mydriver1!ph+0x23 +8 9090
ew mydriver1!ph+0x23 +8+2 9090
ew mydriver1!ph+0x23+8+2+2 9090
eb mydriver1!ph+0x23+8+2+2+2 90
;Mark
eq d745d615b09542e8ba57195ae0a4aa63 mydriver1!pivot	



mydriver!pivot

前面预留一堆nop进行 寄存器的转移
后面call handler
然后jmp back
留0x20个nop 后面不够再说
eq mydriver1!pivot 9090909090909090
eq mydriver1!pivot +8 9090909090909090
eq mydriver1!pivot+10 9090909090909090
eq mydriver1!pivot +18 9090909090909090

eq mydriver1!pivot+0x20 9090909090909090
eq mydriver1!pivot+0x20 +8 9090909090909090
eq mydriver1!pivot+0x20+10 9090909090909090
eq mydriver1!pivot+0x20 +18 9090909090909090
call handler
eb mydriver1!pivot +0x20+18 +8-9-5 48
eb mydriver1!pivot +0x20+18 +8-9-5 +1 89
eb mydriver1!pivot +0x20+18 +8-9-5 +2 f8
eb mydriver1!pivot +0x20+18 +8-9-5 +3 48 
eb mydriver1!pivot +0x20+18 +8-9-5 +4 05 
eb mydriver1!pivot +0x20+18 +8-9-5 +5 80
eb mydriver1!pivot +0x20+18 +8-9-5 +6  00 
eb mydriver1!pivot +0x20+18 +8-9-5 +7  00 
eb mydriver1!pivot +0x20+18 +8-9-5 +8  00 
eb mydriver1!pivot +0x20+18 +8-9-5 +9  48 
eb mydriver1!pivot +0x20+18 +8-9-5 +a  89 
eb mydriver1!pivot +0x20+18 +8-9-5 +b  44 
eb mydriver1!pivot +0x20+18 +8-9-5 +c  24 
eb mydriver1!pivot +0x20+18 +8-9-5 +d  20 
ew mydriver1!pivot +0x20+18 +8 15ff
;mark
eq mydriver1!placedholderrandom12313	0306f15fdadd410898e99a52e7da1f36	
ed mydriver1!pivot +0x20+18 +8 +2 mydriver1!placedholderrandom12313-mydriver1!pivot -0x20-26 
跳转回ph函数


ew  mydriver1!pivot +0x20+18 +8 +2 +4 25ff
ed   mydriver1!pivot+0x20 +18 +8 +2 +4 +2 mydriver1!agsduigasuidgasiufgiag- mydriver1!pivot -18 -8 -2 -4 -6
	;mark
eq mydriver1!agsduigasuidgasiufgiag	mydriver1!ph+0x32 




ed   mydriver1!pivot+0x20+18 +8 +2 +4 50c48348
eb   mydriver1!pivot+0x20+18 +8 +2 +4+4 48
eb   mydriver1!pivot+0x20+18 +8 +2 +4+4 +1 89
eb   mydriver1!pivot+0x20+18 +8 +2 +4+4 +2 fc
89
fc 

ew   mydriver1!pivot    +0x20+18 +8 +2 +4+4 +2+1 25ff
ed  mydriver1!pivot     +0x20+18 +8 +2 +4+4 +2+1+2 mydriver1!agsduigasuidgasiufgiag- (mydriver1!pivot +0x20+18 +8 +2 +4+4 +2+1+2+4)
	;mark               +0x20
ew +f+ mydriver1!pivot  +0x20+18 +8 +2 +4 25ff
ed +f+  mydriver1!pivot +0x20+18 +8 +2 +4 +2 mydriver1!agsduigasuidgasiufgiag- mydriver1!pivot -20 -2 -4-6

// 关键寄存器 r15 rdi rbx





还原从修改位置到call之间的代码
kd> dqs fffff802`12317685 l1
fffff802`12317685  018b48d3`8b0f8b49
kd> dw /c 1  fffff802`12317685+8 l3
fffff802`1231768d  8b48
fffff802`1231768f  d714
fffff802`12317691  8b48
kd> db /c 1  fffff802`12317685+8 +6 l1
fffff802`12317693  00  .



;Mark		 			
eq ddce2b5c5c40472ea46c65762d5ec810 08c5c2fcb18b4eedb8f63f03c7c90879				

yuanshidaimaplaceholder


ew +0n(yuanshidaimachangdu)+mydriver1!ph+0x4a 25ff
ed +0n(yuanshidaimachangdu)+mydriver1!ph+0x4a +2 d745d615b09542e8ba57195ae0a4aa63+8-mydriver1!ph-0x4a -6-0n(yuanshidaimachangdu)
jicunqizhuanyi 

eb      mydriver1!pivot-e+0x20+0x1c-4-3 48
eb      mydriver1!pivot-e+0x20+0x1c-4-3+1 89
eb      mydriver1!pivot-e+0x20+0x1c-4-3+2 e7
ed    mydriver1!pivot  -e+0x20+0x1c-4 f0e48348
ed mydriver1!pivot	   -e+0x20+0x1c 50ec8348
bc *
locateMyHandler
"""
import os
import time


def is_file_stable(file_path, check_interval=1, max_attempts=10):
    last_size = -1
    attempts = 0

    while attempts < max_attempts:
        current_size = os.path.getsize(file_path)

        if current_size == last_size:
            return True  # File is stable, not changing anymore
        last_size = current_size
        attempts += 1
        time.sleep(check_interval)  # Wait before checking again

    return False  # File is still changing after multiple checks


def read_file_when_done(file_path):
    if is_file_stable(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    else:
        raise Exception("File is still being written to!")
ppInsDict = {"push rax": "5048", "push rbx": "53", "push rcx": "51", "push rdx": "52", "push rsi": "56", "push rdi": "57", "push rbp": "55", "push rsp": "54", "push r8 ": "5041", "push r9 ": "5141", "push r10": "5241", "push r11": "5341", "push r12": "5441", "push r13": "5541", "push r14": "5641", "push r15": "5741", "pop r15": "5f41", "pop r14": "5e41", "pop r13": "5d41", "pop r12": "5c41", "pop r11": "5b41", "pop r10": "5a41", "pop r9": "5941", "pop r8": "5841", "pop rsp": "5c", "pop rbp": "5d", "pop rdi": "5f", "pop rsi": "5e", "pop rdx": "5a", "pop rcx": "59", "pop rbx": "5b", "pop rax": "58"}
import argparse

def parse_hex(value):
    """Parse a hex string, allowing optional 0x prefix."""
    value=value.replace('`','')
    return int(value, 16)

# 生成原始代码的写入指令
# 生成后替换原始字符串中的 yuanshidaimaplaceholder 即可
# 示例输入

# fffff802`12317685  ff  .
# fffff802`12317686  25  %
# fffff802`12317687  a9  .
def find_little_endian_offset(data: bytes, value: int):
    # Convert value to little-endian bytes of given size
    target = value.to_bytes(4, "little")

    # Search for the target sequence in data
    index = data.find(target)
    return index if index != -1 else None
def generateOhcWriteWindbgIns(ohc,hba,mb):
    # support original instruction that has relative address, something like: mov     rax,qword ptr [rip+0x29d000]
    # I only support one relative instruction in original code, because there is no need to modify that much instructions
    # 6 bytes space is all we need
    lineArray = ohc.split("\n")
    # get base
    base=lineArray[0].split(" ",1)[0].replace("`","")
    # combine all byte sequence
    hexseq=""
    for i in lineArray:
        if i.strip().__len__() < 2:
            continue
        hexseq=hexseq+i.split(" ")[2]
    byte_array = bytes.fromhex(hexseq)
    from capstone import Cs, CS_ARCH_X86, CS_MODE_64


    md = Cs(CS_ARCH_X86, CS_MODE_64)
    md.detail = True  # Enable detailed disassembly
    realoffsetsRip= 0
    offsets = ''
    aldcnt = 0
    rip=''
    targett=''
    for insn in md.disasm(byte_array, 0x1000):
        print(len(insn.bytes))
        aldcnt = aldcnt + len(insn.bytes)
        opstr = insn.op_str
        print(opstr)
        if opstr.split("rip +", 1).__len__() > 1:
            rip=base+"+0n"+str(aldcnt)
            rip=rip.replace(base,mb+'+0n'+str(hba))
            offsets=opstr.split("rip +",1)[1].split("]",1)[0].strip()
            if (int(offsets, 16) & 0x80000000) != 0:
                realoffsetsRip = 0xffffffff00000000 | int(offsets, 16)

            if realoffsetsRip != 0:
                targett=rip+"+"+ hex(realoffsetsRip)
            else:
                targett=rip+"+"+offsets
            break
    # add support to call instruction, I need to calculate the offset with capstone lib
    realoffsetsCall=0
    if rip=='':
        offsets = ''
        aldcnt = 0
        rip = ''
        targett = ''
        for insn in md.disasm(byte_array, 0x1000):
            print(len(insn.bytes))
            aldcnt = aldcnt + len(insn.bytes)
            opstr = insn.op_str
            print(opstr)
            if opstr.__len__()>=2:
                if opstr[0]=='0':
                   if opstr[1]=='x':
                        # capstone can't decode this call instruction correctly, I 'll decode it manually
                        if byte_array[aldcnt-len(insn.bytes)]==0xe8:
                            import struct
                            offsets=hex(struct.unpack('<I', byte_array[aldcnt-len(insn.bytes)+1:aldcnt-len(insn.bytes)+4+1])[0])
                            # deal with backwards offset
                            if (int(offsets,16)&0x80000000)!=0:
                                realoffsetsCall=0xffffffff00000000|int(offsets,16)
                        else:
                            print("unexpected")
                            sys.exit(0)
                        rip = base + "+0n" + str(aldcnt)
                        rip=rip.replace(base,mb+'+0n'+str(hba))
                        #offsets = opstr.strip()
                        #offsets=hex(int(offsets, 16)-                int(base,16)-aldcnt)
                        if realoffsetsCall!=0:
                            targett = rip + "+" + hex(realoffsetsCall)
                        else:
                            targett = rip + "+" + offsets
                        break

    # Example usage
    data = b"\x48\x81\xec\x30\x01\x00\x00\x48\x8b\x05\xad\x48\x23\x00\x48\x33"
    value = 0x2348AD  # Search for 0x2348AD (DWORD)
    offset=0
    if rip!='':
        offset = find_little_endian_offset(byte_array, int(offsets, 16)  )  # 0x2348AD is 3 bytes

    # return opstr.split("+",1)[1].split("]",1)[0].strip()


    finalString = ""
    index = 0
    for i in lineArray:
        if i.strip().__len__() < 2:
            continue
        finalString = finalString + "eb mydriver1!ph+0x4a+" + hex(index) + " " + i.split(" ")[2] + "\n"
        index = index +1
    if rip!='':
        if realoffsetsCall != 0:
            offsets = hex(realoffsetsCall)
        if realoffsetsRip != 0:
            offsets = hex(realoffsetsRip)
        # targett contains hard coded address, need to be replaced as module_base + offset
        finalString = finalString + "ed mydriver1!ph+0x4a+" + hex(offset) + " " + targett+'-0n'+ str(aldcnt) +'-mydriver1!ph-0x4a'+ "\n"
    global windbgHookIns
    windbgHookIns = windbgHookIns.replace("yuanshidaimaplaceholder", finalString)
def generatePaiWriteWindbgIns(rba):
    # 增加对栈寄存器的支持  16个push 就是16*8 字节，那么rsp需要先+16*8字节，才能恢复到hook前的水平，然后需要根据参数，来确定汇编代码
    # 栈寄存器的参数应该长这个样子  s-28就是原始参数是rsp-28  s+28  原始参数就是rsp+28
    if rba.__len__() < 3:
        return
    pai = ""
    reg = rba.split("/")
    popRegInsArr = ["pop rcx", "pop rdx", "pop r8", "pop r9"]
    index = 0
    realIndex=0
    finalString = ""
    for i in reg:
        #if i.strip().__len__()>1:
        #    if i[0] == 's':
        #        # 栈参数需要进行特殊处理
        #        # 48 8d 44 24 80          lea    rax,[rsp-0x80]
        #        numTooffset=16*8
        #        finalString = finalString + 'eb' + " mydriver1!pivot+" + hex(realIndex) + " " + '48' + "\n"
        #        realIndex=realIndex+1
        #        finalString = finalString + 'eb' + " mydriver1!pivot+" + hex(realIndex) + " " + '8d' + "\n"
        #        realIndex=realIndex+1
        #        finalString = finalString + 'eb' + " mydriver1!pivot+" + hex(realIndex) + " " + '44' + "\n"
        #        realIndex=realIndex+1
        #        finalString = finalString + 'eb' + " mydriver1!pivot+" + hex(realIndex) + " " + '24' + "\n"
        #        realIndex=realIndex+1
        #        finalString = finalString + 'eb' + " mydriver1!pivot+" + hex(realIndex) + " " + '80' + "\n"
        #        realIndex=realIndex+1
        #        if i.split('s',1)[1][0]=='+':
        #            numTooffset=numTooffset+int(i.split('s',1)[1].split('+',1)[1],16)
        #        else:
        #            numTooffset=numTooffset-int(i.split('s',1)[1].split('+',1)[1],16)

        pai = pai + "push " + i + "\n" + popRegInsArr[index] + "\n"
        index = index + 1
    lineArray = pai.split("\n")
    index = realIndex
    for i in lineArray:
        if i.strip().__len__() < 2:
            continue
        writeIns = "eb"
        if ppInsDict[i].__len__() == 4:
            writeIns = "ew"
        finalString = finalString + writeIns + " mydriver1!pivot+" + hex(index) + " " + ppInsDict[i] + "\n"
        if writeIns == "ew":
            index = index + 2
        else:
            index = index + 1
    global windbgHookIns
    windbgHookIns = windbgHookIns.replace("jicunqizhuanyi", finalString)
def replace_in_fileDef(old_string, new_string):
    file_path = r'C:\Users\x\Downloads\密码是1\avscan\filter\avscan.c'
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    content = content.replace(old_string, new_string)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
def replace_in_fileDec(old_string, new_string):
    file_path = r'C:\Users\x\Downloads\密码是1\avscan\filter\avscan.c'
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    content = content.replace(old_string, new_string)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
def replace_in_fileMain(old_string, new_string):
    file_path = r'C:\Users\x\Downloads\密码是1\avscan\filter\avscan.c'
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    if old_string in content:
        a=1
    content = content.replace(old_string, new_string)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def CheckForContentExist(old_string):
    file_path = r'C:\Users\x\Downloads\密码是1\avscan\filter\avscan.c'
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    if content.split(old_string, 1).__len__() > 1:
        return True
    else:
        return False



def _c4508d291ac94f64a7065745934bb450FuncCodeGen(hba):
    template = """
    PVOID ph(PVOID as1) {
	if (as1 == NULL)return NULL;

	myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123");
	return NULL;
}
    """
    if CheckForContentExist('_c4508d291ac94f64a7065745934bb450' + hba):
        return
    template = template.replace(r'myprintf("123")', r'myprintf("_c4508d291ac94f64a7065745934bb450FuncCodeGen' + hba + r'\n")');
    template = template.replace(r'PVOID ph(PVOID as1) {', r'PVOID _c4508d291ac94f64a7065745934bb450' + hba + r'(PVOID as1) {');
    replace_in_fileDef('//_c4508d291ac94f64a7065745934bb450FuncCodeDefineAddMark', r'//_c4508d291ac94f64a7065745934bb450FuncCodeDefineAddMark' + '\n' + template)
    replace_in_fileDec('//_c4508d291ac94f64a7065745934bb450FuncCodeDeclareAddMark',
                    r'//_c4508d291ac94f64a7065745934bb450FuncCodeDeclareAddMark' + '\n' + r'PVOID _c4508d291ac94f64a7065745934bb450' + hba + r'(PVOID as1);')
    replace_in_fileMain('//_c4508d291ac94f64a7065745934bb450FuncCodePreventOptimizeAddMark',
                    r'//_c4508d291ac94f64a7065745934bb450FuncCodePreventOptimizeAddMark' + '\n' + r'_c4508d291ac94f64a7065745934bb450' + hba + r'(NULL);')
def _ac9a3426169e437d9b3d72ee404d9ecaFuncCodeGen(hba):
    template = """
    PVOID ph(PVOID as1) {
	if (as1 == NULL)return NULL;

	myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123");
	return NULL;
}
    """
    if CheckForContentExist('_ac9a3426169e437d9b3d72ee404d9eca' + hba):
        return
    template = template.replace(r'myprintf("123")', r'myprintf("_ac9a3426169e437d9b3d72ee404d9ecaFuncCodeGen' + hba + r'\n")');
    template = template.replace(r'PVOID ph(PVOID as1) {', r'PVOID _ac9a3426169e437d9b3d72ee404d9eca' + hba + r'(PVOID as1) {');
    replace_in_fileDef('//_ac9a3426169e437d9b3d72ee404d9ecaFuncCodeDefineAddMark', r'//_ac9a3426169e437d9b3d72ee404d9ecaFuncCodeDefineAddMark' + '\n' + template)
    replace_in_fileDec('//_ac9a3426169e437d9b3d72ee404d9ecaFuncCodeDeclareAddMark',
                    r'//_ac9a3426169e437d9b3d72ee404d9ecaFuncCodeDeclareAddMark' + '\n' + r'PVOID _ac9a3426169e437d9b3d72ee404d9eca' + hba + r'(PVOID as1);')
    replace_in_fileMain('//_ac9a3426169e437d9b3d72ee404d9ecaFuncCodePreventOptimizeAddMark',
                    r'//_ac9a3426169e437d9b3d72ee404d9ecaFuncCodePreventOptimizeAddMark' + '\n' + r'_ac9a3426169e437d9b3d72ee404d9eca' + hba + r'(NULL);')
def PhFuncCodeGen(hba):
    template = """
    PVOID ph(PVOID as1) {
	if (as1 == NULL)return NULL;

	myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123");
	return NULL;
}
    """
    if CheckForContentExist('ph_' + hba):
        return
    template = template.replace(r'myprintf("123")', r'myprintf("PhFuncCodeGen' + hba + r'\n")');
    template = template.replace(r'PVOID ph(PVOID as1) {', r'PVOID ph_' + hba + r'(PVOID as1) {');
    replace_in_fileDef('//phFunccodeDefineAddMark', r'//phFunccodeDefineAddMark' + '\n' + template)
    replace_in_fileDec('//phFunccodeDeclareAddMark',
                    r'//phFunccodeDeclareAddMark' + '\n' + r'PVOID ph_' + hba + r'(PVOID as1);')
    replace_in_fileMain('//phFunccodePreventOptimizeAddMark',
                    r'//phFunccodePreventOptimizeAddMark' + '\n' + r'ph_' + hba + r'(NULL);')

def PivotFuncCodeGen(hba):
    template = """
    PVOID pivot(PVOID as1) {
	if (as1 == NULL)return NULL;

	myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123");
	return NULL;
}
    """
    # 如果文件中已经有这个函数就不要再生成了
    if CheckForContentExist('pivot_' + hba):
        return
    template = template.replace(r'myprintf("123")', r'myprintf("PivotFuncCodeGen' + hba + r'\n")');
    template = template.replace(r'PVOID pivot(PVOID as1) {', r'PVOID pivot_' + hba + r'(PVOID as1) {');
    replace_in_fileDef('//pivotFunccodeDefineAddMark', r'//pivotFunccodeDefineAddMark' + '\n' + template)
    replace_in_fileDec('//pivotFunccodeDeclareAddMark',
                    r'//pivotFunccodeDeclareAddMark' + '\n' + r'PVOID pivot_' + hba + r'(PVOID as1);')
    replace_in_fileMain('//pivotFunccodePreventOptimizeAddMark',
                    r'//pivotFunccodePreventOptimizeAddMark' + '\n' + r'pivot_' + hba + r'(NULL);')

def agsduigasuidgasiufgiagFuncCodeGen(hba):
    template = """
    PVOID agsduigasuidgasiufgiag(PVOID as1) {
	if (as1 == NULL)return NULL;

	myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123");
	return NULL;
}
    """
    if CheckForContentExist('agsduigasuidgasiufgiag_' + hba):
        return
    template = template.replace(r'myprintf("123")', r'myprintf("agsduigasuidgasiufgiagFuncCodeGen' + hba + r'\n")');
    template = template.replace(r'PVOID agsduigasuidgasiufgiag(PVOID as1) {',
                                r'PVOID agsduigasuidgasiufgiag_' + hba + r'(PVOID as1) {');
    replace_in_fileDef('//agsduigasuidgasiufgiagFunccodeDefineAddMark',
                    r'//agsduigasuidgasiufgiagFunccodeDefineAddMark' + '\n' + template)
    replace_in_fileDec('//agsduigasuidgasiufgiagFunccodeDeclareAddMark',
                    r'//agsduigasuidgasiufgiagFunccodeDeclareAddMark' + '\n' + r'PVOID agsduigasuidgasiufgiag_' + hba + r'(PVOID as1);')
    replace_in_fileMain('//agsduigasuidgasiufgiagFunccodePreventOptimizeAddMark',
                    r'//agsduigasuidgasiufgiagFunccodePreventOptimizeAddMark' + '\n' + r'agsduigasuidgasiufgiag_' + hba + r'(NULL);')

def placedholderrandom12313FuncCodeGen(hba):
    template = """
    PVOID placedholderrandom12313(PVOID as1) {
	if (as1 == NULL)return NULL;

	myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123"); myprintf("123");
	return NULL;
}
    """
    if CheckForContentExist('placedholderrandom12313_' + hba):
        return
    template = template.replace(r'myprintf("123")', r'myprintf("placedholderrandom12313FuncCodeGen' + hba + r'\n")');
    template = template.replace(r'PVOID placedholderrandom12313(PVOID as1) {',
                                r'PVOID placedholderrandom12313_' + hba + r'(PVOID as1) {');
    replace_in_fileDef('//placedholderrandom12313FunccodeDefineAddMark',
                    r'//placedholderrandom12313FunccodeDefineAddMark' + '\n' + template)
    replace_in_fileDec('//placedholderrandom12313FunccodeDeclareAddMark',
                    r'//placedholderrandom12313FunccodeDeclareAddMark' + '\n' + r'PVOID placedholderrandom12313_' + hba + r'(PVOID as1);')
    replace_in_fileMain('//placedholderrandom12313FunccodePreventOptimizeAddMark',
                    r'//placedholderrandom12313FunccodePreventOptimizeAddMark' + '\n' + r'placedholderrandom12313_' + hba + r'(NULL);')


def KHHookHandlerFuncCodeGen(hba,rba):
    template = """
    PVOID KHHookHandler(PVOID a1,PVOID a2,PVOID a3,PVOID a4,PVOID a5) {PBYTE _rsp = a5;
	if (a1 == NULL)return 0;

	return NULL;
}
    """
    if CheckForContentExist('KHHookHandler_' + hba):
        return
    reg = rba.split("/")
    finas=""
    cnt=1
    for i in reg:
        finas=finas+"PBYTE _" +i+"=a"+str(cnt)+";\n"
        cnt=cnt+1
    if finas.__len__()>2:
        template=template.replace("return NULL;",finas+"\n\nreturn NULL;")
    if rba=="''":
        finas="PBYTE _rcx=a1;PBYTE _rdx=a2;PBYTE _r8=a3;PBYTE _r9=a4;"
        template = template.replace("return NULL;", finas + "\n\nreturn NULL;")
    template = template.replace(r'myprintf("123\n")', r'myprintf("' + hba + r'\n")');
    template = template.replace(r'PVOID KHHookHandler(',
                                r'PVOID KHHookHandler_' + hba + r'(');
    replace_in_fileDef('//KHHookHandlerFunccodeDefineAddMark',
                    r'//KHHookHandlerFunccodeDefineAddMark' + '\n' + template)
    replace_in_fileDec('//KHHookHandlerFunccodeDeclareAddMark',
                    r'//KHHookHandlerFunccodeDeclareAddMark' + '\n' + r'PVOID KHHookHandler_' + hba + r'(PVOID a1,PVOID a2,PVOID a3,PVOID a4,PVOID a5);')
    replace_in_fileMain('//KHHookHandlerFunccodePreventOptimizeAddMark',
                    r'//KHHookHandlerFunccodePreventOptimizeAddMark' + '\n' + r'KHHookHandler_' + hba + r'(NULL,NULL,NULL,NULL,NULL);')

import sys
def main():
    # 需要增加对栈寄存器的支持
    parser = argparse.ArgumentParser(description="Hook parameter parser")
    parser.add_argument("-hba", type=parse_hex, required=True, help="Hook begin address (hex)")
    parser.add_argument("-hea", type=parse_hex, required=True, help="Hook end address (hex)")
    #parser.add_argument("-ohc", required=True, help="Original hook code")
    parser.add_argument("-rba", required=True, help="register to be adjusted")
    parser.add_argument("-mn", required=True, help="module name")
    parser.add_argument("-pn", required=True, help="project module name")
    parser.add_argument("-ca", required=True, help="custom jump address")

    args = parser.parse_args()
    global windbgHookIns
    args.mn='('+args.mn+')'
    originalHookCodeLen = args.hea - args.hba
    if originalHookCodeLen < 6:
        print("you can't insert inline hook with space length less than 6")
        exit(-1)
    windbgHookIns = windbgHookIns.replace("(yuanshidaimachangdu)", str(originalHookCodeLen))

    print('please input original code, code len is ' + str(originalHookCodeLen) + ':')
    print('please execute this command to get original code')
    import os
    if os.path.exists(r'c:\users\public\mylogfile.txt'):
        os.remove(r'c:\users\public\mylogfile.txt')
    print(r'.logopen c:\users\public\mylogfile.txt;db /c 1 '+args.mn+'+' + hex(args.hba) + ' l0n' + str(originalHookCodeLen)+';.logclose')
    #ohc = "\n".join(iter(input, ""))  # Stop on empty line
    ohc=''


    while True:
        if os.path.exists(r'c:\users\public\mylogfile.txt'):
            break
    lines = read_file_when_done(r'c:\users\public\mylogfile.txt').split('\n')

    for l in lines:
        if l.strip().__len__()<2:
            continue
        if l.split('mylogfile',1).__len__()>1:
            a=1
        else:
            ohc=ohc+l.strip()+'\n'


    os.remove(r'c:\users\public\mylogfile.txt')




    generateOhcWriteWindbgIns(ohc,args.hba,args.mn)
    generatePaiWriteWindbgIns(args.rba)
    windbgHookIns = windbgHookIns.replace("mydriver1!ph", "mydriver1!ph_" + hex(args.hba))
    windbgHookIns = windbgHookIns.replace("mydriver1!pivot", "mydriver1!pivot_" + hex(args.hba))
    windbgHookIns = windbgHookIns.replace("819f5d66ab064d1991d4ab4ed5c31db6", hex(args.hba) + '+f312be6ae61f4caf8305ffedc3a0f762')
    windbgHookIns = windbgHookIns.replace("-455dc6a29c3f4f32a95e2c3a1a1ae79e-", '' + hex(args.hba) + '-')


    #测试 custom address
    if args.ca!='':
        memres=args.ca
        windbgHookIns = windbgHookIns.replace("4cddef71310442818dbd373c59e45bb6", memres)
        windbgHookIns = windbgHookIns.replace("8d591a5375ee468580ff06c65f2cf77c", memres+ '-f312be6ae61f4caf8305ffedc3a0f762-')
    # 测试


    windbgHookIns = windbgHookIns.replace("0306f15fdadd410898e99a52e7da1f36", "mydriver1!KHHookHandler_" + hex(args.hba))
    windbgHookIns = windbgHookIns.replace("mydriver1!agsduigasuidgasiufgiag", "mydriver1!agsduigasuidgasiufgiag_" + hex(args.hba))
    windbgHookIns = windbgHookIns.replace("mydriver1!placedholderrandom12313", "mydriver1!placedholderrandom12313_" + hex(args.hba))
    windbgHookIns = windbgHookIns.replace("08c5c2fcb18b4eedb8f63f03c7c90879", "f312be6ae61f4caf8305ffedc3a0f762+" + hex(args.hea))
    windbgHookIns = windbgHookIns.replace("4cddef71310442818dbd373c59e45bb6", "mydriver1!_ac9a3426169e437d9b3d72ee404d9eca" + hex(args.hba))
    windbgHookIns = windbgHookIns.replace("8d591a5375ee468580ff06c65f2cf77c", "mydriver1!_ac9a3426169e437d9b3d72ee404d9eca" + hex(args.hba) + '-f312be6ae61f4caf8305ffedc3a0f762-')
    windbgHookIns = windbgHookIns.replace("d745d615b09542e8ba57195ae0a4aa63", "mydriver1!_c4508d291ac94f64a7065745934bb450" + hex(args.hba))
    windbgHookIns = windbgHookIns.replace("ddce2b5c5c40472ea46c65762d5ec810", "mydriver1!_c4508d291ac94f64a7065745934bb450" + hex(args.hba) + '+8')
    # 生成函数
    _ac9a3426169e437d9b3d72ee404d9ecaFuncCodeGen(hex(args.hba))
    _c4508d291ac94f64a7065745934bb450FuncCodeGen(hex(args.hba))

    # 同时还需要对源代码进行更新，生成相应的place holder函数相关代码
    PhFuncCodeGen(hex(args.hba))
    placedholderrandom12313FuncCodeGen(hex(args.hba))
    agsduigasuidgasiufgiagFuncCodeGen(hex(args.hba))
    PivotFuncCodeGen(hex(args.hba))
    KHHookHandlerFuncCodeGen(hex(args.hba),args.rba)
    windbgHookIns = windbgHookIns.replace('locateMyHandler', 'u mydriver1!KHHookHandler_' + hex(args.hba))
    windbgHookIns=windbgHookIns.replace("PBYTE _''=a1;",'\n')
    modulename='PROCEXP152'
    windbgHookIns=windbgHookIns.replace('f312be6ae61f4caf8305ffedc3a0f762',args.mn)
    windbgHookIns=windbgHookIns.replace("PBYTE _''=a1;",'')
    lineconnt=0
    targstring=''
    for line in reversed(windbgHookIns.splitlines()):
        if line.strip().__len__()<2:
            continue

        targstring=line
        break
    new_ins=''
    for line in windbgHookIns.splitlines():
        if line.strip().__len__() < 2:
            continue
        line=line.strip()
        if line[0]!='e':
            continue
        new_ins=new_ins+line+'\n'
    new_ins=new_ins+targstring

    new_ins=new_ins.replace('mydriver1',args.pn)
    new_ins=new_ins.replace('PBYTE _r8=a2','PBYTE _r8=a3')
    print('/*\n' + new_ins + '\n*/')
    with open("output.txt", "w", encoding="utf-8") as file:

        file.write('/*\n' + new_ins + '\n*/')


if __name__ == "__main__":
    main()
