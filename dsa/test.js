let a  = "malayalam"

// const palindromeCheck = () => a === a.split().reverse().join('')

// console.log(palindromeCheck())

let num = 1234

// console.log(Math.floor(Math.log10(num)+1))

function fact(n){
    if(n===0 || n==1) return 1
    let digit = 0
    for(let i=2; i<=n; i++){
        digit += Math.log10(i)
    }
    return Math.floor(digit + 1)
}
console.log(fact(5))