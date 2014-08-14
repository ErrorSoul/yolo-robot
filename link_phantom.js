// phantomjs code to log in to Amazon
// based on the code from this Stackoverflow answer: http://stackoverflow.com/questions/9246438/how-to-submit-a-form-using-phantomjs
// I'm injecting jQuery so this assumes you have jquery in your project directory
 
var page = new WebPage(), testindex = 0, loadInProgress = false;
 
page.onConsoleMessage = function(msg) {
  console.log(msg);
};
 
page.onLoadStarted = function() {
  loadInProgress = true;
  console.log("load started");
};
 
page.onLoadFinished = function() {
  loadInProgress = false;
  console.log("load finished");
};
 
var steps = [
  function() {
    console.log("Load Login Page");
    page.settings.userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11";
    page.open("http://www.braziliawomen.com/");
  },
  function() {
   console.log("Enter Credentials");
   page.injectJs("jquery.min.js");
   page.evaluate(function() {
       $("input[name='first-name']").val('Olga');
        $("input[name='email']").val('ca666tepdd100@yandex.ru');
        $("select[name='day']").val('3');
        $("select[name='month']").val('6');
       $("select[name='year']").val('1984');
       $("input[name='password']").val('O1LlLA');
     
     console.log(document.title);
   });
  },
  function() {
   console.log('login');
   page.evaluate(function() {
     console.log(document.title);
     $('button').submit();
       $('button').click();
   });
  },

   function() {
   console.log('login');
   
    page.evaluate(function() {
     console.log(document.title);
     
   });
  }
]
 
interval = setInterval(function() {
  if (!loadInProgress && typeof steps[testindex] == "function") {
    console.log("step " + (testindex + 1));
    steps[testindex]();
    page.render("images" + (testindex + 1) + ".png");
    testindex++;
  }
  if (typeof steps[testindex] != "function") {
    console.log("test complete!");
    phantom.exit();
  }
}, 2900);
