const alertMessage = require('../helpers/messenger');
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
	const title = 'Video Jotter';
	res.render('index', {title: title}) // renders views/index.handlebars
});

router.get('/showLogin',(req, res) => {
	res.render('user/login')
});

router.get('/user/register',(req, res) => {
	res.render('user/register')
});


router.get('/about', (req, res) => {
	const author = 'Denzel Washington';
	alertMessage(res, 'success', 'This is an important message', 'fas fa-sign-in-alt', true);
	alertMessage(res, 'danger', 'Unauthorised access', 'fas fa-exclamation-circle', false);
	let success_msg = 'Success message';
	let error_msg = 'Error message using error_msg';
	var errors=[{text:"First Error Message"},{text:"Second Error Message"},{text:"Thrid Error Message"}]

	res.render('about', {
	author: author,
	success_msg: success_msg,
	error_msg: error_msg,
	errors: errors
	})
});

// Logout User
router.get('/logout', (req, res) => {
	req.logout();
	res.redirect('/');
});

module.exports = router;
