const fs=require('fs')//file system
fs.writeFileSync('note.txt','This file was created by node.')
var data=5+5;
fs.appendFileSync('note.txt',data)
const ourModule=require('./appp')
console.log(ourModule)
var a=10;
var b=5;
console.log('data is',ourModule.data.control(a,b));
fs.writeFileSync('note.txt',ourModule.data.control(a,b))
console.log('data is',ourModule.data.sensor(a,b));
fs.appendFileSync('note.txt',ourModule.data.sensor(a,b))