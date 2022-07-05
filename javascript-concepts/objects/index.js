///This chapter is focused on objects and their peculiar behaviours
//https://javascript.info/object-methods

let user = {
    name: "Pratyush", // name is a property of the object "user"
    age: 23,
    placeOfWork: "Noida"
}

//using Function Expression to create a function and assign it as the property of the object
user.sayHenlo = () => {
    console.log("Hi! My name is " + user.name + ", I am a " + user.age + " years old working professional, who is based out out " + user.placeOfWork)

}
user.sayHenlo()

let userOne = {
    name: "Nibba",
    age: 23,
    sayBonjour(){
        console.log("Henlo frens, my name is " + this.name + ", I am a " + this.age + " years old kiddo") 
        //using this to reference the properties of the object while adding a method
    }
}

userOne.sayBonjour()