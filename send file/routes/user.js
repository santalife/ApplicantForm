const express = require('express');
const router = express.Router();
// User register URL using HTTP post => /user/register
router.post('/register', (req, res) => {
    console.log(req.body.name)
    var name = req.body.name;
    var email=req.body.email;
    var pw = req.body.password;
    var pw2= req.body.password2;
    let password_error= {text:"Password Must be 4 characters"};
    let password2_error={text:"Passwords do not match"};
    let errors = [];
    let success_msg = "";
    console.log("password1:"+pw)
    console.log("password2:"+pw2)

    if(pw.length < 4){
        errors.push(password_error);
    }
    if(pw != pw2){
        errors.push(password2_error);
    }

    if(pw.length >= 4 && pw === pw2 ){
        success_msg = email +" resgistered successfully"
        res.render('user/login', {
            name:name,
            email:email,
            errors:errors,
            success_msg:success_msg
            })
    }

    else{
        res.render('user/register', {
            name:name,
            email:email,
            errors:errors,
            success_msg:success_msg
            })
    }

    
});
module.exports = router;