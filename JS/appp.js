var methods={};
var c,d=0;
methods.control=function(c,d){
    console.log('Controlling Function')
    var result=c*d;
    return result;
}

methods.sensor=function(c,d)
{
    console.log('Sensing Function')
    return c+d;
}

exports.data=methods;