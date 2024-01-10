function Override(target:any , propertyKey: string, descriptor: PropertyDescriptor)  {
    if (typeof target[propertyKey] === 'undefined') {
        throw new Error(`El método ${propertyKey} no existe para ser sobreescrito.`);
    }
    return descriptor;
}

class Base {
    greet() {
        return "Hola mundo";
    }
}

class Derived extends Base {
    @Override
     greet() {
        return "Hola desde Derived";
    }
}

const c= new Derived()
console.log(new Derived().greet())