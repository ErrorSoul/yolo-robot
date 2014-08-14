var casper = require('casper').create();

casper.start('https://twitter.com/login');
casper.fill("form[action='https://twitter.com/sessions']", {'session[username_or_email]' : "rrrr"}, true)
 

 
casper.then(function() {
    console.log('clicked ok, new location is ' + this.getCurrentUrl());
});
 
casper.run();


casper.then(function(){
    this.capture('click.png', {
        top: 0,
        left: 0,
        width: 1000,
        height: 700
    });
});


casper.run(function(){
    this.exit();
});
