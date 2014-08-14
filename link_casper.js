var casper = require('casper').create();


casper.start("http://www.braziliawomen.com/");
casper.then( function(){
   this.evaluate(function(){
       $("input[name='first-name']").val('Olga');
        $("input[name='email']").val('ca14aatepdd100@yandex.ru');
        $("select[name='day']").val('3');
        $("select[name='month']").val('6');
       $("select[name='year']").val('1984');
       $("input[name='password']").val('O1LlLA');
       $('button').click();
   });
    this.capture('screen.png');
});



casper.then(function() {
    this.wait(1000, function() {
        this.echo("I've waited for a second.");
    });
    console.log('clicked ok, new location is ' + this.getCurrentUrl());
});
casper.then(function(){
    this.wait(10000, function() {
    console.log('clicked ok, new location is ' + this.getCurrentUrl());
    this.capture('click.png', {
        top: 0,
        left: 0,
        width: 1000,
        height: 700
    }); });
     
});


casper.run(function(){
    this.exit();
});
