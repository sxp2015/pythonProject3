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
// 自我保护的混淆方法
// const options = `{selfDefending:true}`

//controlFlowFlattening变量可以控制是否开启控制流平坦化，让逻辑混乱，难以阅读
//deadCodeInjection:true 无用代码注入
// 另外，我们还可以通过设置deadCodeInjectionThreshold 参数来控制无用代码注人的比例。
// 该参数的取值范围为0到1默认值是0.4。
// 对象键名替换如果是一个对象可以使用transformObjectKeys来对对象的键值进行替换示例如下
// 我们可以使用disableConsoleOutput来禁用掉console.log输出功能加大调试难度
// 另外，还有一些特殊的工具包(比如aaencode jencode jsfuck 等)它们可以对代码进行混淆和编码。
// 调试保护，即通过反复执行 debugger 来使得原来的代码无法顺畅执行。
/*
const options = `{
debugProtection: true,
debugProtectionInterval: true
}`
* */

/*
* 我们还可以通过控制domainLock 来控制JavaScrpt代码只能在特定域名下运行这样就可以
* 降低代码被模拟或盗用的风险
*
* const options = `{
domainLock:['xxxxx.com']
}`
* */
const options = `{
compact:false,
controlFlowFlattening: true,
deadCodeInjection:true,
transformObjectKeys:true
}`


function obfuscate(code,options){
    return obfuscator.obfuscate(code,options).getObfuscatedCode()
}
console.log('obfuscate:',obfuscate(code,options))