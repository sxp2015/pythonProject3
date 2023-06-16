const obfuscator = require('javaScript-obfuscator')
/*
* 我们可以通过设置selfDefending 参数来开启代码自我保护功能。开启之后，
* 混淆后的JavaScript会强制以一行形式显示。如果我们将混淆后的代码进行格式化或者重命名，
* 该段代码将无法执行。
* 【代码自我保护】
*  */

const code = `
console.log("hello world")
console.log("hello python")
console.log("hello javascript")
`
const options = `{selfDefending:true}`


function obfuscate(code,options){
    return obfuscator.obfuscate(code,options).getObfuscatedCode()
}
console.log('obfuscate:',obfuscate(code,options))