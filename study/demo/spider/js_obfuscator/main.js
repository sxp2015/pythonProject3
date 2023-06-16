const obfuscator = require('javaScript-obfuscator')
/*
* 那么简单的代码混淆成了这个样子，因为设定“控制流平坦化”选项。
*
* */
const code= `let x = '1'+1
console.log('x',x)`

/*
代码压缩
* 参数compact 的默认值是true，如果定义为 false，则混淆后的代码会分行显示
* **/
const options_1 = `{
    compact:false,
    controlFlowFlattening:true,
}`

/*
 * hexadecimal:将变量名替换为十六进制形式的字符串，如0xabc123
 * mangled:将变量名替换为普通的简写字符，如ab、c等。
 * renameGlobals这个参数还可以指定是否混淆全局变量和函数名称默认值为false
 *
 **/
const options_2 = `{
    compact:false,
    identifierNamesGenerator: 'hexadecimal',
}`

function obfuscate(code,options_2){
    return obfuscator.obfuscate(code,options_2).getObfuscatedCode()
}
console.log('obfuscate:',obfuscate(code,options_2))
