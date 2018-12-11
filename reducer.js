const a = [{balance: 15}, {balance: 15}, {balance: 15}]

const reducer = (total, giftcard) => total + giftcard.balance

console.log(a.reduce(reducer, 0))