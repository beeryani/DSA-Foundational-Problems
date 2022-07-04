// Constructors in JS is equivalent to __init__ method in Python; we will leverage that to learn more in JS
//https://javascript.info/constructor-new#constructor-function
// let's define a constructor

//Constructor Functions are classes of JS

function Beer(name, type, country) {
    this.name = name; // these are objects within the constructor function
    this.type = type;
    this.country = country;
    return {nickname: "Zeher"}
}

broCode = new Beer()
broCode.name = "Bira"
broCode.type = "IPA"
broCode.country = "India"
console.log(broCode)

//now let's move to methods

function Whiskey(name, country){
    this.name = name;
    this.labelSlogan = ()=> {
        return console.log(this.name + " peeke mera dil bole, ole ole")
    };
    this.country = country;
    this.type = ()=> {
        return "This bottle is " + this.name + "ish"
    }

}

petrolDesi = new Whiskey()
petrolDesi.name = "Royal Challenger"
petrolDesi.country = "Bengaluru"
console.log(petrolDesi.type()) //methods need to be added with round bracket to be referenced
petrolDesi.labelSlogan()