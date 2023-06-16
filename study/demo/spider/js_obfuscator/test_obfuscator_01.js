const obfuscator = require('javaScript-obfuscator')
/*
* 我们还可以通过rotateStringArray 参数来控制数组化后结果的元素顺序，
* 默认为 true。还可以通过stringArrayEncoding
* 参数来控制数组的编码形式默认不开启编码如果将其设置为true或base64则会使用Base64编码如果设置为rc4，
* 则使用RC4编码另外可以通过stringArrayThreshold来控制启用编码的概率，其范围为0到1，默认值为0.8

* 【字符串混淆】
*  */

const code = `
var a = "hello world"
`
const options = `{
stringArray:true,
rotateStringArray:true,
stringArrayEncoding:'true', // 'base64' 或 'rc4' 或 false
stringArrayThreshold:1}
`
/*
*可以使用unicodeEscapeSequence 这个参数对字符串进行Unicode转码
* */
const options_2 =`{
compact:false,
unicodeEscapeSequence: true
}`

function obfuscate(code,options_2){
    return obfuscator.obfuscate(code,options_2).getObfuscatedCode()
}
console.log('obfuscate:',obfuscate(code,options_2))